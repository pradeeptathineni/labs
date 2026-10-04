"""Selective CloudCertPrep import and reuse-policy checks."""

from __future__ import annotations

import contextlib
import io
import json
import sys
from unittest.mock import patch

from support import RepositoryCase

import catalog
import cloudcertprep


class CloudCertPrepTests(RepositoryCase):
    """Check selection, attribution, licensing, and refusal behavior."""

    def test_importer_is_selective_attributed_and_uses_generic_creation(self) -> None:
        checkout = self.root / "upstream"
        data_dir = checkout / "src/data/clf-c02"
        data_dir.mkdir(parents=True)
        (checkout / "LICENSE").write_text("MIT License\nPermission is hereby granted...\n")
        (data_dir / "domain1.json").write_text(json.dumps([{
            "id": "q001",
            "question": "Which AWS service records API activity?",
            "options": {"A": "CloudTrail", "B": "S3"},
            "answer": "A",
            "explanation": "CloudTrail records API activity.",
        }]))
        with patch("sys.argv", ["cloudcertprep.py", "--checkout", str(checkout), "--certification", "aws-clf-c02", "--question-id", "q001", "--dry-run"]), contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(cloudcertprep.main(), 0)
        target = self.root / "niches/certification/cloud/aws/aws-clf-c02/domain1-q001"
        self.assertIn("domain1-q001", output.getvalue())
        self.assertFalse(target.exists())

        with patch("sys.argv", ["cloudcertprep.py", "--checkout", str(checkout), "--certification", "aws-clf-c02", "--question-id", "q001", "--yes"]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(cloudcertprep.main(), 0)
        imported = self.root / "niches/certification/cloud/aws/aws-clf-c02/domain1-q001"
        self.assertTrue((imported / "LICENSE-CLOUDCERTPREP.txt").is_file())
        readme = (imported / "README.md").read_text()
        self.assertIn("reproduced from CloudCertPrep under the MIT License", readme)
        self.assertIn("Which AWS service records API activity?", readme)

    def test_importer_refuses_link_only_policy(self) -> None:
        checkout = self.root / "upstream"
        data_dir = checkout / "src/data/clf-c02"
        data_dir.mkdir(parents=True)
        (checkout / "LICENSE").write_text("MIT License\n")
        (data_dir / "domain1.json").write_text(json.dumps([{"id": "q001", "question": "A question"}]))
        self.sources["cloudcertprep"]["reuse"]["policy"] = "link-only"
        catalog.SOURCES_PATH.write_text(json.dumps(self.sources, indent=2) + "\n")
        with patch("sys.argv", ["cloudcertprep.py", "--checkout", str(checkout), "--certification", "aws-clf-c02", "--question-id", "q001", "--yes"]), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(cloudcertprep.main(), 1)
        self.assertFalse((self.root / "niches/certification/cloud/aws/aws-clf-c02/domain1-q001").exists())
