#!/usr/bin/env python3
"""Import a selected CloudCertPrep CLF-C02 bank as one practice lab."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import catalog
import lab_init
import workflow

PROVIDER = "cloudcertprep"
REPO = "nastaso/cloudcertprep"
CERTIFICATION = "clf-c02"
DATA_PREFIX = "src/data/clf-c02/"


def _files(checkout: Path, revision: str) -> list[str]:
    result = subprocess.run(["git", "-C", str(checkout.resolve()), "ls-tree", "-r", "--name-only", revision, DATA_PREFIX], capture_output=True)
    if result.returncode:
        raise catalog.CatalogError(result.stderr.decode(errors="replace"))
    paths = [path for path in result.stdout.decode().splitlines() if re.fullmatch(r"src/data/clf-c02/domain[0-9]+\.json", path)]
    if not paths:
        raise catalog.CatalogError("No committed CLF-C02 domain JSON files found")
    return sorted(paths, key=lambda path: int(re.search(r"domain([0-9]+)", path).group(1)))


def _load_questions(committed: dict[str, bytes], paths: list[str]) -> list[dict[str, Any]]:
    questions = []
    seen = set()
    for path in paths:
        domain = int(re.search(r"domain([0-9]+)", path).group(1))
        try:
            data = json.loads(committed[path])
        except (ValueError, UnicodeDecodeError) as error:
            raise catalog.CatalogError(f"Invalid upstream JSON in {path}: {error}") from error
        if not isinstance(data, list):
            raise catalog.CatalogError(f"Expected question array in {path}")
        for item in data:
            if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not isinstance(item.get("question"), str) or not isinstance(item.get("options"), dict):
                raise catalog.CatalogError(f"Malformed question in {path}")
            if not all(isinstance(key, str) and isinstance(value, str) for key, value in item["options"].items()):
                raise catalog.CatalogError(f"Malformed answer options in {path}")
            answer = item.get("answer")
            if not isinstance(answer, str) and not (isinstance(answer, list) and all(isinstance(value, str) for value in answer)):
                raise catalog.CatalogError(f"Malformed reference answer in {path}")
            key = f"{CERTIFICATION}/domain{domain}/{item['id']}"
            if key in seen:
                raise catalog.CatalogError(f"Duplicate qualified question ID {key}")
            seen.add(key)
            questions.append({"key": key, "domain": domain, "source_file": path, "original": item})
    return questions


def _questions_md(questions: list[dict[str, Any]]) -> str:
    lines = ["# CloudCertPrep CLF-C02 Questions", "", "These are imported prompts. My answers belong in the lab's Solution section or my own files.", ""]
    for entry in questions:
        item = entry["original"]
        lines += [f"## {entry['key']}", "", item["question"], ""]
        lines += [f"- **{key}.** {value}" for key, value in item["options"].items()]
        lines.append("")
    return "\n".join(lines)


def _answers_md(questions: list[dict[str, Any]]) -> str:
    lines = ["# Upstream Reference Answers", "", "> [!IMPORTANT]", "> These answers and explanations come from CloudCertPrep. They are not my answers or evidence of practice.", ""]
    for entry in questions:
        item = entry["original"]
        answer = item["answer"]
        lines += [f"## {entry['key']}", "", "Answer: " + (", ".join(answer) if isinstance(answer, list) else answer), ""]
        if item.get("explanation"):
            lines += [item["explanation"], ""]
    return "\n".join(lines)


def _manifest(files: dict[str, str]) -> str:
    return catalog.json_text({name: hashlib.sha256(content.encode()).hexdigest() for name, content in files.items()})


def _check_owned(path: Path) -> dict[str, str]:
    manifest = catalog.read_json(path / "source/manifest.json")
    contents = {}
    for name, expected in manifest.items():
        actual = (path / name).read_text(encoding="utf-8")
        if hashlib.sha256(actual.encode()).hexdigest() != expected:
            raise catalog.CatalogError(f"Importer-owned file changed: {catalog.display_path(path / name)}")
        contents[name] = actual
    return contents


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Import one selected CloudCertPrep CLF-C02 question bank from Git.")
    parser.add_argument("--checkout", type=Path, required=True)
    parser.add_argument("--list", action="store_true")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--all-domains", action="store_true")
    selection.add_argument("--domain", action="append", type=int)
    selection.add_argument("--question-id", action="append", help="qualified domainN:qNNN; repeat")
    parser.add_argument("--limit", type=int, help="bound selected questions after sorting")
    parser.add_argument("--destination", help="niches/<niche>/<domain>/[subdomain/][groups/...]<collection>")
    parser.add_argument("--subdomain", help="declare the subject subdomain for a new collection; must match the path")
    parser.add_argument("--slug", default="cloudcertprep")
    parser.add_argument("--refresh", action="store_true")
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
        revision, initial = workflow.git_checkout(args.checkout, REPO, ["LICENSE"])
        license_text = initial["LICENSE"].decode("utf-8")
        if "MIT License" not in license_text or "Permission is hereby granted" not in license_text:
            raise catalog.CatalogError("Expected the reviewed MIT license at this revision")
        paths = _files(args.checkout, revision)
        _, committed = workflow.git_checkout(args.checkout, REPO, paths)
        all_questions = _load_questions(committed, paths)
        if args.list:
            for path in paths:
                number = int(re.search(r"domain([0-9]+)", path).group(1))
                print(f"domain{number}: {sum(item['domain'] == number for item in all_questions)} questions")
            return 0
        if args.interactive:
            answer = workflow.prompt("Selection: all or domain number", "all", choices=["all"] + [str(item["domain"]) for item in all_questions])
            args.all_domains = answer == "all"
            args.domain = None if args.all_domains else [int(answer)]
            args.destination = workflow.prompt("Destination collection", args.destination)
            current_subdomain = lab_init.destination(args.destination)["subdomain"]
            args.subdomain = workflow.prompt("Subject subdomain", args.subdomain or current_subdomain, optional=True)
            args.slug = workflow.prompt("Lab slug", args.slug)
        if not (args.all_domains or args.domain or args.question_id):
            raise catalog.CatalogError("Select --all-domains, --domain, or --question-id")
        if not args.destination:
            raise catalog.CatalogError("Choose --destination")
        if args.limit is not None and args.limit < 1:
            raise catalog.CatalogError("--limit must be positive")
        destination = lab_init.destination(args.destination, args.subdomain)
        if args.all_domains:
            selected = all_questions
        elif args.domain:
            wanted = set(args.domain)
            selected = [item for item in all_questions if item["domain"] in wanted]
            if wanted - {item["domain"] for item in selected}:
                raise catalog.CatalogError("Selected domain does not exist")
        else:
            wanted = {f"{CERTIFICATION}/{value.replace(':', '/')}" for value in args.question_id}
            selected = [item for item in all_questions if item["key"] in wanted]
            if wanted - {item["key"] for item in selected}:
                raise catalog.CatalogError("Selected qualified question ID does not exist")
        if args.limit is not None:
            selected = selected[:args.limit]
        if not selected:
            raise catalog.CatalogError("The selection is empty")
        source_url = f"https://github.com/{REPO}/tree/{revision}/src/data/{CERTIFICATION}"
        data = {"certification": CERTIFICATION, "selection": {"domains": sorted({item["domain"] for item in selected}), "question_keys": [item["key"] for item in selected]}, "questions": selected}
        owned = {"questions.json": catalog.json_text(data), "QUESTIONS.md": _questions_md(selected), "REFERENCE-ANSWERS.md": _answers_md(selected), "source/LICENSE.txt": license_text}
        owned["source/manifest.json"] = _manifest(owned)
        readme = "\n".join([
            "# CloudCertPrep CLF-C02 Question Bank", "", f"Source: [CloudCertPrep CLF-C02 data]({source_url})", "",
            "> [!IMPORTANT]", "> The questions and reference answers are imported from CloudCertPrep under its MIT License. They are not my responses.", "",
            "## Exercise Definition", "", f"I will work through this adopted bank of {len(selected)} questions across CLF-C02 domains {', '.join(map(str, sorted({item['domain'] for item in selected})))}. I will explain choices, review mistakes, and record my own responses separately.", "",
            "[Questions](QUESTIONS.md) · [Upstream reference answers](REFERENCE-ANSWERS.md)", "", "## Solution", "",
        ])
        records, _ = catalog.collect_labs()
        identity = f"{CERTIFICATION}/bank/{args.slug}"
        prior = next((item for item in records if item["source"].get("provider") == PROVIDER and item["source"].get("item_id") == identity), None)
        if prior:
            path = catalog.ROOT / prior["path"]
            if path.parent != (catalog.ROOT / args.destination).absolute():
                raise catalog.CatalogError(f"Existing bank lives in another collection: {prior['path']}")
            old = _check_owned(path)
            if prior["source"].get("revision") == revision and all(old.get(key) == value for key, value in owned.items() if key != "source/manifest.json"):
                print(f"No change: {prior['path']} ({len(selected)} questions)")
                return 0
            if not args.refresh:
                raise catalog.CatalogError("Bank selection or upstream content changed; rerun with --refresh to review")
            metadata = catalog.ordered_lab(catalog.read_json(path / "lab.json"))
            metadata["source"]["revision"] = revision
            metadata["source"]["url"] = source_url
            catalog.collect_labs(overrides={path / "lab.json": metadata})
            changes = {key: value for key, value in owned.items() if (path / key).read_text(encoding="utf-8") != value}
            workflow.preview(catalog.display_path(path), metadata, sorted(changes) + ["lab.json"])
            print("Review the README Exercise Definition and summary if the adopted bank scope changed; my Solution is untouched.")
            if args.dry_run:
                return 0
            if not args.interactive and not args.yes:
                parser.error("writing requires --yes")
            if args.interactive and not workflow.confirm():
                print("No changes made.")
                return 0
            for key, value in changes.items():
                catalog.write_text_atomic(path / key, value)
            catalog.write_text_atomic(path / "lab.json", catalog.json_text(metadata))
            catalog.update_catalog()
            print(f"Refreshed {catalog.display_path(path)}")
            return 0
        fields = dict(destination, title="CloudCertPrep CLF-C02 Question Bank", slug=args.slug, summary="Review selected AWS Cloud Practitioner questions and explain the reasoning behind each answer.", type="question-bank", skills=["cloud-concepts", "security-compliance", "billing-pricing"], tools=["aws"], provider=PROVIDER, item_id=identity, source_url=source_url, revision=revision)
        plan = lab_init.plan_lab(fields, sources, files={"README.md": readme, **owned})
        lab_init.preview_plan(plan)
        if args.dry_run:
            return 0
        if not args.interactive and not args.yes:
            parser.error("writing requires --yes")
        if args.interactive and not workflow.confirm():
            print("No changes made.")
            return 0
        lab_init.write_plans([plan], sources)
        print(f"Imported one bank with {len(selected)} questions: {catalog.display_path(plan['path'])}")
    except (catalog.CatalogError, OSError, UnicodeDecodeError, EOFError, KeyboardInterrupt) as error:
        if isinstance(error, (EOFError, KeyboardInterrupt)):
            print("\nNo changes made.")
            return 0
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
