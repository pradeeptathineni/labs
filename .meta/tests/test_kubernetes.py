"""A small source fixture checks adoption ownership, repeats and refreshes."""
import json

from test_labs import RepositoryCase


class KubernetesTests(RepositoryCase):
    def test_adapters_preserve_personal_work_and_source_boundaries(self):
        sources = json.loads((self.root / '.meta/catalog/sources.json').read_text())
        sources['platformlab-cka']['reuse']['policy'] = 'copy'
        (self.root / '.meta/catalog/sources.json').write_text(json.dumps(sources))
        assessment = 'facilitator/assets/exams/cka/001/assessment.json'
        fixtures = [
            ('platformlab.py', 'theplatformlab/CKA-Certified-Kubernetes-Administrator', 'exercises', {
                'README.md': '# Source\n', 'LICENSE': 'MIT License\nPermission is hereby granted\n',
                'exercises/01-pods/README.md': '# Pods\n\n## Tasks\n\nInspect a [dependency](../../missing.yaml).\n\n## Hints\n\nUpstream answer.\n',
            }, 'exercises/01-pods/README.md'),
            ('ckx.py', 'sailor-sh/CK-X', 'cka', {
                'LICENSE': 'Business Source License 1.1\n',
                'facilitator/assets/exams/labs.json': json.dumps({'labs': [{'id': 'cka-001', 'name': 'First assessment', 'category': 'CKA', 'assetPath': 'assets/exams/cka/001'}, {'category': 'Other'}]}),
                assessment: json.dumps({'questions': [{'id': 'one', 'answer': 'Upstream answer'}]}),
                'facilitator/assets/exams/cka/001/config.json': json.dumps({'lab': 'cka-001', 'questions': 'assessment.json'}),
            }, assessment),
        ]
        for script, repo, track, files, changed in fixtures:
            with self.subTest(script=script):
                upstream = self.upstream(script, files, 'https://github.com/' + repo)
                collection = 'niches/code/devops/orchestration/' + script.removesuffix('.py')
                args = ('--checkout', str(upstream), '--track', track, '--all-track', '--destination', collection, '--subdomain', 'orchestration')
                preview = self.command('importers', script, *args, '--dry-run')
                self.assertEqual(preview.returncode, 0, preview.stderr)
                self.assertFalse((self.root / collection).exists())
                canceled = self.command('importers', script, *args, '--interactive', stdin='\n\n\n\nn\n')
                self.assertEqual(canceled.returncode, 0, canceled.stderr)
                self.assertFalse((self.root / collection).exists())
                applied = self.command('importers', script, *args, '--yes')
                self.assertEqual(applied.returncode, 0, applied.stderr)
                lab = next((self.root / collection).glob('*/lab.json')).parent
                readme = (lab / 'README.md').read_text()
                self.assertEqual(readme.split('## Solution')[1].strip(), '')
                if script == 'ckx.py':
                    self.assertNotIn('Upstream answer', ''.join(p.read_text() for p in (lab / 'source').glob('*')))
                else:
                    self.assertIn('upstream target unavailable', (lab / 'source/UPSTREAM.md').read_text())
                (lab / 'README.md').write_text(readme + '\nMy independent attempt.\n')
                saved = (lab / 'README.md').read_bytes()
                repeat = self.command('importers', script, *args, '--yes')
                self.assertIn('Adopted 0 new units', repeat.stdout)
                target = upstream / changed
                target.write_text(target.read_text().replace('Upstream answer', 'Revised upstream answer'))
                self.git('add', '.', cwd=upstream)
                self.git('commit', '-qm', 'source revision', cwd=upstream)
                refused = self.command('importers', script, *args, '--yes')
                self.assertIn('--refresh', refused.stderr)
                refreshed = self.command('importers', script, *args, '--refresh', '--yes')
                self.assertEqual(refreshed.returncode, 0, refreshed.stderr)
                self.assertEqual((lab / 'README.md').read_bytes(), saved)
                self.assertEqual(self.metadata(lab)['tracking']['status'], 'not-started')
