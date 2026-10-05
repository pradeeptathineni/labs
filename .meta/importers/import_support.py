"""Shared adoption preview/refresh guards around the existing initializer."""
import argparse
import hashlib
import subprocess
from pathlib import Path

import catalog
import lab_init
import workflow


def committed_paths(checkout, revision):
    result = subprocess.run(['git', '-C', str(checkout), 'ls-tree', '-r', '--name-only', revision], capture_output=True, text=True, check=True)
    return result.stdout.splitlines()


def parser(description):
    result = argparse.ArgumentParser(description=description)
    result.add_argument('--checkout', type=Path, required=True)
    result.add_argument('--list', action='store_true')
    result.add_argument('--track')
    selection = result.add_mutually_exclusive_group()
    selection.add_argument('--all-track', action='store_true')
    selection.add_argument('--item', action='append')
    result.add_argument('--destination')
    result.add_argument('--subdomain')
    result.add_argument('--refresh', action='store_true')
    result.add_argument('--dry-run', action='store_true')
    result.add_argument('--interactive', action='store_true')
    result.add_argument('--yes', action='store_true')
    return result


def select(args, items):
    if args.interactive and (args.yes or args.dry_run):
        raise catalog.CatalogError('--interactive cannot be combined with --yes or --dry-run')
    tracks = sorted({item['track'] for item in items})
    if args.list:
        for item in items:
            print(f"{item['track']} | {item['id']} | {item['data']['title']}")
        return []
    if args.interactive:
        args.track = workflow.prompt('Track', args.track, choices=tracks)
        keys = [item['id'] for item in items if item['track'] == args.track]
        selected = workflow.prompt('Item or all', 'all' if args.all_track else None, choices=keys + ['all'])
        args.all_track = selected == 'all'
        args.item = None if args.all_track else [selected]
        args.destination = workflow.prompt('Destination collection', args.destination)
        current = lab_init.destination(args.destination)['subdomain']
        args.subdomain = workflow.prompt('Subject subdomain', args.subdomain or current, optional=True)
    if args.track not in tracks or not args.destination or not (args.item or args.all_track):
        raise catalog.CatalogError('Choose --track, --destination and --item or --all-track; use --list')
    candidates = {item['id']: item for item in items if item['track'] == args.track}
    keys = list(candidates) if args.all_track else args.item
    if len(set(keys)) != len(keys):
        raise catalog.CatalogError('Duplicate adoption selection')
    if set(keys) - set(candidates):
        raise catalog.CatalogError('Unknown source item in selected track')
    return [candidates[key] for key in keys]


def manifest(files):
    return catalog.json_text({name: hashlib.sha256(content.encode()).hexdigest() for name, content in sorted(files.items())})


def protected_files(path):
    record = catalog.read_json(path / 'source/manifest.json')
    if not isinstance(record, dict) or not record:
        raise catalog.CatalogError('Invalid importer manifest')
    contents = {}
    for name, expected in record.items():
        relative = Path(name)
        if relative.is_absolute() or '..' in relative.parts or not name.startswith('source/') or name == 'source/manifest.json':
            raise catalog.CatalogError('Unsafe importer-owned path')
        target = path / name
        if target.is_symlink() or any(parent.is_symlink() for parent in target.parents if parent.is_relative_to(path)):
            raise catalog.CatalogError('Importer-owned source cannot be a symlink')
        actual = target.read_text(encoding='utf-8')
        if hashlib.sha256(actual.encode()).hexdigest() != expected:
            raise catalog.CatalogError(f'Importer-owned file changed: {catalog.display_path(target)}')
        contents[name] = actual
    return contents


def adopt(args, items, provider, sources):
    selected = select(args, items)
    if args.list:
        return
    destination = lab_init.destination(args.destination, args.subdomain)
    parent = lab_init._parent(destination)
    records, _ = catalog.collect_labs()
    existing = {(r['source']['provider'], r['source'].get('item_id')): r for r in records}
    plans, updates = [], []
    for item in selected:
        files = item['files']
        owned = {name: content for name, content in files.items() if name != 'README.md'}
        if any(not name.startswith('source/') for name in owned):
            raise catalog.CatalogError('Only source snapshots belong to this adapter')
        owned_manifest = manifest(owned)
        files = {**files, 'source/manifest.json': owned_manifest}
        prior = existing.get((provider, item['id']))
        if prior:
            path = catalog.ROOT / prior['path']
            if path.parent != parent:
                raise catalog.CatalogError('Existing source item is in another collection')
            old = protected_files(path)
            if set(old) != set(owned):
                raise catalog.CatalogError('Snapshot file selection changed; review adapter migration explicitly')
            if old == owned and prior['source'].get('revision') == item['data']['revision']:
                print(f'No change: {prior["path"]}')
                continue
            if not args.refresh:
                raise catalog.CatalogError(f'Changed upstream item {item["id"]}; use --refresh')
            metadata = catalog.ordered_lab(catalog.read_json(path / 'lab.json'))
            metadata['source'].update(revision=item['data']['revision'], url=item['data']['source_url'])
            changed = {name: text for name, text in {**owned, 'source/manifest.json': owned_manifest}.items() if (path / name).read_text(encoding='utf-8') != text}
            updates.append((path, metadata, changed))
        else:
            data = {**destination, **item['data'], 'provider': provider, 'item_id': item['id']}
            plans.append(lab_init.plan_lab(data, sources, files=files, existing_plans=plans))
    overrides = {plan['path'] / 'lab.json': plan['metadata'] for plan in plans}
    overrides.update({path / 'lab.json': metadata for path, metadata, _ in updates})
    catalog.collect_labs(overrides=overrides, collection_overrides=lab_init.collection_updates(plans))
    for plan in plans:
        lab_init.preview_plan(plan)
    for path, metadata, changed in updates:
        workflow.preview(catalog.display_path(path), metadata, [*changed, 'lab.json'])
        print('Review the original README definition and source links manually; personal content is preserved.')
    if args.dry_run:
        return
    if not args.interactive and not args.yes:
        raise catalog.CatalogError('Writing requires --yes')
    if args.interactive and not workflow.confirm():
        print('No changes made.')
        return
    if plans:
        lab_init.write_plans(plans, sources)
    for path, metadata, changed in updates:
        for name, text in changed.items():
            catalog.write_text_atomic(path / name, text)
        catalog.write_text_atomic(path / 'lab.json', catalog.json_text(metadata))
    if updates:
        catalog.update_catalog()
    print(f'Adopted {len(plans)} new units; refreshed {len(updates)} units.')
