#!/usr/bin/env python3
"""Validate the practice corpus and generate deterministic browsing views."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import stat
import sys
import tempfile
from urllib.parse import unquote
from collections import Counter, defaultdict
from collections.abc import Mapping
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[2]
NICHES = ROOT / "niches"
SCHEMA_DIR = ROOT / ".meta/catalog/schema"
LAB_SCHEMA_PATH = SCHEMA_DIR / "lab.schema.json"
SOURCE_SCHEMA_PATH = SCHEMA_DIR / "source.schema.json"
COLLECTION_SCHEMA_PATH = SCHEMA_DIR / "collection.schema.json"
SOURCES_PATH = ROOT / ".meta/catalog/sources.json"
LABS_PATH = ROOT / ".meta/catalog/labs.json"
CATALOG_PATH = ROOT / "CATALOG.md"
SLUG_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
ORDER_PATTERN = re.compile(r"([0-9]+)-([a-z0-9]+(?:-[a-z0-9]+)*)")
LAB_DIR_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
DISPLAY_NAMES = {"aws": "AWS", "devops": "DevOps", "mit": "MIT"}
SUBJECT_TITLES = {
    ("cloud", "aws"): "AWS Cloud",
    ("systems", "distributed"): "Distributed Systems",
}


class CatalogError(Exception):
    """A repository validation error suitable for the command line."""


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise CatalogError(f"Missing required file: {display_path(path)}") from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CatalogError(f"Invalid JSON in {display_path(path)}: {error}") from error


def load_schema(path: Path) -> dict[str, Any]:
    schema = read_json(path)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as error:
        raise CatalogError(f"Invalid schema in {display_path(path)}: {error.message}") from error
    return schema


def validate_document(document: Any, schema: dict[str, Any], label: str) -> None:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(document), key=lambda error: (str(list(error.path)), error.message))
    if errors:
        details = "; ".join(f"{'.'.join(map(str, error.path)) or '$'}: {error.message}" for error in errors)
        raise CatalogError(f"Invalid {label}: {details}")


def load_sources() -> dict[str, Any]:
    sources = read_json(SOURCES_PATH)
    validate_document(sources, load_schema(SOURCE_SCHEMA_PATH), display_path(SOURCES_PATH))
    return sources


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def lab_paths() -> list[Path]:
    """Stop at a lab root, skipping hidden trees and symlinks but reporting bad depth."""
    if not NICHES.is_dir():
        raise CatalogError(f"Missing lab hierarchy directory: {display_path(NICHES)}")
    found: list[Path] = []
    for parent, dirs, files in os.walk(NICHES, topdown=True, followlinks=False):
        dirs[:] = sorted(child for child in dirs if not child.startswith(".") and child != ".shared" and not (Path(parent) / child).is_symlink())
        if "lab.json" in files:
            path = Path(parent) / "lab.json"
            if path.is_symlink():
                continue
            _lab_path_parts(path)
            found.append(path)
            dirs.clear()
    return sorted(found)


def collection_info(parent: Path, overrides: Mapping[Path, Any] | None = None) -> dict[str, Any]:
    descriptor = parent / "collection.json"
    if descriptor.is_symlink():
        raise CatalogError(f"Collection descriptor cannot be a symlink: {display_path(descriptor)}")
    if overrides and parent in overrides:
        value = overrides[parent]
    elif descriptor.is_file():
        value = read_json(descriptor)
    else:
        return {}
    validate_document(value, load_schema(COLLECTION_SCHEMA_PATH), display_path(descriptor))
    return value


def collection_parts(parent: Path, descriptor: dict[str, Any] | None = None) -> dict[str, Any]:
    """Separate the declared subject prefix from the remaining collection hierarchy."""
    try:
        parts = parent.absolute().relative_to(NICHES.absolute()).parts
    except ValueError as error:
        raise CatalogError(f"Collection must be under niches/: {display_path(parent)}") from error
    if len(parts) < 3:
        raise CatalogError(f"Bad collection depth at {display_path(parent)}; use niche/domain/[subdomain/][groups/...]collection")
    for part in parts:
        if not SLUG_PATTERN.fullmatch(part):
            raise CatalogError(f"Invalid hierarchy name {part!r} in {display_path(parent)}")
    niche, domain, *ancestors, collection = parts
    info = collection_info(parent) if descriptor is None else descriptor
    subdomain = None
    if info.get("has_subdomain"):
        if not ancestors:
            raise CatalogError(f"Collection declares a subdomain but has no subdomain directory: {display_path(parent)}")
        subdomain, *ancestors = ancestors
    return {"niche": niche, "domain": domain, "subdomain": subdomain, "groups": ancestors, "collection": collection}


def _lab_path_parts(path: Path, collection_overrides: Mapping[Path, Any] | None = None) -> tuple[dict[str, Any], str, int | None]:
    try:
        parts = path.resolve().relative_to(NICHES.resolve()).parts
    except ValueError as error:
        raise CatalogError(f"Lab must be under niches/: {display_path(path)}") from error
    if path.name != "lab.json" or len(parts) < 5:
        raise CatalogError(f"Bad lab depth at {display_path(path)}; use niche/domain/[subdomain/][groups/...]collection/lab/lab.json")
    folder = parts[-2]
    if not LAB_DIR_PATTERN.fullmatch(folder):
        raise CatalogError(f"Invalid lab folder {folder!r} in {display_path(path)}")
    info = collection_info(path.parent.parent, collection_overrides)
    hierarchy = collection_parts(path.parent.parent, info)
    order = None
    slug = folder
    if info.get("ordered") is True:
        match = ORDER_PATTERN.fullmatch(folder)
        if match is None or int(match.group(1)) < 1:
            raise CatalogError(f"Ordered collection requires a positive number prefix: {display_path(path)}")
        order = int(match.group(1))
        slug = match.group(2)
    return hierarchy, slug, order


def source_for(provider: str, sources: dict[str, Any]) -> dict[str, Any]:
    if provider not in sources:
        raise CatalogError(f"Unregistered source provider {provider!r}")
    return sources[provider]


def require_copy_permission(provider: str, sources: dict[str, Any]) -> dict[str, Any]:
    source = source_for(provider, sources)
    if source.get("reuse", {}).get("policy") != "copy":
        raise CatalogError(f"Source {provider!r} does not have a copy policy")
    return source


def normalize_difficulty(value: str, provider: str, sources: dict[str, Any], schema: dict[str, Any] | None = None) -> str:
    choices = (schema or load_schema(LAB_SCHEMA_PATH))["properties"]["difficulty"]["enum"]
    mapped = source_for(provider, sources).get("difficulty_map", {}).get(value, value)
    if mapped not in choices:
        raise CatalogError(f"Unknown difficulty {value!r}; choose {', '.join(choices)} or a mapped source label")
    return mapped


def ordered_lab(metadata: dict[str, Any]) -> dict[str, Any]:
    """One serialization order for migration, commands, and importers."""
    result: dict[str, Any] = {"title": metadata["title"]}
    for key in ("summary", "type", "difficulty", "skills", "goals"):
        if key in metadata:
            result[key] = metadata[key]
    result["source"] = {key: metadata["source"][key] for key in ("provider", "item_id", "url", "revision") if key in metadata["source"]}
    if "links" in metadata and metadata["links"]:
        result["links"] = {key: metadata["links"][key] for key in ("solution", "demo") if key in metadata["links"]}
    tracking = metadata["tracking"]
    result["tracking"] = {"status": tracking["status"], "dates": {key: tracking["dates"][key] for key in ("created", "started", "updated", "completed")}}
    if "content_sha256" in tracking:
        result["tracking"]["content_sha256"] = tracking["content_sha256"]
    return result


def ordered_source(record: dict[str, Any]) -> dict[str, Any]:
    result = {key: record[key] for key in ("type", "name", "url") if key in record}
    if "reuse" in record:
        result["reuse"] = {key: record["reuse"][key] for key in ("policy_url", "license", "license_url", "notes", "policy", "verified") if key in record["reuse"]}
    if "difficulty_map" in record:
        result["difficulty_map"] = record["difficulty_map"]
    return result


def json_text(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def lab_record(path: Path, metadata: Any, sources: dict[str, Any], schema: dict[str, Any] | None = None, *, collection_overrides: Mapping[Path, Any] | None = None) -> dict[str, Any]:
    validate_document(metadata, schema or load_schema(LAB_SCHEMA_PATH), display_path(path))
    hierarchy, slug, order = _lab_path_parts(path, collection_overrides)
    source = metadata["source"]
    source_record = source_for(source["provider"], sources)
    if source_record["type"] == "local" and any(key in source for key in ("item_id", "url", "revision")):
        raise CatalogError(f"Local source cannot have external item fields: {display_path(path)}")
    if source_record["type"] == "external" and not source.get("url"):
        raise CatalogError(f"External lab needs a source URL: {display_path(path)}")
    dates = metadata["tracking"]["dates"]
    if dates["started"] and dates["completed"] and dates["started"] > dates["completed"]:
        raise CatalogError(f"Started date follows completed date: {display_path(path)}")
    for target in metadata.get("links", {}).values():
        if not target.startswith(("http://", "https://")) and not (ROOT / target).is_file():
            raise CatalogError(f"Local link does not exist: {target} in {display_path(path)}")
    record = ordered_lab(metadata)
    record.update({
        **hierarchy,
        "path": path.parent.relative_to(ROOT).as_posix(), "slug": slug, "order": order,
        "source_display": {"name": source_record["name"], "type": source_record["type"], "url": source_record.get("url")},
    })
    descriptor = collection_info(path.parent.parent, collection_overrides)
    record["collection_title"] = descriptor.get("title") or _readme_title(path.parent.parent) or display_name(hierarchy["collection"], sources)
    if "source_url" in descriptor:
        record["collection_source_url"] = descriptor["source_url"]
    record["goals_effective"] = sorted(set(metadata.get("goals", [])) | set(descriptor.get("goals", [])))
    question_file = path.parent / "questions.json"
    if metadata["type"] == "question-bank" and question_file.is_file():
        data = read_json(question_file)
        if not isinstance(data, dict) or not isinstance(data.get("questions"), list):
            raise CatalogError(f"Question bank needs a questions array: {display_path(question_file)}")
        record["question_count"] = len(data["questions"])
    return record


def _readme_title(parent: Path) -> str | None:
    readme = parent / "README.md"
    if readme.is_file():
        first = readme.read_text(encoding="utf-8").splitlines()[0:1]
        if first and first[0].startswith("# "):
            return first[0][2:].strip()
    return None


def collect_labs(overrides: Mapping[Path, Any] | None = None, sources_override: dict[str, Any] | None = None, *, collection_overrides: Mapping[Path, Any] | None = None) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    sources = sources_override if sources_override is not None else load_sources()
    validate_document(sources, load_schema(SOURCE_SCHEMA_PATH), display_path(SOURCES_PATH))
    schema = load_schema(LAB_SCHEMA_PATH)
    by_path = {path.absolute(): read_json(path) for path in lab_paths()}
    for path, value in (overrides or {}).items():
        by_path[path.absolute()] = value
    records = [lab_record(path, value, sources, schema, collection_overrides=collection_overrides) for path, value in sorted(by_path.items())]
    source_ids: dict[tuple[str, str], str] = {}
    collection_paths: set[Path] = set()
    container_paths: set[Path] = set()
    subdomains = {(item["domain"], item["subdomain"]) for item in records if item["subdomain"]}
    orders: dict[tuple[Path, int], str] = {}
    slugs: dict[tuple[Path, str], str] = {}
    for record in records:
        path = ROOT / record["path"]
        parent = path.parent
        collection_paths.add(parent)
        container_paths.update(ancestor for ancestor in parent.parents if ancestor.is_relative_to(NICHES))
        if record["subdomain"] is None:
            first_container = record["groups"][0] if record["groups"] else record["collection"]
            if (record["domain"], first_container) in subdomains:
                raise CatalogError(f"Subject boundary conflicts for {record['domain']}/{first_container}: {record['path']}. Declare has_subdomain consistently across niches.")
        source = record["source"]
        if source.get("item_id"):
            key = (source["provider"], source["item_id"])
            if key in source_ids:
                raise CatalogError(f"Duplicate source item {key}: {source_ids[key]} and {record['path']}")
            source_ids[key] = record["path"]
        slug_key = (parent, record["slug"])
        if slug_key in slugs:
            raise CatalogError(f"Duplicate lab slug in {display_path(parent)}: {record['slug']}")
        slugs[slug_key] = record["path"]
        if record["order"] is not None:
            order_key = (parent, record["order"])
            if order_key in orders:
                raise CatalogError(f"Duplicate order in {display_path(parent)}: {record['order']}")
            orders[order_key] = record["path"]
    conflict = collection_paths & container_paths
    if conflict:
        raise CatalogError(f"Directory is both collection and container: {display_path(sorted(conflict)[0])}")
    records.sort(key=lambda item: (item["niche"], item["domain"], item["subdomain"] or "", item["groups"], item["collection"], item["order"] or 0, item["slug"]))
    return records, sources


def render_labs(records: list[dict[str, Any]]) -> str:
    return json_text(records)


def _escape(value: str) -> str:
    return value.replace("[", "\\[").replace("]", "\\]").replace("|", "\\|")


def _label(value: str) -> str:
    return value.replace("-", " ").capitalize()


def display_name(value: str, sources: dict[str, Any] | None = None) -> str:
    """Use known spelling for labels, without assigning subject or source identity."""
    if sources and value in sources:
        return sources[value]["name"]
    return DISPLAY_NAMES.get(value, value.replace("-", " ").title())


def subject_title(domain: str, subdomain: str | None) -> str:
    if (domain, subdomain) in SUBJECT_TITLES:
        return SUBJECT_TITLES[domain, subdomain]
    return " / ".join(display_name(part) for part in (domain, subdomain) if part)


def render_catalog(records: list[dict[str, Any]], sources: dict[str, Any]) -> str:
    statuses = Counter(item["tracking"]["status"] for item in records)
    types = Counter(item["type"] for item in records)
    lines = [
        "<style>",
        "small {",
        "  display: inline-block;",
        "}",
        "summary, small {",
        "    margin: 0 0 15px 0;",
        "}",
        "summary small {",
        "    margin: 0 0 0 15px;",
        "}",
        ".catalog-section-title {",
        "    font-size: 1.25em;",
        "    font-weight: 600;",
        "}",
        ".catalog-all > h3, .catalog-all > details, .catalog-all > hr {",
        "    margin-left: 2.5rem;",
        "}",
        "</style>",
        "",
        "# Lab Catalog",
        "",
        f"**{len(records)} labs** · {statuses['complete']} complete · {statuses['in-progress']} in progress · {statuses['not-started']} planned · {statuses['paused']} paused · {statuses['abandoned']} abandoned",
        "",
        "**Types:** " + " · ".join(f"{_label(key)} {value}" for key, value in sorted(types.items(), key=lambda pair: (-pair[1], _label(pair[0])))),
        "",
    ]
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in records:
        groups[str(Path(item["path"]).parent)].append(item)
    ranked = sorted(groups.values(), key=lambda items: (
        not any(item["tracking"]["status"] != "not-started" for item in items),
        items[0]["domain"], items[0]["subdomain"] or "", items[0]["path"],
    ))
    for status, title, empty_message in (
        ("complete", "✅ Completed", "No completed labs yet."),
        ("in-progress", "🛠️ In progress", "No labs in progress yet."),
    ):
        lines += ["---", "", "<details open>", f'<summary class="catalog-section-title">{title}</summary>', ""]
        found = False
        for items in ranked:
            matches = [item for item in items if item["tracking"]["status"] == status]
            if not matches:
                continue
            found = True
            heading, path_line = _collection_display(matches, sources)
            lines += [f"**{heading}**<br/>{path_line}", ""]
            for item in matches:
                lines += _catalog_entry(item, show_order=False, anchor=False)
            lines.append("")
        if not found:
            lines.append(empty_message)
        lines += ["", "</details>", ""]
    skills = Counter(skill for item in records for skill in item["skills"])
    lines += ["---", "", "<details>", '<summary class="catalog-section-title">🔎 Browse by skill</summary>', ""]
    if skills:
        for skill, count in skills.most_common():
            matches = [item for item in records if skill in item["skills"]]
            links = ", ".join(f"[{_escape(item['title'])}](#{_anchor(item)})" for item in matches)
            lines.append(f"- **{skill}** ({count}): {links}")
    else:
        lines.append("No skills indexed yet.")
    goals = Counter(goal for item in records for goal in item["goals_effective"])
    if goals:
        lines += ["", "**Goals**", ""]
        for goal, count in goals.most_common():
            matches = [item for item in records if goal in item["goals_effective"]]
            links = ", ".join(f"[{_escape(item['title'])}](#{_anchor(item)})" for item in matches)
            lines.append(f"- **{goal}** ({count}): {links}")
    lines += ["", "</details>", ""]
    lines += ["---", "", '<details class="catalog-all">', '<summary class="catalog-section-title">📚 Browse all labs</summary>', ""]
    subjects: dict[tuple[str, str | None], list[list[dict[str, Any]]]] = defaultdict(list)
    for items in ranked:
        subjects[items[0]["domain"], items[0]["subdomain"]].append(items)
    # Ranking collections first also puts subjects with recorded work first.
    for subject, collections in subjects.items():
        lines += ["---", "", f"### {_escape(subject_title(*subject))}", ""]
        for items in collections:
            heading, path_line = _collection_display(items, sources)
            lines += ["<details>", f"<summary>{heading}<br/>{path_line}</summary>", ""]
            for item in items:
                lines += _catalog_entry(item)
            lines += ["", "</details>", ""]
    lines += ["</details>", ""]
    return "\n".join(lines).rstrip() + "\n"


def _collection_display(items: list[dict[str, Any]], sources: dict[str, Any]) -> tuple[str, str]:
    first = items[0]
    title = " / ".join([*(display_name(group, sources) for group in first["groups"]), first["collection_title"]])
    relative_path = Path(first["path"]).parent
    breadcrumb = " / ".join(relative_path.parts[1:])
    collection_path = ROOT / relative_path
    readme = collection_path / "README.md"
    source_url = first.get("collection_source_url")
    # Markdown links and backticks stay literal inside summary; use their HTML forms.
    heading = f"{html.escape(title)} · {html.escape(display_name(first['niche']))}"
    count = f"{len(items)} lab{'s' if len(items) != 1 else ''}"
    path_line = f"<small><code>{html.escape(breadcrumb)}</code> · {count}"
    if readme.is_file():
        path_line += f' · <a href="{html.escape(display_path(readme))}">notes</a>'
    if source_url:
        path_line += f' · <a href="{html.escape(source_url)}">ref</a>'
    return heading, path_line + "</small>"


def _catalog_entry(item: dict[str, Any], *, show_order: bool = True, anchor: bool = True) -> list[str]:
    base = item["path"]
    source = item["source"]
    marker = f"{item['order']}." if show_order and item["order"] is not None else "-"
    summary = item.get("summary", "Open the source brief and work through the exercise.")
    readme = ROOT / base / "README.md"
    exercise = f"[{_escape(item['title'])}]({base}/README.md#exercise-definition)" if readme.is_file() else _escape(item["title"])
    links = item.get("links", {})
    solution = links.get("solution")
    if solution:
        solution_link = f" · [Solution]({solution})"
    elif item["tracking"]["status"] != "not-started" and readme.is_file() and _readme_has_solution(readme):
        solution_link = f" · [Solution]({base}/README.md#solution)"
    else:
        solution_link = ""
    details = [_label(item["type"]), _label(item["tracking"]["status"])]
    details.append(f"Updated {item['tracking']['dates']['updated']}")
    if item["skills"]:
        details.append(" ".join(f"`{skill}`" for skill in item["skills"]))
    if item["goals_effective"]:
        details.append("Goals: " + ", ".join(item["goals_effective"]))
    if source.get("url"):
        details.append(f"[ref]({source['url']})")
    indent = " " * (len(marker) + 1)
    anchor_tag = f'<a id="{_anchor(item)}"></a>' if anchor else ""
    return [
        f"{marker} {anchor_tag}{exercise}{solution_link} — {_escape(summary)}",
        f"{indent}<br/><small>{' · '.join(details)}</small>",
    ]


def _readme_has_solution(readme: Path) -> bool:
    content = readme.read_text(encoding="utf-8")
    heading = re.search(r"(?m)^## Solution[ \t]*$", content)
    if heading is None:
        return False
    section = re.split(r"(?m)^## ", content[heading.end():], maxsplit=1)[0]
    return bool(section.strip())


def _anchor(item: dict[str, Any]) -> str:
    return "lab-" + slugify(item["path"].replace("/", "-"))


class _HTMLLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            self.targets.extend(value for key, value in attrs if key == "href" and value)


def validate_local_links(include_catalog: bool = True) -> None:
    """Check Markdown and HTML link targets without visiting external sites."""
    documents = [ROOT / "README.md"]
    if include_catalog:
        documents.append(CATALOG_PATH)
    documents += list((ROOT / ".meta").rglob("README.md"))
    documents += list(NICHES.rglob("README.md"))
    for document in documents:
        if not document.is_file():
            continue
        content = document.read_text(encoding="utf-8")
        links = _HTMLLinks()
        links.feed(content)
        targets = [match.group(1) for match in re.finditer(r"\]\(([^)]+)\)", content)] + links.targets
        for value in targets:
            target = unquote(html.unescape(value).split("#", 1)[0])
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (document.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError as error:
                raise CatalogError(f"Local link escapes repository: {display_path(document)} -> {target}") from error
            if not resolved.exists():
                raise CatalogError(f"Broken local link: {display_path(document)} -> {target}")


def write_text_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="", dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, mode)
        temporary.replace(path)
    finally:
        if temporary:
            temporary.unlink(missing_ok=True)


def expected_catalogs(records: list[dict[str, Any]], sources: dict[str, Any]) -> dict[Path, str]:
    return {LABS_PATH: render_labs(records), CATALOG_PATH: render_catalog(records, sources)}


def write_catalog(records: list[dict[str, Any]], sources: dict[str, Any]) -> None:
    for path, content in expected_catalogs(records, sources).items():
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            write_text_atomic(path, content)


def update_catalog(check: bool = False) -> None:
    records, sources = collect_labs()
    if check:
        validate_local_links()
    if check:
        stale = [display_path(path) for path, content in expected_catalogs(records, sources).items() if not path.exists() or path.read_text(encoding="utf-8") != content]
        if stale:
            raise CatalogError("Stale catalog: " + ", ".join(stale))
        print(f"Catalog is valid and current ({len(records)} labs).")
    else:
        validate_local_links(include_catalog=False)
        write_catalog(records, sources)
        validate_local_links()
        print(f"Generated catalogs for {len(records)} labs.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate labs and generate their browsing catalog.")
    parser.add_argument("--check", action="store_true", help="read-only stale check")
    args = parser.parse_args()
    try:
        update_catalog(check=args.check)
    except (CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
