"""A build must preserve the catalog, escape text, and be reproducible."""
import hashlib
import json
import re
import shutil

from test_labs import HERE, RepositoryCase


class SiteTests(RepositoryCase):
    def test_private_repository_links_are_marked_in_both_views(self):
        shutil.copytree(HERE / '.meta/site', self.root / '.meta/site', ignore=shutil.ignore_patterns('__pycache__'))
        (self.root / 'README.md').write_text('# Labs\n')
        (self.root / '.meta/catalog/atlas.json').write_text(json.dumps({'goals': {}, 'niche_guidance': [], 'opportunities': [], 'unresolved_sources': []}))
        repository = 'https://github.com/example/private'
        registry = self.root / '.meta/catalog/repository-visibility.json'
        registry.write_text(json.dumps({repository: 'private'}))
        collection = self.root / 'niches/code/devops/tasks'
        collection.mkdir(parents=True)
        (collection / 'collection.json').write_text(json.dumps({'source_url': repository + '/tree/main'}))
        lab = self.init('code', 'devops', 'tasks', 'Private links', '--source', 'organization',
                        '--source-url', repository + '/blob/main/brief.md',
                        '--link', 'solution=https://github.com/EXAMPLE/PRIVATE/tree/main/solution',
                        '--link', 'demo=https://raw.githubusercontent.com/example/private/main/demo.md')
        for name, target in [('Public', repository + '-public'), ('Unknown', 'https://github.com/example/unknown'),
                             ('Other host', 'https://github.com.example.invalid/example/private')]:
            self.init('code', 'devops', 'other', name, '--link', 'solution=' + target)
        self.git('add', '.')
        self.git('commit', '-qm', 'private link fixture')
        before = (lab / 'lab.json').read_bytes()
        for visibility in ('private', 'public'):
            registry.write_text(json.dumps({repository: visibility}))
            generated = self.command('scripts', 'catalog.py')
            self.assertEqual(generated.returncode, 0, generated.stderr)
            built = self.command('scripts', 'build_site.py')
            self.assertEqual(built.returncode, 0, built.stderr)
            markdown = (self.root / 'CATALOG.md').read_text()
            output = self.root / '.meta/build/pages'
            html = (output / 'index.html').read_text()
            info = json.loads((output / 'build-info.json').read_text())
            labs = json.loads((output / info['payload']).read_text())['labs']
            item = next(item for item in labs if item['title'] == 'Private links')
            expected = ['solution', 'demo', 'source', 'collection_source'] if visibility == 'private' else []
            self.assertEqual(item.get('private_links', []), expected)
            for label in ('Solution', 'Demo', 'ref'):
                self.assertEqual('[🔒 ' + label + ']' in markdown, visibility == 'private')
                self.assertEqual('>🔒 ' + label + '</a>' in html, visibility == 'private')
            for item in labs:
                if item['title'] != 'Private links':
                    self.assertEqual(item.get('private_links', []), [])
            self.assertIn('[Private links]', markdown)
            self.assertNotIn('[🔒 Private links]', markdown)
            self.assertEqual((lab / 'lab.json').read_bytes(), before)

    def test_historical_completion_dates_reconcile_with_markdown_and_site(self):
        shutil.copytree(HERE / '.meta/site', self.root / '.meta/site', ignore=shutil.ignore_patterns('__pycache__'))
        (self.root / 'README.md').write_text('# Labs\n')
        (self.root / '.meta/catalog/atlas.json').write_text(json.dumps({'goals': {}, 'niche_guidance': [], 'opportunities': [], 'unresolved_sources': []}))
        history = ('--created', '2023-04-09', '--started', '2023-04-09', '--status', 'complete', '--completed', '2023-04-30')
        linked = self.init('code', 'devops', 'tasks', 'Historical solution', *history, '--link', 'solution=https://example.com/private')
        unlinked = self.init('code', 'devops', 'tasks', 'Finished without link', *history)
        self.init('code', 'devops', 'tasks', 'Planned')
        original_dates = self.metadata(linked)['tracking']['dates']
        self.git('add', '.')
        self.git('commit', '-qm', 'historical fixture')

        # Content recording and reopening must retain the original completion.
        readme = linked / 'README.md'
        readme.write_text(readme.read_text() + '\nLater maintenance notes.\n')
        self.git('add', '.')
        synced = self.command('scripts', 'lab_sync.py', '--yes')
        self.assertEqual(synced.returncode, 0, synced.stderr)
        for status in ('complete', 'in-progress', 'complete'):
            changed = self.command('scripts', 'lab_meta.py', str(linked), '--status', status, '--yes')
            self.assertEqual(changed.returncode, 0, changed.stderr)
            dates = self.metadata(linked)['tracking']['dates']
            for name in ('created', 'started', 'completed'):
                self.assertEqual(dates[name], original_dates[name])
            self.assertNotEqual(dates['updated'], dates['completed'])
            before = {lab: (lab / 'lab.json').read_bytes() for lab in (linked, unlinked)}
            built = self.command('scripts', 'build_site.py')
            self.assertEqual(built.returncode, 0, built.stderr)
            markdown = (self.root / 'CATALOG.md').read_text()
            html = (self.root / '.meta/build/pages/index.html').read_text()
            for lab, current_status in ((linked, status), (unlinked, 'complete')):
                path = lab.relative_to(self.root).as_posix()
                md_rows = [line for line in markdown.splitlines() if path + '/README.md' in line and '<br>' in line]
                html_rows = re.findall(r'<li class="lab" data-path="' + re.escape(path) + r'"[^>]*>(.*?)</li>', html)
                self.assertTrue(md_rows)
                self.assertTrue(html_rows)
                for row in md_rows + html_rows:
                    self.assertEqual('Completed 2023-04-30' in row, current_status == 'complete')
                    self.assertIn('Updated ' + self.metadata(lab)['tracking']['dates']['updated'], row)
                if lab == linked and current_status == 'complete':
                    self.assertTrue(all('[Solution](https://example.com/private) · Completed 2023-04-30' in row for row in md_rows))
                    self.assertTrue(all('>Solution</a> · Completed 2023-04-30' in row for row in html_rows))
                self.assertEqual((lab / 'lab.json').read_bytes(), before[lab])

    def test_full_lifecycle_through_hook_and_release_snapshots(self):
        shutil.copytree(HERE / '.meta/site', self.root / '.meta/site', ignore=shutil.ignore_patterns('__pycache__'))
        (self.root / '.gitignore').write_text('.meta/build/\n__pycache__/\n')
        (self.root / 'README.md').write_text('# Labs\n')
        (self.root / '.meta/catalog/atlas.json').write_text(json.dumps({'goals': {}, 'niche_guidance': [], 'opportunities': [], 'unresolved_sources': []}))
        hook = self.root / '.githooks/pre-commit'
        hook.parent.mkdir()
        shutil.copy2(HERE / '.githooks/pre-commit', hook)
        hook.chmod(0o755)
        self.git('config', 'core.hooksPath', '.githooks')
        lab = self.init('code', 'devops', 'tasks', 'Lifecycle')
        previous = None
        for status in ['not-started', 'in-progress', 'complete', 'in-progress', 'complete']:
            if status != 'not-started':
                result = self.command('scripts', 'lab_meta.py', str(lab), '--status', status, '--yes')
                self.assertEqual(result.returncode, 0, result.stderr)
            if status == 'in-progress' and previous is None:
                readme = lab / 'README.md'
                readme.write_text(readme.read_text() + '\nI reproduced the behavior and recorded the evidence.\n')
                self.assertEqual(self.metadata(lab)['tracking']['status'], status)
            self.git('add', '.')
            self.git('commit', '-qm', status)
            self.assertEqual(self.git('status', '--porcelain').stdout, '')
            before = (lab / 'lab.json').read_bytes()
            result = self.command('scripts', 'build_site.py', '--release')
            self.assertEqual(result.returncode, 0, result.stderr)
            output = self.root / '.meta/build/pages'
            info = json.loads((output / 'build-info.json').read_text())
            record = json.loads((output / info['payload']).read_text())['labs'][0]
            self.assertEqual(record['status'], status)
            self.assertIn(info['source_commit'], record['exercise_url'])
            self.assertEqual(bool(record['solution_url']), status != 'not-started')
            dates = self.metadata(lab)['tracking']['dates']
            if previous:
                self.assertEqual(dates['started'], previous['started'])
                self.assertEqual(dates['completed'], previous['completed'])
            if status == 'complete':
                previous = dates
                self.assertIsNotNone(dates['completed'])
            self.assertEqual((lab / 'lab.json').read_bytes(), before)
            self.assertEqual(self.git('status', '--porcelain').stdout, '')

    # Keep archived checks out of the site while preserving normal labs
    def test_catalog_build_is_safe_and_read_only(self):
        shutil.copytree(HERE / '.meta/site', self.root / '.meta/site', ignore=shutil.ignore_patterns('__pycache__'))
        (self.root / '.gitignore').write_text('.meta/build/\n__pycache__/\n')
        (self.root / 'README.md').write_text('# Labs\n')
        (self.root / '.meta/catalog/atlas.json').write_text(json.dumps({'goals': {}, 'niche_guidance': [], 'opportunities': [], 'unresolved_sources': []}))
        lab = self.init('code', 'systems', 'tasks', 'One', '--summary', '<script>bad()</script>', '--tool', 'python')

        # An archived record must not count as another learning lab
        archive = self.root / '.meta/archive'
        archive.mkdir()
        (archive / 'lab.json').write_bytes((lab / 'lab.json').read_bytes())

        self.git('add', '.')
        self.command('scripts', 'lab_sync.py', '--yes')
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')
        metadata = (lab / 'lab.json').read_bytes()
        receipt = self.root / '.meta/build/catalog-generation.json'
        receipt.unlink()  # Release verification must not depend on local receipts.
        outputs = [self.root / '.meta/build' / name for name in ('one', 'two')]
        for output in outputs:
            built = self.command('scripts', 'build_site.py', '--output', output.relative_to(self.root).as_posix(), '--base-path', '/labs/', '--release')
            self.assertEqual(built.returncode, 0, built.stderr)
        hashes = lambda folder: {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.rglob('*') if p.is_file()}
        self.assertEqual(hashes(outputs[0]), hashes(outputs[1]))
        info = json.loads((outputs[0] / 'build-info.json').read_text())
        payload = json.loads((outputs[0] / info['payload']).read_text())

        # Both the static page and search data must use the learning labs only
        self.assertEqual(info['lab_count'], 1)
        self.assertEqual(len(payload['labs']), 1)

        record = json.loads((self.root / '.meta/catalog/labs.json').read_text())[0]
        item = payload['labs'][0]
        self.assertEqual(item['path'], record['path'])
        self.assertEqual(item['dates'], record['tracking']['dates'])
        self.assertEqual(item['tools'], record['tools_effective'])
        self.assertIn(info['source_commit'], item['exercise_url'])
        html = (outputs[0] / 'index.html').read_text()
        self.assertIn('&lt;script&gt;bad()', html)
        self.assertNotIn('<script>bad()', html)
        self.assertEqual((lab / 'lab.json').read_bytes(), metadata)
        self.assertFalse(receipt.exists())
        self.assertEqual(self.git('status', '--porcelain').stdout, '')
        (outputs[0] / 'escape').symlink_to(self.root / 'README.md')
        rejected = self.command('scripts', 'build_site.py', '--output', '.meta/build/one')
        self.assertIn('links', rejected.stderr)
        self.assertEqual((self.root / 'README.md').read_text(), '# Labs\n')
