"""Small shared input and lifecycle rules for metadata commands."""

from __future__ import annotations

import copy
import json
import subprocess
from datetime import date
from pathlib import Path
from typing import Any

import catalog


def prompt(label: str, current: Any = None, *, choices: list[str] | None = None, suggestions: list[str] | None = None, optional: bool = False) -> Any:
    """Blank keeps a value; a dash explicitly clears an optional field."""
    hints = []
    if choices:
        hints.append("choices: " + ", ".join(choices))
    if suggestions:
        hints.append("existing: " + ", ".join(suggestions))
    display = "" if current is None else ", ".join(current) if isinstance(current, list) else str(current)
    suffix = f" [{display}]" if display or optional else ""
    if hints:
        suffix += " (" + "; ".join(hints) + ")"
    while True:
        value = input(f"{label}{suffix}: ").strip()
        if value == "" and current is not None:
            return current
        if value == "-" and optional:
            return None
        if value == "" and optional:
            return None
        if not value:
            print("A value is required.")
            continue
        if choices and value not in choices:
            print("Choose one of the listed values.")
            continue
        return value


def prompt_list(label: str, current: list[str], *, suggestions: list[str] | None = None) -> list[str]:
    answer = prompt(label + " (comma separated)", current, suggestions=suggestions, optional=True)
    if answer is None:
        return []
    if isinstance(answer, list):
        return answer
    return sorted({part.strip() for part in answer.split(",") if part.strip()})


def confirm() -> bool:
    return input("Write these changes? [y/N]: ").strip().casefold() in ("y", "yes")


def preview(path: str, record: dict[str, Any], files: list[str], removals: list[str] | None = None) -> None:
    print(f"Path: {path}\nRecord:\n{catalog.json_text(record)}Files: " + (", ".join(files) or "none"))
    if removals:
        print("Remove: " + ", ".join(removals))


def valid_date(value: str | None) -> str | None:
    if value is None:
        return None
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as error:
        raise catalog.CatalogError(f"Invalid date {value!r}; use YYYY-MM-DD") from error


def apply_lab_changes(current: dict[str, Any], changes: dict[str, Any], sources: dict[str, Any]) -> dict[str, Any]:
    """Apply one candidate for flags, prompts, and adapters, then canonicalize it."""
    updated = copy.deepcopy(current)
    for key in ("title", "summary", "type", "difficulty", "skills", "tools", "goals", "links"):
        if key in changes:
            if changes[key] is None and key in ("summary", "difficulty", "tools", "goals", "links"):
                updated.pop(key, None)
            else:
                updated[key] = changes[key]
    if "source" in changes:
        updated["source"] = changes["source"]
    status = changes.get("status", updated["tracking"]["status"])
    old_status = updated["tracking"]["status"]
    updated["tracking"]["status"] = status
    dates = updated["tracking"]["dates"]
    today = date.today().isoformat()
    if status != old_status and status == "in-progress" and dates["started"] is None:
        dates["started"] = today
    if status != old_status and status == "complete" and dates["completed"] is None:
        dates["completed"] = today
    for key in ("created", "started", "completed"):
        if key in changes:
            dates[key] = valid_date(changes[key])
    if "difficulty" in updated:
        updated["difficulty"] = catalog.normalize_difficulty(updated["difficulty"], updated["source"]["provider"], sources)
    for key in ("skills", "tools", "goals"):
        if key in updated:
            updated[key] = sorted(set(updated[key]))
    return catalog.ordered_lab(updated)


def make_source(provider: str, item_id: str | None = None, url: str | None = None, revision: str | None = None) -> dict[str, str]:
    result = {"provider": provider}
    for key, value in (("item_id", item_id), ("url", url), ("revision", revision)):
        if value:
            result[key] = value
    return result


def parse_links(values: list[str]) -> dict[str, str]:
    links = {}
    for pair in values:
        if "=" not in pair:
            raise catalog.CatalogError("Links use solution=URL or demo=URL")
        key, value = pair.split("=", 1)
        if key not in ("solution", "demo") or not value:
            raise catalog.CatalogError("Links use solution=URL or demo=URL")
        links[key] = value
    return links


def git_checkout(checkout: Path, expected_repo: str, paths: list[str]) -> tuple[str, dict[str, bytes]]:
    """Read only committed bytes after checking the named upstream origin."""
    checkout = checkout.resolve()

    def git(*args: str) -> bytes:
        process = subprocess.run(["git", "-C", str(checkout), *args], capture_output=True)
        if process.returncode:
            detail = process.stderr.decode("utf-8", errors="replace").strip()
            raise catalog.CatalogError(detail or f"Cannot read upstream {args[-1]}")
        return process.stdout

    origin = git("remote", "get-url", "origin").decode().strip()
    normalized = origin.removesuffix(".git")
    accepted = {f"https://github.com/{expected_repo}", f"git@github.com:{expected_repo}"}
    if normalized not in accepted:
        raise catalog.CatalogError(f"Unexpected upstream origin {origin!r}; expected {expected_repo}")
    revision = git("rev-parse", "HEAD^{commit}").decode().strip()
    return revision, {path: git("show", f"{revision}:{path}") for path in paths}
