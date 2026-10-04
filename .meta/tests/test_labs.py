"""Exercise the source-independent hierarchy and content tracking invariants."""

from __future__ import annotations

import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
IMPORTER_DIR = Path(__file__).resolve().parents[1] / "importers"
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(IMPORTER_DIR))

import catalog
import lab_init
import lab_meta
import lab_sync
import source_meta
from support import RepositoryCase


class LabArchitectureTests(RepositoryCase):
    """Check hierarchy, metadata, source, and tracking behavior."""

    def test_hierarchy_shapes_sources_and_mixed_collection(self) -> None:
        self.add_lab("niches/code/software/backend/devroadmaps/rest-api", "external-a", "backend-rest-api")
        self.add_lab("niches/code/data/tidytuesday/gutenberg", "external-a", "tuesday-gutenberg")
        self.add_lab("niches/certification/cloud/aws/aws-saa-c03/resilience", "external-a", "saa-resilience")
        self.add_lab("niches/certification/cloud/aws/aws-saa-c03/cost", "external-b", "saa-cost")
        self.add_lab("niches/writing/argumentation/mit-ocw-problems-of-philosophy/paper-1", "created")
        self.add_lab("niches/mathematics/problem-solving/project-euler/multiples", "generated")

        records, _ = catalog.collect_labs()
        by_path = {record["path"]: record for record in records}
        self.assertEqual(by_path["niches/code/software/backend/devroadmaps/rest-api"]["subdomain"], "backend")
        self.assertIsNone(by_path["niches/code/data/tidytuesday/gutenberg"]["subdomain"])
        self.assertEqual(by_path["niches/code/data/tidytuesday/gutenberg"]["source"]["provider"], "external-a")
        self.assertEqual(by_path["niches/writing/argumentation/mit-ocw-problems-of-philosophy/paper-1"]["source"]["provider"], "created")
        self.assertEqual(by_path["niches/mathematics/problem-solving/project-euler/multiples"]["source"]["provider"], "generated")
        saa = [record for record in records if record["collection"] == "aws-saa-c03"]
        self.assertEqual({record["source"]["provider"] for record in saa}, {"external-a", "external-b"})

    def test_ordered_and_unordered_collections_and_duplicate_order(self) -> None:
        self.add_lab("niches/code/devops/roadmap-sh/01-first", "external-a", "first")
        self.add_lab("niches/code/devops/roadmap-sh/02-second", "external-a", "second")
        records, _ = catalog.collect_labs()
        self.assertEqual([record["order"] for record in records], [1, 2])
        with self.assertRaisesRegex(catalog.CatalogError, "Duplicate order"):
            self.add_lab("niches/code/devops/roadmap-sh/02-other", "external-a", "other")
            catalog.collect_labs()

    def test_mixed_ordering_is_rejected(self) -> None:
        self.add_lab("niches/code/devops/roadmap-sh/01-first", "external-a", "first")
        self.add_lab("niches/code/devops/roadmap-sh/second", "external-a", "second")
        with self.assertRaisesRegex(catalog.CatalogError, "mixes numbered and unnumbered"):
            catalog.collect_labs()

    def test_invalid_depth_and_provider_are_rejected(self) -> None:
        self.add_lab("niches/code/devops/aws/extra/roadmap-sh/lab", "external-a", "deep")
        with self.assertRaisesRegex(catalog.CatalogError, "niches/<niche>/<domain>"):
            catalog.collect_labs()
        for metadata_path in catalog.lab_paths():
            metadata_path.unlink()
        self.add_lab("niches/code/devops/roadmap-sh/lab", "missing-source", "missing")
        with self.assertRaisesRegex(catalog.CatalogError, "not registered"):
            catalog.collect_labs()

    def test_copy_guard_rejects_link_only_and_review_sources(self) -> None:
        with self.assertRaisesRegex(catalog.CatalogError, "copying requires policy 'copy'"):
            catalog.require_copy_permission("link-only", self.sources)
        with self.assertRaisesRegex(catalog.CatalogError, "copying requires policy 'copy'"):
            catalog.require_copy_permission("external-b", self.sources)
        self.assertEqual(catalog.require_copy_permission("external-a", self.sources)["name"], "Source A")

    def test_new_organization_sources_fit_the_same_registry_contract(self) -> None:
        candidate = dict(self.sources)
        candidate["rearc"] = {
            "type": "organization",
            "name": "Rearc",
            "url": "https://www.rearc.io/",
            "reuse": {"policy": "review"},
        }
        catalog.validate_document(candidate, catalog.load_schema(catalog.SOURCE_SCHEMA_PATH), "test sources")
        self.assertEqual(catalog.source_for("rearc", candidate)["type"], "organization")

    def test_catalog_order_is_deterministic(self) -> None:
        self.add_lab("niches/code/data/z-collection/zeta", "external-a", "zeta")
        self.add_lab("niches/code/data/a-collection/alpha", "external-b", "alpha")
        first, sources = catalog.collect_labs()
        second, _ = catalog.collect_labs()
        self.assertEqual(catalog.render_labs(first), catalog.render_labs(second))
        self.assertEqual([item["collection"] for item in first], ["a-collection", "z-collection"])
        self.assertEqual(catalog.render_catalog(first, sources), catalog.render_catalog(second, sources))

    def test_fingerprint_ignores_metadata_and_ignored_files(self) -> None:
        lab = self.add_lab("niches/code/software/backend/devroadmaps/rest-api", "external-a", "api")
        first = lab_sync.fingerprint_lab(lab)
        self.assertEqual(first, lab_sync.fingerprint_lab(lab))
        (lab / "cache").mkdir()
        (lab / "cache/build.log").write_text("ignored\n")
        self.assertEqual(first, lab_sync.fingerprint_lab(lab))
        metadata_path = lab / "lab.json"
        metadata = json.loads(metadata_path.read_text())
        metadata["status"] = "in-progress"
        metadata_path.write_text(json.dumps(metadata))
        self.assertEqual(first, lab_sync.fingerprint_lab(lab))
        (lab / "README.md").write_text("# Edited content\n")
        self.assertNotEqual(first, lab_sync.fingerprint_lab(lab))

    def test_interactive_naming_lists_existing_slugs_and_source_item_ids(self) -> None:
        self.add_lab("niches/code/software/backend/devroadmaps/rest-api", "external-a", "backend-rest-api")
        self.assertEqual(lab_init._collection_slugs("code", "software", "backend", "devroadmaps"), ["rest-api"])
        self.assertEqual(lab_init._source_item_ids("external-a"), ["backend-rest-api"])

    def test_sync_updates_date_without_changing_status_and_check_never_writes(self) -> None:
        lab = self.add_lab("niches/code/software/backend/devroadmaps/rest-api", "external-a", "api", order_status="in-progress")
        path = lab / "lab.json"
        metadata = json.loads(path.read_text())
        metadata["dates"]["started"] = "2026-01-02"
        metadata["tracking"]["content_sha256"] = lab_sync.fingerprint_lab(lab)
        path.write_text(json.dumps(metadata, indent=2) + "\n")
        (lab / "README.md").write_text("# A meaningful content change\n")
        before = path.read_bytes()
        with self.assertRaisesRegex(catalog.CatalogError, "tracking is stale"):
            lab_sync.sync_all(check=True)
        self.assertEqual(path.read_bytes(), before)

        lab_sync.sync_all()
        updated = json.loads(path.read_text())
        self.assertEqual(updated["dates"]["updated"], date.today().isoformat())
        self.assertEqual(updated["status"], "in-progress")
        self.assertEqual(updated["dates"]["started"], "2026-01-02")
        catalog.update_catalog(check=True)

    def test_first_sync_initializes_tracking_without_moving_updated_date(self) -> None:
        lab = self.add_lab("niches/code/software/backend/devroadmaps/rest-api", "external-a", "api", order_status="paused")
        path = lab / "lab.json"
        metadata = json.loads(path.read_text())
        metadata.pop("tracking")
        path.write_text(json.dumps(metadata, indent=2) + "\n")
        lab_sync.sync_all()
        updated = json.loads(path.read_text())
        self.assertEqual(updated["dates"]["updated"], "2026-01-01")
        self.assertEqual(updated["status"], "paused")
        self.assertEqual(updated["tracking"]["content_sha256"], lab_sync.fingerprint_lab(lab))

    def test_interactive_enum_lists_names_and_closed_choices(self) -> None:
        prompts: list[str] = []
        answers = iter(["new-value", "challenge"])
        def answer(prompt: str) -> str:
            prompts.append(prompt)
            return next(answers)
        with patch("builtins.input", side_effect=answer):
            value = lab_init._prompt_value("Kind", "project", existing=["exercise", "project"], choices=["project", "challenge"], free=False)
        self.assertEqual(value, "challenge")
        self.assertIn("existing values: exercise, project", prompts[0])
        self.assertIn("choose one: project, challenge", prompts[0])

    def test_interactive_lab_update_blank_inputs_preserve_everything(self) -> None:
        lab = self.add_lab("niches/code/software/backend/devroadmaps/rest-api", "external-a", "api")
        path = lab / "lab.json"
        current = json.loads(path.read_text())
        schema = catalog.load_schema(catalog.LAB_SCHEMA_PATH)
        answers = ["", "", "", "", "", "", "", ""]
        with patch("builtins.input", side_effect=answers), contextlib.redirect_stdout(io.StringIO()):
            updated = lab_meta._interactive_update(current, schema, self.sources)
        self.assertEqual(updated, current)

    def test_source_enum_prompt_shows_existing_values_and_group(self) -> None:
        prompts: list[str] = []
        def answer(prompt: str) -> str:
            prompts.append(prompt)
            return "copy"
        with patch("builtins.input", side_effect=answer):
            value = source_meta._prompt("Reuse policy", "review", choices=["copy", "link-only", "review"], existing=["copy", "review"])
        self.assertEqual(value, "copy")
        self.assertIn("currently used: copy, review", prompts[0])
        self.assertIn("choose one: copy, link-only, review", prompts[0])

    def test_interactive_source_cancel_leaves_registry_unwritten(self) -> None:
        original = catalog.SOURCES_PATH.read_bytes()
        answers = ["sample-source", "", "Sample source", "https://example.com", "", "", "", "", "", "", "n"]
        with patch("sys.argv", ["source_meta.py", "create", "--interactive"]), patch("builtins.input", side_effect=answers), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(source_meta.main(), 0)
        self.assertEqual(catalog.SOURCES_PATH.read_bytes(), original)
        self.assertNotIn("sample-source", catalog.load_sources())

    def test_source_meta_flag_crud_keeps_schema_and_refreshes_catalog(self) -> None:
        with patch("sys.argv", [
            "source_meta.py", "create", "demo-source", "--name", "Demo Source", "--type", "external",
            "--url", "https://example.com/demo", "--reuse-policy", "copy", "--policy-url", "https://example.com/license",
        ]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(source_meta.main(), 0)
        self.assertEqual(catalog.load_sources()["demo-source"]["reuse"]["policy_url"], "https://example.com/license")
        with patch("sys.argv", ["source_meta.py", "update", "demo-source", "--reuse-policy", "link-only"]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(source_meta.main(), 0)
        output = io.StringIO()
        with patch("sys.argv", ["source_meta.py", "view", "demo-source"]), contextlib.redirect_stdout(output):
            self.assertEqual(source_meta.main(), 0)
        self.assertIn('"policy": "link-only"', output.getvalue())
        catalog.update_catalog(check=True)

if __name__ == "__main__":
    unittest.main()
