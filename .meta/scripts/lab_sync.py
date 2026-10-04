#!/usr/bin/env python3
"""Refresh derived content fingerprints and truthful last-updated dates."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

import catalog


def fingerprint_entries(entries: list[tuple[str, bytes, bool]]) -> str:
    """Hash sorted relative paths, file types, and bytes with unambiguous framing."""
    digest = hashlib.sha256()
    for relative_path, content, is_symlink in sorted(entries, key=lambda item: os.fsencode(item[0])):
        path_bytes = os.fsencode(relative_path)
        digest.update(len(path_bytes).to_bytes(8, "big"))
        digest.update(path_bytes)
        digest.update(b"L" if is_symlink else b"F")
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
    return digest.hexdigest()


def _read_regular_file(path: Path) -> bytes:
    """Read a file without following a last-component symlink."""
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(path, flags)
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise catalog.CatalogError(f"Fingerprint input is not a regular file: {catalog.display_path(path)}")
        with os.fdopen(descriptor, "rb", closefd=False) as source:
            return source.read()
    finally:
        os.close(descriptor)


def fingerprint_lab(lab_path: Path) -> str:
    """Hash meaningful Git files; represent symlinks as links and skip lab.json."""
    absolute_lab = lab_path.resolve()
    try:
        relative_lab = absolute_lab.relative_to(catalog.ROOT.resolve())
    except ValueError as error:
        raise catalog.CatalogError("Fingerprint target must be inside the repository.") from error
    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z", "--", relative_lab.as_posix()],
            cwd=catalog.ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        detail = getattr(error, "stderr", b"")
        if isinstance(detail, bytes):
            detail = detail.decode("utf-8", errors="replace").strip()
        raise catalog.CatalogError(f"Could not enumerate files for {catalog.display_path(lab_path)}: {detail or error}") from error
    entries: list[tuple[str, bytes, bool]] = []
    for encoded_path in result.stdout.split(b"\0"):
        if not encoded_path:
            continue
        relative_file = Path(os.fsdecode(encoded_path))
        if relative_file.name == "lab.json":
            continue
        file_path = catalog.ROOT / relative_file
        try:
            file_mode = file_path.lstat().st_mode
        except FileNotFoundError:
            raise catalog.CatalogError(f"Git listed a missing fingerprint input: {catalog.display_path(file_path)}")
        if stat.S_ISLNK(file_mode):
            # Hash the link text, never the target; a link may leave the repository.
            content = os.readlink(file_path).encode("utf-8", errors="surrogateescape")
            is_symlink = True
        elif stat.S_ISREG(file_mode):
            content = _read_regular_file(file_path)
            is_symlink = False
        else:
            raise catalog.CatalogError(f"Unsupported fingerprint input type: {catalog.display_path(file_path)}")
        entries.append((relative_file.relative_to(relative_lab).as_posix(), content, is_symlink))
    return fingerprint_entries(entries)


def sync_all(check: bool = False) -> None:
    """Initialize missing fingerprints or mark changed content without touching status."""
    today = date.today().isoformat()
    overrides: dict[Path, dict[str, Any]] = {}
    stale: list[str] = []
    changed: list[tuple[Path, dict[str, Any]]] = []
    for metadata_path in catalog.lab_paths():
        current = catalog.read_json(metadata_path)
        if not isinstance(current, dict):
            raise catalog.CatalogError(f"Lab metadata must be an object: {catalog.display_path(metadata_path)}")
        updated = dict(current)
        updated["dates"] = dict(current.get("dates", {}))
        updated["tracking"] = dict(current.get("tracking", {}))
        previous = updated["tracking"].get("content_sha256")
        fingerprint = fingerprint_lab(metadata_path.parent)
        if previous != fingerprint:
            if check:
                stale.append(catalog.display_path(metadata_path))
                continue
            if previous is None:
                updated["dates"].setdefault("updated", updated["dates"].get("created"))
            else:
                updated["dates"]["updated"] = today
            updated["tracking"]["content_sha256"] = fingerprint
            changed.append((metadata_path, updated))
            overrides[metadata_path] = updated
    if stale:
        raise catalog.CatalogError("Lab content tracking is stale: " + ", ".join(stale) + ". Run python3 .meta/scripts/lab_sync.py.")
    if check:
        catalog.collect_labs()
        print(f"Lab content tracking is current ({len(catalog.lab_paths())} labs).")
        return
    records, sources = catalog.collect_labs(overrides=overrides)
    for metadata_path, metadata in changed:
        catalog.write_text_atomic(metadata_path, json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")
    catalog.write_catalog(records, sources)
    print(f"Synchronized {len(changed)} lab metadata file(s); content changes never alter status.")


def main() -> int:
    """Run write mode or a read-only staleness check."""
    parser = argparse.ArgumentParser(description="Synchronize deterministic lab content tracking.")
    parser.add_argument("--check", action="store_true", help="detect stale fingerprints without writing")
    args = parser.parse_args()
    try:
        sync_all(check=args.check)
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
