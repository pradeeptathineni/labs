#!/usr/bin/env python3
"""Build a deterministic, allowlisted Pages artifact from the shared catalog."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote, urlsplit

import atlas
import catalog
import lab_sync

REPOSITORY = "https://github.com/pradeeptathineni/labs"
SITE = catalog.ROOT / ".meta/site"
BUILD = catalog.ROOT / ".meta/build"
STATUS_LABELS = {"not-started": "Planned", "in-progress": "In progress", "complete": "Complete", "paused": "Paused", "abandoned": "Abandoned"}
FACETS = {"domain": "Subject", "niche": "Niche", "status": "Status", "subdomain": "Specialization", "tool": "Tool", "goal": "Goal / certification", "collection": "Collection", "provider": "Source", "skill": "Skill", "type": "Lab type", "difficulty": "Difficulty", "priority": "Atlas priority"}


def git_text(*args: str) -> str:
    return lab_sync._git(*args).decode().strip()


def github_link(target: str | None, revision: str, kind: str = "blob") -> str | None:
    if not target:
        return None
    if urlsplit(target).scheme:
        return catalog.safe_url(target)
    path, _, fragment = target.partition("#")
    if Path(path).is_absolute() or ".." in Path(path).parts:
        raise catalog.CatalogError(f"Unsafe repository link: {target}")
    url = f"{REPOSITORY}/{kind}/{revision}/" + quote(path, safe="/")
    return url + ("#" + quote(fragment, safe="-._~") if fragment else "")


def projection(records: list[dict], plan: dict, revision: str) -> dict:
    """Public fields are selected explicitly; no exercise bodies or private notes."""
    work = []
    for record in records:
        item = {key: record[key] for key in ("title", "type", "skills", "niche", "domain", "subdomain", "groups", "collection_path", "collection_title", "collection_breadcrumb", "subject_title", "path", "order")}
        item.update(id=record["path"], summary=record.get("summary", ""), difficulty=record.get("difficulty"),
                    tools=record["tools_effective"], goals=record["goals_effective"],
                    provider=record["source"]["provider"], source_name=record["source_display"]["name"],
                    source_url=catalog.safe_url(record["source"]["url"]) if record["source"].get("url") else None,
                    status=record["tracking"]["status"], dates=record["tracking"]["dates"],
                    exercise_url=github_link(record["exercise_link"], revision), solution_url=github_link(record["solution_link"], revision),
                    demo_url=github_link(record.get("links", {}).get("demo"), revision),
                    collection_url=github_link(record["collection_path"], revision, "tree"))
        if "question_count" in record:
            item["question_count"] = record["question_count"]
        work.append(item)
    opportunities = []
    for record in plan["opportunities"]:
        item = {key: record[key] for key in ("id", "title", "provider", "source_name", "materials_url", "unit", "priority", "adoption", "deliverable", "access", "evidence_scope", "checked_on", "notes", "niche", "domain", "subdomain", "groups", "subject_title", "collection_breadcrumb", "adopted_paths", "adopted_count", "reuse_policy") if key in record}
        target = record["target"]
        item.update(collection_path=target["collection_path"], collection_title=catalog.display_name(record["collection"]),
                    tools=target.get("tools", []), goals=target.get("goals", []), type=record["lab_type"], skills=[],
                    collection_url=github_link(target["collection_path"], revision, "tree") if record["collection_exists"] else None)
        opportunities.append(item)
    labels = {key: catalog.display_name(key) for key in sorted({value for item in work + opportunities for value in [item["niche"], item["domain"], item["subdomain"], *item["tools"], *item["skills"]] if value})}
    goals = {key: {field: value[field] for field in ("title", "type", "issuer", "url")} for key, value in plan["goals"].items()}
    payload = {"version": 1, "source_commit": revision, "labs": work, "opportunities": opportunities,
               "goals": goals, "labels": labels, "status_labels": STATUS_LABELS,
               "counts": {"labs": len(work), "opportunities": len(opportunities), "statuses": {status: sum(item["status"] == status for item in work) for status in STATUS_LABELS}},
               "niche_guidance": plan["niche_guidance"], "unresolved_sources": plan["unresolved_sources"]}
    return payload


def e(value) -> str:
    return html.escape(str(value), quote=True)


def link(url: str | None, label: str, css: str = "") -> str:
    return f'<a class="{e(css)}" href="{e(url)}">{e(label)}</a>' if url else ""


def badges(item: dict, payload: dict) -> str:
    values = [("Tool", payload["labels"].get(value, value)) for value in item["tools"]]
    values += [("Preparation goal", payload["goals"].get(value, {}).get("title", value)) for value in item["goals"]]
    return ''.join(f'<span class="tag" title="{e(kind)}">{e(value)}</span>' for kind, value in values)


def lab_html(item: dict, payload: dict) -> str:
    anchor = "work-" + hashlib.sha256(item["path"].encode()).hexdigest()[:20]
    summary = f'<p>{e(item["summary"])}</p>' if item["summary"] else ""
    skills = f'<p class="muted skills">Target skills: {e(", ".join(item["skills"]))}</p>' if item["skills"] else ""
    bank = f'<span>{item["question_count"]} source questions · one lab</span>' if "question_count" in item else ""
    title = link(item["exercise_url"], item["title"]) if item["exercise_url"] else e(item["title"])
    actions = ' · '.join(filter(None, [link(item["exercise_url"], "Exercise definition"), link(item["solution_url"], "Solution"), link(item["demo_url"], "Demo"), link(item["source_url"], "Original source")]))
    return f'''<article class="lab" id="{anchor}" data-id="{e(item['id'])}">
+<div class="entry-top"><span class="status {e(item['status'])}">{e(STATUS_LABELS[item['status']])}</span><span class="kind">{e(catalog.display_name(item['type']))}</span>{bank}</div>
+<h4>{title}</h4>{summary}<div class="tags">{badges(item, payload)}</div>{skills}
+<p class="muted">{e(item['source_name'])} · Content updated <time datetime="{e(item['dates']['updated'])}">{e(item['dates']['updated'])}</time></p>
+<p class="entry-links">{actions} · <a href="?lab={quote(item['path'], safe='')}">Share this lab</a></p></article>'''.replace('\n+', '\n')


def opportunity_html(item: dict, payload: dict) -> str:
    destination = link(item["collection_url"], item["collection_path"]) if item["collection_url"] else e(item["collection_path"])
    adoption = f"{item['adopted_count']} matching labs adopted" if item["adopted_count"] else "Not adopted"
    work_link = link("?collection=" + quote(item["collection_path"], safe=""), "Browse adopted work") if item["adopted_count"] else ""
    return f'''<article class="opportunity" data-id="{e(item['id'])}"><div class="entry-top"><span class="status">{e(item['priority'].capitalize())}</span><span>{e(adoption)}</span></div>
+<h4>{link(item['materials_url'], item['title'])}</h4><p>{e(item['deliverable'])}</p><p class="muted">{e(item['unit'])} · {e(item['type'])} · {e(item['adoption'])}</p>
+<div class="tags">{badges(item, payload)}</div><details class="evidence"><summary>Source, destination &amp; adoption notes</summary>
+<p>{link(item['materials_url'], item['source_name'])} · Reuse: {e(item['reuse_policy'])}</p><p class="path">{destination}</p>
+<p>Evidence checked {e(item['checked_on'])}: {e(item['evidence_scope'])}.</p><p>{e(item.get('access', ''))}</p><p>{e(item.get('notes', ''))}</p>
+<p>Adoption does not mean completion or exhaust this source.</p></details><p class="entry-links">{work_link} {link('?view=atlas&opportunity=' + quote(item['id'], safe=''), 'Share this opportunity')}</p></article>'''.replace('\n+', '\n')


def grouped_html(items: list[dict], payload: dict, view: str) -> str:
    subjects = defaultdict(lambda: defaultdict(list))
    for item in items:
        subjects[(item["domain"], item["subdomain"] or "")][item["collection_path"]].append(item)
    lines = []
    for subject, collections in sorted(subjects.items()):
        lines.append(f'<section class="subject"><h2>{e(catalog.subject_title(subject[0], subject[1] or None))}</h2>')
        for index, (_, entries) in enumerate(sorted(collections.items())):
            first = entries[0]
            heading = " / ".join(first["collection_breadcrumb"])
            count_label = "labs" if view == "work" else "opportunities"
            lines.append(f'<details class="collection"{" open" if index == 0 else ""}><summary><span>{e(heading)}</span><span class="count">{len(entries)} {count_label}</span></summary><div class="entries">')
            for item in entries:
                lines.append(lab_html(item, payload) if view == "work" else opportunity_html(item, payload))
            lines.append('</div></details>')
        lines.append('</section>')
    return '\n'.join(lines) or '<p class="empty">No work adopted yet. Browse the practice atlas to choose a first unit.</p>'


def build(output: Path, base_path: str = "/", release: bool = False) -> dict:
    if not base_path.startswith("/") or ".." in base_path.split("/") or "?" in base_path or "#" in base_path:
        raise catalog.CatalogError("Base path must be an absolute URL path such as /labs/")
    catalog.update_catalog(check=True)
    records, sources = catalog.collect_labs()
    plan = atlas.load_atlas(records, sources)
    revision = git_text("rev-parse", "HEAD")
    dirty = bool(git_text("status", "--porcelain", "--untracked-files=normal"))
    if release and dirty:
        raise catalog.CatalogError("Release builds require a clean tracked snapshot and no untracked inputs")
    if release:
        lab_sync.sync_all(check=True)
    payload = projection(records, plan, revision)
    files = {}
    for name in ("catalog.css", "catalog.js"):
        content = (SITE / "assets" / name).read_bytes()
        stem, suffix = name.rsplit(".", 1)
        hashed = f"assets/{stem}.{hashlib.sha256(content).hexdigest()[:16]}.{suffix}"
        files[hashed] = content
    data = catalog.json_text(payload).encode()
    data_name = f"catalog.{hashlib.sha256(data).hexdigest()[:16]}.json"
    files[data_name] = data
    css_name, js_name = list(files)[:2]
    counts = payload["counts"]
    summary = ''.join(f'<a class="stat" href="?status={status}"><strong>{counts["statuses"][status]}</strong><span>{e(label)}</span></a>' for status, label in STATUS_LABELS.items())
    substitutions = {"CSS": css_name, "JS": js_name, "DATA": data_name, "SUMMARY": summary,
                     "WORK": grouped_html(payload["labs"], payload, "work"), "ATLAS": grouped_html(payload["opportunities"], payload, "atlas"),
                     "LAB_COUNT": str(len(records)), "ATLAS_COUNT": str(len(plan["opportunities"])),
                     "COMMIT": revision, "SHORT_COMMIT": revision[:7], "BUILD_STATE": "Local preview · uncommitted changes" if dirty else "Published snapshot" if release else "Local preview · clean snapshot",
                     "REPO": REPOSITORY, "GUIDANCE": ''.join(f'<li><strong>{e(catalog.display_name(item["niche"]))}.</strong> {e(item["reason"])}</li>' for item in plan["niche_guidance"]),
                     "LEADS": ''.join(f'<li>{link(item["url"], item["provider"])}: {e(item["reason"])}</li>' for item in plan["unresolved_sources"])}
    template = (SITE / "index.template.html").read_text(encoding="utf-8")
    for key, value in substitutions.items():
        template = template.replace("{{" + key + "}}", value)
    if re.search(r"\{\{[A-Z_]+\}\}", template):
        raise catalog.CatalogError("Unresolved site template placeholder")
    files["index.html"] = template.encode()
    files[".nojekyll"] = b""
    info = {"generator": "labs-pages-v1", "source_commit": revision, "source_commit_time": git_text("show", "-s", "--format=%cI", "HEAD"), "dirty": dirty, "base_path": base_path,
            "lab_count": len(records), "opportunity_count": len(plan["opportunities"]), "payload": data_name, "files": sorted([*files, "build-info.json"])}
    files["build-info.json"] = catalog.json_text(info).encode()
    output = output.absolute()
    if not output.is_relative_to(BUILD.absolute()) or output == BUILD.absolute() or ".." in output.parts:
        raise catalog.CatalogError("Output must be a dedicated directory under .meta/build/")
    for parent in [output, *output.parents]:
        if parent.is_symlink():
            raise catalog.CatalogError("Refusing symlinked output directory")
    if output.exists() and any(output.iterdir()):
        check_output(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".pages-", dir=output.parent) as temp:
        staging = Path(temp) / "site"
        staging.mkdir()
        for name, content in files.items():
            target = staging / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        check_output(staging)
        if output.exists():
            shutil.rmtree(output)
        staging.rename(output)
    result = {**info, "output": str(output), "file_count": len(files), "bytes": sum(len(value) for value in files.values())}
    print(catalog.json_text({key: result[key] for key in ("source_commit", "dirty", "lab_count", "opportunity_count", "output", "file_count", "bytes")}), end="")
    return result


def check_output(output: Path) -> None:
    info_path = output / "build-info.json"
    if not info_path.is_file() or info_path.is_symlink():
        raise catalog.CatalogError("Refusing an unmanaged output directory (missing build-info.json)")
    info = catalog.read_json(info_path)
    if info.get("generator") != "labs-pages-v1":
        raise catalog.CatalogError("Refusing an unmanaged output directory")
    actual = set()
    for path in output.rglob("*"):
        if path.is_symlink() or (path.is_file() and path.stat().st_nlink != 1):
            raise catalog.CatalogError("Publish artifact cannot contain symbolic or hard links")
        if path.is_file():
            actual.add(path.relative_to(output).as_posix())
    allowed = re.compile(r"(?:index\.html|build-info\.json|\.nojekyll|catalog\.[a-f0-9]{16}\.json|assets/catalog\.[a-f0-9]{16}\.(?:css|js))")
    if actual != set(info.get("files", [])) or len(actual) != 6 or not all(allowed.fullmatch(name) for name in actual):
        raise catalog.CatalogError("Unexpected files in publish artifact")
    document = (output / "index.html").read_text(encoding="utf-8")
    for target in re.findall(r'(?:src|href|data-catalog)="([^"?#]+)"', document):
        if not target.startswith(("https://", "http://", "/")) and not (output / target).is_file():
            raise catalog.CatalogError(f"Missing static asset: {target}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=BUILD / "pages")
    parser.add_argument("--base-path", default="/")
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--check-output", action="store_true")
    args = parser.parse_args()
    try:
        if args.check_output:
            check_output(args.output)
            print("Static artifact is valid.")
        else:
            build(args.output, args.base_path, args.release)
    except (catalog.CatalogError, OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
