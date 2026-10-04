#!/usr/bin/env python3
"""Validate lab metadata and build deterministic, source-independent catalogs.

A lab's path gives its browsing facets; lab.json keeps only maintained facts and
source provenance. Keeping those boundaries strict prevents one provider's
catalog from quietly becoming the repository's hierarchy schema.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import sys
import tempfile
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[2]
NICHES = ROOT / "niches"
SCHEMA_DIR = ROOT / ".meta/catalog/schema"
LAB_SCHEMA_PATH = SCHEMA_DIR / "lab.schema.json"
SOURCE_SCHEMA_PATH = SCHEMA_DIR / "source.schema.json"
SOURCES_PATH = ROOT / ".meta/catalog/sources.json"
LABS_PATH = ROOT / ".meta/catalog/labs.json"
CATALOG_PATH = ROOT / "CATALOG.md"

SLUG_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LAB_DIR_PATTERN = re.compile(r"(?:(?P<order>[0-9]+)-)?(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)")


class CatalogError(Exception):
    """An expected metadata or catalog problem suitable for the command line."""


def display_path(path: Path) -> str:
    """Return a repository-relative path when possible."""
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def read_json(path: Path) -> Any:
    """Read UTF-8 JSON and report common file and parse errors clearly."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise CatalogError(f"Missing required file: {display_path(path)}") from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        if isinstance(error, json.JSONDecodeError):
            location, detail = f" at line {error.lineno}, column {error.colno}", error.msg
        else:
            location, detail = "", "file is not valid UTF-8"
        raise CatalogError(f"Invalid JSON in {display_path(path)}{location}: {detail}") from error


def load_schema(path: Path) -> dict[str, Any]:
    """Read and validate a Draft 2020-12 JSON Schema."""
    schema = read_json(path)
    if not isinstance(schema, dict):
        raise CatalogError(f"Schema must be a JSON object: {display_path(path)}")
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as error:
        raise CatalogError(f"Invalid schema in {display_path(path)}: {error.message}") from error
    return schema


def _instance_path(error: Any) -> str:
    """Format a jsonschema instance path for concise diagnostics."""
    parts = [str(part) for part in error.absolute_path]
    return "$" + "".join(f"[{part}]" if part.isdigit() else f".{part}" for part in parts)


def validate_document(document: Any, schema: dict[str, Any], label: str) -> None:
    """Validate a document and include every actionable schema error."""
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(document),
        key=lambda error: (list(map(str, error.absolute_path)), error.message),
    )
    if errors:
        detail = "; ".join(f"{_instance_path(error)} {error.message}" for error in errors)
        raise CatalogError(f"Invalid {label}: {detail}")


def load_sources() -> dict[str, Any]:
    """Load and validate the source registry."""
    sources = read_json(SOURCES_PATH)
    validate_document(sources, load_schema(SOURCE_SCHEMA_PATH), display_path(SOURCES_PATH))
    return sources


def slugify(value: str) -> str:
    """Make a predictable ASCII folder slug from a human-readable title."""
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def lab_paths() -> list[Path]:
    """Find every metadata file so an illegal-depth lab cannot hide from checks."""
    if not NICHES.is_dir():
        raise CatalogError(f"Missing lab hierarchy directory: {display_path(NICHES)}")
    return sorted(NICHES.rglob("lab.json"))


