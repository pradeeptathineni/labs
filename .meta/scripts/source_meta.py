#!/usr/bin/env python3
"""Create, view, and update provenance sources with checked candidates."""

from __future__ import annotations

import argparse
import copy
import sys
from typing import Any

import catalog
import workflow


def _parser() -> argparse.ArgumentParser:
    schema = catalog.load_schema(catalog.SOURCE_SCHEMA_PATH)
    definitions = schema["$defs"]
    types = definitions["source"]["properties"]["type"]["enum"]
    policies = definitions["reuse"]["properties"]["policy"]["enum"]
    parser = argparse.ArgumentParser(description="Manage the source registry.")
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("create", "view", "update"):
        sub = commands.add_parser(command)
        sub.add_argument("provider", nargs="?")
        sub.add_argument("--interactive", action="store_true")
        sub.add_argument("--dry-run", action="store_true")
        sub.add_argument("--yes", action="store_true")
        if command == "view":
            continue
        sub.add_argument("--name")
        sub.add_argument("--type", choices=types)
        sub.add_argument("--url")
        sub.add_argument("--reuse-policy", choices=policies)
        for key in ("policy-url", "license", "license-url", "notes", "verified"):
            sub.add_argument("--" + key)
            sub.add_argument("--clear-" + key, action="store_true")
        sub.add_argument("--clear-url", action="store_true")
        sub.add_argument("--difficulty-map", action="append", default=[], metavar="LABEL=LEVEL")
        sub.add_argument("--remove-difficulty-map", action="append", default=[], metavar="LABEL")
    return parser


def _choose_id(registry: dict[str, Any], command: str) -> str:
    return workflow.prompt("Source ID", choices=sorted(registry) if command != "create" else None, suggestions=sorted(registry))


def _changes(args: argparse.Namespace, existing: dict[str, Any] | None) -> dict[str, Any]:
    changes: dict[str, Any] = {}
    for key in ("name", "type", "url"):
        value = getattr(args, key)
        if value is not None:
            changes[key] = value
    if args.clear_url:
        changes["url"] = None
    reuse = {}
    if args.reuse_policy is not None:
        reuse["policy"] = args.reuse_policy
    for key in ("policy_url", "license", "license_url", "notes", "verified"):
        value = getattr(args, key)
        if getattr(args, "clear_" + key):
            if value is not None:
                raise catalog.CatalogError(f"Cannot set and clear {key} together")
            reuse[key] = None
        elif value is not None:
            reuse[key] = value
    if reuse:
        changes["reuse"] = reuse
    mapping = dict(existing.get("difficulty_map", {})) if existing else {}
    for pair in args.difficulty_map:
        if "=" not in pair:
            raise catalog.CatalogError("Difficulty maps use LABEL=LEVEL")
        label, level = pair.split("=", 1)
        mapping[label] = level
    for label in args.remove_difficulty_map:
        mapping.pop(label, None)
    if args.difficulty_map or args.remove_difficulty_map:
        changes["difficulty_map"] = mapping
    return changes


def _interactive_changes(existing: dict[str, Any] | None, registry: dict[str, Any]) -> dict[str, Any]:
    schema = catalog.load_schema(catalog.SOURCE_SCHEMA_PATH)["$defs"]
    current = existing or {}
    changes = {
        "type": workflow.prompt("Type", current.get("type", "external"), choices=schema["source"]["properties"]["type"]["enum"]),
        "name": workflow.prompt("Name", current.get("name")),
    }
    if changes["type"] != "local":
        changes["url"] = workflow.prompt("Canonical URL", current.get("url"), optional=changes["type"] == "organization")
        reuse = current.get("reuse", {})
        choices = schema["reuse"]["properties"]["policy"]["enum"]
        changes["reuse"] = {"policy": workflow.prompt("Reuse policy", reuse.get("policy", "review"), choices=choices)}
        for key in ("policy_url", "license", "license_url", "notes", "verified"):
            changes["reuse"][key] = workflow.prompt(key.replace("_", " ").capitalize(), reuse.get(key), optional=True)
        map_text = workflow.prompt("Difficulty map LABEL=LEVEL (comma separated)", ", ".join(f"{key}={value}" for key, value in current.get("difficulty_map", {}).items()), optional=True)
        if map_text:
            pairs = [part.strip() for part in map_text.split(",") if part.strip()]
            mapping = {}
            for pair in pairs:
                if "=" not in pair:
                    raise catalog.CatalogError("Difficulty maps use LABEL=LEVEL")
                key, value = pair.split("=", 1)
                mapping[key] = value
            changes["difficulty_map"] = mapping
        else:
            changes["difficulty_map"] = {}
    return changes


