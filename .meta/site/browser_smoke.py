#!/usr/bin/env python3
"""Short real-browser check of root/project mounts, filters and fallback HTML."""
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


def smoke(base, browser, screenshots, payload):
    errors = []
    context = browser.new_context(viewport={"width": 1440, "height": 1100})
    page = context.new_page()
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.on("console", lambda message: errors.append(message.text) if message.type == "error" else None)
    page.goto(base, wait_until="networkidle")
    expect(page.locator("#controls")).to_be_visible()
    expect(page.locator("#result-count")).to_have_text(f"{len(payload['labs'])} of {len(payload['labs'])} adopted labs")
    page.keyboard.press("Tab")
    assert page.evaluate("document.activeElement.tagName") == "A"
    page.locator("h1").click()
    page.screenshot(path=str(screenshots / "desktop.png"), full_page=False)
    first = payload['labs'][0]
    query = f"?domain={first['domain']}&niche={first['niche']}&provider={first['provider']}&status=not-started"
    page.goto(base + query)
    expected = sum(item['domain'] == first['domain'] and item['niche'] == first['niche'] and item['provider'] == first['provider'] and item['status'] == 'not-started' for item in payload['labs'])
    expect(page.locator("#result-count")).to_have_text(f"{expected} of {len(payload['labs'])} adopted labs")
    page.reload()
    expect(page.locator("#result-count")).to_have_text(f"{expected} of {len(payload['labs'])} adopted labs")
    page.locator("#reset").click()
    expect(page.locator("#result-count")).to_have_text(f"{len(payload['labs'])} of {len(payload['labs'])} adopted labs")
    page.go_back()
    expect(page.locator("#result-count")).to_have_text(f"{expected} of {len(payload['labs'])} adopted labs")
    page.go_forward()
    expect(page.locator("#result-count")).to_have_text(f"{len(payload['labs'])} of {len(payload['labs'])} adopted labs")
    page.goto(base + '?status=not-started&status=complete')
    matched = sum(item['status'] in ('not-started', 'complete') for item in payload['labs'])
    expect(page.locator("#result-count")).to_have_text(f"{matched} of {len(payload['labs'])} adopted labs")
    page.goto(base + '?view=atlas&tool=python&niche=code')
    matched = sum('python' in item['tools'] and item['niche'] == 'code' for item in payload['opportunities'])
    expect(page.locator("#result-count")).to_have_text(f"{matched} of {len(payload['opportunities'])} opportunities")
    page.goto(base + '?view=atlas&tool=kubernetes&goal=cka&niche=code')
    matched = sum('kubernetes' in item['tools'] and 'cka' in item['goals'] and item['niche'] == 'code' for item in payload['opportunities'])
    expect(page.locator("#result-count")).to_have_text(f"{matched} of {len(payload['opportunities'])} opportunities")
    page.goto(base + '?lab=' + quote(first['id'], safe=''))
    expect(page.locator('#work-results .lab')).to_have_count(1)
    page.locator('#sort').select_option('title')
    expect(page).to_have_url(__import__('re').compile('sort=title'))
    page.goto(base + '?lab=obsolete-path')
    expect(page.locator('#empty-state')).to_be_visible()
    page.locator('#empty-state a').click()
    expect(page.locator('#empty-state')).to_be_hidden()
    page.locator('#search').fill('<img src=x onerror=alert(1)>')
    expect(page.locator('#empty-state')).to_be_visible()
    expect(page.locator('#active-filters img')).to_have_count(0)
    page.locator('#reset').click()
    page.set_viewport_size({"width": 390, "height": 844})
    page.evaluate("window.scrollTo(0, 0)")
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'), "Horizontal overflow"
    page.screenshot(path=str(screenshots / 'mobile.png'), full_page=False)
    page.emulate_media(color_scheme='dark', reduced_motion='reduce')
    page.screenshot(path=str(screenshots / 'mobile-dark.png'), full_page=False)
    assert not errors, errors
    context.close()

    fallback = browser.new_context(java_script_enabled=False)
    page = fallback.new_page()
    page.goto(base)
    expect(page.locator('.lab')).to_have_count(len(payload['labs']))
    expect(page.locator('.opportunity')).to_have_count(len(payload['opportunities']))
    assert page.locator('.lab h4 a').first.get_attribute('href').startswith('https://github.com/')
    fallback.close()
    blocked = browser.new_context()
    page = blocked.new_page()
    page.route('**/catalog.*.json', lambda route: route.abort())
    page.goto(base)
    expect(page.locator('#load-warning')).to_be_visible()
    expect(page.locator('.lab')).to_have_count(len(payload['labs']))
    blocked.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=ROOT / '.meta/build/pages')
    parser.add_argument('--url', help='Optional deployed URL for an explicitly authorized live review')
    args = parser.parse_args()
    info = json.loads((args.directory / 'build-info.json').read_text())
    payload = json.loads((args.directory / info['payload']).read_text())
    screenshots = ROOT / '.meta/build/browser-smoke'
    screenshots.mkdir(parents=True, exist_ok=True)
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Handler, directory=str(args.directory)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            urls = [args.url] if args.url else [f'http://127.0.0.1:{server.server_port}/', f'http://127.0.0.1:{server.server_port}/labs/']
            for base in urls:
                smoke(base, browser, screenshots, payload)
                print(f'Browser smoke passed: {base}')
            browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    main()
