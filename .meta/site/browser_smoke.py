#!/usr/bin/env python3
"""Check the page locally, or at --url after publishing. No lab execution."""
import argparse
import functools
import http.server
import json
import threading
from pathlib import Path
from urllib.parse import quote

from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[2]


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/labs/'):
            self.path = self.path[len('/labs'):]
        return super().do_GET()

    def log_message(self, *args):
        pass


def check(browser, url, labs, screenshots, expected_commit, published=False):
    context = browser.new_context(viewport={'width': 1440, 'height': 900})
    page = context.new_page()
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(url, wait_until='networkidle')
    expect(page).to_have_title('Practical Labs')
    expect(page.locator('h1')).to_have_text('Practical Labs')
    favicon = page.locator('link[rel="icon"]').get_attribute('href')
    icon_response = context.request.get(url + favicon)
    assert icon_response.ok and '<svg' in icon_response.text(), 'Brain favicon unavailable'
    # A deployment can succeed while a browser still receives an older snapshot.
    info_response = context.request.get(url + 'build-info.json')
    assert info_response.ok, 'Published build metadata unavailable'
    info = info_response.json()
    assert info['source_commit'] == expected_commit and (not published or not info['dirty']), 'Published commit differs from the expected clean snapshot'
    payload_response = context.request.get(url + info['payload'])
    assert payload_response.ok, 'Published catalog unavailable'
    payload = payload_response.json()
    assert payload['source_commit'] == expected_commit and payload['labs'] == labs, 'Published catalog differs from the expected snapshot'
    atlas_link = page.get_by_role('link', name='Practice atlas', exact=True)
    assert atlas_link.get_attribute('href').endswith(f'/blob/{expected_commit}/PRACTICE-ATLAS.md'), 'Practice atlas link differs from the published snapshot'
    expect(page.locator('#result-count')).to_have_text(f'{len(labs)} of {len(labs)} labs')
    expect(page.locator('main > details')).to_have_count(4)

    # Open Completed and In progress on a fresh visit
    for section in range(4):
        expect(page.locator('main > details').nth(section)).to_have_js_property(
            'open', section < 2
        )
    expect(page.locator("#work-results .collection[open]")).to_have_count(0)
    expect(page.locator('body')).to_have_attribute('data-catalog', info['payload'])
    for section, status in enumerate(['complete', 'in-progress']):
        expect(page.locator('main > details').nth(section).locator('.lab')).to_have_count(sum(lab['status'] == status for lab in labs))
    for lab in labs:
        row = page.locator('#work-results .lab').filter(has=page.locator(f'a[href="{lab["exercise_url"]}"]'))
        expect(row.locator('.meta')).to_contain_text(payload['status_labels'][lab['status']])
        solution_label = '🔒 Solution' if 'solution' in lab.get('private_links', []) else 'Solution'
        solutions = row.get_by_role('link', name=solution_label, exact=True, include_hidden=True)
        expect(solutions).to_have_count(int(bool(lab['solution_url'])))
        if lab['solution_url']:
            expect(solutions).to_have_attribute('href', lab['solution_url'])
        if lab['status'] == 'complete':
            completion = 'Completed ' + lab['dates']['completed']
            expect(row.locator('.meta')).to_contain_text(completion)
            if lab['solution_url']:
                expect(row.locator('.meta')).to_contain_text(solution_label + ' · ' + completion)
        else:
            expect(row.locator('.meta')).not_to_contain_text('Completed ')
    page.keyboard.press('Tab')
    assert page.evaluate('document.activeElement.tagName') == 'A'
    page.locator('h1').click()
    page.screenshot(path=str(screenshots / 'desktop.png'))
    page.locator('#browse > summary').click()
    for facet in ['skill', 'tool', 'goal', 'subject']:
        key = {'skill': 'skills', 'tool': 'tools', 'goal': 'goals'}.get(facet)
        values = lambda lab: lab[key] if key else [lab['domain'] + ('/' + lab['subdomain'] if lab['subdomain'] else '')]
        value = next(values(lab)[0] for lab in labs if values(lab))
        page.locator(f'[data-facet="{facet}"]').click()
        page.locator('#browse-search').fill(value)
        page.locator('#browse-value').select_option(value)
        expect(page.locator('#work-results .lab')).to_have_count(sum(value in values(lab) for lab in labs))
    page.locator('#reset').click()
    page.locator('#browse > summary').click()
    first = labs[0]
    page.goto(url + '?lab=' + quote(first['path'], safe=''))

    # A saved lab link must reveal its result inside All labs
    expect(page.locator('#all-labs')).to_have_js_property('open', True)
    expect(page.locator('#work-results .lab')).to_have_count(1)
    page.reload()
    expect(page.locator('#work-results .lab')).to_have_count(1)
    page.locator('#reset').click()
    expect(page.locator('#work-results .lab')).to_have_count(len(labs))
    page.go_back()
    expect(page.locator('#work-results .lab')).to_have_count(1)
    page.locator('#reset').click()
    page.locator('#filter').select_option(json.dumps(['provider', first['provider']], separators=(',', ':')))
    expect(page.locator('#work-results .lab')).to_have_count(sum(lab['provider'] == first['provider'] for lab in labs))
    page.locator('#search').fill('no-such-lab-zzzzz')
    expect(page.locator('#empty-state')).to_be_visible()

    # Reload a saved search and keep its result visible
    page.reload()
    expect(page.locator('#all-labs')).to_have_js_property('open', True)
    expect(page.locator('#empty-state')).to_be_visible()

    page.locator('#reset').click()
    page.set_viewport_size({'width': 390, 'height': 844})
    page.evaluate('window.scrollTo(0, 0)')
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), 'Horizontal overflow'
    page.screenshot(path=str(screenshots / 'mobile.png'))
    page.locator('#work-results .collection > summary').first.click()
    expect(page.locator('#work-results .lab').first).to_be_visible()
    page.screenshot(path=str(screenshots / 'mobile-expanded.png'))
    page.emulate_media(color_scheme='dark')
    page.screenshot(path=str(screenshots / 'mobile-dark.png'))
    assert not errors, errors
    context.close()
    context = browser.new_context(java_script_enabled=False)
    page = context.new_page()
    page.goto(url)

    # Keep the same section defaults when JavaScript is turned off
    expect(page.locator('main > details[open]')).to_have_count(2)
    page.locator('#all-labs > summary').click()
    expect(page.locator('#work-results .lab')).to_have_count(len(labs))
    page.locator('#work-results .collection > summary').first.click()
    expect(page.locator('#work-results .lab').first).to_be_visible()
    context.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url')
    args = parser.parse_args()
    directory = ROOT / '.meta/build/pages'
    info = json.loads((directory / 'build-info.json').read_text())
    labs = json.loads((directory / info['payload']).read_text())['labs']
    screenshots = ROOT / '.meta/build/browser-smoke'
    screenshots.mkdir(parents=True, exist_ok=True)
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Handler, directory=str(directory)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            for url in [args.url] if args.url else [f'http://127.0.0.1:{server.server_port}/', f'http://127.0.0.1:{server.server_port}/labs/']:
                check(browser, url, labs, screenshots, info['source_commit'], published=bool(args.url))
            browser.close()
    finally:
        server.shutdown()
    print('Browser check passed: published snapshot, lifecycle sections, Solution links, filter/search, link/reload/back, narrow screen, and no-JS links.')


if __name__ == '__main__':
    main()
