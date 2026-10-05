#!/usr/bin/env python3
"""Sync staged lab work and generated views immediately before a commit."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import catalog
import lab_sync


def _names(*arguments: str) -> set[str]:
    return {os.fsdecode(name) for name in lab_sync._git(*arguments).split(b"\0") if name}


def _relevant(path: str) -> bool:
    return path.startswith("niches/") or path.startswith(".meta/catalog/") or path in {
        "CATALOG.md", "PRACTICE-ATLAS.md", ".meta/scripts/catalog.py", ".meta/scripts/lab_sync.py", ".meta/scripts/atlas.py", ".meta/scripts/lab_init.py",
    }


def _touched_labs(staged: set[str]) -> list[Path]:
    selected = []
    for metadata in catalog.lab_paths():
        root = metadata.parent.relative_to(catalog.ROOT).as_posix() + "/"
        if any(path.startswith(root) and path != root + "lab.json" for path in staged):
            selected.append(metadata.parent)
    return selected


def sync_for_commit() -> None:
    staged = _names("diff", "--cached", "--name-only", "-z")
    if not any(_relevant(path) for path in staged):
        return

    inputs = ("niches/", ".meta/catalog/sources.json", ".meta/catalog/atlas.json", ".meta/catalog/schema/", ".meta/scripts/catalog.py", ".meta/scripts/atlas.py", ".meta/scripts/lab_init.py", ".meta/scripts/lab_sync.py", ".meta/scripts/commit_sync.py")
    unstaged = _names("diff", "--name-only", "-z", "--", *inputs)
    untracked = _names("ls-files", "--others", "--exclude-standard", "-z", "--", *inputs)
    if unstaged or untracked:
        pending = sorted(unstaged | untracked)
        raise catalog.CatalogError("Unstaged lab/catalog inputs could enter this commit: " + ", ".join(pending) + ". Stage intended work first.")

    records, sources = catalog.collect_labs()
    expected = catalog.expected_catalogs(records, sources)
    unstaged_views = _names("diff", "--name-only", "-z", "--", "CATALOG.md", ".meta/catalog/labs.json", "PRACTICE-ATLAS.md")
    for path, content in expected.items():
        name = path.relative_to(catalog.ROOT).as_posix()
        if name in staged | unstaged_views and path.is_file() and path.read_text(encoding="utf-8") != content:
            raise catalog.CatalogError(f"Generated view has edits outside the generator: {name}. Update its inputs or regenerate it before committing.")

    touched = _touched_labs(staged)
    if touched:
        lab_sync.sync_all(paths=[str(path) for path in touched])
    else:
        catalog.write_catalog(records, sources)
    outputs = [str(path.relative_to(catalog.ROOT)) for path in expected]
    outputs += [str(path.relative_to(catalog.ROOT) / "lab.json") for path in touched]
    lab_sync._git("add", "--", *outputs)
    lab_sync.sync_all(check=True)
    catalog.update_catalog(check=True)


def main() -> int:
    try:
        sync_for_commit()
    except (catalog.CatalogError, OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
