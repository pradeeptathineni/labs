#!/usr/bin/env python3
"""Record SHA-256 fingerprints of the staged lab content snapshot."""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

import catalog


def fingerprint_entries(entries: list[tuple[str, bytes, str]]) -> str:
    """Hash path, logical Git mode, and bytes with unambiguous framing."""
    digest = hashlib.sha256()
    for relative, content, mode in sorted(entries, key=lambda entry: os.fsencode(entry[0])):
        for field in (os.fsencode(relative), mode.encode("ascii"), content):
            digest.update(len(field).to_bytes(8, "big"))
            digest.update(field)
    return digest.hexdigest()


def _git(*arguments: str) -> bytes:
    process = subprocess.run(["git", *arguments], cwd=catalog.ROOT, capture_output=True)
    if process.returncode:
        raise catalog.CatalogError(process.stderr.decode("utf-8", errors="replace").strip() or f"git {' '.join(arguments)} failed")
    return process.stdout


def _entries(lab: Path) -> list[tuple[str, bytes, str]]:
    relative_lab = lab.absolute().relative_to(catalog.ROOT.absolute()).as_posix()
    prefix = relative_lab + "/"
    listed = _git("ls-files", "--stage", "-z", "--", relative_lab).split(b"\0")
    entries = []
    for row in listed:
        if not row:
            continue
        header, path_bytes = row.split(b"\t", 1)
        mode, oid, stage = header.decode("ascii").split()
        if stage != "0":
            raise catalog.CatalogError(f"Unresolved Git merge stage in {os.fsdecode(path_bytes)}")
        path = os.fsdecode(path_bytes)
        if not path.startswith(prefix):
            continue
        name = path[len(prefix):]
        if name == "lab.json":
            continue
        if mode not in ("100644", "100755", "120000"):
            raise catalog.CatalogError(f"Unsupported Git mode {mode} for {path}")
        entries.append((name, _git("cat-file", "blob", oid), mode))
    return entries


def fingerprint_lab(lab: Path) -> str:
    return fingerprint_entries(_entries(lab))


def _unstaged_content(lab: Path) -> list[str]:
    relative = lab.absolute().relative_to(catalog.ROOT.absolute()).as_posix()
    names = _git("diff", "--name-only", "-z", "--", relative).split(b"\0")
    return [os.fsdecode(name) for name in names if name and os.fsdecode(name) != relative + "/lab.json"]


def _selected_paths(values: list[str] | None) -> list[Path]:
    all_paths = catalog.lab_paths()
    if not values:
        return all_paths
    selected = []
    for value in values:
        path = Path(value).resolve()
        if path.is_dir():
            path /= "lab.json"
        catalog._lab_path_parts(path)
        if path not in all_paths:
            raise catalog.CatalogError(f"Lab does not exist: {catalog.display_path(path)}")
        selected.append(path)
    return sorted(set(selected))


def sync_all(check: bool = False, paths: list[str] | None = None) -> int:
    """Validate all candidates before replacing any metadata or generated view."""
    selected = _selected_paths(paths)
    changed: dict[Path, dict[str, Any]] = {}
    today = date.today().isoformat()
    for path in selected:
        unstaged = _unstaged_content(path.parent)
        if unstaged:
            raise catalog.CatalogError("Unstaged lab content: " + ", ".join(unstaged) + ". Stage intended content before syncing.")
        current = catalog.read_json(path)
        fingerprint = fingerprint_lab(path.parent)
        previous = current["tracking"].get("content_sha256")
        if previous != fingerprint:
            updated = catalog.ordered_lab(current)
            updated["tracking"]["content_sha256"] = fingerprint
            if previous is not None:
                updated["tracking"]["dates"]["updated"] = today
            changed[path] = updated
    if check:
        if changed:
            raise catalog.CatalogError("Stale fingerprints: " + ", ".join(catalog.display_path(path) for path in changed) + ". Run lab_sync.py --yes and stage its output.")
        catalog.collect_labs()
        print(f"Lab content tracking is current ({len(selected)} labs checked).")
        return 0
    records, sources = catalog.collect_labs(overrides=changed)
    for path, metadata in changed.items():
        catalog.write_text_atomic(path, catalog.json_text(metadata))
    catalog.write_catalog(records, sources)
    print(f"Synchronized {len(changed)} lab metadata file(s); status was unchanged.")
    return len(changed)


def main() -> int:
    parser = argparse.ArgumentParser(description="Record Git index content fingerprints for labs.")
    parser.add_argument("lab", nargs="*", help="optional lab paths; default is all labs")
    parser.add_argument("--check", action="store_true", help="read-only stale check")
    parser.add_argument("--yes", action="store_true", help="write changed fingerprints")
    args = parser.parse_args()
    if not args.check and not args.yes:
        parser.error("writing requires --yes")
    try:
        sync_all(check=args.check, paths=args.lab)
    except (catalog.CatalogError, OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
