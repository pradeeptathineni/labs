#!/usr/bin/env python3
"""Import selected static DevRoadmaps project ideas without executing JavaScript."""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import catalog
import lab_init
import workflow

PROVIDER = "devroadmaps"
REPO = "rudra496/devroadmaps"
PROJECT_FILE = "js/project-ideas.js"


def _literal(node: Any) -> Any:
    """Decode only inert AST literals, rejecting expressions and duplicate keys."""
    if node.type == "Literal" and (node.value is None or isinstance(node.value, (str, int, float, bool))):
        if getattr(node, "regex", None):
            raise catalog.CatalogError("Regular expressions are not project data")
        return node.value
    if node.type == "ArrayExpression":
        if any(value is None for value in node.elements):
            raise catalog.CatalogError("Sparse project arrays are unsupported")
        return [_literal(value) for value in node.elements]
    if node.type == "ObjectExpression":
        result = {}
        for field in node.properties:
            if field.type != "Property" or field.computed or field.method or field.shorthand or field.kind != "init":
                raise catalog.CatalogError("Executable or computed project property is unsupported")
            key_node = field.key
            if key_node.type == "Identifier":
                key = key_node.name
            elif key_node.type == "Literal" and isinstance(key_node.value, str):
                key = key_node.value
            else:
                raise catalog.CatalogError("Project object keys must be static strings")
            if key in result:
                raise catalog.CatalogError(f"Duplicate project key {key!r}")
            result[key] = _literal(field.value)
        return result
    raise catalog.CatalogError(f"Executable JavaScript expression {node.type} is not project data")


def parse_projects(text: str) -> dict[str, list[dict[str, Any]]]:
    try:
        import esprima
        tree = esprima.parseScript(text, loc=True)
    except ImportError as error:
        raise catalog.CatalogError("Install .meta/importers/requirements.txt for DevRoadmaps parsing") from error
    except Exception as error:
        raise catalog.CatalogError(f"Cannot parse upstream project JavaScript: {error}") from error
    declarations = []
    for statement in tree.body:
        if statement.type == "VariableDeclaration":
            declarations += [item for item in statement.declarations if item.id.type == "Identifier" and item.id.name == "PROJECT_IDEAS"]
    if len(declarations) != 1:
        raise catalog.CatalogError("Expected exactly one top-level PROJECT_IDEAS declaration")
    root = declarations[0].init
    if root is None:
        raise catalog.CatalogError("PROJECT_IDEAS has no static value")
    projects = _literal(root)
    if not isinstance(projects, dict):
        raise catalog.CatalogError("PROJECT_IDEAS must be an object")
    # Keep source line numbers from the parser; formatting and quotes may change.
    for field in root.properties:
        track = field.key.name if field.key.type == "Identifier" else field.key.value
        if isinstance(projects[track], list) and field.value.type == "ArrayExpression":
            for item, node in zip(projects[track], field.value.elements):
                if isinstance(item, dict):
                    item["_line"] = node.loc.start.line
    for track, items in projects.items():
        if not isinstance(track, str) or not isinstance(items, list):
            raise catalog.CatalogError("Each project track must be an array")
        titles = set()
        for item in items:
            if not isinstance(item, dict) or not all(isinstance(item.get(key), str) and item[key].strip() for key in ("title", "desc", "difficulty")):
                raise catalog.CatalogError(f"Malformed project in track {track}")
            if not isinstance(item.get("tech"), list) or not all(isinstance(value, str) for value in item["tech"]):
                raise catalog.CatalogError(f"Malformed project skills in track {track}")
            slug = catalog.slugify(item["title"])
            if not slug or slug in titles:
                raise catalog.CatalogError(f"Duplicate or invalid project title in track {track}: {item['title']}")
            titles.add(slug)
    return projects


def _project_key(track: str, title: str) -> str:
    return f"project-ideas/{track}/{catalog.slugify(title)}"


def _snapshot(item: dict[str, Any], track: str, key: str) -> str:
    return catalog.json_text({"key": key, "track": track, "title": item["title"], "desc": item["desc"], "difficulty": item["difficulty"], "tech": item["tech"]})


