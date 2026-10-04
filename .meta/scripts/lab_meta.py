#!/usr/bin/env python3
"""Inspect or safely update one lab's maintained metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import catalog


def _date_value(value: str) -> str:
    """Validate an ISO calendar date for argparse."""
    if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value) is None:
        raise argparse.ArgumentTypeError("use a valid date in YYYY-MM-DD form")
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as error:
        raise argparse.ArgumentTypeError("use a valid date in YYYY-MM-DD form") from error


def _parser(kind_values: list[str], status_values: list[str]) -> argparse.ArgumentParser:
    """Build the metadata maintenance CLI from the checked-in schema."""
    parser = argparse.ArgumentParser(description="View or update one lab's metadata.")
    parser.add_argument("lab", nargs="?", help="path to a lab directory or its lab.json")
    parser.add_argument("--title")
    parser.add_argument("--kind", choices=kind_values)
    parser.add_argument("--status", choices=status_values)
    difficulty = parser.add_mutually_exclusive_group()
    difficulty.add_argument("--difficulty")
    difficulty.add_argument("--clear-difficulty", action="store_true")
    parser.add_argument("--add-skill", action="append", default=[])
    parser.add_argument("--remove-skill", action="append", default=[])
    parser.add_argument("--source", "--source-provider", dest="source_provider")
    parser.add_argument("--item-id", "--source-id", dest="item_id")
    parser.add_argument("--source-url")
    parser.add_argument("--created", type=_date_value, metavar="YYYY-MM-DD")
    started = parser.add_mutually_exclusive_group()
    started.add_argument("--started", type=_date_value, metavar="YYYY-MM-DD")
    started.add_argument("--clear-started", action="store_true")
    completed = parser.add_mutually_exclusive_group()
    completed.add_argument("--completed", type=_date_value, metavar="YYYY-MM-DD")
    completed.add_argument("--clear-completed", action="store_true")
    parser.add_argument("--interactive", action="store_true")
    parser.add_argument("--yes", action="store_true", help="confirm an interactive write without asking again")
    return parser


def _metadata_path(value: str) -> Path:
    """Resolve a lab argument and keep updates inside the canonical hierarchy."""
    path = Path(value).resolve()
    if path.is_dir():
        path /= "lab.json"
    try:
        path.relative_to(catalog.NICHES.resolve())
    except ValueError as error:
        raise catalog.CatalogError("Lab path must be inside niches/.") from error
    if path.name != "lab.json" or not path.is_file():
        raise catalog.CatalogError(f"Lab metadata not found: {catalog.display_path(path)}.")
    catalog._lab_path_parts(path)
    return path


def _select_lab() -> str:
    """Display known lab paths and let an interactive caller select one."""
    paths = catalog.lab_paths()
    if not paths:
        raise catalog.CatalogError("There are no labs to update.")
    for index, path in enumerate(paths, start=1):
        print(f"{index}. {catalog.display_path(path.parent)}")
    while True:
        answer = input("Lab number: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(paths):
            return str(paths[int(answer) - 1])
        print("Choose one of the listed numbers.")


def _prompt(label: str, default: str, *, choices: list[str] = (), existing: list[str] = (), optional: bool = False) -> str:
    """Prompt with unique repository values plus any closed enum group."""
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


def _used_values(field: str) -> list[str]:
    """Return values already used for closed metadata enums."""
    values: set[str] = set()
    for path in catalog.lab_paths():
        metadata = catalog.read_json(path)
        if field == "difficulty":
            value = metadata.get(field)
            if value:
                values.add(value)
        elif metadata.get(field):
            values.add(metadata[field])
    return sorted(values)


def _used_skills() -> list[str]:
    """Return current skill tags so new tags do not drift into near-duplicates."""
    values: set[str] = set()
    for path in catalog.lab_paths():
        values.update(catalog.read_json(path).get("skills", []))
    return sorted(values)


def _interactive_update(current: dict[str, Any], schema: dict[str, Any], sources: dict[str, Any]) -> dict[str, Any]:
    """Gather a complete proposed record while blank inputs preserve current values."""
    updated = json.loads(json.dumps(current))
    updated["title"] = _prompt("Title", current["title"])
    updated["kind"] = _prompt("Kind", current["kind"], choices=schema["properties"]["kind"]["enum"], existing=_used_values("kind"))
    updated["status"] = _prompt("Status", current["status"], choices=schema["properties"]["status"]["enum"], existing=_used_values("status"))
    providers = sorted(sources)
    used_providers = sorted({catalog.read_json(path)["source"]["provider"] for path in catalog.lab_paths()})
    provider = _prompt("Source provider", current["source"]["provider"], choices=providers, existing=used_providers)
    provider_record = catalog.source_for(provider, sources)
    if provider_record["type"] == "local":
        updated["source"] = {"provider": provider}
    else:
        prior = current["source"] if current["source"]["provider"] == provider else {}
        used_item_ids = sorted({
            item["source"]["item_id"]
            for item_path in catalog.lab_paths()
            if (item := catalog.read_json(item_path)).get("source", {}).get("provider") == provider
            and item["source"].get("item_id")
        })
        item_id = _prompt("Source item ID", prior.get("item_id", ""), existing=used_item_ids)
        url = _prompt("Source item URL", prior.get("url", ""))
        updated["source"] = {"provider": provider, "item_id": item_id, "url": url}
    difficulty_values = sorted(set(schema["properties"]["difficulty"]["enum"]) | set(provider_record.get("difficulty_map", {})))
    difficulty = _prompt("Difficulty", current.get("difficulty", ""), choices=difficulty_values, existing=_used_values("difficulty"), optional=True)
    if difficulty:
        updated["difficulty"] = catalog.normalize_difficulty(difficulty, provider, sources, schema)
    else:
        updated.pop("difficulty", None)
    known_skills = ", ".join(_used_skills())
    hint = f"; existing values: {known_skills}" if known_skills else ""
    skill_text = input(f"Skills [{', '.join(current['skills'])}] (comma separated{hint}; '-' clears): ").strip()
    if skill_text == "-":
        updated["skills"] = []
    elif skill_text:
        updated["skills"] = sorted({item.strip() for item in skill_text.split(",") if item.strip()})
    print("Lifecycle dates are managed separately by explicit flags; updated is content-derived.")
    return updated


def _validate_skills(skills: list[str]) -> None:
    """Reject non-normalized skill tags before applying a mutation."""
    for skill in skills:
        if not catalog.SLUG_PATTERN.fullmatch(skill):
            raise catalog.CatalogError(f"Skill {skill!r} must be lowercase kebab-case, such as performance-monitoring.")


def _apply_updates(current: dict[str, Any], args: argparse.Namespace, sources: dict[str, Any], schema: dict[str, Any]) -> dict[str, Any]:
    """Apply requested field changes and first-entry lifecycle dates."""
    updated = dict(current)
    updated["dates"] = dict(current["dates"])
    if args.title is not None:
        if not args.title.strip():
            raise catalog.CatalogError("Title cannot be empty.")
        updated["title"] = args.title.strip()
    if args.kind is not None:
        updated["kind"] = args.kind
    if args.status is not None:
        old_status = current["status"]
        updated["status"] = args.status
        today = date.today().isoformat()
        if old_status != args.status and args.status == "in-progress" and updated["dates"]["started"] is None:
            updated["dates"]["started"] = today
        if old_status != args.status and args.status == "complete" and updated["dates"]["completed"] is None:
            updated["dates"]["completed"] = today
    if args.difficulty is not None:
        updated["difficulty"] = catalog.normalize_difficulty(args.difficulty, args.source_provider or current["source"]["provider"], sources, schema)
    elif args.clear_difficulty:
        updated.pop("difficulty", None)
    added, removed = set(args.add_skill), set(args.remove_skill)
    if added & removed:
        raise catalog.CatalogError("Cannot add and remove the same skill: " + ", ".join(sorted(added & removed)) + ".")
    _validate_skills(args.add_skill + args.remove_skill)
    updated["skills"] = sorted((set(current["skills"]) | added) - removed)
    has_source = args.source_provider is not None or args.item_id is not None or args.source_url is not None
    if has_source:
        provider = args.source_provider or current["source"]["provider"]
        provider_data = catalog.source_for(provider, sources)
        if provider_data["type"] == "local":
            if args.item_id or args.source_url:
                raise catalog.CatalogError(f"Local source {provider!r} cannot have an item ID or URL.")
            updated["source"] = {"provider": provider}
        else:
            item_id = args.item_id or (current["source"].get("item_id") if provider == current["source"]["provider"] else None)
            url = args.source_url or (current["source"].get("url") if provider == current["source"]["provider"] else None)
            if not item_id or not url:
                raise catalog.CatalogError("External sources need both --item-id and --source-url.")
            updated["source"] = {"provider": provider, "item_id": item_id, "url": url}
    if args.created is not None:
        updated["dates"]["created"] = args.created
    if args.started is not None:
        updated["dates"]["started"] = args.started
    elif args.clear_started:
        updated["dates"]["started"] = None
    if args.completed is not None:
        updated["dates"]["completed"] = args.completed
    elif args.clear_completed:
        updated["dates"]["completed"] = None
    return updated


def _has_changes(args: argparse.Namespace) -> bool:
    """Tell a read-only view from a requested mutation."""
    return any((args.title is not None, args.kind is not None, args.status is not None, args.difficulty is not None, args.clear_difficulty, bool(args.add_skill), bool(args.remove_skill), args.source_provider is not None, args.item_id is not None, args.source_url is not None, args.created is not None, args.started is not None, args.clear_started, args.completed is not None, args.clear_completed))


def main() -> int:
    """Read, validate, and optionally update a lab before refreshing catalogs."""
    try:
        schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
        sources = catalog.load_sources()
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    parser = _parser(schema["properties"]["kind"]["enum"], schema["properties"]["status"]["enum"])
    args = parser.parse_args()
    try:
        if args.interactive and not args.lab:
            args.lab = _select_lab()
        if not args.lab:
            parser.error("lab is required unless interactive selection is used")
        path = _metadata_path(args.lab)
        current = catalog.read_json(path)
        catalog.lab_record(path, current, sources, schema)
        if args.interactive:
            updated = _interactive_update(current, schema, sources)
        elif not _has_changes(args):
            print(json.dumps(current, indent=2, ensure_ascii=False))
            return 0
        else:
            updated = _apply_updates(current, args, sources, schema)
        if updated == current:
            print("No metadata changes requested.")
            return 0
        records, checked_sources = catalog.collect_labs(overrides={path: updated})
        if args.interactive:
            print(f"\nPath:\n{catalog.display_path(path.parent)}\n\nMetadata:\n{json.dumps(updated, indent=2, ensure_ascii=False)}")
            if not args.yes:
                answer = input("Write these changes? [y/N]: ").strip().casefold()
                if answer not in {"y", "yes"}:
                    print("No changes made.")
                    return 0
        catalog.write_text_atomic(path, json.dumps(updated, indent=2, ensure_ascii=False) + "\n")
        catalog.write_catalog(records, checked_sources)
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Updated {catalog.display_path(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
