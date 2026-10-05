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


def check(browser, url, labs, screenshots):
    context = browser.new_context(viewport={'width': 1440, 'height': 900})
    page = context.new_page()
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(url, wait_until='networkidle')
    expect(page.locator('#result-count')).to_have_text(f'{len(labs)} of {len(labs)} labs')
    expect(page.locator('main > details')).to_have_count(4)
    expect(page.locator("#work-results .collection[open]")).to_have_count(0)
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
                check(browser, url, labs, screenshots)
            browser.close()
    finally:
        server.shutdown()
    print('Browser check passed: catalog, filter/search, link/reload/back, narrow screen, and no-JS links.')


if __name__ == '__main__':
    main()