def _candidate(existing: dict[str, Any] | None, changes: dict[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(existing or {})
    for key in ("type", "name", "url"):
        if key in changes:
            if changes[key] is None:
                candidate.pop(key, None)
            else:
                candidate[key] = changes[key]
    if candidate.get("type") == "local":
        for key in ("url", "reuse", "difficulty_map"):
            candidate.pop(key, None)
        return catalog.ordered_source(candidate)
    if "reuse" in changes:
        reuse = candidate.setdefault("reuse", {})
        for key, value in changes["reuse"].items():
            if value is None:
                reuse.pop(key, None)
            else:
                reuse[key] = workflow.valid_date(value) if key == "verified" else value
    if "difficulty_map" in changes:
        if changes["difficulty_map"]:
            candidate["difficulty_map"] = changes["difficulty_map"]
        else:
            candidate.pop("difficulty_map", None)
    return catalog.ordered_source(candidate)


def main() -> int:
    parser = _parser()
    args = parser.parse_args()
    if args.interactive and (args.yes or args.dry_run):
        parser.error("--interactive cannot be combined with --yes or --dry-run")
    try:
        registry = catalog.load_sources()
        provider = args.provider or (_choose_id(registry, args.command) if args.interactive else None)
        if not provider:
            parser.error("source ID is required")
        existing = registry.get(provider)
        if args.command == "view":
            if existing is None:
                raise catalog.CatalogError(f"Source ID {provider!r} is not registered")
            print(catalog.json_text(existing), end="")
            return 0
        if args.command == "create" and existing is not None:
            raise catalog.CatalogError(f"Source ID {provider!r} already exists; use update")
        if args.command == "update" and existing is None:
            raise catalog.CatalogError(f"Source ID {provider!r} is not registered")
        changes = _interactive_changes(existing, registry) if args.interactive else _changes(args, existing)
        if args.command == "update" and not changes:
            print(catalog.json_text(existing), end="")
            return 0
        if not args.interactive and not args.dry_run and not args.yes:
            parser.error("writing requires --yes")
        candidate = _candidate(existing, changes)
        if candidate == existing:
            print("No source changes requested.")
            return 0
        updated = dict(registry)
        updated[provider] = candidate
        catalog.validate_document(updated, catalog.load_schema(catalog.SOURCE_SCHEMA_PATH), "source registry")
        records, _ = catalog.collect_labs(sources_override=updated)
        removals = sorted(set(existing or {}) - set(candidate))
        workflow.preview(f".meta/catalog/sources.json::{provider}", candidate, ["sources.json", "CATALOG.md", "labs.json"], removals)
        if args.dry_run:
            return 0
        if args.interactive and not workflow.confirm():
            print("No changes made.")
            return 0
        catalog.write_text_atomic(catalog.SOURCES_PATH, catalog.json_text({key: catalog.ordered_source(value) for key, value in updated.items()}))
        catalog.write_catalog(records, updated)
        print(f"{args.command.capitalize()}d source {provider}")
    except (catalog.CatalogError, OSError, EOFError, KeyboardInterrupt) as error:
        if isinstance(error, (EOFError, KeyboardInterrupt)):
            print("\nNo changes made.")
            return 0
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
