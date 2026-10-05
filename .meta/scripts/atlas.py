#!/usr/bin/env python3
"""Validate a finite practice plan and match it to adopted work, offline."""

from __future__ import annotations

import argparse
import html
import sys
from collections import defaultdict
from pathlib import Path

import catalog
import lab_init


def load_atlas(records: list[dict], sources: dict) -> dict:
    path = catalog.ROOT / ".meta/catalog/atlas.json"
    plan = catalog.read_json(path)
    catalog.validate_document(plan, catalog.load_schema(catalog.SCHEMA_DIR / "atlas.schema.json"), "practice atlas")
    collections = {catalog.ROOT / r["collection_path"]: catalog.collection_info(catalog.ROOT / r["collection_path"]) for r in records}
    opportunities = []
    ids = set()
    for opportunity in plan["opportunities"]:
        item = dict(opportunity)
        if item["id"] in ids:
            raise catalog.CatalogError(f"Duplicate opportunity: {item['id']}")
        ids.add(item["id"])
        provider = catalog.source_for(item["provider"], sources)
        catalog.safe_url(item["materials_url"])
        target = item["target"]
        relative = target["collection_path"]
        if Path(relative).is_absolute() or ".." in Path(relative).parts or relative != Path(relative).as_posix():
            raise catalog.CatalogError(f"Invalid proposed collection path: {relative}")
        parent = catalog.ROOT / relative
        descriptor = {key: value for key, value in target.items() if key != "collection_path"}
        catalog.validate_document(descriptor, catalog.load_schema(catalog.COLLECTION_SCHEMA_PATH), relative)
        # Initialization owns the path and filesystem safety rules for plans too.
        parts = catalog.collection_parts(parent, descriptor)
        lab_init._parent(parts)
        current = collections.get(parent, catalog.collection_info(parent))
        if current and current.get("has_subdomain", False) != descriptor.get("has_subdomain", False):
            raise catalog.CatalogError(f"Subject boundary disagrees with existing collection: {relative}")
        collections[parent] = descriptor
        matches = [record for record in records if record["source"]["provider"] == item["provider"]
                   and record["collection_path"] == relative
                   and ("item_ids" not in item or record["source"].get("item_id") in item["item_ids"])]
        item.update(parts)
        item.update({"source_name": provider["name"], "reuse_policy": provider.get("reuse", {}).get("policy", "review"),
                     "subject_title": catalog.subject_title(parts["domain"], parts["subdomain"]),
                     "collection_breadcrumb": [catalog.display_name(parts["niche"]), *(catalog.display_name(group, sources) for group in parts["groups"]), catalog.display_name(parts["collection"], sources)],
                     "adopted_paths": [record["path"] for record in matches],
                     "adopted_count": len(matches), "collection_exists": any(record["collection_path"] == relative for record in records)})
        opportunities.append(item)
    catalog.validate_collection_layout(collections)
    return {**plan, "opportunities": opportunities}


def goal_label(goal: str, plan: dict) -> str:
    return plan["goals"].get(goal, {}).get("title", goal)


