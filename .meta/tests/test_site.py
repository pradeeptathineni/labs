"""A build must preserve the catalog, escape text, and be reproducible."""
import hashlib
import json
import shutil

from test_labs import HERE, RepositoryCase


class SiteTests(RepositoryCase):
    def test_catalog_build_is_safe_and_read_only(self):
        shutil.copytree(HERE / '.meta/site', self.root / '.meta/site', ignore=shutil.ignore_patterns('__pycache__'))
        (self.root / '.gitignore').write_text('.meta/build/\n__pycache__/\n')
        (self.root / 'README.md').write_text('# Labs\n')
        (self.root / '.meta/catalog/atlas.json').write_text(json.dumps({'goals': {}, 'niche_guidance': [], 'opportunities': [], 'unresolved_sources': []}))
        lab = self.init('code', 'systems', 'tasks', 'One', '--summary', '<script>bad()</script>', '--tool', 'python')
        self.git('add', '.')
        self.command('scripts', 'lab_sync.py', '--yes')
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')
        metadata = (lab / 'lab.json').read_bytes()
        outputs = [self.root / '.meta/build' / name for name in ('one', 'two')]
        for output in outputs:
            built = self.command('scripts', 'build_site.py', '--output', output.relative_to(self.root).as_posix(), '--base-path', '/labs/', '--release')
            self.assertEqual(built.returncode, 0, built.stderr)
        hashes = lambda folder: {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.rglob('*') if p.is_file()}
        self.assertEqual(hashes(outputs[0]), hashes(outputs[1]))
        info = json.loads((outputs[0] / 'build-info.json').read_text())
        payload = json.loads((outputs[0] / info['payload']).read_text())
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
        self.assertEqual(self.git('status', '--porcelain').stdout, '')
        (outputs[0] / 'escape').symlink_to(self.root / 'README.md')
        rejected = self.command('scripts', 'build_site.py', '--output', '.meta/build/one')
        self.assertIn('links', rejected.stderr)
        self.assertEqual((self.root / 'README.md').read_text(), '# Labs\n')
