#!/usr/bin/env python3
"""View or edit one lab using the same candidate for flags and prompts."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

import catalog
import workflow


def _parser() -> argparse.ArgumentParser:
    schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
    parser = argparse.ArgumentParser(description="View or edit maintained lab metadata.")
    parser.add_argument("lab", nargs="?", help="lab folder or lab.json")
    parser.add_argument("--title")
    parser.add_argument("--summary")
    parser.add_argument("--clear-summary", action="store_true")
    parser.add_argument("--type", choices=schema["properties"]["type"]["enum"])
    parser.add_argument("--difficulty")
    parser.add_argument("--clear-difficulty", action="store_true")
    parser.add_argument("--skill", action="append", help="replace skills; repeat")
    parser.add_argument("--add-skill", action="append", default=[])
    parser.add_argument("--remove-skill", action="append", default=[])
    parser.add_argument("--goal", action="append", help="replace goals; repeat")
    parser.add_argument("--clear-goals", action="store_true")
    parser.add_argument("--tool", action="append", help="replace local tools; repeat")
    parser.add_argument("--clear-tools", action="store_true")
    parser.add_argument("--link", action="append", default=[], metavar="solution=URL")
    parser.add_argument("--clear-link", action="append", default=[], choices=["solution", "demo"])
    parser.add_argument("--source")
    parser.add_argument("--item-id")
    parser.add_argument("--clear-item-id", action="store_true")
    parser.add_argument("--source-url")
    parser.add_argument("--clear-source-url", action="store_true")
    parser.add_argument("--revision")
    parser.add_argument("--clear-revision", action="store_true")
    parser.add_argument("--status", choices=schema["properties"]["tracking"]["properties"]["status"]["enum"])
    for name in ("created", "started", "completed"):
        parser.add_argument("--" + name)
    for name in ("started", "completed"):
        parser.add_argument("--clear-" + name, action="store_true")
    parser.add_argument("--interactive", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--yes", action="store_true")
    return parser


def _path(value: str) -> Path:
    path = Path(value).resolve()
    if path.is_dir():
        path /= "lab.json"
    catalog._lab_path_parts(path)
    if not path.is_file():
        raise catalog.CatalogError(f"Lab metadata not found: {catalog.display_path(path)}")
    return path


def _select_lab() -> str:
    paths = catalog.lab_paths()
    if not paths:
        raise catalog.CatalogError("There are no labs to edit")
    for index, path in enumerate(paths, 1):
        print(f"{index}. {catalog.display_path(path.parent)}")
    answer = workflow.prompt("Lab number", choices=[str(index) for index in range(1, len(paths) + 1)])
    return str(paths[int(answer) - 1])


def _flag_changes(args: argparse.Namespace, current: dict[str, Any]) -> dict[str, Any]:
    changes = {}
    for key in ("title", "summary", "type", "difficulty", "status", "created", "started", "completed"):
        value = getattr(args, key)
        if value is not None:
            changes[key] = value
    for key in ("summary", "difficulty", "started", "completed"):
        if getattr(args, "clear_" + key):
            if key in changes:
                raise catalog.CatalogError(f"Cannot set and clear {key} together")
            changes[key] = None
    if args.skill is not None:
        changes["skills"] = args.skill
    elif args.add_skill or args.remove_skill:
        changes["skills"] = sorted((set(current["skills"]) | set(args.add_skill)) - set(args.remove_skill))
    if args.goal is not None:
        changes["goals"] = args.goal
    if args.clear_goals:
        if args.goal:
            raise catalog.CatalogError("Cannot set and clear goals together")
        changes["goals"] = None
    if args.tool is not None:
        changes["tools"] = args.tool
    if args.clear_tools:
        if args.tool:
            raise catalog.CatalogError("Cannot set and clear tools together")
        changes["tools"] = None
    links = copy.deepcopy(current.get("links", {}))
    links.update(workflow.parse_links(args.link))
    for key in args.clear_link:
        links.pop(key, None)
    if args.link or args.clear_link:
        changes["links"] = links or None
    source_flags = any((args.source, args.item_id, args.source_url, args.revision, args.clear_item_id, args.clear_source_url, args.clear_revision))
    if source_flags:
        provider = args.source or current["source"]["provider"]
        prior = current["source"] if provider == current["source"]["provider"] else {}
        source = {"provider": provider}
        for key, value, clear in (("item_id", args.item_id, args.clear_item_id), ("url", args.source_url, args.clear_source_url), ("revision", args.revision, args.clear_revision)):
            if value is not None and clear:
                raise catalog.CatalogError(f"Cannot set and clear source {key} together")
            candidate = None if clear else value if value is not None else prior.get(key)
            if candidate:
                source[key] = candidate
        changes["source"] = source
    return changes


def _interactive_changes(current: dict[str, Any], sources: dict[str, Any]) -> dict[str, Any]:
    schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
    changes: dict[str, Any] = {}
    changes["title"] = workflow.prompt("Title", current["title"])
    changes["summary"] = workflow.prompt("Summary", current.get("summary"), optional=True)
    changes["type"] = workflow.prompt("Type", current["type"], choices=schema["properties"]["type"]["enum"])
    changes["difficulty"] = workflow.prompt("Difficulty", current.get("difficulty"), choices=schema["properties"]["difficulty"]["enum"], optional=True)
    records, _ = catalog.collect_labs()
    used_skills = sorted({skill for record in records for skill in record["skills"]})
    changes["skills"] = workflow.prompt_list("Skills", current["skills"], suggestions=used_skills)
    changes["goals"] = workflow.prompt_list("Goals", current.get("goals", [])) or None
    changes["tools"] = workflow.prompt_list("Tools", current.get("tools", [])) or None
    provider = workflow.prompt("Source provider", current["source"]["provider"], choices=sorted(sources))
    prior = current["source"] if provider == current["source"]["provider"] else {}
    source = {"provider": provider}
    if sources[provider]["type"] != "local":
        for key, label in (("item_id", "Source item ID"), ("url", "Source item URL"), ("revision", "Source revision")):
            answer = workflow.prompt(label, prior.get(key), optional=True)
            if answer:
                source[key] = answer
    changes["source"] = source
    links = {}
    for key in ("solution", "demo"):
        answer = workflow.prompt(key.capitalize() + " link", current.get("links", {}).get(key), optional=True)
        if answer:
            links[key] = answer
    changes["links"] = links or None
    choices = schema["properties"]["tracking"]["properties"]["status"]["enum"]
    changes["status"] = workflow.prompt("Status", current["tracking"]["status"], choices=choices)
    for key in ("created", "started", "completed"):
        old_value = current["tracking"]["dates"][key]
        answer = workflow.prompt(key.capitalize() + " date YYYY-MM-DD", old_value, optional=key != "created")
        if answer != old_value:
            changes[key] = answer
    return changes


def main() -> int:
    parser = _parser()
    args = parser.parse_args()
    if args.interactive and (args.yes or args.dry_run):
        parser.error("--interactive cannot be combined with --yes or --dry-run")
    try:
        sources = catalog.load_sources()
        lab = args.lab or (_select_lab() if args.interactive else None)
        if not lab:
            parser.error("lab is required unless --interactive is used")
        path = _path(lab)
        current = catalog.read_json(path)
        catalog.lab_record(path, current, sources)
        changes = _interactive_changes(current, sources) if args.interactive else _flag_changes(args, current)
        if not changes:
            print(catalog.json_text(current), end="")
            return 0
        if not args.interactive and not args.dry_run and not args.yes:
            parser.error("writing requires --yes")
        candidate = workflow.apply_lab_changes(current, changes, sources)
        if candidate == current:
            print("No metadata changes requested.")
            return 0
        records, checked_sources = catalog.collect_labs(overrides={path: candidate})
        workflow.preview(catalog.display_path(path), candidate, ["lab.json", "CATALOG.md", ".meta/catalog/labs.json"])
        if args.dry_run:
            return 0
        if args.interactive and not workflow.confirm():
            print("No changes made.")
            return 0
        catalog.write_text_atomic(path, catalog.json_text(candidate))
        catalog.write_catalog(records, checked_sources)
        print(f"Updated {catalog.display_path(path)}")
    except (catalog.CatalogError, OSError, EOFError, KeyboardInterrupt) as error:
        if isinstance(error, (EOFError, KeyboardInterrupt)):
            print("\nNo changes made.")
            return 0
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
