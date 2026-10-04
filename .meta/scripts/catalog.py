#!/usr/bin/env python3
"""Validate lab metadata and build deterministic repository catalogs.

The lab.json beside each lab is authoritative for maintained facts. Directory
names provide structural facts such as niche, provider, slug, path, and order;
the generated catalog combines both without asking for duplicate metadata.
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
LAB_DIR_PATTERN = re.compile(
    r"(?:(?P<order>[0-9]+)-)?(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)"
)


class CatalogError(Exception):
    """An expected metadata or catalog problem suitable for the command line."""


def display_path(path: Path) -> str:
    """Return a repository-relative path when possible."""
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def read_json(path: Path) -> Any:
    """Read UTF-8 JSON and turn common file/parse failures into useful errors."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise CatalogError(f"Missing required file: {display_path(path)}") from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        if isinstance(error, json.JSONDecodeError):
            location = f" at line {error.lineno}, column {error.colno}"
            detail = error.msg
        else:
            location = ""
            detail = "file is not valid UTF-8"
        raise CatalogError(
            f"Invalid JSON in {display_path(path)}{location}: {detail}"
        ) from error


def load_schema(path: Path) -> dict[str, Any]:
    """Read and validate a Draft 2020-12 JSON Schema."""
    schema = read_json(path)
    if not isinstance(schema, dict):
        raise CatalogError(f"Schema must be a JSON object: {display_path(path)}")
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as error:
        raise CatalogError(
            f"Invalid schema in {display_path(path)}: {error.message}"
        ) from error
    return schema


def _instance_path(error: Any) -> str:
    """Format a jsonschema instance path for concise diagnostics."""
    parts = [str(part) for part in error.absolute_path]
    return "$" + "".join(f"[{part}]" if part.isdigit() else f".{part}" for part in parts)


def validate_document(document: Any, schema: dict[str, Any], label: str) -> None:
    """Validate a document with jsonschema and report every actionable issue."""
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(document),
        key=lambda error: (list(map(str, error.absolute_path)), error.message),
    )
    if errors:
        detail = "; ".join(
            f"{_instance_path(error)} {error.message}" for error in errors
        )
        raise CatalogError(f"Invalid {label}: {detail}")


def load_sources() -> dict[str, Any]:
    """Load and validate the provider registry."""
    sources = read_json(SOURCES_PATH)
    schema = load_schema(SOURCE_SCHEMA_PATH)
    validate_document(sources, schema, display_path(SOURCES_PATH))
    return sources


def slugify(value: str) -> str:
    """Make a predictable ASCII folder slug from a human-readable title."""
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def _lab_path_parts(
    metadata_path: Path,
) -> tuple[str, str | None, str, str, int | None]:
    """Derive niche, optional domain, provider, slug, and order from a lab path.

    Both ``niche/provider/lab`` and ``niche/domain/provider/lab`` are useful:
    small or personal collections need not invent a domain just to fit a tree.
    """
    absolute_path = metadata_path.resolve()
    try:
        relative = absolute_path.relative_to(NICHES.resolve())
    except ValueError as error:
        raise CatalogError(
            f"Lab must live under {display_path(NICHES)}/: {display_path(metadata_path)}"
        ) from error

    if len(relative.parts) not in {4, 5} or relative.name != "lab.json":
        raise CatalogError(
            "A lab must be at niches/<niche>/<provider>/<lab>/lab.json or "
            "niches/<niche>/<domain>/<provider>/<lab>/lab.json: "
            f"{display_path(metadata_path)}"
        )

    if len(relative.parts) == 4:
        niche, provider, lab_dir, _ = relative.parts
        domain = None
    else:
        niche, domain, provider, lab_dir, _ = relative.parts
    for label, value in (("niche", niche), ("domain", domain), ("provider", provider)):
        if value is None:
            continue
        if not SLUG_PATTERN.fullmatch(value):
            raise CatalogError(
                f"Invalid {label} directory {value!r} in {display_path(metadata_path)}."
            )

    match = LAB_DIR_PATTERN.fullmatch(lab_dir)
    if match is None:
        raise CatalogError(
            f"Lab directory must be a lowercase slug with an optional numeric prefix: "
            f"{display_path(metadata_path.parent)}"
        )
    order_value = match.group("order")
    order = int(order_value) if order_value is not None else None
    if order == 0:
        raise CatalogError(f"Lab order must be positive: {display_path(metadata_path)}")
    return niche, domain, provider, match.group("slug"), order


def source_for(provider: str, sources: dict[str, Any]) -> dict[str, Any]:
    """Return a provider definition, rejecting unregistered path components."""
    source = sources.get(provider)
    if source is None:
        raise CatalogError(
            f"Provider {provider!r} is not registered in .meta/catalog/sources.json."
        )
    return source


def collection_for(
    niche: str, domain: str | None, provider: str, sources: dict[str, Any]
) -> dict[str, Any] | None:
    """Return collection metadata matching this path, if the source defines it."""
    source = source_for(provider, sources)
    location = niche if domain is None else f"{niche}/{domain}"
    return source.get("collections", {}).get(location)


