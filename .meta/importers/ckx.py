#!/usr/bin/env python3
"""Adopt CK-X assessment identities and pinned links, without copying bodies."""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import catalog
import workflow
import import_support

PROVIDER = 'ck-x'
REPO = 'sailor-sh/CK-X'
INDEX = 'facilitator/assets/exams/labs.json'


def inventory(checkout, sources):
    catalog.source_for(PROVIDER, sources)
    revision, committed = workflow.git_checkout(checkout, REPO, [INDEX, 'LICENSE'])
    license_text = committed['LICENSE'].decode()
    if 'Business Source License 1.1' not in license_text:
        raise catalog.CatalogError('The committed CK-X license needs a new review')
    index = json.loads(committed[INDEX])
    if not isinstance(index, dict) or not isinstance(index.get('labs'), list):
        raise catalog.CatalogError('Expected a CK-X labs index')
    selected = [item for item in index['labs'] if item.get('category') in ('CKA', 'CKAD', 'CKS')]
    ids = [item.get('id') for item in selected]
    if len(ids) != len(set(ids)) or not all(isinstance(value, str) and catalog.SLUG_PATTERN.fullmatch(value) for value in ids):
        raise catalog.CatalogError('Duplicate or invalid upstream assessment identity')
    items = []
    for row in sorted(selected, key=lambda item: item['id']):
        track = row['category'].lower()
        if not re.fullmatch(r'assets/exams/' + track + r'/[0-9]+', row.get('assetPath', '')):
            raise catalog.CatalogError('Unexpected assessment asset path')
        folder = 'facilitator/' + row['assetPath']
        paths = [folder + '/assessment.json', folder + '/config.json']
        _, assets = workflow.git_checkout(checkout, REPO, paths)
        assessment = json.loads(assets[paths[0]])
        config = json.loads(assets[paths[1]])
        questions = assessment.get('questions')
        if not isinstance(questions, list) or not questions or config.get('lab') != row['id'] or config.get('questions') != 'assessment.json':
            raise catalog.CatalogError('Assessment metadata does not match its index identity')
        question_ids = [question.get('id') for question in questions]
        if len(question_ids) != len(set(question_ids)) or not all(isinstance(value, str) and value for value in question_ids):
            raise catalog.CatalogError('Invalid or duplicate question IDs inside assessment')
        url = f'https://github.com/{REPO}/blob/{revision}/{paths[0]}'
        setup = f'https://github.com/{REPO}/tree/{revision}/{folder}'
        license_url = f'https://github.com/{REPO}/blob/{revision}/LICENSE'
        readme = f'''# {row['name']}

Source: [CK-X assessment `{row['id']}`]({url})

## Exercise Definition

Independently attempt the complete **{row['name']}** assessment (`{row['id']}`), containing {len(questions)} upstream tasks at this revision. Preserve its task IDs when recording commands, reasoning, verification and any incomplete attempts.

Read the [pinned assessment]({url}) and its [environment metadata and dependencies]({setup}) before planning an authorized practice environment. The source uses a simulator and setup/validation scripts; none have been run for this adoption. Reference answers remain upstream and are not my work.

This is a source-linked assessment. Its body, answers and executable assets are not copied here. The [BSL 1.1 notice and additional conditions]({license_url}) require a scoped review before copying or running the simulator. This practice set does not establish official exam alignment or readiness.

## Solution
'''
        snapshot = {'id': row['id'], 'name': row['name'], 'assessment_path': paths[0], 'revision': revision,
                    'question_ids': question_ids, 'assessment_sha256': hashlib.sha256(assets[paths[0]]).hexdigest(),
                    'config_sha256': hashlib.sha256(assets[paths[1]]).hexdigest(), 'handling': 'linked; bodies, answers and executable assets not copied'}
        data = {'title': row['name'], 'slug': row['id'], 'type': 'problem-set', 'skills': ['orchestration', 'troubleshooting'],
                'source_url': url, 'revision': revision, 'collection_descriptor': {'title': 'CK-X assessments', 'has_subdomain': True, 'tools': ['kubernetes'], 'goals': [track]}}
        items.append({'id': row['id'], 'track': track, 'data': data, 'files': {'README.md': readme, 'source/item.json': catalog.json_text(snapshot)}})
    return items


def main():
    args = import_support.parser(__doc__).parse_args()
    try:
        sources = catalog.load_sources()
        import_support.adopt(args, inventory(args.checkout, sources), PROVIDER, sources)
    except (catalog.CatalogError, OSError, ValueError, EOFError, KeyboardInterrupt) as error:
        if isinstance(error, (EOFError, KeyboardInterrupt)):
            print('\nNo changes made.')
            return 0
        print(f'error: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
