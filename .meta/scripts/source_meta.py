#!/usr/bin/env python3
"""Create, inspect, and update registered provenance sources."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from datetime import date
from typing import Any

import catalog


SOURCE_TYPES = ["external", "organization", "local"]
REUSE_POLICIES = ["copy", "link-only", "review"]


def _parser() -> argparse.ArgumentParser:
    """Build source subcommands around the registry's fixed schema."""
    parser = argparse.ArgumentParser(description="Manage source provenance without path-based provider rules.")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("create", "view", "update"):
        command = commands.add_parser(name)
        command.add_argument("provider", nargs="?", help="unique lowercase source ID")
        command.add_argument("--interactive", action="store_true")
        command.add_argument("--yes", action="store_true", help="confirm an interactive write without asking again")
        if name != "view":
            command.add_argument("--name")
            command.add_argument("--type", choices=SOURCE_TYPES)
            command.add_argument("--url")
            command.add_argument("--reuse-policy", choices=REUSE_POLICIES)
            command.add_argument("--license")
            command.add_argument("--license-url")
            command.add_argument("--policy-url")
            command.add_argument("--verified")
            command.add_argument("--notes")
            command.add_argument("--difficulty-map", action="append", default=[], metavar="SOURCE=LEVEL")
            command.add_argument("--clear-license", action="store_true")
            command.add_argument("--clear-license-url", action="store_true")
            command.add_argument("--clear-policy-url", action="store_true")
            command.add_argument("--clear-verified", action="store_true")
            command.add_argument("--clear-notes", action="store_true")
    return parser


def _prompt(label: str, default: str, *, choices: list[str] = (), existing: list[str] = (), optional: bool = False) -> str:
    """Prompt with existing unique values and explicit closed enum groups."""
    hints = []
    if existing:
        hints.append("currently used: " + ", ".join(existing))
    if choices:
        hints.append("choose one: " + ", ".join(choices))
    suffix = f" [{default}]" if default else " []" if optional else ""
    if hints:
        suffix += " (" + "; ".join(hints) + ")"
    while True:
        value = input(f"{label}{suffix}: ").strip()
        if value == "-" and optional:
            return ""
        value = value or default
        if optional and not value:
            return ""
        if not value:
            print("A value is required.")
            continue
        if choices and value not in choices:
            print("Choose one of the listed values.")
            continue
        return value


def _interactive(args: argparse.Namespace, registry: dict[str, Any]) -> dict[str, Any] | None:
    """Collect a source record; return None for read-only interactive selection."""
    ids = sorted(registry)
    if args.command == "view" and not args.provider:
        args.provider = _prompt("Source ID", "", choices=ids, existing=ids, optional=False)
    elif not args.provider:
        args.provider = _prompt("Source ID", "", existing=ids)
    if args.command == "view":
        return None
    current = registry.get(args.provider, {})
    if args.command == "create" and current:
        raise catalog.CatalogError(f"Source ID {args.provider!r} already exists; use update.")
    types_in_use = sorted({record["type"] for record in registry.values()})
    args.type = _prompt("Type", current.get("type", "external"), choices=SOURCE_TYPES, existing=types_in_use)
    args.name = _prompt("Name", current.get("name", ""))
    if args.type != "local":
        args.url = _prompt("Canonical URL", current.get("url", ""))
        reuse = current.get("reuse", {})
        policies_in_use = sorted({record["reuse"]["policy"] for record in registry.values() if "reuse" in record})
        args.reuse_policy = _prompt("Reuse policy", reuse.get("policy", "review"), choices=REUSE_POLICIES, existing=policies_in_use)
        args.license = _prompt("License identifier", reuse.get("license", ""), optional=True) or None
        args.license_url = _prompt("License URL", reuse.get("license_url", ""), optional=True) or None
        args.policy_url = _prompt("Source policy URL", reuse.get("policy_url", ""), optional=True) or None
        args.verified = _prompt("Verified date (YYYY-MM-DD)", reuse.get("verified", date.today().isoformat()), optional=True) or None
        args.notes = _prompt("Reuse notes", reuse.get("notes", ""), optional=True) or None
    return current


def _date(value: str | None) -> str | None:
    """Return a valid ISO date for reuse verification."""
    if value is None:
        return None
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as error:
        raise catalog.CatalogError("Reuse verification date must be YYYY-MM-DD.") from error


