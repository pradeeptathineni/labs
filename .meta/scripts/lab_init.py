#!/usr/bin/env python3
"""Initialize one bounded lab from one validated plan."""

from __future__ import annotations

import argparse
import os
import sys
import tempfile
from datetime import date
from pathlib import Path
from typing import Any

import catalog
import lab_sync
import workflow


def starter_readme(title: str, source_name: str | None, url: str | None) -> str:
    lines = [f"# {title}", ""]
    if url:
        lines += [f"Source: [{source_name or 'Original source'}]({url})", ""]
    lines += ["## Exercise Definition", ""]
    if url:
        lines += [f"Read the [original exercise definition]({url}).", ""]
    return "\n".join(lines + ["## Solution", ""])


def _parent(data: dict[str, Any]) -> Path:
    parts = [data["niche"], data["domain"]]
    if data.get("subdomain"):
        parts.append(data["subdomain"])
    parts.extend(data.get("groups", []))
    parts.append(data["collection"])
    for part in parts:
        if not catalog.SLUG_PATTERN.fullmatch(part):
            raise catalog.CatalogError(f"Hierarchy name must be lowercase kebab-case: {part!r}")
    parent = catalog.NICHES.joinpath(*parts)
    cursor = catalog.NICHES
    for part in parts:
        cursor /= part
        if cursor.is_symlink():
            raise catalog.CatalogError(f"Refusing symlinked lab parent: {catalog.display_path(cursor)}")
        if cursor.exists() and not cursor.is_dir():
            raise catalog.CatalogError(f"Lab parent is not a directory: {catalog.display_path(cursor)}")
        if (cursor / "lab.json").exists():
            raise catalog.CatalogError(f"Cannot create a collection inside a lab: {catalog.display_path(cursor)}")
    return parent


def destination(value: str, subdomain: str | None = None) -> dict[str, Any]:
    """Interpret an importer destination using the same subject boundary as init."""
    parent = Path(value).absolute()
    descriptor = catalog.collection_info(parent)
    if subdomain is not None:
        if not descriptor.get("has_subdomain") and ("has_subdomain" in descriptor or any(parent.glob("*/lab.json"))):
            raise catalog.CatalogError(f"Subject boundary disagrees with existing collection: {catalog.display_path(parent)}")
        descriptor = dict(descriptor, has_subdomain=True)
    parts = catalog.collection_parts(parent, descriptor)
    if subdomain is not None and parts["subdomain"] != subdomain:
        raise catalog.CatalogError("--subdomain must match the directory immediately after the domain")
    _parent(parts)
    return parts


def collection_updates(plans: list[dict[str, Any]]) -> dict[Path, dict[str, Any]]:
    updates = {}
    for plan in plans:
        for parent, descriptor in plan["collection_updates"].items():
            if parent in updates and updates[parent] != descriptor:
                raise catalog.CatalogError(f"Conflicting collection plans: {catalog.display_path(parent)}")
            updates[parent] = descriptor
    return updates


def preview_plan(plan: dict[str, Any]) -> None:
    for parent, descriptor in plan["collection_updates"].items():
        workflow.preview(catalog.display_path(parent), descriptor, ["collection.json"])
    workflow.preview(catalog.display_path(plan["path"]), plan["metadata"], sorted(plan["files"]) + ["lab.json"])


