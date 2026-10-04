#!/usr/bin/env python3
"""Selectively materialize licensed CloudCertPrep JSON questions as labs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import catalog
import lab_init


PROVIDER = "cloudcertprep"


def _parser() -> argparse.ArgumentParser:
    """Require a narrow item selection so imports cannot dump entire exams."""
    parser = argparse.ArgumentParser(description="Import selected CloudCertPrep questions from a local checkout.")
    parser.add_argument("--checkout", required=True, type=Path, help="local CloudCertPrep repository checkout")
    parser.add_argument("--certification", required=True, help="target collection, e.g. aws-clf-c02")
    parser.add_argument("--domain", type=int, help="one CloudCertPrep exam domain number")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--question-id", action="append", help="select a stable question ID; repeat as needed")
    selection.add_argument("--limit", type=int, help="select the first N questions after domain/ID sorting")
    selection.add_argument("--range", nargs=2, metavar=("START_ID", "END_ID"), help="inclusive ID range within --domain")
    parser.add_argument("--dry-run", action="store_true", help="preview selected items without writing")
    parser.add_argument("--yes", action="store_true", help="confirm materializing source content under its registered copy policy")
    return parser


def _id_number(value: str) -> int:
    """Sort numbered upstream IDs numerically while retaining arbitrary IDs last."""
    match = re.search(r"([0-9]+)$", value)
    return int(match.group(1)) if match else sys.maxsize


def _load_items(checkout: Path, certification: str, bank_domain: int | None) -> list[tuple[int, dict[str, Any]]]:
    """Read the upstream JSON files without executing any upstream JavaScript."""
    if not catalog.SLUG_PATTERN.fullmatch(certification):
        raise catalog.CatalogError("Certification must be a lowercase kebab-case collection slug.")
    exam_slug = certification.removeprefix("aws-")
    data_dir = checkout.resolve() / "src/data" / exam_slug
    if not data_dir.is_dir():
        raise catalog.CatalogError(f"No CloudCertPrep data directory: {data_dir}")
    files = sorted(data_dir.glob("domain*.json"))
    items: list[tuple[int, dict[str, Any]]] = []
    for path in files:
        match = re.fullmatch(r"domain([0-9]+)", path.stem)
        if match is None:
            continue
        domain_number = int(match.group(1))
        if bank_domain is not None and domain_number != bank_domain:
            continue
        data = catalog.read_json(path)
        if not isinstance(data, list):
            raise catalog.CatalogError(f"Expected a JSON array in {path}.")
        for item in data:
            if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not isinstance(item.get("question"), str):
                raise catalog.CatalogError(f"Unexpected question record in {path}.")
            item["_domain_number"] = domain_number
            items.append((domain_number, item))
    return sorted(items, key=lambda pair: (pair[0], _id_number(pair[1]["id"]), pair[1]["id"]))


def _select(items: list[tuple[int, dict[str, Any]]], args: argparse.Namespace) -> list[tuple[int, dict[str, Any]]]:
    """Apply explicit IDs, a bounded count, or an inclusive stable-ID range."""
    if args.question_id:
        requested = set(args.question_id)
        selected = [pair for pair in items if pair[1]["id"] in requested]
        found = {pair[1]["id"] for pair in selected}
        missing = sorted(requested - found)
        if missing:
            raise catalog.CatalogError("Question IDs were not found in the selected domain(s): " + ", ".join(missing))
        if len(selected) != len(requested):
            raise catalog.CatalogError("Question IDs must be unique in the selected bank.")
        return selected
    if args.limit is not None:
        if args.limit < 1:
            raise catalog.CatalogError("--limit must be positive.")
        return items[:args.limit]
    if not args.domain:
        raise catalog.CatalogError("--range requires --domain to identify one exam bank.")
    start, end = args.range
    start_number, end_number = _id_number(start), _id_number(end)
    if start_number == sys.maxsize or end_number == sys.maxsize or start_number > end_number:
        raise catalog.CatalogError("Range IDs must end in ascending numbers, such as q001 q010.")
    return [pair for pair in items if start_number <= _id_number(pair[1]["id"]) <= end_number]


def render_question(item: dict[str, Any], source_url: str, source_name: str, license_text: str) -> tuple[str, str]:
    """Build the question page and include the upstream MIT notice verbatim."""
    title = f"{item.get('_certification', 'AWS certification').upper()} question {item['id']}"
    lines = [
        f"# {title}",
        "",
        f"Source: [{source_name}]({source_url})",
        "",
        "> [!IMPORTANT]",
        "> This question and explanation are reproduced from CloudCertPrep under the MIT License.",
        "> Original source: https://github.com/nastaso/cloudcertprep. Formatting was adjusted for this lab.",
        "",
        "## Question",
        "",
        item["question"],
        "",
    ]
    options = item.get("options", {})
    if isinstance(options, dict):
        for key, value in options.items():
            lines.append(f"- **{key}.** {value}")
    answer = item.get("answer")
    if answer is not None:
        lines.extend(["", "## Answer", "", str(answer), ""])
    if item.get("explanation"):
        lines.extend(["## Explanation", "", item["explanation"], ""])
    return "\n".join(lines), license_text


def main() -> int:
    """Preview or import only explicitly selected question records."""
    parser = _parser()
    args = parser.parse_args()
    try:
        sources = catalog.load_sources()
        source = catalog.require_copy_permission(PROVIDER, sources)
        selected = _select(_load_items(args.checkout, args.certification, args.domain), args)
        if not selected:
            raise catalog.CatalogError("The selection matched no questions.")
        license_path = args.checkout.resolve() / "LICENSE"
        if not license_path.is_file():
            raise catalog.CatalogError("The source checkout must contain its upstream LICENSE file.")
        license_text = license_path.read_text(encoding="utf-8")
        if not license_text.strip():
            raise catalog.CatalogError("The upstream LICENSE file is empty.")
        if not args.dry_run and not args.yes:
            parser.error("materializing source content requires --yes; use --dry-run to preview")
        schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
        for domain_number, item in selected:
            item_id = f"{args.certification}-domain{domain_number}-{item['id']}"
            title = f"{args.certification.upper()} question {item['id']}"
            slug = f"domain{domain_number}-{catalog.slugify(item['id'])}"
            item["_certification"] = args.certification
            source_url = f"{source['url']}/blob/main/src/data/{args.certification.removeprefix('aws-')}/domain{domain_number}.json"
            readme, copied_license = render_question(item, source_url, source["name"], license_text)
            preview_path = Path("niches") / "certification" / "cloud" / "aws" / args.certification / slug
            if args.dry_run:
                print(f"{catalog.display_path(preview_path)}  {item_id}  {title}")
                continue
            import argparse as argparse_module
            create_args = argparse_module.Namespace(
                niche="certification", domain="cloud", subdomain="aws", collection=args.certification,
                title=title, slug=slug, source=PROVIDER, kind="question", status="not-started",
                difficulty=None, skill=["aws", "certification"], item_id=item_id, source_url=source_url,
                ordered=False,
            )
            created = lab_init.create_lab(create_args, schema, sources, readme_override=readme, additional_files={"LICENSE-CLOUDCERTPREP.txt": copied_license})
            print(f"Imported {catalog.display_path(created)}")
    except (catalog.CatalogError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