def _lab_path_parts(metadata_path: Path) -> tuple[str, str, str | None, str, str, int | None]:
    """Parse only the two supported hierarchy shapes and the optional order prefix.

    The metadata filename is included in ``relative.parts``. A fourth structural
    level between domain and collection is deliberately rejected.
    """
    absolute_path = metadata_path.resolve()
    try:
        relative = absolute_path.relative_to(NICHES.resolve())
    except ValueError as error:
        raise CatalogError(f"Lab must live under niches/: {display_path(metadata_path)}") from error
    if relative.name != "lab.json" or len(relative.parts) not in {5, 6}:
        raise CatalogError(
            "A lab must be at niches/<niche>/<domain>/<collection>/<lab>/lab.json or "
            "niches/<niche>/<domain>/<subdomain>/<collection>/<lab>/lab.json: "
            f"{display_path(metadata_path)}"
        )
    if len(relative.parts) == 5:
        niche, domain, collection, lab_dir, _ = relative.parts
        subdomain = None
    else:
        niche, domain, subdomain, collection, lab_dir, _ = relative.parts
    for label, value in (("niche", niche), ("domain", domain), ("subdomain", subdomain), ("collection", collection)):
        if value is not None and not SLUG_PATTERN.fullmatch(value):
            raise CatalogError(f"Invalid {label} directory {value!r} in {display_path(metadata_path)}.")
    match = LAB_DIR_PATTERN.fullmatch(lab_dir)
    if match is None:
        raise CatalogError(f"Lab directory must be a lowercase slug with an optional numeric prefix: {display_path(metadata_path.parent)}")
    order_value = match.group("order")
    order = int(order_value) if order_value is not None else None
    if order == 0:
        raise CatalogError(f"Lab order must be positive: {display_path(metadata_path)}")
    return niche, domain, subdomain, collection, match.group("slug"), order


def source_for(provider: str, sources: dict[str, Any]) -> dict[str, Any]:
    """Return a registered source, rejecting typos without path-based inference."""
    source = sources.get(provider)
    if source is None:
        raise CatalogError(f"Source provider {provider!r} is not registered in .meta/catalog/sources.json.")
    return source


def require_copy_permission(provider: str, sources: dict[str, Any]) -> dict[str, Any]:
    """Return source policy only when repository tooling may materialize content."""
    source = source_for(provider, sources)
    policy = source.get("reuse", {}).get("policy")
    if policy != "copy":
        raise CatalogError(
            f"Source {provider!r} has reuse policy {policy!r}; copying requires policy 'copy'."
        )
    return source


def normalize_difficulty(value: str, provider: str, sources: dict[str, Any], lab_schema: dict[str, Any] | None = None) -> str:
    """Map a source-specific label onto the repository's small difficulty scale."""
    schema = lab_schema or load_schema(LAB_SCHEMA_PATH)
    normalized = schema["properties"]["difficulty"]["enum"]
    if value in normalized:
        return value
    mappings = source_for(provider, sources).get("difficulty_map", {})
    mapped = mappings.get(value)
    if mapped in normalized:
        return mapped
    choices = ", ".join(normalized)
    if mappings:
        choices += ", or a configured source level (" + ", ".join(sorted(mappings)) + ")"
    raise CatalogError(f"Unknown difficulty {value!r}; use {choices}.")


def lab_record(metadata_path: Path, metadata: Any, sources: dict[str, Any], lab_schema: dict[str, Any] | None = None) -> dict[str, Any]:
    """Validate local metadata and combine it with hierarchy-derived facts."""
    schema = lab_schema or load_schema(LAB_SCHEMA_PATH)
    validate_document(metadata, schema, display_path(metadata_path))
    if not isinstance(metadata, dict):
        raise CatalogError(f"Lab metadata must be a JSON object: {display_path(metadata_path)}")
    niche, domain, subdomain, collection, slug, order = _lab_path_parts(metadata_path)
    source_item = metadata["source"]
    provider = source_item["provider"]
    provider_data = source_for(provider, sources)
    if provider_data["type"] == "local":
        if "item_id" in source_item or "url" in source_item:
            raise CatalogError(f"Local source {provider!r} cannot have an external item ID or URL: {display_path(metadata_path)}.")
    elif not source_item.get("item_id") or not source_item.get("url"):
        raise CatalogError(f"External source {provider!r} needs an item_id and URL: {display_path(metadata_path)}.")

    record: dict[str, Any] = {
        "title": metadata["title"],
        "kind": metadata["kind"],
        "status": metadata["status"],
        "skills": sorted(metadata["skills"]),
        "source": dict(source_item),
        "dates": {key: metadata["dates"][key] for key in ("created", "started", "updated", "completed")},
        "tracking": dict(metadata["tracking"]),
        "niche": niche,
        "domain": domain,
        "subdomain": subdomain,
        "collection": collection,
        "slug": slug,
        "order": order,
        "path": absolute_path_relative(metadata_path),
    }
    if "difficulty" in metadata:
        record["difficulty"] = metadata["difficulty"]
    return record