def plan_lab(data: dict[str, Any], sources: dict[str, Any], *, files: dict[str, str] | None = None, existing_plans: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Build one complete candidate without writing any file."""
    parent = _parent(data)
    provider = data.get("provider") or data.get("source") or "created"
    source_record = catalog.source_for(provider, sources)
    title = data["title"].strip()
    if not title:
        raise catalog.CatalogError("Title cannot be empty")
    slug = data.get("slug") or catalog.slugify(title)
    if not catalog.SLUG_PATTERN.fullmatch(slug):
        raise catalog.CatalogError(f"Invalid lab slug: {slug!r}")
    descriptor = catalog.collection_info(parent)
    proposed_descriptor = dict(data.get("collection_descriptor", {}))
    proposed_descriptor.update(catalog.collection_info(parent, collection_updates(existing_plans or [])))
    catalog.validate_document(proposed_descriptor, catalog.load_schema(catalog.COLLECTION_SCHEMA_PATH), "proposed collection")
    has_subdomain = bool(data.get("subdomain"))
    if descriptor.get("has_subdomain", False) != has_subdomain:
        if "has_subdomain" in descriptor or (parent.exists() and any(parent.glob("*/lab.json"))):
            raise catalog.CatalogError(f"Subject boundary disagrees with existing collection: {catalog.display_path(parent)}")
        proposed_descriptor["has_subdomain"] = has_subdomain
    siblings = [p for p in parent.iterdir() if p.is_dir()] if parent.exists() else []
    planned_siblings = [plan["path"] for plan in (existing_plans or []) if plan["path"].parent == parent]
    all_siblings = siblings + planned_siblings
    for sibling in all_siblings:
        name = sibling.name
        existing_slug = catalog.ORDER_PATTERN.fullmatch(name).group(2) if proposed_descriptor.get("ordered") and catalog.ORDER_PATTERN.fullmatch(name) else name
        if existing_slug == slug:
            raise catalog.CatalogError(f"Lab slug already exists in collection: {slug}")
    if proposed_descriptor.get("ordered"):
        numbers = [int(match.group(1)) for child in all_siblings if (match := catalog.ORDER_PATTERN.fullmatch(child.name))]
        folder = f"{max(numbers, default=0) + 1:02d}-{slug}"
    else:
        folder = slug
    path = parent / folder
    if path.exists():
        raise catalog.CatalogError(f"Refusing to overwrite {catalog.display_path(path)}")
    source = workflow.make_source(provider, data.get("item_id"), data.get("source_url"), data.get("revision"))
    if source_record["type"] == "local" and len(source) > 1:
        raise catalog.CatalogError("Local source cannot have item, URL, or revision")
    today = date.today().isoformat()
    status = data.get("status", "not-started")
    dates = {
        "created": workflow.valid_date(data.get("created") or today),
        "started": workflow.valid_date(data.get("started")),
        "updated": today,
        "completed": workflow.valid_date(data.get("completed")),
    }
    if status == "in-progress" and dates["started"] is None:
        dates["started"] = today
    if status == "complete" and dates["completed"] is None:
        dates["completed"] = today
    content = dict(files or {})
    content.setdefault("README.md", starter_readme(title, source_record["name"], source.get("url")))
    for relative in content:
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts or relative == "lab.json":
            raise catalog.CatalogError(f"Unsafe lab file path: {relative}")
    entries = [(relative, text.encode("utf-8"), "100644") for relative, text in content.items()]
    metadata: dict[str, Any] = {"title": title, "type": data.get("type", "exercise"), "skills": sorted(set(data.get("skills", []))), "source": source, "tracking": {"status": status, "dates": dates, "content_sha256": lab_sync.fingerprint_entries(entries)}}
    for key in ("summary", "difficulty", "tools", "goals", "links"):
        if data.get(key):
            metadata[key] = sorted(set(data[key])) if key in ("tools", "goals") else data[key]
    if "difficulty" in metadata:
        metadata["difficulty"] = catalog.normalize_difficulty(metadata["difficulty"], provider, sources)
    metadata = catalog.ordered_lab(metadata)
    updates = {parent: proposed_descriptor} if proposed_descriptor != descriptor else {}
    plan = {"path": path, "metadata": metadata, "files": content, "collection_updates": updates}
    plans = [*(existing_plans or []), plan]
    catalog.collect_labs(
        overrides={item["path"] / "lab.json": item["metadata"] for item in plans},
        sources_override=sources,
        collection_overrides=collection_updates(plans),
    )
    return plan


def write_plans(plans: list[dict[str, Any]], sources: dict[str, Any]) -> None:
    """Validate the whole batch and stage file contents before any destination moves."""
    overrides = {plan["path"] / "lab.json": plan["metadata"] for plan in plans}
    descriptors = collection_updates(plans)
    catalog.collect_labs(overrides=overrides, sources_override=sources, collection_overrides=descriptors)
    with tempfile.TemporaryDirectory(prefix=".lab-init-", dir=catalog.ROOT / ".meta") as temporary:
        staged = Path(temporary)
        for index, plan in enumerate(plans):
            target = staged / str(index)
            target.mkdir()
            for relative, content in plan["files"].items():
                catalog.write_text_atomic(target / relative, content)
            catalog.write_text_atomic(target / "lab.json", catalog.json_text(plan["metadata"]))
        for parent, descriptor in descriptors.items():
            catalog.write_text_atomic(parent / "collection.json", catalog.json_text(descriptor))
        for index, plan in enumerate(plans):
            destination = plan["path"]
            if destination.exists():
                raise catalog.CatalogError(f"Refusing to overwrite {catalog.display_path(destination)}")
            destination.parent.mkdir(parents=True, exist_ok=True)
            (staged / str(index)).rename(destination)
    catalog.update_catalog()


def create_lab(data: dict[str, Any], sources: dict[str, Any], *, files: dict[str, str] | None = None) -> Path:
    plan = plan_lab(data, sources, files=files)
    write_plans([plan], sources)
    return plan["path"]


def _parser() -> argparse.ArgumentParser:
    schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
    parser = argparse.ArgumentParser(description="Initialize a lab and refresh the catalog.")
    for name in ("niche", "domain", "collection", "title"):
        parser.add_argument(name, nargs="?")
    parser.add_argument("--subdomain", help="optional subject specialization immediately after the domain")
    parser.add_argument("--group", dest="groups", action="append", default=[], help="provider or collection grouping after the subject; repeat for nested groups")
    parser.add_argument("--slug")
    parser.add_argument("--summary")
    parser.add_argument("--type", choices=schema["properties"]["type"]["enum"], default="exercise")
    parser.add_argument("--difficulty")
    parser.add_argument("--skill", action="append", default=[])
    parser.add_argument("--tool", action="append", default=[])
    parser.add_argument("--goal", action="append", default=[])
    parser.add_argument("--link", action="append", default=[], metavar="solution=URL")
    parser.add_argument("--source", default="created")
    parser.add_argument("--item-id")
    parser.add_argument("--source-url")
    parser.add_argument("--revision")
    parser.add_argument("--status", choices=schema["properties"]["tracking"]["properties"]["status"]["enum"], default="not-started")
    for name in ("created", "started", "completed"):
        parser.add_argument("--" + name)
    parser.add_argument("--interactive", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--yes", action="store_true")
    return parser


def _interactive(data: dict[str, Any], sources: dict[str, Any]) -> dict[str, Any]:
    schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
    records, _ = catalog.collect_labs()
    parents = []
    for key in ("niche", "domain", "subdomain", "groups", "collection", "title", "slug"):
        matching = [item for item in records if all(item.get(parent) == data.get(parent) for parent in parents)]
        suggestions = sorted({"/".join(item[key]) if key == "groups" else item[key] for item in matching if item.get(key)})
        default = data.get(key)
        if key == "slug" and not default and data.get("title"):
            default = catalog.slugify(data["title"])
        if key == "groups":
            answer = workflow.prompt("Groupings (slash separated)", "/".join(default or []), suggestions=suggestions, optional=True)
            data[key] = answer.split("/") if answer else []
        else:
            data[key] = workflow.prompt(key.capitalize(), default, suggestions=suggestions, optional=key in ("subdomain", "slug"))
        if key not in ("title", "slug"):
            parents.append(key)
    data["summary"] = workflow.prompt("Summary", data.get("summary"), optional=True)
    data["type"] = workflow.prompt("Type", data.get("type", "exercise"), choices=schema["properties"]["type"]["enum"])
    data["source"] = workflow.prompt("Source provider", data.get("source", "created"), choices=sorted(sources))
    provider = sources[data["source"]]
    data["difficulty"] = workflow.prompt("Difficulty", data.get("difficulty"), choices=schema["properties"]["difficulty"]["enum"] + list(provider.get("difficulty_map", {})), optional=True)
    data["skills"] = workflow.prompt_list("Skills", data.get("skills", []), suggestions=sorted({skill for item in records for skill in item["skills"]}))
    data["goals"] = workflow.prompt_list("Goals", data.get("goals", []))
    data["tools"] = workflow.prompt_list("Tools", data.get("tools", []))
    if provider["type"] != "local":
        for key in ("item_id", "source_url", "revision"):
            data[key] = workflow.prompt(key.replace("_", " ").capitalize(), data.get(key), optional=True)
    for key in ("solution", "demo"):
        data.setdefault("links", {})[key] = workflow.prompt(key.capitalize() + " link", data.get("links", {}).get(key), optional=True)
    data["links"] = {key: value for key, value in data["links"].items() if value}
    data["status"] = workflow.prompt("Status", data.get("status", "not-started"), choices=schema["properties"]["tracking"]["properties"]["status"]["enum"])
    data["created"] = data.get("created") or date.today().isoformat()
    for key in ("created", "started", "completed"):
        data[key] = workflow.prompt(key.capitalize() + " date YYYY-MM-DD", data.get(key), optional=key != "created")
    return data


def main() -> int:
    parser = _parser()
    args = parser.parse_args()
    if args.interactive and (args.yes or args.dry_run):
        parser.error("--interactive cannot be combined with --yes or --dry-run")
    if not args.interactive and not args.dry_run and not args.yes:
        parser.error("writing requires --yes")
    try:
        sources = catalog.load_sources()
        data = vars(args).copy()
        data["skills"] = args.skill
        data["goals"] = args.goal
        data["tools"] = args.tool
        data["links"] = workflow.parse_links(args.link)
        if args.interactive:
            data = _interactive(data, sources)
        elif not all(data.get(key) for key in ("niche", "domain", "collection", "title")):
            parser.error("niche, domain, collection, and title are required")
        plan = plan_lab(data, sources)
        preview_plan(plan)
        if args.dry_run:
            return 0
        if args.interactive and not workflow.confirm():
            print("No changes made.")
            return 0
        write_plans([plan], sources)
        print(f"Created {catalog.display_path(plan['path'])}")
    except (catalog.CatalogError, OSError, EOFError, KeyboardInterrupt) as error:
        if isinstance(error, (EOFError, KeyboardInterrupt)):
            print("\nNo changes made.")
            return 0
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
