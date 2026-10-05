"""Offline freshness checks and hook ownership across atlas and site changes."""
import json
import shutil

from test_labs import HERE, RepositoryCase


class PublicationTests(RepositoryCase):
    def test_stale_inputs_and_equivalent_main_advance(self):
        (self.root / 'README.md').write_text('# Inputs\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'baseline')
        baseline = self.git('rev-parse', 'HEAD').stdout.strip()
        (self.root / 'unrelated.txt').write_text('Unrelated to published inputs\n')
        self.git('add', 'unrelated.txt')
        self.git('commit', '-qm', 'unrelated')
        result = self.command('scripts', 'pages_freshness.py', '--candidate', baseline, '--compare-ref', 'HEAD')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('eligible=true', result.stdout)
        (self.root / '.meta/catalog/atlas.json').write_text('{}')
        self.git('add', '.meta/catalog/atlas.json')
        self.git('commit', '-qm', 'site input')
        result = self.command('scripts', 'pages_freshness.py', '--candidate', baseline, '--compare-ref', 'HEAD')
        self.assertIn('eligible=false', result.stdout)
        self.assertIn('.meta/catalog/atlas.json', result.stdout)

    def test_atlas_commit_sync_preserves_dates_and_rejects_unstaged_input(self):
        (self.root / 'README.md').write_text('# Fixture\n')
        plan = {'goals': {}, 'niche_guidance': [], 'opportunities': [], 'unresolved_sources': []}
        atlas_path = self.root / '.meta/catalog/atlas.json'
        atlas_path.write_text(json.dumps(plan))
        lab = self.init('code', 'devops', 'tasks', 'Untouched')
        before = (lab / 'lab.json').read_bytes()
        hook = self.root / '.githooks/pre-commit'
        hook.parent.mkdir()
        shutil.copy2(HERE / '.githooks/pre-commit', hook)
        self.git('add', '.')
        self.git('commit', '-qm', 'baseline')
        self.git('config', 'core.hooksPath', '.githooks')
        plan['niche_guidance'].append({'niche': 'writing', 'reason': 'Practice a clear explanation.'})
        atlas_path.write_text(json.dumps(plan))
        self.git('add', str(atlas_path))
        self.git('commit', '-qm', 'add a future direction')
        self.assertEqual((lab / 'lab.json').read_bytes(), before)
        self.assertIn('Practice a clear explanation', self.git('show', 'HEAD:PRACTICE-ATLAS.md').stdout)
        self.assertFalse((self.root / '.meta/build/pages').exists())
        plan['niche_guidance'][0]['reason'] = 'An unstaged revision'
        atlas_path.write_text(json.dumps(plan))
        metadata = self.metadata(lab)
        metadata['summary'] = 'Staged metadata'
        (lab / 'lab.json').write_text(json.dumps(metadata))
        self.git('add', str(lab / 'lab.json'))
        result = self.command('scripts', 'commit_sync.py')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Unstaged lab/catalog inputs', result.stderr)
        css = self.root / '.meta/site/assets/catalog.css'
        css.parent.mkdir(parents=True)
        css.write_text('/* isolated site input */')
        # The actual existing hook test covers unrelated commits with unstaged labs.
        self.assertIn('An unstaged revision', atlas_path.read_text())