def render_atlas(plan: dict, records: list[dict]) -> str:
    escape = catalog._escape
    opportunities = plan["opportunities"]
    adopted = {path for item in opportunities for path in item["adopted_paths"]}
    lines = ["# Practice Atlas", "", "[Lab catalog](CATALOG.md) · [Visual workbench](https://pradeeptathineni.github.io/labs/) · [How I use this repo](README.md)", "",
             f"**{len(opportunities)} reviewed opportunities** · {len(adopted)} matching adopted labs · {len(records)} labs in the whole repository", "",
             "A registered source is something I know about. An opportunity is a reviewed choice; an adopted lab is a concrete plan. Starting and completing it are separate, explicit decisions. Counts here never measure proficiency or a source's completion.", "",
             "Subjects bring related niches together. A path supplies one home: `niches/<niche>/<domain>/[<subdomain>/][<group>/...]<collection>/<lab>/`. Tools name technologies; goals name intentions, including certification preparation.", "",
             "## Next up: Kubernetes", "", "Practical work lives in Code; explanation and objective review live in Study. Both share DevOps / Orchestration. Adopted sets remain planned until I start them.", ""]
    for item in opportunities:
        if item["priority"] == "next":
            lines.append(f"- [{escape(item['title'])}](#{item['id']}) — {item['adopted_count']} matching labs adopted" if item["adopted_count"] else f"- [{escape(item['title'])}](#{item['id']}) — not adopted")
    lines += ["", "## Other forms of practice", ""]
    for entry in plan["niche_guidance"]:
        lines.append(f"- **{catalog.display_name(entry['niche'])}:** {escape(entry['reason'])}")
    lines += ["", "## Browse by subject", ""]
    subjects = defaultdict(list)
    for item in opportunities:
        subjects[item["subject_title"]].append(item)
    for subject, items in sorted(subjects.items()):
        lines += [f"### {escape(subject)}", ""]
        for item in items:
            lines.append(f"- {catalog.display_name(item['niche'])}: [{escape(item['title'])}](#{item['id']}) · {item['priority']}")
        lines.append("")
    lines += ["## Opportunities", ""]
    for item in opportunities:
        target = item["target"]
        path = target["collection_path"]
        destination = f"[`{path}`]({path}/)" if item["collection_exists"] else f"`{path}` (proposed)"
        lines += [f'<a id="{item["id"]}"></a>', f"### {escape(item['title'])}", "",
                  f"**{item['priority'].capitalize()}** · {catalog.display_name(item['niche'])} · {escape(item['subject_title'])} · {item['adoption']} · {item['lab_type']}", "",
                  f"[Source: {escape(item['source_name'])}]({item['materials_url']}) · reuse policy: {item['reuse_policy']}", "",
                  f"**Destination:** {destination}", "", f"**Unit:** {escape(item['unit'])}", "", f"**Intended output:** {escape(item['deliverable'])}", ""]
        if target.get("tools"):
            lines += ["**Tools:** " + ", ".join(target["tools"]), ""]
        if target.get("goals"):
            lines += ["**Preparation goals:** " + "; ".join(escape(goal_label(goal, plan)) for goal in target["goals"]), ""]
        lines += [f"**Evidence ({item['checked_on']}):** {escape(item['evidence_scope'])}", "", f"**Access:** {escape(item.get('access', 'Review before adoption.'))}", ""]
        if item.get("notes"):
            lines += [f"**Adoption limits:** {escape(item['notes'])}", ""]
        if item["adopted_paths"]:
            lines += [f"**{item['adopted_count']} matching labs adopted**; this does not exhaust the source.", ""]
            titles = {record["path"]: record["title"] for record in records}
            lines += [f"- [{escape(titles[path])}]({path}/README.md)" for path in item["adopted_paths"]]
        else:
            lines += ["**Not adopted.** Review the selected material and reuse policy, then initialize one meaningful unit."]
        lines.append("")
    lines += ["## Deferred or unverified leads", ""]
    for lead in plan["unresolved_sources"]:
        lines += [f"- [{escape(lead['provider'])}]({lead['url']}): {escape(lead['reason'])}"]
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="read-only consistency check")
    parser.add_argument("--list", action="store_true", help="preview opportunities and adoption counts")
    parser.add_argument("--priority", choices=["next", "later", "explore"])
    args = parser.parse_args()
    try:
        records, sources = catalog.collect_labs()
        plan = load_atlas(records, sources)
        if args.list:
            for item in plan["opportunities"]:
                if not args.priority or item["priority"] == args.priority:
                    print(f"{item['id']} | {item['priority']} | {item['adopted_count']} adopted | {item['target']['collection_path']}")
            return 0
        path = catalog.ROOT / "PRACTICE-ATLAS.md"
        expected = render_atlas(plan, records)
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                raise catalog.CatalogError("Stale atlas: run python3 .meta/scripts/atlas.py")
        else:
            catalog.write_text_atomic(path, expected)
        print(f"Atlas {'is valid and current' if args.check else 'generated'} ({len(plan['opportunities'])} opportunities; {len(records)} actual labs).")
    except (catalog.CatalogError, OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
