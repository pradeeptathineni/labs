#!/usr/bin/env python3
"""Create one lab while keeping hierarchy, metadata, and provenance distinct."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from datetime import date
from pathlib import Path
from typing import Any

import catalog
import lab_sync


def _parser(kind_values: list[str], status_values: list[str]) -> argparse.ArgumentParser:
    """Build the flag interface from the maintained metadata schema."""
    parser = argparse.ArgumentParser(description="Create a lab and refresh the generated catalog.")
    parser.add_argument("niche", nargs="?", help="broad problem-solving area")
    parser.add_argument("domain", nargs="?", help="recognizable discipline")
    parser.add_argument("collection", nargs="?", help="coherent body of work")
    parser.add_argument("title", nargs="?", help="human-readable lab title")
    parser.add_argument("--subdomain", help="optional stable specialization one level below domain")
    parser.add_argument("--slug", help="folder slug; defaults to one derived from the title")
    parser.add_argument("--source", help="registered provenance provider (defaults to created)")
    parser.add_argument("--kind", choices=kind_values, default="project")
    parser.add_argument("--status", choices=status_values, default="not-started")
    parser.add_argument("--difficulty", help="normalized level or a source-mapped level")
    parser.add_argument("--skill", action="append", default=[], metavar="SLUG", help="skill tag; repeat as needed")
    parser.add_argument("--item-id", "--source-id", dest="item_id", help="stable source item ID")
    parser.add_argument("--source-url", help="canonical URL for this source item")
    parser.add_argument("--ordered", action="store_true", help="number this collection, including its first lab")
    parser.add_argument("--interactive", action="store_true", help="prompt for values and preview before writing")
    parser.add_argument("--yes", action="store_true", help="confirm a noninteractive write explicitly")
    return parser


def _existing_values() -> dict[str, set[str]]:
    """Collect existing facet and lab slugs for the interactive naming prompts."""
    values = {key: set() for key in ("niche", "domain", "subdomain", "collection", "lab")}
    for metadata_path in catalog.lab_paths():
        niche, domain, subdomain, collection, slug, _ = catalog._lab_path_parts(metadata_path)
        values["niche"].add(niche)
        values["domain"].add(domain)
        if subdomain:
            values["subdomain"].add(subdomain)
        values["collection"].add(collection)
        values["lab"].add(slug)
    return values


def _collection_slugs(niche: str, domain: str, subdomain: str | None, collection: str) -> list[str]:
    """List names already occupied in the exact target collection."""
    parent = catalog.NICHES / niche / domain
    if subdomain:
        parent /= subdomain
    parent /= collection
    if not parent.is_dir():
        return []
    slugs = []
    for child in parent.iterdir():
        match = catalog.LAB_DIR_PATTERN.fullmatch(child.name)
        if child.is_dir() and match:
            slugs.append(match.group("slug"))
    return sorted(set(slugs))


def _source_item_ids(provider: str) -> list[str]:
    """List source item IDs already assigned to one provider."""
    identifiers = []
    for metadata_path in catalog.lab_paths():
        source = catalog.read_json(metadata_path).get("source", {})
        if source.get("provider") == provider and source.get("item_id"):
            identifiers.append(source["item_id"])
    return sorted(set(identifiers))


def _prompt_value(label: str, default: str, *, existing: list[str] = (), choices: list[str] = (), free: bool = True, optional: bool = False) -> str:
    """Prompt while distinguishing reusable names from closed schema enums."""
    hints: list[str] = []
    if existing:
        hints.append("existing values: " + ", ".join(existing))
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
        if not free and value not in choices:
            print("Choose one of the listed values.")
            continue
        return value


def _interactive_values(args: argparse.Namespace, schema: dict[str, Any], sources: dict[str, Any]) -> None:
    """Fill missing CLI values and show repository values before choosing names."""
    existing = _existing_values()
    args.niche = _prompt_value("Niche", args.niche or "", existing=sorted(existing["niche"]))
    args.domain = _prompt_value("Domain", args.domain or "", existing=sorted(existing["domain"]))
    args.subdomain = _prompt_value("Subdomain", args.subdomain or "", existing=sorted(existing["subdomain"]), optional=True) or None
    args.collection = _prompt_value("Collection", args.collection or "", existing=sorted(existing["collection"]))
    args.title = _prompt_value("Title", args.title or "")
    default_slug = args.slug or catalog.slugify(args.title)
    args.slug = _prompt_value(
        "Lab slug", default_slug,
        existing=_collection_slugs(args.niche, args.domain, args.subdomain, args.collection),
    )
    kind_values = schema["properties"]["kind"]["enum"]
    status_values = schema["properties"]["status"]["enum"]
    current_kinds = sorted({catalog.read_json(path)["kind"] for path in catalog.lab_paths()})
    current_statuses = sorted({catalog.read_json(path)["status"] for path in catalog.lab_paths()})
    args.kind = _prompt_value("Kind", args.kind or "project", choices=kind_values, existing=current_kinds, free=False)
    args.status = _prompt_value("Status", args.status or "not-started", choices=status_values, existing=current_statuses, free=False)
    provider_ids = sorted(sources)
    current_providers = sorted({catalog.read_json(path)["source"]["provider"] for path in catalog.lab_paths()})
    args.source = _prompt_value("Source provider", args.source or "created", choices=provider_ids, existing=current_providers, free=False)
    source = catalog.source_for(args.source, sources)
    difficulty_values = sorted(set(schema["properties"]["difficulty"]["enum"]) | set(source.get("difficulty_map", {})))
    current_difficulties = sorted({catalog.read_json(path).get("difficulty") for path in catalog.lab_paths()} - {None})
    args.difficulty = _prompt_value("Difficulty", args.difficulty or "", choices=difficulty_values, existing=current_difficulties, free=False, optional=True)
    skills = ",".join(args.skill)
    skill_text = input(f"Skills [{skills}] (comma separated; '-' clears): ").strip()
    if skill_text == "-":
        args.skill = []
    elif skill_text:
        args.skill = [item.strip() for item in skill_text.split(",") if item.strip()]
    if source["type"] != "local":
        args.item_id = _prompt_value("Source item ID", args.item_id or "", existing=_source_item_ids(args.source))
        args.source_url = _prompt_value("Source item URL", args.source_url or "")
    else:
        args.item_id = None
        args.source_url = None
    if args.difficulty == "":
        args.difficulty = None
    args.ordered = _yes_no("Number this collection?", args.ordered)


def _yes_no(label: str, default: bool) -> bool:
    """Ask a yes/no question without treating Enter as confirmation."""
    suffix = "Y/n" if default else "y/N"
    answer = input(f"{label} [{suffix}]: ").strip().casefold()
    if not answer:
        return default
    return answer in {"y", "yes"}


def _check_parent_safety(parent: Path) -> None:
    """Reject symlinked hierarchy components before creating directories."""
    try:
        relative = parent.relative_to(catalog.ROOT)
    except ValueError as error:
        raise catalog.CatalogError("The lab path must stay inside this repository.") from error
    current = catalog.ROOT
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise catalog.CatalogError(f"Refusing to create a lab through symlink: {current}")
        if current.exists() and not current.is_dir():
            raise catalog.CatalogError(f"Lab parent is not a directory: {current}")
    try:
        parent.resolve().relative_to(catalog.NICHES.resolve())
    except ValueError as error:
        raise catalog.CatalogError("The lab path must stay under niches/.") from error


def _next_order(parent: Path) -> int:
    """Choose the first unused positive number in an ordered collection."""
    occupied = set()
    if parent.exists():
        for child in parent.iterdir():
            match = catalog.LAB_DIR_PATTERN.fullmatch(child.name)
            if child.is_dir() and match and match.group("order"):
                occupied.add(int(match.group("order")))
    candidate = 1
    while candidate in occupied:
        candidate += 1
    return candidate


def _lab_folder(parent: Path, slug: str, ordered: bool) -> str:
    """Choose a safe folder name and reject any existing slug in the collection."""
    if parent.exists():
        for child in parent.iterdir():
            match = catalog.LAB_DIR_PATTERN.fullmatch(child.name)
            if match and match.group("slug") == slug:
                raise catalog.CatalogError(f"Lab slug {slug!r} already exists: {catalog.display_path(child)}.")
        existing_ordered = any(
            child.is_dir() and (match := catalog.LAB_DIR_PATTERN.fullmatch(child.name)) and match.group("order")
            for child in parent.iterdir()
        )
        if existing_ordered:
            ordered = True
    return f"{_next_order(parent):02d}-{slug}" if ordered else slug


def _starter_readme(title: str, source_name: str | None, item_url: str | None) -> str:
    """Create a neutral starting point that links rather than copies source text."""
    lines = [f"# {title}", ""]
    if source_name and item_url:
        lines.extend([f"Source: [{source_name}]({item_url})", ""])
    lines.extend(["## Problem", ""])
    return "\n".join(lines)


def create_lab(args: argparse.Namespace, schema: dict[str, Any], sources: dict[str, Any], *, readme_override: str | None = None, additional_files: dict[str, str] | None = None, metadata_override: dict[str, Any] | None = None) -> Path:
    """Validate a proposed lab, stage its two files, and atomically add its folder."""
    for label, value in (("niche", args.niche), ("domain", args.domain), ("subdomain", args.subdomain), ("collection", args.collection)):
        if value is not None and not catalog.SLUG_PATTERN.fullmatch(value):
            raise catalog.CatalogError(f"{label.capitalize()} must be lowercase kebab-case: {value!r}.")
    if not args.title.strip():
        raise catalog.CatalogError("Title cannot be empty.")
    provider_id = args.source or "created"
    source_provider = catalog.source_for(provider_id, sources)
    if source_provider["type"] == "local":
        if args.item_id or args.source_url:
            raise catalog.CatalogError(f"Local source {provider_id!r} cannot have an item ID or URL.")
        source_item: dict[str, str] = {"provider": provider_id}
    else:
        if not args.item_id or not args.source_url:
            raise catalog.CatalogError("External sources need both --item-id and --source-url.")
        source_item = {"provider": provider_id, "item_id": args.item_id.strip(), "url": args.source_url.strip()}
    slug = args.slug or catalog.slugify(args.title)
    if not catalog.SLUG_PATTERN.fullmatch(slug):
        raise catalog.CatalogError("Slug must use lowercase letters or numbers separated by hyphens.")
    parent = catalog.NICHES / args.niche / args.domain
    if args.subdomain:
        parent /= args.subdomain
    parent /= args.collection
    _check_parent_safety(parent)
    folder = _lab_folder(parent, slug, args.ordered)
    target = parent / folder
    if target.exists():
        raise catalog.CatalogError(f"Refusing to overwrite existing path: {catalog.display_path(target)}.")
    difficulty = catalog.normalize_difficulty(args.difficulty, provider_id, sources, schema) if args.difficulty else None
    today = date.today().isoformat()
    source_name = source_provider["name"] if source_item.get("url") else None
    readme = readme_override if readme_override is not None else _starter_readme(args.title.strip(), source_name, source_item.get("url"))
    content_entries = [("README.md", readme.encode("utf-8"), False)]
    content_entries.extend((relative_path, content.encode("utf-8"), False) for relative_path, content in (additional_files or {}).items())
    metadata: dict[str, Any] = metadata_override or {
        "title": args.title.strip(),
        "kind": args.kind,
        "status": args.status,
        "skills": sorted(set(args.skill)),
        "source": source_item,
        "dates": {"created": today, "started": today if args.status == "in-progress" else None, "updated": today, "completed": today if args.status == "complete" else None},
        "tracking": {"content_sha256": lab_sync.fingerprint_entries(content_entries)},
    }
    metadata_path = target / "lab.json"
    records, current_sources = catalog.collect_labs(overrides={metadata_path: metadata})
    with tempfile.TemporaryDirectory(prefix=".lab-init-", dir=parent if parent.exists() else catalog.NICHES) as temporary_dir:
        staged = Path(temporary_dir) / folder
        staged.mkdir()
        catalog.write_text_atomic(staged / "README.md", readme)
        catalog.write_text_atomic(staged / "lab.json", json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")
        for relative_path, content in (additional_files or {}).items():
            output_path = (staged / relative_path).resolve()
            try:
                output_path.relative_to(staged.resolve())
            except ValueError as error:
                raise catalog.CatalogError("Additional lab files must stay inside the new lab.") from error
            catalog.write_text_atomic(output_path, content)
        parent.mkdir(parents=True, exist_ok=True)
        staged.rename(target)
    lab_sync.sync_all(check=False)
    return target


def main() -> int:
    """Create a lab, optionally using confirmation-first interactive input."""
    try:
        schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
        sources = catalog.load_sources()
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    parser = _parser(schema["properties"]["kind"]["enum"], schema["properties"]["status"]["enum"])
    args = parser.parse_args()
    try:
        if args.interactive:
            _interactive_values(args, schema, sources)
        else:
            if not all((args.niche, args.domain, args.collection, args.title)):
                parser.error("niche, domain, collection, and title are required unless --interactive is used")
            args.source = args.source or "created"
        for label, value in (("niche", args.niche), ("domain", args.domain), ("subdomain", args.subdomain), ("collection", args.collection)):
            if value is not None and not catalog.SLUG_PATTERN.fullmatch(value):
                raise catalog.CatalogError(f"{label.capitalize()} must be lowercase kebab-case: {value!r}.")
        if not args.title.strip():
            raise catalog.CatalogError("Title cannot be empty.")
        if args.slug and not catalog.SLUG_PATTERN.fullmatch(args.slug):
            raise catalog.CatalogError("Slug must use lowercase letters or numbers separated by hyphens.")
        provider = catalog.source_for(args.source or "created", sources)
        if provider["type"] != "local" and not args.interactive and (not args.item_id or not args.source_url):
            parser.error("external sources need --item-id and --source-url")
        slug = args.slug or catalog.slugify(args.title)
        parent = catalog.NICHES / args.niche / args.domain
        if args.subdomain:
            parent /= args.subdomain
        parent /= args.collection
        _check_parent_safety(parent)
        folder = _lab_folder(parent, slug, args.ordered)
        target = parent / folder
        item_url = args.source_url if provider["type"] != "local" else None
        readme = _starter_readme(args.title.strip(), provider["name"] if item_url else None, item_url)
        tracking = lab_sync.fingerprint_entries([("README.md", readme.encode("utf-8"), False)])
        metadata: dict[str, Any] = {
            "title": args.title.strip(), "kind": args.kind, "status": args.status,
            "skills": sorted(set(args.skill)),
            "source": {"provider": args.source or "created"},
            "dates": {"created": date.today().isoformat(), "started": date.today().isoformat() if args.status == "in-progress" else None, "updated": date.today().isoformat(), "completed": date.today().isoformat() if args.status == "complete" else None},
            "tracking": {"content_sha256": tracking},
        }
        if provider["type"] != "local":
            metadata["source"].update({"item_id": args.item_id, "url": args.source_url})
        if args.difficulty:
            metadata["difficulty"] = catalog.normalize_difficulty(args.difficulty, args.source or "created", sources, schema)
        catalog.collect_labs(overrides={target / "lab.json": metadata})
        if args.interactive:
            print(f"\nPath:\n{catalog.display_path(target)}\n\nMetadata:\n{json.dumps(metadata, indent=2, ensure_ascii=False)}")
            if not args.yes and not _yes_no("Write these changes?", False):
                print("No changes made.")
                return 0
        created = create_lab(args, schema, sources, metadata_override=metadata)
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Created {catalog.display_path(created)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
