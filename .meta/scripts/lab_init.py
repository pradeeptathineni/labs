#!/usr/bin/env python3
"""Create one lab without overwriting work and refresh the aggregate catalog.

The hierarchy determines niche, domain, provider, slug, and optional order.
Maintained facts such as title, skills, and source-item identity are collected
at creation so a new folder is catalog-ready from its first commit.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import catalog


def _parser(kind_values: list[str], status_values: list[str]) -> argparse.ArgumentParser:
    """Build the CLI with choices taken from the checked-in metadata schema."""
    parser = argparse.ArgumentParser(
        description="Create a lab folder, its starter README, metadata, and catalog entry."
    )
    parser.add_argument("niche", help="broad problem-solving area, such as code")
    parser.add_argument("provider", help="registered source or local-work category")
    parser.add_argument("title", help="human-readable lab title")
    parser.add_argument("--domain", help="optional discipline within the niche")
    parser.add_argument("--slug", help="folder slug; defaults to one derived from title")
    parser.add_argument(
        "--kind", choices=kind_values, default="project", help="what kind of lab this is"
    )
    parser.add_argument(
        "--status",
        choices=status_values,
        default="not-started",
        help="initial lifecycle state",
    )
    parser.add_argument(
        "--difficulty",
        help="normalized difficulty, or a provider level mapped in sources.json",
    )
    parser.add_argument(
        "--skill",
        action="append",
        default=[],
        metavar="SLUG",
        help="skill practiced by this lab; repeat for each lowercase kebab-case skill",
    )
    parser.add_argument("--source-id", help="stable ID of the external item")
    parser.add_argument(
        "--source-url", dest="item_url", help="canonical URL of the external item"
    )
    return parser


def _check_parent_safety(parent: Path) -> None:
    """Reject symlinked hierarchy components before making any directories."""
    try:
        relative = parent.relative_to(catalog.ROOT)
    except ValueError as error:
        raise catalog.CatalogError(
            "The lab path must stay inside this repository."
        ) from error
    current = catalog.ROOT
    for part in relative.parts:
        current = current / part
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
    occupied: set[int] = set()
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
    """Choose the folder name, rejecting duplicate slugs before creating anything."""
    if parent.exists():
        for child in parent.iterdir():
            match = catalog.LAB_DIR_PATTERN.fullmatch(child.name)
            if match and match.group("slug") == slug:
                raise catalog.CatalogError(
                    f"A lab with slug {slug!r} already exists: "
                    f"{catalog.display_path(child)}."
                )
    if ordered:
        return f"{_next_order(parent):02d}-{slug}"
    return slug


def _starter_readme(title: str, source_name: str | None, item_url: str | None) -> str:
    """Create a neutral starting point without copying or inventing challenge text."""
    lines = [f"# {title}", ""]
    if source_name and item_url:
        lines.extend([f"Source: [{source_name}]({item_url})", ""])
    lines.extend(["## Problem", ""])
    return "\n".join(lines)


def main() -> int:
    """Create and validate a lab, then update the generated catalog."""
    try:
        schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
        sources = catalog.load_sources()
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    parser = _parser(
        schema["properties"]["kind"]["enum"],
        schema["properties"]["status"]["enum"],
    )
    args = parser.parse_args()

    try:
        for label, value in (
            ("niche", args.niche),
            ("provider", args.provider),
            ("domain", args.domain),
        ):
            if value is None:
                continue
            if not catalog.SLUG_PATTERN.fullmatch(value):
                raise catalog.CatalogError(
                    f"{label.capitalize()} must be lowercase kebab-case: {value!r}."
                )
        if not args.title.strip():
            raise catalog.CatalogError("Title cannot be empty.")
        slug = args.slug or catalog.slugify(args.title)
        if not catalog.SLUG_PATTERN.fullmatch(slug):
            raise catalog.CatalogError(
                "Slug must use lowercase letters or numbers separated by hyphens."
            )
        parent = catalog.NICHES / args.niche
        if args.domain is not None:
            parent /= args.domain
        parent /= args.provider
        if bool(args.source_id) != bool(args.item_url):
            raise catalog.CatalogError("Provide both --source-id and --source-url.")
        provider_data = catalog.source_for(args.provider, sources)
        if provider_data["type"] == "local":
            if args.source_id or args.item_url:
                raise catalog.CatalogError(
                    f"Provider {args.provider!r} is local; omit external source options."
                )
            collection = None
        else:
            collection = catalog.collection_for(
                args.niche, args.domain, args.provider, sources
            )
            if not args.source_id or not args.item_url:
                raise catalog.CatalogError(
                    "External labs need both --source-id and --source-url."
                )

        _check_parent_safety(parent)
        folder = _lab_folder(
            parent, slug, bool(collection and collection.get("ordered", False))
        )
        target = parent / folder
        if target.exists():
            raise catalog.CatalogError(
                f"Refusing to overwrite existing path: {catalog.display_path(target)}."
            )
        difficulty = (
            catalog.normalize_difficulty(
                args.difficulty, target / "lab.json", sources, schema
            )
            if args.difficulty
            else None
        )

        today = date.today().isoformat()
        metadata: dict[str, object] = {
            "title": args.title.strip(),
            "kind": args.kind,
            "status": args.status,
            "skills": sorted(set(args.skill)),
            "dates": {
                "created": today,
                "started": today if args.status == "in-progress" else None,
                "completed": today if args.status == "complete" else None,
            },
        }
        if difficulty:
            metadata["difficulty"] = difficulty
        if args.source_id and args.item_url:
            metadata["source"] = {"id": args.source_id, "url": args.item_url}

        metadata_path = target / "lab.json"
        record_list, current_sources = catalog.collect_labs(
            overrides={metadata_path: metadata}
        )

        parent.mkdir(parents=True, exist_ok=True)
        _check_parent_safety(parent)
        target.mkdir()
        source_name = sources.get(args.provider, {}).get("name") if args.source_id else None
        readme = _starter_readme(args.title.strip(), source_name, args.item_url)
        catalog.write_text_atomic(target / "README.md", readme)
        catalog.write_text_atomic(
            metadata_path, json.dumps(metadata, indent=2, ensure_ascii=False) + "\n"
        )
        catalog.write_catalog(record_list, current_sources)
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Created {catalog.display_path(target)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