def normalize_difficulty(
    value: str,
    metadata_path: Path,
    sources: dict[str, Any],
    lab_schema: dict[str, Any] | None = None,
) -> str:
    """Map an optional provider vocabulary onto the repository-wide levels.

    Source and collection mappings are data in ``sources.json``. A supplied
    normalized value needs no mapping; an unmapped provider value is rejected.
    """
    schema = lab_schema or load_schema(LAB_SCHEMA_PATH)
    normalized = schema["properties"]["difficulty"]["enum"]
    if value in normalized:
        return value

    niche, domain, provider, _, _ = _lab_path_parts(metadata_path)
    source = source_for(provider, sources)
    collection = collection_for(niche, domain, provider, sources)
    mappings = dict(source.get("difficulty_map", {}))
    if collection is not None:
        mappings.update(collection.get("difficulty_map", {}))
    mapped = mappings.get(value)
    if mapped in normalized:
        return mapped

    choices = ", ".join(normalized)
    if mappings:
        choices += ", or a configured source level (" + ", ".join(sorted(mappings)) + ")"
    raise CatalogError(f"Unknown difficulty {value!r}; use {choices}.")


def lab_record(
    metadata_path: Path,
    metadata: Any,
    sources: dict[str, Any],
    lab_schema: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate local metadata and enrich it with facts derived from its path."""
    schema = lab_schema or load_schema(LAB_SCHEMA_PATH)
    validate_document(metadata, schema, display_path(metadata_path))
    if not isinstance(metadata, dict):
        # The schema error above normally catches this; retain a clear guard for callers.
        raise CatalogError(f"Lab metadata must be an object: {display_path(metadata_path)}")

    niche, domain, provider, slug, order = _lab_path_parts(metadata_path)
    provider_data = source_for(provider, sources)
    collection = collection_for(niche, domain, provider, sources)
    source_item = metadata.get("source")

    if provider_data["type"] == "local":
        if source_item is not None:
            raise CatalogError(
                f"Local provider {provider!r} cannot have an external source object: "
                f"{display_path(metadata_path)}."
            )
    else:
        if source_item is None:
            raise CatalogError(
                f"Add a source id and URL to {display_path(metadata_path)}."
            )
        if collection is not None and collection.get("ordered", False) and order is None:
            collection_path = provider + "/" + niche
            if domain is not None:
                collection_path += "/" + domain
            raise CatalogError(
                f"Lab in ordered collection {collection_path} needs a "
                f"numeric folder prefix: {display_path(metadata_path.parent)}."
            )

    # The source directory names the provider; source.id and source.url identify
    # the particular external item without duplicating its provider or collection.
    record: dict[str, Any] = {
        "title": metadata["title"],
        "kind": metadata["kind"],
        "status": metadata["status"],
    }
    if "difficulty" in metadata:
        record["difficulty"] = metadata["difficulty"]
    record["skills"] = sorted(metadata["skills"])
    record["dates"] = {
        field: metadata["dates"][field]
        for field in ("created", "started", "completed")
    }
    if source_item is not None:
        record["source"] = {"id": source_item["id"], "url": source_item["url"]}

    record.update(
        {
            "niche": niche,
            "domain": domain,
            "provider": provider,
            "slug": slug,
            "path": metadata_path.resolve()
            .parent.relative_to(ROOT.resolve())
            .as_posix(),
        }
    )
    if order is not None:
        record["order"] = order
    return record


def collect_labs(
    overrides: Mapping[Path, Any] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Validate all intended lab folders and return their normalized records.

    Overrides let the initializer or metadata editor validate a proposed change
    before it writes that change to disk.
    """
    lab_schema = load_schema(LAB_SCHEMA_PATH)
    sources = load_sources()
    if not NICHES.is_dir():
        raise CatalogError(f"Missing lab hierarchy directory: {display_path(NICHES)}")
    override_map = {path.resolve(): value for path, value in (overrides or {}).items()}
    records: list[dict[str, Any]] = []
    discovered: set[Path] = set()

    # Lab folders have either three or four hierarchy levels below niches.
    metadata_paths = sorted(
        {*NICHES.glob("*/*/*/lab.json"), *NICHES.glob("*/*/*/*/lab.json")}
    )
    for metadata_path in metadata_paths:
        absolute_path = metadata_path.resolve()
        discovered.add(absolute_path)
        metadata = override_map.get(absolute_path)
        if metadata is None:
            metadata = read_json(metadata_path)
        records.append(lab_record(metadata_path, metadata, sources, lab_schema))

    # Include a new, not-yet-written lab during init validation.
    for metadata_path, metadata in sorted(override_map.items()):
        if metadata_path not in discovered:
            records.append(lab_record(metadata_path, metadata, sources, lab_schema))

    source_ids: dict[tuple[str, str], str] = {}
    numbered_labs: dict[tuple[str, str | None, str, int], str] = {}
    for record in records:
        if "source" in record:
            key = (record["provider"], record["source"]["id"])
            previous = source_ids.get(key)
            if previous is not None:
                raise CatalogError(
                    f"Duplicate source ID {key[1]!r} for provider {key[0]!r}: "
                    f"{previous} and {record['path']}."
                )
            source_ids[key] = record["path"]
        if "order" in record:
            key = (
                record["niche"],
                record["domain"],
                record["provider"],
                record["order"],
            )
            previous = numbered_labs.get(key)
            if previous is not None:
                raise CatalogError(
                    f"Duplicate order {record['order']} in "
                    f"{record['provider']}/{record['niche']}/{record['domain']}: "
                    f"{previous} and {record['path']}."
                )
            numbered_labs[key] = record["path"]

    records.sort(
        key=lambda record: (
            record["niche"],
            record["domain"] or "",
            record["provider"],
            record.get("order", sys.maxsize),
            record["path"],
        )
    )
    return records, sources


def render_labs(records: list[dict[str, Any]]) -> str:
    """Serialize records in their already-normalized deterministic order."""
    return json.dumps(records, indent=2, ensure_ascii=False) + "\n"


def _markdown_text(value: str) -> str:
    """Escape characters that can break a title or value in a Markdown table."""
    return value.replace("\\", "\\\\").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def render_catalog(records: list[dict[str, Any]], sources: dict[str, Any]) -> str:
    """Render the human-readable catalog from normalized lab records."""
    lines = [
        "# Lab Catalog",
        "",
        f"{len(records)} labs, generated from their neighboring `lab.json` files.",
        "",
        "> Do not edit this file by hand. Run `python3 .meta/scripts/catalog.py`.",
    ]
    groups: dict[tuple[str, str | None, str], list[dict[str, Any]]] = {}
    for record in records:
        key = (record["niche"], record["domain"], record["provider"])
        groups.setdefault(key, []).append(record)

    for (niche, domain, provider), group in groups.items():
        source = sources.get(provider)
        collection_path = niche if domain is None else f"{niche}/{domain}"
        collection = source.get("collections", {}).get(collection_path) if source else None
        if collection is not None:
            heading = collection["name"]
            context = (
                f"{niche} / "
                + (f"{domain} / " if domain is not None else "")
                + f"[{_markdown_text(source['name'])}]({collection['url']})"
            )
        else:
            heading = source["name"] if source else provider.replace("-", " ").title()
            context = " / ".join(
                part
                for part in (niche, domain, source["name"] if source else provider)
                if part is not None
            )
        lines.extend(
            [
                "",
                f"## {heading}",
                "",
                context,
                "",
                "| # | Lab | Kind | Difficulty | Status | Skills | Source |",
                "| ---: | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for record in group:
            number = str(record.get("order", "—"))
            title = _markdown_text(record["title"])
            kind = record["kind"].capitalize()
            difficulty = record.get("difficulty", "—").capitalize()
            status = record["status"].replace("-", " ").capitalize()
            skills = ", ".join(record["skills"]) or "—"
            source_item = record.get("source")
            original = (
                f"[View]({source_item['url']})" if source_item is not None else "—"
            )
            lines.append(
                f"| {number} | [{title}]({record['path']}/) | {kind} | "
                f"{difficulty} | {status} | {_markdown_text(skills)} | {original} |"
            )
    return "\n".join(lines) + "\n"


def write_text_atomic(path: Path, content: str) -> None:
    """Replace one file atomically so readers never see a partially written JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        mode = stat.S_IMODE(path.stat().st_mode)
    except FileNotFoundError:
        mode = 0o644
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary_path = Path(temporary.name)
            os.chmod(temporary_path, mode)
            temporary.write(content)
            temporary.flush()
            os.fsync(temporary.fileno())
        temporary_path.replace(path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def write_catalog(records: list[dict[str, Any]], sources: dict[str, Any]) -> None:
    """Write generated outputs only when their contents have changed."""
    expected = {
        LABS_PATH: render_labs(records),
        CATALOG_PATH: render_catalog(records, sources),
    }
    for path, content in expected.items():
        if not path.exists() or path.read_bytes() != content.encode("utf-8"):
            write_text_atomic(path, content)


def update_catalog(check: bool = False) -> None:
    """Validate the corpus and either write or check its generated catalogs."""
    records, sources = collect_labs()
    expected = {
        LABS_PATH: render_labs(records),
        CATALOG_PATH: render_catalog(records, sources),
    }
    if check:
        stale = [
            display_path(path)
            for path, content in expected.items()
            if not path.exists() or path.read_bytes() != content.encode("utf-8")
        ]
        if stale:
            raise CatalogError(
                "Generated catalog files are stale: "
                + ", ".join(stale)
                + ". Run python3 .meta/scripts/catalog.py."
            )
        print(f"Catalog is valid and current ({len(records)} labs).")
        return

    write_catalog(records, sources)
    print(f"Generated catalogs for {len(records)} labs.")


def main() -> int:
    """Parse catalog options and report expected failures without a traceback."""
    parser = argparse.ArgumentParser(
        description="Validate lab metadata and generate the lab catalogs."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate without writing and fail if generated files are stale",
    )
    args = parser.parse_args()
    try:
        update_catalog(check=args.check)
    except (CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
