#!/usr/bin/env python3
"""Inspect or safely update one lab's maintained metadata.

Status changes set first-started and first-completed dates when those dates are
unset. Explicit date options override that automatic behavior, and historical
dates remain available after a status is moved back to an earlier state.
"""

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
    parser = argparse.ArgumentParser(
        description="View a lab's metadata or update its status, skills, source, or dates."
    )
    parser.add_argument("lab", help="path to a lab directory or its lab.json")
    parser.add_argument("--title", help="set the human-readable title")
    parser.add_argument("--kind", choices=kind_values, help="set the lab kind")
    parser.add_argument("--status", choices=status_values, help="set the lifecycle state")

    difficulty = parser.add_mutually_exclusive_group()
    difficulty.add_argument(
        "--difficulty",
        help="set normalized difficulty or a provider level mapped in sources.json",
    )
    difficulty.add_argument(
        "--clear-difficulty", action="store_true", help="remove the optional difficulty"
    )

    parser.add_argument(
        "--add-skill",
        action="append",
        default=[],
        metavar="SLUG",
        help="add a lowercase kebab-case skill; repeat as needed",
    )
    parser.add_argument(
        "--remove-skill",
        action="append",
        default=[],
        metavar="SLUG",
        help="remove a skill; repeat as needed",
    )

    parser.add_argument("--source-id", help="set the stable external item ID")
    parser.add_argument(
        "--source-url", dest="item_url", help="set the canonical external item URL"
    )

    parser.add_argument(
        "--created", type=_date_value, metavar="YYYY-MM-DD", help="override creation date"
    )
    started = parser.add_mutually_exclusive_group()
    started.add_argument(
        "--started", type=_date_value, metavar="YYYY-MM-DD", help="override first-started date"
    )
    started.add_argument(
        "--clear-started", action="store_true", help="clear first-started date"
    )
    completed = parser.add_mutually_exclusive_group()
    completed.add_argument(
        "--completed",
        type=_date_value,
        metavar="YYYY-MM-DD",
        help="override first-completed date",
    )
    completed.add_argument(
        "--clear-completed", action="store_true", help="clear first-completed date"
    )
    return parser


def _metadata_path(value: str) -> Path:
    """Resolve a lab argument and keep updates inside the intended hierarchy."""
    path = Path(value).resolve()
    if path.is_dir():
        path /= "lab.json"
    try:
        path.relative_to(catalog.NICHES.resolve())
    except ValueError as error:
        raise catalog.CatalogError("Lab path must be inside niches/.") from error
    if path.name != "lab.json" or not path.is_file():
        raise catalog.CatalogError(
            f"Lab metadata not found: {catalog.display_path(path)}."
        )
    return path


def _validate_skill_slugs(skills: list[str]) -> None:
    """Reject non-normalized tags before applying a mutation."""
    for skill in skills:
        if not catalog.SLUG_PATTERN.fullmatch(skill):
            raise catalog.CatalogError(
                f"Skill {skill!r} must be lowercase kebab-case, "
                "such as performance-monitoring."
            )


def _apply_updates(current: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
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
        if old_status != args.status and args.status == "in-progress":
            if updated["dates"]["started"] is None:
                updated["dates"]["started"] = date.today().isoformat()
        if old_status != args.status and args.status == "complete":
            if updated["dates"]["completed"] is None:
                updated["dates"]["completed"] = date.today().isoformat()

    if args.difficulty is not None:
        updated["difficulty"] = args.difficulty
    elif args.clear_difficulty:
        updated.pop("difficulty", None)

    to_add = set(args.add_skill)
    to_remove = set(args.remove_skill)
    overlap = to_add & to_remove
    if overlap:
        names = ", ".join(sorted(overlap))
        raise catalog.CatalogError(f"Cannot add and remove the same skill: {names}.")
    _validate_skill_slugs(args.add_skill + args.remove_skill)
    skills = set(current["skills"])
    skills.update(to_add)
    skills.difference_update(to_remove)
    updated["skills"] = sorted(skills)

    has_source_option = args.source_id is not None or args.item_url is not None
    if has_source_option and not (args.source_id and args.item_url):
        raise catalog.CatalogError("Provide both --source-id and --source-url.")
    if has_source_option:
        updated["source"] = {"id": args.source_id, "url": args.item_url}

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


def main() -> int:
    """Read, validate, and optionally update a lab before refreshing its catalog."""
    try:
        schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    parser = _parser(
        schema["properties"]["kind"]["enum"],
        schema["properties"]["status"]["enum"],
    )
    args = parser.parse_args()

    try:
        path = _metadata_path(args.lab)
        current = catalog.read_json(path)
        if not isinstance(current, dict):
            raise catalog.CatalogError(
                f"Lab metadata must be a JSON object: {catalog.display_path(path)}."
            )
        sources = catalog.load_sources()
        catalog.lab_record(path, current, sources, schema)
        if args.difficulty is not None:
            args.difficulty = catalog.normalize_difficulty(
                args.difficulty, path, sources, schema
            )

        has_changes = any(
            (
                args.title is not None,
                args.kind is not None,
                args.status is not None,
                args.difficulty is not None,
                args.clear_difficulty,
                bool(args.add_skill),
                bool(args.remove_skill),
                args.source_id is not None,
                args.item_url is not None,
                args.created is not None,
                args.started is not None,
                args.clear_started,
                args.completed is not None,
                args.clear_completed,
            )
        )
        if not has_changes:
            print(json.dumps(current, indent=2, ensure_ascii=False))
            return 0

        updated = _apply_updates(current, args)
        records, sources = catalog.collect_labs(overrides={path: updated})
        catalog.write_text_atomic(
            path, json.dumps(updated, indent=2, ensure_ascii=False) + "\n"
        )
        catalog.write_catalog(records, sources)
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Updated {catalog.display_path(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
