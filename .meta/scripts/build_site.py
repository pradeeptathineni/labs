#!/usr/bin/env python3
"""Build a deterministic, allowlisted Pages artifact from the shared catalog."""
from __future__ import annotations

import argparse
import hashlib
import html
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
    """Publish only the fields the catalog page displays or searches."""
    labs = []
    for record in records:
        item = {key: record[key] for key in ("title", "type", "skills", "niche", "domain", "subdomain", "collection_path", "collection_breadcrumb", "subject_title", "path", "order")}
        item.update(summary=record.get("summary", ""), tools=record["tools_effective"], goals=record["goals_effective"],
                    provider=record["source"]["provider"], source_name=record["source_display"]["name"],
                    source_url=catalog.safe_url(record["source"]["url"]) if record["source"].get("url") else None,
                    status=record["tracking"]["status"], dates=record["tracking"]["dates"],
                    exercise_url=github_link(record["exercise_link"], revision), solution_url=github_link(record["solution_link"], revision),
                    demo_url=github_link(record.get("links", {}).get("demo"), revision))
        if "question_count" in record:
            item["question_count"] = record["question_count"]
        labs.append(item)
    labels = {key: catalog.display_name(key) for key in sorted({value for item in labs for value in [item["niche"], *item["tools"], *item["skills"]]})}
    return {"version": 1, "source_commit": revision, "labs": labs, "labels": labels,
            "goals": {key: value["title"] for key, value in plan["goals"].items()}, "status_labels": STATUS_LABELS}


def e(value) -> str:
    return html.escape(str(value), quote=True)


def link(url: str | None, label: str) -> str:
    return f'<a href="{e(url)}">{e(label)}</a>' if url else e(label)


def lab_html(item: dict) -> str:
    details = [STATUS_LABELS[item['status']], catalog.display_name(item['type']), 'Updated ' + item['dates']['updated']]
    if item['tools']:
        details.append('Tools: ' + ', '.join(item['tools']))
    if item['goals']:
        details.append('Goals: ' + ', '.join(item['goals']))
    if 'question_count' in item:
        details.append(f"{item['question_count']} source questions")
    actions = [link(item['source_url'], item['source_name'])]
    if item['solution_url']:
        actions.append(link(item['solution_url'], 'Solution'))
    if item['demo_url']:
        actions.append(link(item['demo_url'], 'Demo'))
    actions.append(link('?lab=' + quote(item['path'], safe='') + '#all-labs', 'Link'))
    summary = f'<p>{e(item["summary"])}</p>' if item['summary'] else ''
    skills = f'<p class="meta">Skills: {e(", ".join(item["skills"]))}</p>' if item['skills'] else ''
    return f'<li class="lab" data-path="{e(item["path"])}"><div class="lab-title">{link(item["exercise_url"], item["title"])}</div>{summary}<p class="meta">{e(" · ".join(details))}</p>{skills}<p class="meta">{" · ".join(actions)}</p></li>'


def grouped_html(items: list[dict]) -> str:
    collections = defaultdict(list)
    for item in items:
        collections[item['domain'], item['subdomain'] or '', item['collection_path']].append(item)
    lines, previous = [], None
    for (domain, subdomain, _), group in sorted(collections.items()):
        first = group[0]
        subject = (domain, subdomain)
        if subject != previous:
            lines.append(f'<h2>{e(first["subject_title"])}</h2>')
            previous = subject
        lines.append(f'<h3>{e(" / ".join(first["collection_breadcrumb"]))} <span class="count">({len(group)})</span></h3>')
        lines.append('<ul class="labs">' + ''.join(lab_html(item) for item in group) + '</ul>')
    return '\n'.join(lines)


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
    counts = Counter(item['status'] for item in payload['labs'])
    completed = [item for item in payload['labs'] if item['status'] == 'complete']
    progress = [item for item in payload['labs'] if item['status'] == 'in-progress']
    skills = Counter(skill for item in payload['labs'] for skill in item['skills'])
    summary = f"{len(records)} labs · {counts['complete']} complete · {counts['in-progress']} in progress · {counts['not-started']} planned"
    summary += ''.join(f" · {counts[status]} {status}" for status in ('paused', 'abandoned') if counts[status])
    substitutions = {"CSS": css_name, "JS": js_name, "DATA": data_name,
                     "SUMMARY": summary,
                     "COMPLETE": grouped_html(completed) or '<p>No completed labs yet.</p>',
                     "PROGRESS": grouped_html(progress) or '<p>No labs in progress yet.</p>',
                     "COMPLETE_COUNT": str(len(completed)), "PROGRESS_COUNT": str(len(progress)),
                     "WORK": grouped_html(payload['labs']) or '<p>No labs adopted yet.</p>',
                     "SKILLS": ' · '.join(link('?skill=' + quote(skill, safe='') + '#all-labs', f'{skill} ({count})') for skill, count in sorted(skills.items())) or 'No skills indexed yet.',
                     "LAB_COUNT": str(len(records)), "COMMIT": revision, "SHORT_COMMIT": revision[:7],
                     "BUILD_STATE": "Local preview with uncommitted changes" if dirty else "Published" if release else "Local preview",
                     "REPO": REPOSITORY}
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
