#!/usr/bin/env python3
"""Skip an obsolete site snapshot; input-equivalent main advances are eligible."""
import argparse
import os
import sys

import catalog
import lab_sync

# Keep aligned with pages.yml paths. Untracked/ignored build output is never input.
PREFIXES = ('niches/', '.meta/', '.githooks/')
FILES = {'.github/workflows/pages.yml', '.github/workflows/catalog.yml', 'README.md', 'CATALOG.md', 'PRACTICE-ATLAS.md', '.gitignore', '.gitattributes'}


def relevant(path):
    return path.startswith(PREFIXES) or path in FILES


def changed_inputs(candidate, main):
    # Compare endpoint trees, not commit counts: unrelated main changes are fine.
    names = lab_sync._git('diff', '--name-only', '-z', candidate, main, '--').split(b'\0')
    return sorted(os.fsdecode(name) for name in names if name and relevant(os.fsdecode(name)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', default='HEAD')
    parser.add_argument('--compare-ref', help='Use an existing local ref for offline checks')
    args = parser.parse_args()
    try:
        target = args.compare_ref
        if not target:
            # Public, read-only fetch; checkout does not retain workflow credentials.
            lab_sync._git('fetch', '--no-tags', 'https://github.com/pradeeptathineni/labs.git', 'refs/heads/main')
            target = 'FETCH_HEAD'
        changed = changed_inputs(args.candidate, target)
        fresh = not changed
        print('eligible=' + str(fresh).lower())
        if changed:
            print('Skipping stale site inputs: ' + ', '.join(changed))
        else:
            print('Candidate matches the current site inputs on main.')
        if os.environ.get('GITHUB_OUTPUT'):
            with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
                output.write('eligible=' + str(fresh).lower() + '\n')
    except (catalog.CatalogError, OSError) as error:
        print(f'error: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