def _apply(args: argparse.Namespace, existing: dict[str, Any] | None) -> dict[str, Any]:
    """Apply only supported source fields, preserving schema shape."""
    if args.command == "create":
        kind = args.type or "external"
        record: dict[str, Any] = {"type": kind, "name": args.name or ""}
        if kind != "local":
            policy = args.reuse_policy
            if not policy:
                raise catalog.CatalogError("External sources need --reuse-policy.")
            record["url"] = args.url or ""
            reuse: dict[str, Any] = {"policy": policy}
            for option, key in (("license", "license"), ("license_url", "license_url"), ("policy_url", "policy_url"), ("verified", "verified"), ("notes", "notes")):
                value = getattr(args, option)
                if value:
                    reuse[key] = _date(value) if key == "verified" else value
            record["reuse"] = reuse
        for mapping in args.difficulty_map:
            if "=" not in mapping:
                raise catalog.CatalogError("Difficulty maps use SOURCE=LEVEL.")
            label, level = mapping.split("=", 1)
            record.setdefault("difficulty_map", {})[label] = level
        return record

    if existing is None:
        raise catalog.CatalogError(f"Source ID {args.provider!r} is not registered.")
    record = copy.deepcopy(existing)
    if args.type is not None:
        record["type"] = args.type
    if args.name is not None:
        record["name"] = args.name
    if record["type"] == "local":
        record.pop("url", None)
        record.pop("reuse", None)
        record.pop("difficulty_map", None)
        return record
    if args.url is not None:
        record["url"] = args.url
    reuse = record.setdefault("reuse", {})
    if args.reuse_policy is not None:
        reuse["policy"] = args.reuse_policy
    for option, key, clear in (
        ("license", "license", args.clear_license),
        ("license_url", "license_url", args.clear_license_url),
        ("policy_url", "policy_url", args.clear_policy_url),
        ("verified", "verified", args.clear_verified),
        ("notes", "notes", args.clear_notes),
    ):
        value = getattr(args, option)
        if clear:
            reuse.pop(key, None)
        elif value is not None:
            reuse[key] = _date(value) if key == "verified" else value
    for mapping in args.difficulty_map:
        if "=" not in mapping:
            raise catalog.CatalogError("Difficulty maps use SOURCE=LEVEL.")
        label, level = mapping.split("=", 1)
        record.setdefault("difficulty_map", {})[label] = level
    return record


def _has_flags(args: argparse.Namespace) -> bool:
    """Detect whether a flag-mode update has any requested edits."""
    return any((args.name is not None, args.type is not None, args.url is not None, args.reuse_policy is not None, args.license is not None, args.license_url is not None, args.policy_url is not None, args.verified is not None, args.notes is not None, bool(args.difficulty_map), args.clear_license, args.clear_license_url, args.clear_policy_url, args.clear_verified, args.clear_notes))


def main() -> int:
    """Validate a proposed registry, check referenced labs, then write atomically."""
    parser = _parser()
    args = parser.parse_args()
    try:
        registry = catalog.load_sources()
        if args.interactive:
            existing = _interactive(args, registry)
        else:
            existing = registry.get(args.provider) if args.provider else None
        if not args.provider:
            parser.error("provider is required unless --interactive is used")
        if args.command == "view":
            record = existing or registry.get(args.provider)
            if record is None:
                raise catalog.CatalogError(f"Source ID {args.provider!r} is not registered.")
            print(json.dumps(record, indent=2, ensure_ascii=False))
            return 0
        if args.command == "update" and not args.interactive and not _has_flags(args):
            record = registry.get(args.provider)
            if record is None:
                raise catalog.CatalogError(f"Source ID {args.provider!r} is not registered.")
            print(json.dumps(record, indent=2, ensure_ascii=False))
            return 0
        updated = _apply(args, existing)
        candidate = copy.deepcopy(registry)
        candidate[args.provider] = updated
        catalog.validate_document(candidate, catalog.load_schema(catalog.SOURCE_SCHEMA_PATH), catalog.display_path(catalog.SOURCES_PATH))
        records, _ = catalog.collect_labs(sources_override=candidate)
        if args.interactive:
            print(f"\nSource ID:\n{args.provider}\n\nSource record:\n{json.dumps(updated, indent=2, ensure_ascii=False)}")
            if not args.yes:
                answer = input("Write these changes? [y/N]: ").strip().casefold()
                if answer not in {"y", "yes"}:
                    print("No changes made.")
                    return 0
        catalog.write_text_atomic(catalog.SOURCES_PATH, json.dumps(candidate, indent=2, ensure_ascii=False) + "\n")
        catalog.write_catalog(records, candidate)
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Updated source {args.provider}" if args.command == "update" else f"Created source {args.provider}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