def _manifest(snapshot: str, license_text: str) -> str:
    return catalog.json_text({"project_sha256": hashlib.sha256(snapshot.encode()).hexdigest(), "license_sha256": hashlib.sha256(license_text.encode()).hexdigest()})


def _readme(item: dict[str, Any], url: str) -> str:
    return "\n".join([
        f"# {item['title']}", "", f"Source: [DevRoadmaps project idea]({url})", "",
        "> [!IMPORTANT]", "> The exercise definition is copied from DevRoadmaps under its MIT License; my solution starts below.", "",
        "## Exercise Definition", "", item["desc"], "", "## Solution", "",
    ])


def _owned_files(path: Path) -> tuple[str, str, dict[str, str]]:
    source = path / "source"
    manifest_path = source / "manifest.json"
    if not manifest_path.is_file():
        raise catalog.CatalogError(f"Missing importer manifest in {catalog.display_path(path)}")
    manifest = catalog.read_json(manifest_path)
    project_path = source / "project.json"
    license_path = source / "LICENSE.txt"
    snapshot = project_path.read_text(encoding="utf-8")
    license_text = license_path.read_text(encoding="utf-8")
    if hashlib.sha256(snapshot.encode()).hexdigest() != manifest.get("project_sha256") or hashlib.sha256(license_text.encode()).hexdigest() != manifest.get("license_sha256"):
        raise catalog.CatalogError(f"Importer-owned source files were modified: {catalog.display_path(path)}")
    return snapshot, license_text, manifest


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Import selected DevRoadmaps project ideas from committed Git data.")
    parser.add_argument("--checkout", required=True, type=Path)
    parser.add_argument("--list", action="store_true", help="list tracks and item keys without writing")
    parser.add_argument("--track")
    parser.add_argument("--item", action="append", help="select title slug or full project key; repeat")
    parser.add_argument("--all-track", action="store_true", help="select every item in the given track")
    parser.add_argument("--destination", help="niches/<niche>/<domain>/[subdomain/][groups/...]<collection>")
    parser.add_argument("--subdomain", help="declare the subject subdomain for a new collection; must match the path")
    parser.add_argument("--refresh", action="store_true", help="review a changed upstream revision of selected items")
    parser.add_argument("--interactive", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--yes", action="store_true")
    return parser


def main() -> int:
    parser = _parser()
    args = parser.parse_args()
    if args.interactive and (args.yes or args.dry_run):
        parser.error("--interactive cannot be combined with --yes or --dry-run")
    try:
        sources = catalog.load_sources()
        catalog.require_copy_permission(PROVIDER, sources)
        revision, committed = workflow.git_checkout(args.checkout, REPO, [PROJECT_FILE, "LICENSE"])
        license_text = committed["LICENSE"].decode("utf-8")
        if "MIT License" not in license_text or "Permission is hereby granted" not in license_text:
            raise catalog.CatalogError("Expected the reviewed MIT license at this revision")
        projects = parse_projects(committed[PROJECT_FILE].decode("utf-8"))
        if args.list:
            for track, items in projects.items():
                print(f"{track}: " + ", ".join(_project_key(track, item["title"]) for item in items))
            return 0
        if args.interactive:
            args.track = workflow.prompt("Track", args.track, choices=sorted(projects))
            choices = [_project_key(args.track, item["title"]) for item in projects[args.track]]
            choice = workflow.prompt("Item key or all", "all" if args.all_track else None, choices=choices + ["all"])
            args.all_track = choice == "all"
            args.item = None if args.all_track else [choice]
            args.destination = workflow.prompt("Destination collection", args.destination)
            current_subdomain = lab_init.destination(args.destination)["subdomain"]
            args.subdomain = workflow.prompt("Subject subdomain", args.subdomain or current_subdomain, optional=True)
        if not args.track or args.track not in projects:
            raise catalog.CatalogError("Choose an existing --track; use --list")
        if bool(args.item) == args.all_track:
            raise catalog.CatalogError("Choose --item or --all-track")
        if not args.destination:
            raise catalog.CatalogError("Choose --destination")
        destination = lab_init.destination(args.destination, args.subdomain)
        by_key = {_project_key(args.track, item["title"]): item for item in projects[args.track]}
        requested = list(by_key) if args.all_track else [key if key.startswith("project-ideas/") else f"project-ideas/{args.track}/{key}" for key in args.item]
        missing = sorted(set(requested) - set(by_key))
        if missing:
            raise catalog.CatalogError("Unknown project key(s): " + ", ".join(missing))
        records, _ = catalog.collect_labs()
        existing = {(record["source"]["provider"], record["source"].get("item_id")): record for record in records}
        plans = []
        updates = []
        for key in requested:
            item = by_key[key]
            line = item["_line"]
            url = f"https://github.com/{REPO}/blob/{revision}/{PROJECT_FILE}" + (f"#L{line}" if line else "")
            snapshot = _snapshot(item, args.track, key)
            files = {"README.md": _readme(item, url), "source/project.json": snapshot, "source/LICENSE.txt": license_text, "source/manifest.json": _manifest(snapshot, license_text)}
            prior = existing.get((PROVIDER, key))
            if prior:
                path = catalog.ROOT / prior["path"]
                if path.parent != (catalog.ROOT / args.destination).absolute():
                    raise catalog.CatalogError(f"Existing project is in another collection: {prior['path']}")
                old_snapshot, old_license, _ = _owned_files(path)
                if prior["source"].get("revision") == revision and old_snapshot == snapshot and old_license == license_text:
                    print(f"No change: {prior['path']}")
                    continue
                if not args.refresh:
                    raise catalog.CatalogError(f"Changed upstream project {key}; rerun with --refresh to review it")
                candidate = catalog.ordered_lab(catalog.read_json(path / "lab.json"))
                candidate["source"]["revision"] = revision
                candidate["source"]["url"] = url
                changes = {name: content for name, content in files.items() if name != "README.md" and (path / name).read_text(encoding="utf-8") != content}
                updates.append((path, candidate, changes, old_snapshot != snapshot, item["desc"]))
            else:
                # Upstream calls this field tech; capabilities are curated separately.
                data = dict(destination, title=item["title"], slug=catalog.slugify(item["title"]), summary=item["desc"], type="project", difficulty=item["difficulty"], skills=[], tools=[catalog.slugify(value) for value in item["tech"]], provider=PROVIDER, item_id=key, source_url=url, revision=revision)
                plans.append(lab_init.plan_lab(data, sources, files=files, existing_plans=plans))
        overrides = {plan["path"] / "lab.json": plan["metadata"] for plan in plans}
        overrides.update({path / "lab.json": metadata for path, metadata, _, _, _ in updates})
        catalog.collect_labs(overrides=overrides, collection_overrides=lab_init.collection_updates(plans))
        for plan in plans:
            lab_init.preview_plan(plan)
        for path, metadata, changes, definition_changed, desc in updates:
            workflow.preview(catalog.display_path(path), metadata, sorted(changes) + ["lab.json"])
            if definition_changed:
                print(f"Definition changed; manually review README Exercise Definition against: {desc}")
        if args.dry_run:
            return 0
        if not args.interactive and not args.yes:
            parser.error("writing requires --yes")
        if args.interactive and not workflow.confirm():
            print("No changes made.")
            return 0
        if plans:
            lab_init.write_plans(plans, sources)
        for path, metadata, changes, definition_changed, _ in updates:
            for relative, content in changes.items():
                catalog.write_text_atomic(path / relative, content)
            catalog.write_text_atomic(path / "lab.json", catalog.json_text(metadata))
            if definition_changed:
                print(f"Review README Exercise Definition in {catalog.display_path(path)}")
        if updates:
            catalog.update_catalog()
        print(f"Imported {len(plans)} new project(s); refreshed {len(updates)} project(s).")
    except (catalog.CatalogError, OSError, UnicodeDecodeError, EOFError, KeyboardInterrupt) as error:
        if isinstance(error, (EOFError, KeyboardInterrupt)):
            print("\nNo changes made.")
            return 0
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
