"""Static publishing has no authority over canonical metadata or lab progress."""
import hashlib
import json
import shutil
from pathlib import Path

from test_labs import HERE, RepositoryCase


class SiteTests(RepositoryCase):
    def setUp(self):
        super().setUp()
        shutil.copytree(HERE / '.meta/site', self.root / '.meta/site', ignore=shutil.ignore_patterns('__pycache__'))
        (self.root / '.gitignore').write_text('.meta/build/\n__pycache__/\n')
        (self.root / 'README.md').write_text('# Test workbench\n')
        (self.root / '.meta/catalog/atlas.json').write_text(json.dumps({'goals': {}, 'niche_guidance': [], 'opportunities': [], 'unresolved_sources': []}))

    def hashes(self, path):
        return {p.relative_to(path).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in path.rglob('*') if p.is_file()}

    def test_shared_payload_safe_links_and_deterministic_read_only_build(self):
        lab = self.init('code', 'systems', 'tasks', '<img src=x onerror=alert(1)>', '--slug', 'one', '--summary', '<script>bad()</script>', '--tool', 'python', '--goal', 'personal-goal')
        (lab / 'notes.md').write_text('# Personal solution\n\n## Evidence\nActual content\n')
        result = self.command('scripts', 'lab_meta.py', str(lab), '--link', 'solution=' + (lab / 'notes.md').relative_to(self.root).as_posix() + '#evidence', '--yes')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.git('add', '.')
        self.command('scripts', 'lab_sync.py', '--yes')
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')
        baseline = self.git('status', '--porcelain').stdout
        metadata = (lab / 'lab.json').read_bytes()
        for output in ['one', 'two']:
            built = self.command('scripts', 'build_site.py', '--output', '.meta/build/' + output, '--base-path', '/labs/', '--release')
            self.assertEqual(built.returncode, 0, built.stderr)
        one = self.root / '.meta/build/one'
        self.assertEqual(json.loads((one / 'build-info.json').read_text()), json.loads((self.root / '.meta/build/two/build-info.json').read_text()))
        self.assertEqual(self.hashes(one), self.hashes(self.root / '.meta/build/two'))
        info = json.loads((one / 'build-info.json').read_text())
        payload = json.loads((one / info['payload']).read_text())
        record = json.loads((self.root / '.meta/catalog/labs.json').read_text())[0]
        item = payload['labs'][0]
        self.assertEqual(item['id'], record['path'])
        self.assertEqual(item['dates'], record['tracking']['dates'])
        self.assertEqual(item['tools'], record['tools_effective'])
        self.assertEqual(item['goals'], record['goals_effective'])
        self.assertEqual(payload['counts']['labs'], 1)
        self.assertEqual(payload['counts']['opportunities'], 0)
        self.assertTrue(item['solution_url'].endswith('/notes.md#evidence'))
        self.assertIn(info['source_commit'], item['exercise_url'])
        html = (one / 'index.html').read_text()
        self.assertIn('&lt;script&gt;bad()', html)
        self.assertNotIn('<script>bad()', html)
        self.assertNotIn('source/manifest', json.dumps(payload))
        self.assertEqual(self.git('status', '--porcelain').stdout, baseline)
        self.assertEqual((lab / 'lab.json').read_bytes(), metadata)
        (one / 'escape').symlink_to(self.root / 'README.md')
        rejected = self.command('scripts', 'build_site.py', '--output', '.meta/build/one')
        self.assertIn('links', rejected.stderr)
        self.assertEqual((self.root / 'README.md').read_text(), '# Test workbench\n')

    def test_empty_corpus_stale_inputs_and_unmanaged_outputs(self):
        self.assertEqual(self.command('scripts', 'catalog.py').returncode, 0)
        self.git('add', '.')
        self.git('commit', '-qm', 'empty fixture')
        built = self.command('scripts', 'build_site.py')
        self.assertEqual(built.returncode, 0, built.stderr)
        html = (self.root / '.meta/build/pages/index.html').read_text()
        self.assertIn('No work adopted yet', html)
        refused = self.command('scripts', 'build_site.py', '--output', 'niches')
        self.assertIn('dedicated directory', refused.stderr)
        unmanaged = self.root / '.meta/build/unmanaged'
        unmanaged.mkdir()
        (unmanaged / 'keep.txt').write_text('preserve')
        refused = self.command('scripts', 'build_site.py', '--output', str(unmanaged.resolve()))
        self.assertIn('unmanaged', refused.stderr)
        self.assertEqual((unmanaged / 'keep.txt').read_text(), 'preserve')
        (self.root / 'CATALOG.md').write_text('stale')
        refused = self.command('scripts', 'build_site.py')
        self.assertIn('Stale catalog', refused.stderr)
        self.assertEqual((self.root / 'CATALOG.md').read_text(), 'stale')