def absolute_path_relative(metadata_path: Path) -> str:
    """Return the lab directory relative to the repository root."""
    return metadata_path.resolve().parent.relative_to(ROOT.resolve()).as_posix()


def _collection_key(record: dict[str, Any]) -> tuple[str, str, str | None, str]:
    """Return the complete, source-independent collection identity."""
    return (record["niche"], record["domain"], record["subdomain"], record["collection"])


def collect_labs(overrides: Mapping[Path, Any] | None = None, sources_override: dict[str, Any] | None = None) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Validate all labs and return normalized records in stable hierarchy order."""
    lab_schema = load_schema(LAB_SCHEMA_PATH)
    sources = sources_override if sources_override is not None else load_sources()
    validate_document(sources, load_schema(SOURCE_SCHEMA_PATH), display_path(SOURCES_PATH))
    override_map = {path.resolve(): value for path, value in (overrides or {}).items()}
    records: list[dict[str, Any]] = []
    discovered: set[Path] = set()
    for metadata_path in lab_paths():
        absolute = metadata_path.resolve()
        discovered.add(absolute)
        metadata = override_map.get(absolute)
        if metadata is None:
            metadata = read_json(metadata_path)
        records.append(lab_record(metadata_path, metadata, sources, lab_schema))
    for metadata_path, metadata in sorted(override_map.items()):
        if metadata_path not in discovered:
            records.append(lab_record(metadata_path, metadata, sources, lab_schema))

    source_ids: dict[tuple[str, str], str] = {}
    lab_slugs: dict[tuple[tuple[str, str, str | None, str], str], str] = {}
    orders: dict[tuple[tuple[str, str, str | None, str], int], str] = {}
    collection_orders: dict[tuple[str, str, str | None, str], set[int | None]] = {}
    for record in records:
        provider, item_id = record["source"]["provider"], record["source"].get("item_id")
        if item_id is not None:
            key = (provider, item_id)
            previous = source_ids.get(key)
            if previous is not None:
                raise CatalogError(f"Duplicate source item ID {item_id!r} for {provider!r}: {previous} and {record['path']}.")
            source_ids[key] = record["path"]
        collection = _collection_key(record)
        slug_key = (collection, record["slug"])
        previous = lab_slugs.get(slug_key)
        if previous is not None:
            raise CatalogError(f"Duplicate lab slug {record['slug']!r} in collection: {previous} and {record['path']}.")
        lab_slugs[slug_key] = record["path"]
        order = record["order"]
        collection_orders.setdefault(collection, set()).add(order)
        if order is not None:
            order_key = (collection, order)
            previous = orders.get(order_key)
            if previous is not None:
                raise CatalogError(f"Duplicate order {order} in collection: {previous} and {record['path']}.")
            orders[order_key] = record["path"]
    for collection, values in collection_orders.items():
        if None in values and len(values) > 1:
            name = "/".join(part for part in collection if part)
            raise CatalogError(f"Collection {name} mixes numbered and unnumbered lab folders.")

    records.sort(key=lambda item: (item["niche"], item["domain"], item["subdomain"] or "", item["collection"], item["order"] if item["order"] is not None else sys.maxsize, item["path"]))
    return records, sources


def render_labs(records: list[dict[str, Any]]) -> str:
    """Serialize records in their normalized deterministic order."""
    return json.dumps(records, indent=2, ensure_ascii=False) + "\n"


def _markdown_text(value: str) -> str:
    """Escape characters that can break a title or value in a Markdown table."""
    return value.replace("\\", "\\\\").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def _title(value: str) -> str:
    """Make path slugs readable without assigning meaning to particular facets."""
    return value.replace("-", " ").title()


def render_catalog(records: list[dict[str, Any]], sources: dict[str, Any]) -> str:
    """Render a readable catalog grouped only by hierarchy, with sources per row."""
    lines = ["# Lab Catalog", "", f"{len(records)} labs, generated from their neighboring `lab.json` files.", "", "> Do not edit this file by hand. Run `python3 .meta/scripts/catalog.py`."]
    groups: dict[tuple[str, str, str | None, str], list[dict[str, Any]]] = {}
    for record in records:
        groups.setdefault(_collection_key(record), []).append(record)
    for (niche, domain, subdomain, collection), group in groups.items():
        facets = [niche, domain]
        if subdomain:
            facets.append(subdomain)
        facets.append(collection)
        lines.extend(["", f"## {' / '.join(_title(part) for part in facets)}", "", "| # | Lab | Kind | Difficulty | Status | Skills | Source |", "| ---: | --- | --- | --- | --- | --- | --- |"])
        for index, record in enumerate(group, start=1):
            source_item = record["source"]
            provider = source_item["provider"]
            source = sources[provider]
            item_url = source_item.get("url")
            label = _markdown_text(source["name"])
            if item_url:
                original = f"[{label}]({item_url})"
            else:
                original = label
            status = record["status"].replace("-", " ").title()
            skills = ", ".join(record["skills"]) or "—"
            order = record["order"] if record["order"] is not None else index
            difficulty = record.get("difficulty", "—").capitalize()
            lines.append(f"| {order} | [{_markdown_text(record['title'])}]({record['path']}/) | {record['kind'].replace('-', ' ').title()} | {difficulty} | {status} | {_markdown_text(skills)} | {original} |")
    return "\n".join(lines) + "\n"


def write_text_atomic(path: Path, content: str) -> None:
    """Replace one UTF-8 file atomically and preserve existing permissions."""
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="", dir=path.parent, delete=False) as temporary:
            temporary_path = Path(temporary.name)
            temporary.write(content)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.chmod(temporary_path, mode)
        temporary_path.replace(path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def expected_catalogs(records: list[dict[str, Any]], sources: dict[str, Any]) -> dict[Path, str]:
    """Build the exact generated outputs used by write and check modes."""
    return {LABS_PATH: render_labs(records), CATALOG_PATH: render_catalog(records, sources)}


def write_catalog(records: list[dict[str, Any]], sources: dict[str, Any]) -> None:
    """Write generated outputs only when their contents have changed."""
    for path, content in expected_catalogs(records, sources).items():
        if not path.exists() or path.read_bytes() != content.encode("utf-8"):
            write_text_atomic(path, content)


def update_catalog(check: bool = False) -> None:
    """Validate the corpus and either write or check its generated catalogs."""
    records, sources = collect_labs()
    expected = expected_catalogs(records, sources)
    if check:
        stale = [display_path(path) for path, content in expected.items() if not path.exists() or path.read_bytes() != content.encode("utf-8")]
        if stale:
            raise CatalogError("Generated catalog files are stale: " + ", ".join(stale) + ". Run python3 .meta/scripts/catalog.py.")
        print(f"Catalog is valid and current ({len(records)} labs).")
        return
    write_catalog(records, sources)
    print(f"Generated catalogs for {len(records)} labs.")


def main() -> int:
    """Run catalog generation or report stale output without mutation."""
    parser = argparse.ArgumentParser(description="Validate lab metadata and generate the lab catalogs.")
    parser.add_argument("--check", action="store_true", help="validate without writing and fail if generated files are stale")
    args = parser.parse_args()
    try:
        update_catalog(check=args.check)
    except (CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
