"""Small command-level checks for hierarchy, mutation, tracking, and imports."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
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
    def test_empty_corpus_and_two_shapes_ignore_nested_fixture(self) -> None:
        self.assertEqual(self.command("scripts", "catalog.py").returncode, 0)
        self.assertEqual(self.command("scripts", "catalog.py", "--check").returncode, 0)
        direct = self.init("code", "devops", "roadmap-sh", "First task")
        grouped = self.init("study", "systems", "course-abc", "Second task", "--group", "mit")
        nested = direct / "solution/fixture/lab.json"
        nested.parent.mkdir(parents=True)
        nested.write_text("not a root")
        self.assertEqual(self.command("scripts", "catalog.py").returncode, 0)
        records = json.loads((self.root / ".meta/catalog/labs.json").read_text())
        self.assertEqual(len(records), 2)
        self.assertEqual(records[1]["group"], "mit")
        self.assertEqual(records[1]["source"]["provider"], "created")
        self.assertTrue(grouped.is_dir())

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
        bad = self.root / "niches/code/devops/too/deep/extra/lab/lab.json"
        bad.parent.mkdir(parents=True)
        bad.write_bytes((first / "lab.json").read_bytes())
        result = self.command("scripts", "catalog.py", "--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Bad lab depth", result.stderr)
        bad.unlink()
        group_collection = self.root / "niches/code/devops/course/another/thing"
        group_collection.mkdir(parents=True)
        (group_collection / "lab.json").write_bytes((first / "lab.json").read_bytes())
        result = self.command("scripts", "catalog.py", "--check")
        self.assertIn("both collection and group", result.stderr)

    def test_collision_cancellation_clearing_and_lifecycle(self) -> None:
        one = self.init("code", "devops", "tasks", "One", "--summary", "Original summary")
        two = self.init("code", "devops", "tasks", "Two")
        collision = self.command("scripts", "lab_init.py", "code", "devops", "tasks", "One", "--yes")
        self.assertNotEqual(collision.returncode, 0)
        before = (one / "lab.json").read_bytes()
        cancelled = self.command("scripts", "lab_meta.py", str(one), "--interactive", stdin="\n" * 13 + "n\n")
        self.assertEqual(cancelled.returncode, 0, cancelled.stderr)
        self.assertEqual((one / "lab.json").read_bytes(), before)
        flagged = self.command("scripts", "lab_meta.py", str(one), "--status", "in-progress", "--clear-summary", "--yes")
        self.assertEqual(flagged.returncode, 0, flagged.stderr)
        answers = ["", "", "", "", "", "", "", "", "", "in-progress", "", "", "", "y"]
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
        args = ["--checkout", str(upstream), "--track", "devops", "--all-track", "--destination", "niches/code/devops/devroadmaps"]
        preview = self.command("importers", "devroadmaps.py", *args, "--dry-run")
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertFalse((self.root / "niches/code/devops/devroadmaps/one").exists())
        imported = self.command("importers", "devroadmaps.py", *args, "--yes")
        self.assertEqual(imported.returncode, 0, imported.stderr)
        lab = self.root / "niches/code/devops/devroadmaps/one"
        self.assertEqual(self.metadata(lab)["type"], "project")
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
        args = ["--checkout", str(upstream), "--all-domains", "--destination", "niches/study/cloud/aws/clf-c02"]
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


if __name__ == "__main__":
    unittest.main()
