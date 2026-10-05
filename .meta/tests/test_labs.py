"""Small command-level checks for hierarchy, mutation, tracking, and imports."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parents[2]
PYTHON = sys.executable


class RepositoryCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for section in ("scripts", "importers", "catalog/schema"):
            source = HERE / ".meta" / section
            target = self.root / ".meta" / section
            target.mkdir(parents=True)
            for path in source.glob("*.py" if section != "catalog/schema" else "*.json"):
                shutil.copy2(path, target / path.name)
        (self.root / ".meta/catalog/sources.json").write_bytes((HERE / ".meta/catalog/sources.json").read_bytes())
        (self.root / "niches").mkdir()
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "user.name", "Lab Tests")

    def git(self, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(["git", *args], cwd=cwd or self.root, capture_output=True, text=True, check=True)

    def command(self, section: str, name: str, *args: str, stdin: str | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run([PYTHON, str(self.root / ".meta" / section / name), *args], cwd=self.root, input=stdin, capture_output=True, text=True)

    def init(self, *args: str) -> Path:
        result = self.command("scripts", "lab_init.py", *args, "--yes")
        self.assertEqual(result.returncode, 0, result.stderr)
        path = next(line.removeprefix("Created ") for line in result.stdout.splitlines() if line.startswith("Created "))
        return self.root / path

    def metadata(self, lab: Path) -> dict:
        return json.loads((lab / "lab.json").read_text())

    def upstream(self, name: str, files: dict[str, str], origin: str) -> Path:
        path = self.root / name
        path.mkdir()
        self.git("init", "-q", cwd=path)
        self.git("remote", "add", "origin", origin, cwd=path)
        self.git("config", "user.email", "test@example.com", cwd=path)
        self.git("config", "user.name", "Lab Tests", cwd=path)
        for relative, content in files.items():
            target = path / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
        self.git("add", ".", cwd=path)
        self.git("commit", "-qm", "upstream fixture", cwd=path)
        return path


class CoreTests(RepositoryCase):
    def test_explicit_tools_and_goals_share_collection_defaults(self) -> None:
        parent = self.root / "niches/code/devops/tasks"
        parent.mkdir(parents=True)
        (parent / "collection.json").write_text(json.dumps({"tools": ["kubernetes"], "goals": ["cka"]}))
        lab = self.init("code", "devops", "tasks", "Tool practice", "--tool", "python", "--tool", "python", "--goal", "personal-goal")
        record = json.loads((self.root / ".meta/catalog/labs.json").read_text())[0]
        self.assertEqual(record["tools_effective"], ["kubernetes", "python"])
        self.assertEqual(record["goals_effective"], ["cka", "personal-goal"])
        tracking = self.metadata(lab)["tracking"]
        result = self.command("scripts", "lab_meta.py", str(lab), "--clear-tools", "--yes")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("tools", self.metadata(lab))
        self.assertEqual(self.metadata(lab)["tracking"], tracking)
        invalid = self.command("scripts", "lab_meta.py", str(lab), "--tool", "Bad Tool", "--yes")
        self.assertNotEqual(invalid.returncode, 0)

    def test_subjects_and_nested_collections_ignore_lab_fixtures(self) -> None:
        self.assertEqual(self.command("scripts", "catalog.py").returncode, 0)
        self.assertEqual(self.command("scripts", "catalog.py", "--check").returncode, 0)
        direct = self.init("code", "devops", "roadmap-sh", "First task")
        grouped = self.init("study", "systems", "course-abc", "Second task", "--group", "mit")
        specialized = self.init("code", "systems", "course-abc", "Third task", "--subdomain", "distributed", "--group", "practice", "--group", "mit")
        cloud = self.init("code", "cloud", "projects", "Fourth task", "--subdomain", "aws")
        study = self.init("study", "cloud", "clf-c02", "Fifth task", "--subdomain", "aws")
        nested = direct / "solution/fixture/lab.json"
        nested.parent.mkdir(parents=True)
        nested.write_text("not a root")
        self.assertEqual(self.command("scripts", "catalog.py").returncode, 0)
        records = json.loads((self.root / ".meta/catalog/labs.json").read_text())
        self.assertEqual(len(records), 5)
        by_path = {self.root / item["path"]: item for item in records}
        self.assertEqual(by_path[grouped]["groups"], ["mit"])
        self.assertIsNone(by_path[grouped]["subdomain"])
        self.assertEqual(by_path[grouped]["source"]["provider"], "created")
        self.assertEqual(by_path[specialized]["subdomain"], "distributed")
        self.assertEqual(by_path[specialized]["groups"], ["practice", "mit"])
        self.assertEqual(by_path[cloud]["subdomain"], by_path[study]["subdomain"])
        self.assertNotIn("subdomain", self.metadata(cloud))
        self.assertTrue(json.loads((cloud.parent / "collection.json").read_text())["has_subdomain"])
        self.assertTrue(grouped.is_dir())
        catalog = (self.root / "CATALOG.md").read_text()
        self.assertIn("### Systems\n", catalog)
        self.assertIn("### Distributed Systems\n", catalog)
        self.assertEqual(catalog.count("### AWS Cloud\n"), 1)
        self.assertNotIn("### Systems / MIT", catalog)
        conflict = self.command("scripts", "lab_init.py", "writing", "cloud", "notes", "Ambiguous", "--group", "aws", "--yes")
        self.assertIn("Subject boundary conflicts", conflict.stderr)
        self.assertFalse((self.root / "niches/writing").exists())
        nested_lab = self.command("scripts", "lab_init.py", "code", "cloud", "nested", "Hidden lab", "--subdomain", "aws", "--group", "projects", "--group", "fourth-task", "--yes")
        self.assertIn("inside a lab", nested_lab.stderr)

    def test_subdomain_creation_preview_and_prompt_share_one_plan(self) -> None:
        args = ["code", "systems", "course", "Task", "--subdomain", "distributed", "--group", "mit"]
        target = self.root / "niches/code/systems/distributed/mit/course"
        preview = self.command("scripts", "lab_init.py", *args, "--dry-run")
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn('"has_subdomain": true', preview.stdout)
        self.assertFalse(target.exists())
        cancelled = self.command("scripts", "lab_init.py", *args, "--interactive", stdin="\n" * 20 + "n\n")
        self.assertEqual(cancelled.returncode, 0, cancelled.stderr)
        self.assertFalse(target.exists())
        created = self.command("scripts", "lab_init.py", *args, "--interactive", stdin="\n" * 20 + "y\n")
        self.assertEqual(created.returncode, 0, created.stderr)
        self.assertTrue((target / "task/lab.json").exists())
        self.assertTrue(json.loads((target / "collection.json").read_text())["has_subdomain"])
        mismatch = self.command("scripts", "lab_init.py", "code", "systems", "course", "Another task", "--group", "distributed", "--group", "mit", "--yes")
        self.assertIn("Subject boundary disagrees", mismatch.stderr)
        self.assertFalse((target / "another-task").exists())

    def test_bad_depth_ambiguity_and_order_descriptor(self) -> None:
        collection = self.root / "niches/code/devops/course"
        collection.mkdir(parents=True)
        (collection / "collection.json").write_text('{"title":"Course","ordered":true}\n')
        first = self.init("code", "devops", "course", "First task")
        self.assertEqual(first.name, "01-first-task")
        (collection / "03-deliberate-gap").mkdir()
        (collection / "03-deliberate-gap/lab.json").write_bytes((first / "lab.json").read_bytes())
        fourth = self.init("code", "devops", "course", "Fourth task")
        self.assertEqual(fourth.name, "04-fourth-task")
        year = self.init("writing", "philosophy", "papers", "Paper", "--slug", "24-00-paper-1")
        records = json.loads((self.root / ".meta/catalog/labs.json").read_text())
        self.assertIsNone(next(item for item in records if item["path"] == year.relative_to(self.root).as_posix())["order"])
        bad = self.root / "niches/code/too-shallow/lab.json"
        bad.parent.mkdir(parents=True)
        bad.write_bytes((first / "lab.json").read_bytes())
        result = self.command("scripts", "catalog.py", "--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Bad lab depth", result.stderr)
        bad.unlink()
        group_collection = self.root / "niches/code/devops/course/another/collection/thing"
        group_collection.mkdir(parents=True)
        (group_collection / "lab.json").write_bytes((first / "lab.json").read_bytes())
        result = self.command("scripts", "catalog.py", "--check")
        self.assertIn("both collection and container", result.stderr)

    def test_catalog_collection_links_and_multiline_entries(self) -> None:
        collection = self.root / "niches/code/cloud/aws/projects"
        collection.mkdir(parents=True)
        (collection / "collection.json").write_text(json.dumps({
            "title": "Example projects",
            "source_url": "https://example.com/projects",
            "has_subdomain": True,
            "ordered": True,
        }))
        (collection / "README.md").write_text("# Example projects\n")
        first_lab = self.init("code", "cloud", "projects", "First task", "--subdomain", "aws", "--summary", "First summary", "--source", "roadmap-sh", "--source-url", "https://example.com/first", "--skill", "aws", "--skill", "route53")
        second_lab = self.init("code", "cloud", "projects", "Second task", "--subdomain", "aws", "--type", "project", "--source", "roadmap-sh", "--source-url", "https://example.com/second")
        self.init("code", "cloud", "other", "Unordered task", "--type", "project")
        self.init("study", "cloud", "practice", "Study task", "--subdomain", "aws", "--type", "project")
        self.init("study", "systems", "course", "Course task", "--subdomain", "distributed", "--group", "mit")
        catalog = (self.root / "CATALOG.md").read_text().splitlines()
        style = "\n".join(catalog).split("</style>", 1)[0]
        self.assertIn("small {\n  display: inline-block;\n}", style)
        self.assertIn("summary, small {\n    margin: 0 0 15px 0;\n}", style)
        self.assertIn("summary small {\n    margin: 0 0 0 15px;\n}", style)
        self.assertIn(".catalog-section-title {\n    font-size: 1.25em;\n    font-weight: 600;\n}", style)
        self.assertIn(".catalog-all > h3, .catalog-all > details, .catalog-all > hr {\n    margin-left: 2.5rem;\n}", style)
        self.assertNotIn('style="', "\n".join(catalog))
        self.assertNotIn("`Created by me`", "\n".join(catalog))
        self.assertIn("**5 labs** · 0 complete · 0 in progress · 5 planned · 0 paused · 0 abandoned", catalog)
        self.assertIn("**Types:** Project 3 · Exercise 2", catalog)
        self.assertNotIn("Imported material is planned practice", "\n".join(catalog))
        domains = [index for index, line in enumerate(catalog) if line.startswith("### ")]
        self.assertEqual(catalog.count("---"), 4 + len(domains))
        self.assertEqual(catalog[domains[0] - 2], "---")
        self.assertTrue(all("---" in catalog[start + 1:end] for start, end in zip(domains, domains[1:])))
        summaries = [line for line in catalog if line.startswith('<summary class="catalog-section-title">')]
        self.assertEqual(summaries[:4], ['<summary class="catalog-section-title">✅ Completed</summary>', '<summary class="catalog-section-title">🛠️ In progress</summary>', '<summary class="catalog-section-title">🔎 Browse by skill</summary>', '<summary class="catalog-section-title">📚 Browse all labs</summary>'])
        self.assertEqual(catalog[catalog.index(summaries[0]) - 1], "<details open>")
        self.assertEqual(catalog[catalog.index(summaries[1]) - 1], "<details open>")
        self.assertEqual(catalog[catalog.index(summaries[2]) - 1], "<details>")
        self.assertEqual(catalog[catalog.index(summaries[3]) - 1], '<details class="catalog-all">')
        self.assertEqual(catalog.count("### AWS Cloud"), 1)
        self.assertFalse(any(line.startswith("### [") for line in catalog))
        aws_section = "\n".join(catalog).split("### AWS Cloud\n", 1)[1].split("\n### ", 1)[0]
        self.assertIn('<summary>Example projects · Code<br/><small><code>code / cloud / aws / projects</code> · 2 labs · <a href="niches/code/cloud/aws/projects/README.md">notes</a> · <a href="https://example.com/projects">ref</a></small></summary>', aws_section)
        self.assertIn('<summary>Practice · Study<br/><small><code>study / cloud / aws / practice</code> · 1 lab</small></summary>', aws_section)
        self.assertNotIn("Unordered task", aws_section)
        self.assertIn('<summary>MIT / Course · Study<br/><small><code>study / systems / distributed / mit / course</code> · 1 lab</small></summary>', catalog)
        first = next(index for index, line in enumerate(catalog) if "First summary" in line)
        self.assertTrue(catalog[first].startswith('1. <a id="lab-niches-code-cloud-aws-projects-01-first-task"></a>'))
        self.assertIn("<br/><small>Exercise · Not started · Updated ", catalog[first + 1])
        self.assertIn("`aws` `route53`", catalog[first + 1])
        self.assertTrue(catalog[first + 1].endswith("[ref](https://example.com/first)</small>"))
        self.assertTrue(catalog[first + 2].startswith('2. <a id="lab-niches-code-cloud-aws-projects-02-second-task"></a>'))
        self.assertTrue(next(line for line in catalog if "Unordered task" in line).startswith("- <a id="))
        completed = self.command("scripts", "lab_meta.py", str(first_lab), "--status", "complete", "--yes")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        in_progress = self.command("scripts", "lab_meta.py", str(second_lab), "--status", "in-progress", "--yes")
        self.assertEqual(in_progress.returncode, 0, in_progress.stderr)
        updated = (self.root / "CATALOG.md").read_text()
        completed_section = updated.split('<summary class="catalog-section-title">✅ Completed</summary>', 1)[1].split("</details>", 1)[0]
        progress_section = updated.split('<summary class="catalog-section-title">🛠️ In progress</summary>', 1)[1].split("</details>", 1)[0]
        self.assertIn("**5 labs** · 1 complete · 1 in progress · 3 planned · 0 paused · 0 abandoned", updated)
        self.assertIn('**Example projects · Code**<br/><small><code>code / cloud / aws / projects</code> · 1 lab', completed_section)
        self.assertIn("First summary", completed_section)
        self.assertNotIn(" · [Solution]", completed_section)
        self.assertIn("Second task", progress_section)
        self.assertEqual(updated.count('id="lab-niches-code-cloud-aws-projects-01-first-task"'), 1)
        self.assertEqual(self.command("scripts", "catalog.py", "--check").returncode, 0)
        (collection / "README.md").write_text('# Example projects\n\n<a href="missing.md">Broken notes</a>\n')
        self.assertIn("Broken local link", self.command("scripts", "catalog.py", "--check").stderr)

    def test_commit_hook_syncs_staged_lab_content(self) -> None:
        lab = self.init("code", "systems", "course", "Tracked", "--subdomain", "distributed", "--group", "mit")
        metadata = self.metadata(lab)
        metadata["tracking"]["dates"]["updated"] = "2020-01-01"
        (lab / "lab.json").write_text(json.dumps(metadata) + "\n")
        self.assertEqual(self.command("scripts", "catalog.py").returncode, 0)
        hook = self.root / ".githooks/pre-commit"
        hook.parent.mkdir()
        shutil.copy2(HERE / ".githooks/pre-commit", hook)
        hook.chmod(0o755)
        (self.root / "README.md").write_text("# Fixture\n")
        self.git("add", ".")
        self.git("commit", "-qm", "baseline")
        self.git("config", "core.hooksPath", ".githooks")

        original_hash = self.metadata(lab)["tracking"]["content_sha256"]
        readme = lab / "README.md"
        readme.write_text(readme.read_text() + "\nA worked note.\n")
        self.assertEqual(self.metadata(lab)["tracking"]["content_sha256"], original_hash)
        self.git("add", str(readme))
        self.git("commit", "-qm", "record lab work")
        recorded = self.metadata(lab)
        self.assertNotEqual(recorded["tracking"]["content_sha256"], original_hash)
        self.assertEqual(recorded["tracking"]["dates"]["updated"], date.today().isoformat())
        self.assertEqual(recorded["tracking"]["status"], "not-started")
        relative_metadata = (lab / "lab.json").relative_to(self.root).as_posix()
        self.assertEqual(self.git("show", f"HEAD:{relative_metadata}").stdout, (lab / "lab.json").read_text())
        self.assertEqual(self.git("show", "HEAD:CATALOG.md").stdout, (self.root / "CATALOG.md").read_text())

        started = self.command("scripts", "lab_meta.py", str(lab), "--status", "in-progress", "--yes")
        self.assertEqual(started.returncode, 0, started.stderr)
        self.git("add", relative_metadata)
        self.git("commit", "-qm", "start lab")
        recorded = self.metadata(lab)
        previous_commit = json.loads(self.git("show", f"HEAD^:{relative_metadata}").stdout)
        self.assertEqual(recorded["tracking"]["status"], "in-progress")
        self.assertEqual(recorded["tracking"]["content_sha256"], previous_commit["tracking"]["content_sha256"])
        self.assertEqual(self.git("show", "HEAD:CATALOG.md").stdout, (self.root / "CATALOG.md").read_text())

        descriptor_path = lab.parent / "collection.json"
        descriptor = json.loads(descriptor_path.read_text())
        descriptor["title"] = "Nested course"
        descriptor_path.write_text(json.dumps(descriptor) + "\n")
        self.git("add", str(descriptor_path))
        self.git("commit", "-qm", "name collection")
        self.assertEqual(self.metadata(lab), recorded)
        self.assertIn("Nested course", self.git("show", "HEAD:CATALOG.md").stdout)

        readme.write_text(readme.read_text() + "\nAn unstaged draft.\n")
        (self.root / "README.md").write_text("# Fixture\n\nStructure notes.\n")
        self.git("add", "README.md")
        self.git("commit", "-qm", "update structure notes")
        self.assertEqual(self.metadata(lab), recorded)
        candidate = self.metadata(lab)
        candidate["summary"] = "A staged metadata edit"
        (lab / "lab.json").write_text(json.dumps(candidate) + "\n")
        self.git("add", str(lab / "lab.json"))
        blocked = subprocess.run(["git", "commit", "-m", "reject mixed snapshot"], cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn("Unstaged lab/catalog inputs", blocked.stderr)
        self.assertIn("An unstaged draft.", readme.read_text())

    def test_collision_cancellation_clearing_and_lifecycle(self) -> None:
        one = self.init("code", "devops", "tasks", "One", "--summary", "Original summary")
        two = self.init("code", "devops", "tasks", "Two")
        collision = self.command("scripts", "lab_init.py", "code", "devops", "tasks", "One", "--yes")
        self.assertNotEqual(collision.returncode, 0)
        before = (one / "lab.json").read_bytes()
        cancelled = self.command("scripts", "lab_meta.py", str(one), "--interactive", stdin="\n" * 14 + "n\n")
        self.assertEqual(cancelled.returncode, 0, cancelled.stderr)
        self.assertEqual((one / "lab.json").read_bytes(), before)
        flagged = self.command("scripts", "lab_meta.py", str(one), "--status", "in-progress", "--clear-summary", "--yes")
        self.assertEqual(flagged.returncode, 0, flagged.stderr)
        answers = ["", "", "", "", "", "", "", "", "", "", "in-progress", "", "", "", "y"]
        prompted = self.command("scripts", "lab_meta.py", str(two), "--interactive", stdin="\n".join(answers) + "\n")
        self.assertEqual(prompted.returncode, 0, prompted.stderr)
        self.assertEqual(self.metadata(one)["tracking"]["dates"]["started"], self.metadata(two)["tracking"]["dates"]["started"])
        self.assertNotIn("summary", self.metadata(one))
        direct = self.command("scripts", "lab_meta.py", str(one), "--status", "complete", "--yes")
        self.assertEqual(direct.returncode, 0, direct.stderr)
        self.assertIsNotNone(self.metadata(one)["tracking"]["dates"]["completed"])
        self.command("scripts", "lab_meta.py", str(one), "--status", "in-progress", "--yes")
        self.assertIsNotNone(self.metadata(one)["tracking"]["dates"]["completed"])
        invalid = self.command("scripts", "lab_meta.py", str(one), "--started", "2026-12-01", "--completed", "2026-11-01", "--yes")
        self.assertNotEqual(invalid.returncode, 0)

    def test_source_creation_collision_and_interactive_clear(self) -> None:
        result = self.command("scripts", "source_meta.py", "create", "organization", "--type", "organization", "--name", "Again", "--reuse-policy", "review", "--yes")
        self.assertNotEqual(result.returncode, 0)
        result = self.command("scripts", "source_meta.py", "create", "test-org", "--type", "organization", "--name", "Test org", "--reuse-policy", "review", "--notes", "Old note", "--yes")
        self.assertEqual(result.returncode, 0, result.stderr)
        answers = ["", "", "", "", "", "", "", "-", "", "", "y"]
        result = self.command("scripts", "source_meta.py", "update", "test-org", "--interactive", stdin="\n".join(answers) + "\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        record = json.loads((self.root / ".meta/catalog/sources.json").read_text())["test-org"]
        self.assertNotIn("notes", record["reuse"])
        self.assertNotIn("verified", record["reuse"])
        self.assertNotIn("url", record)

    def test_staged_fingerprint_and_read_only_checks(self) -> None:
        lab = self.init("code", "devops", "tasks", "Tracked")
        self.git("add", ".")
        self.assertEqual(self.command("scripts", "lab_sync.py", "--check").returncode, 0)
        original = self.metadata(lab)["tracking"]["content_sha256"]
        (lab / "README.md").write_text((lab / "README.md").read_text() + "\nA new definition.\n")
        unstaged = self.command("scripts", "lab_sync.py", "--check")
        self.assertIn("Stage intended content", unstaged.stderr)
        self.git("add", str(lab / "README.md"))
        self.assertIn("Stale fingerprints", self.command("scripts", "lab_sync.py", "--check").stderr)
        self.assertEqual(self.command("scripts", "lab_sync.py", "--yes").returncode, 0)
        revised = self.metadata(lab)["tracking"]["content_sha256"]
        self.assertNotEqual(original, revised)
        self.git("add", str(lab / "lab.json"))
        self.assertEqual(self.command("scripts", "lab_sync.py", "--check").returncode, 0)
        nested = lab / "solution/fixture/lab.json"
        nested.parent.mkdir(parents=True)
        nested.write_text("nested metadata is content\n")
        self.git("add", str(nested))
        self.command("scripts", "lab_sync.py", "--yes")
        with_nested = self.metadata(lab)["tracking"]["content_sha256"]
        self.assertNotEqual(revised, with_nested)
        self.git("rm", "-fq", str(nested))
        self.command("scripts", "lab_sync.py", "--yes")
        self.assertEqual(self.metadata(lab)["tracking"]["content_sha256"], revised)
        self.git("add", str(lab / "lab.json"))
        self.assertEqual(self.command("scripts", "lab_sync.py", "--check").returncode, 0)
        os.chmod(lab / "README.md", 0o755)
        self.git("add", str(lab / "README.md"))
        self.command("scripts", "lab_sync.py", "--yes")
        self.assertNotEqual(self.metadata(lab)["tracking"]["content_sha256"], revised)
        external = self.root / "outside.txt"
        external.write_text("first")
        link = lab / "solution/link"
        link.parent.mkdir(parents=True, exist_ok=True)
        link.symlink_to(external)
        self.git("add", str(link))
        self.command("scripts", "lab_sync.py", "--yes")
        link_hash = self.metadata(lab)["tracking"]["content_sha256"]
        external.write_text("second")
        self.assertEqual(self.command("scripts", "lab_sync.py", "--check").returncode, 0)
        self.assertEqual(self.metadata(lab)["tracking"]["content_sha256"], link_hash)
        self.assertEqual(self.command("scripts", "catalog.py", "--check").returncode, 0)
        (self.root / "CATALOG.md").write_text("stale")
        self.assertNotEqual(self.command("scripts", "catalog.py", "--check").returncode, 0)
        self.assertEqual((self.root / "CATALOG.md").read_text(), "stale")

    def test_missing_fingerprint_establishes_baseline_without_new_date(self) -> None:
        lab = self.init("study", "systems", "notes", "Review")
        metadata = self.metadata(lab)
        metadata["tracking"]["dates"]["created"] = "2020-01-01"
        metadata["tracking"]["dates"]["updated"] = "2020-01-01"
        metadata["tracking"].pop("content_sha256")
        (lab / "lab.json").write_text(json.dumps(metadata) + "\n")
        self.git("add", ".")
        result = self.command("scripts", "lab_sync.py", "--yes")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.metadata(lab)["tracking"]["dates"]["updated"], "2020-01-01")
        self.assertEqual(self.metadata(lab)["tracking"]["status"], "not-started")


class ImporterTests(RepositoryCase):
    MIT = "MIT License\n\nCopyright (c) Test\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\n"

    def test_devroadmaps_static_parser_import_and_refresh_guard(self) -> None:
        js = "// static data\nconst PROJECT_IDEAS = { devops: [{ title: \"One\", difficulty: 'Beginner', desc: 'Build one.', tech: ['Git'], },], };\n"
        upstream = self.upstream("devroadmaps", {"LICENSE": self.MIT, "js/project-ideas.js": js}, "https://github.com/rudra496/devroadmaps.git")
        destination = "niches/code/systems/distributed/practice/devroadmaps"
        args = ["--checkout", str(upstream), "--track", "devops", "--all-track", "--destination", destination, "--subdomain", "distributed"]
        preview = self.command("importers", "devroadmaps.py", *args, "--dry-run")
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertFalse((self.root / destination).exists())
        imported = self.command("importers", "devroadmaps.py", *args, "--yes")
        self.assertEqual(imported.returncode, 0, imported.stderr)
        lab = self.root / destination / "one"
        self.assertEqual(self.metadata(lab)["type"], "project")
        self.assertTrue(json.loads((lab.parent / "collection.json").read_text())["has_subdomain"])
        self.assertIn("No change", self.command("importers", "devroadmaps.py", *args, "--yes").stdout)
        (lab / "README.md").write_text((lab / "README.md").read_text() + "My Solution notes stay here.\n")
        (upstream / "js/project-ideas.js").write_text(js.replace("Build one.", "Build two."))
        self.git("add", ".", cwd=upstream)
        self.git("commit", "-qm", "change definition", cwd=upstream)
        conflict = self.command("importers", "devroadmaps.py", *args, "--yes")
        self.assertIn("--refresh", conflict.stderr)
        refreshed = self.command("importers", "devroadmaps.py", *args, "--refresh", "--yes")
        self.assertEqual(refreshed.returncode, 0, refreshed.stderr)
        self.assertIn("My Solution notes stay here.", (lab / "README.md").read_text())
        self.assertIn("Build one.", (lab / "README.md").read_text())
        (lab / "source/project.json").write_text("manual change")
        changed_owned = self.command("importers", "devroadmaps.py", *args, "--refresh", "--yes")
        self.assertIn("Importer-owned", changed_owned.stderr)
        (upstream / "js/project-ideas.js").write_text(js.replace("'Build one.'", "makeProject()"))
        self.git("add", ".", cwd=upstream)
        self.git("commit", "-qm", "unsafe expression", cwd=upstream)
        unsafe = self.command("importers", "devroadmaps.py", *args, "--yes", "--refresh")
        self.assertIn("Executable JavaScript", unsafe.stderr)
        self.assertIn("Build one.", (lab / "README.md").read_text())
        (upstream / "js/project-ideas.js").write_text(js.replace("desc: 'Build one.'", "desc: 'Build one.', desc: 'Again.'"))
        self.git("add", ".", cwd=upstream)
        self.git("commit", "-qm", "duplicate key", cwd=upstream)
        duplicate = self.command("importers", "devroadmaps.py", *args, "--yes", "--refresh")
        self.assertIn("Duplicate project key", duplicate.stderr)

    def test_cloudcertprep_one_bank_and_multi_answer(self) -> None:
        questions = [{"id": "q001", "question": "Choose two", "options": {"A": "first", "B": "second"}, "answer": ["A", "B"], "isMultiAnswer": True, "explanation": "Both."}]
        upstream = self.upstream("cloudcertprep", {"LICENSE": self.MIT, "src/data/clf-c02/domain1.json": json.dumps(questions)}, "https://github.com/nastaso/cloudcertprep.git")
        args = ["--checkout", str(upstream), "--all-domains", "--destination", "niches/study/cloud/aws/clf-c02", "--subdomain", "aws"]
        preview = self.command("importers", "cloudcertprep.py", *args, "--dry-run")
        self.assertEqual(preview.returncode, 0, preview.stderr)
        imported = self.command("importers", "cloudcertprep.py", *args, "--yes")
        self.assertEqual(imported.returncode, 0, imported.stderr)
        lab = self.root / "niches/study/cloud/aws/clf-c02/cloudcertprep"
        data = json.loads((lab / "questions.json").read_text())
        self.assertEqual(len(data["questions"]), 1)
        self.assertEqual(data["questions"][0]["original"]["answer"], ["A", "B"])
        self.assertEqual(self.metadata(lab)["tracking"]["status"], "not-started")
        self.assertNotIn("Answer: ", (lab / "README.md").read_text())
        self.assertIn("No change", self.command("importers", "cloudcertprep.py", *args, "--yes").stdout)
        records = json.loads((self.root / ".meta/catalog/labs.json").read_text())
        self.assertEqual(records[0]["question_count"], 1)
        catalog = (self.root / "CATALOG.md").read_text()
        metadata_line = next(line for line in catalog.splitlines() if "<br/><small>Question bank" in line)
        self.assertNotIn("materialized questions", metadata_line)
        self.assertNotIn("`CloudCertPrep`", metadata_line)
        self.assertIn("Not started · Updated ", metadata_line)
        self.assertIn("`aws`", metadata_line)
        self.assertTrue(metadata_line.endswith(f"[ref]({records[0]['source']['url']})</small>"))


if __name__ == "__main__":
    unittest.main()
