#!/usr/bin/env python3
"""Initialize a collection before its first lab, using the shared hierarchy."""

from __future__ import annotations

import argparse
import sys

import catalog
import lab_init
import workflow


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('niche', 'domain', 'collection'):
        parser.add_argument(name)
    parser.add_argument('--subdomain')
    parser.add_argument('--group', dest='groups', action='append', default=[])
    parser.add_argument('--title', required=True)
    parser.add_argument('--source-url')
    parser.add_argument('--ordered', action='store_true')
    parser.add_argument('--tool', action='append', default=[])
    parser.add_argument('--goal', action='append', default=[])
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--yes', action='store_true')
    args = parser.parse_args()
    if not args.dry_run and not args.yes:
        parser.error('writing requires --yes')
    try:
        parent = lab_init._parent(vars(args))
        if (parent / 'collection.json').exists():
            raise catalog.CatalogError('Collection already initialized: ' + catalog.display_path(parent))
        descriptor = {'title': args.title.strip(), 'has_subdomain': bool(args.subdomain)}
        if args.source_url:
            descriptor['source_url'] = catalog.safe_url(args.source_url)
        if args.ordered:
            descriptor['ordered'] = True
        for key, values in (('tools', args.tool), ('goals', args.goal)):
            if values:
                descriptor[key] = sorted(set(values))
        catalog.validate_document(descriptor, catalog.load_schema(catalog.COLLECTION_SCHEMA_PATH), 'proposed collection')
        catalog.collect_labs(collection_overrides={parent: descriptor})
        workflow.preview(catalog.display_path(parent), descriptor, ['collection.json', 'README.md'])
        if args.dry_run:
            return 0
        catalog.write_text_atomic(parent / 'collection.json', catalog.json_text(descriptor))
        if not (parent / 'README.md').exists():
            reference = f'\n[Original program or collection]({args.source_url})\n' if args.source_url else ''
            catalog.write_text_atomic(parent / 'README.md', f'# {args.title.strip()}\n{reference}')
        catalog.update_catalog()
        print('Initialized ' + catalog.display_path(parent))
    except (catalog.CatalogError, OSError) as error:
        print(f'error: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
