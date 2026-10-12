# 02-log-archive-tool/test_log_archive.py - Check saved logs and write errors
# Usage: python3 -m unittest test_log_archive -v

# Load the tools used to run and check the command
from contextlib import redirect_stdout
from datetime import datetime, timezone
import io
from pathlib import Path
import runpy
import stat
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import Mock, patch

# Find the command and load it without running its command-line entry point
SCRIPT = Path(__file__).with_name("log-archive")
main = runpy.run_path(str(SCRIPT))["main"]


# Check each run in a separate folder
class ArchiveTests(unittest.TestCase):
    # Create sample logs and remove them after the test
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()

        # Keep spaces in the paths to check they work
        self.source = self.root / "sample logs"
        self.source.mkdir()
        (self.source / "app.log").write_bytes(b"started\n")
        self.output = self.root / "saved archives"

    # Run the command with the sample folders unless other paths are given
    def run_tool(self, source=None, output=None):
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(source or self.source),
                str(output or self.output),
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )

    # Check the archive's contents, permissions, and history entry
    def test_saved_logs(self):
        # Add hidden files, a subfolder, and a link to an outside file
        self.output = self.root / "archives"
        (self.source / ".hidden").write_bytes(b"hidden\n")
        (self.source / "nested").mkdir()
        (self.source / "nested/error.log").write_bytes(b"error\n")
        outside = self.root / "outside.txt"
        outside.write_bytes(b"outside\n")
        (self.source / "linked.log").symlink_to(outside)

        # Omit the output path to check the default folder
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(self.source)],
            cwd=self.root,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        saved = Path(result.stdout.strip())
        self.assertEqual(saved.parent, self.output)

        # Read the saved log with tar, separately from the Python command
        content = subprocess.check_output(
            ["tar", "-xOzf", str(saved), "logs/app.log"]
        )
        self.assertEqual(content, b"started\n")

        # Check hidden files and subfolders, and keep the link as a link
        with tarfile.open(saved) as archive:
            self.assertIn("logs/.hidden", archive.getnames())
            self.assertIn("logs/nested/error.log", archive.getnames())
            self.assertTrue(archive.getmember("logs/linked.log").issym())

        # Leave the source alone and keep the saved archive private
        self.assertEqual((self.source / "app.log").read_bytes(), b"started\n")
        self.assertEqual(stat.S_IMODE(saved.stat().st_mode), 0o600)
        self.assertRegex(
            (self.output / "archive.log").read_text(),
            r"^\d{8}_\d{6} UTC "
            + saved.name.replace(".", r"\.")
            + r"\n$",
        )

    # Keep both files when runs share the same time
    def test_same_second(self):
        # Hold the clock still for both runs
        clock = Mock()
        clock.now.return_value = datetime(
            2026, 10, 11, 12, 0, 0, tzinfo=timezone.utc
        )
        with (
            patch.dict(main.__globals__, datetime=clock),
            redirect_stdout(io.StringIO()),
        ):
            first = main([str(self.source), str(self.output)])
            original = first.read_bytes()
            second = main([str(self.source), str(self.output)])

        # Check different names, unchanged bytes, and two history entries
        self.assertNotEqual(first, second)
        self.assertTrue(first.name.startswith("logs_archive_20261011_120000_"))
        self.assertTrue(second.name.startswith("logs_archive_20261011_120000_"))
        self.assertEqual(first.read_bytes(), original)
        self.assertEqual(
            len(
                (self.output / "archive.log").read_text().splitlines()
            ),
            2,
        )

    # Reject bad source paths and a history file that points elsewhere
    def test_bad_paths(self):
        # A missing path or a file must not create the output folder
        for source in (self.root / "missing", self.source / "app.log"):
            with self.subTest(source=source):
                result = self.run_tool(source=source)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertFalse(self.output.exists())

        # Point the history path at a file that must stay unchanged
        self.output.mkdir()
        outside = self.root / "history.txt"
        outside.write_text("keep this\n")
        (self.output / "archive.log").symlink_to(outside)

        # Reject the link before saving anything
        result = self.run_tool()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(outside.read_text(), "keep this\n")
        self.assertEqual(list(self.output.glob("*.tar.gz")), [])

    # Reject output inside the source, including paths through a link
    def test_output_inside_logs(self):
        # Give the source a second path through a folder link
        alias = self.root / "alias"
        alias.symlink_to(self.source, target_is_directory=True)

        # None of these paths should leave an archive in the source
        for output in (
            self.source,
            self.source / "archives",
            alias / "archives",
        ):
            with self.subTest(output=output):
                result = self.run_tool(output=output)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("outside the log folder", result.stderr)
        self.assertEqual(
            list(self.source.iterdir()),
            [self.source / "app.log"],
        )

    # Remove an unfinished file when saving fails
    def test_archive_failure(self):
        # Leave partial bytes behind to check cleanup after a write error
        def failed_write(path, *args, **kwargs):
            Path(path).write_bytes(b"unfinished")
            raise OSError("disk full")

        # Make the archive writer fail and check that no file remains
        with patch("tarfile.open", side_effect=failed_write):
            with self.assertRaisesRegex(OSError, "disk full"):
                main([str(self.source), str(self.output)])
        self.assertEqual(list(self.output.iterdir()), [])

    # Keep the finished archive when its history entry cannot be written
    def test_log_failure(self):
        # A directory at the history path makes the append fail
        self.output.mkdir()
        (self.output / "archive.log").mkdir()

        # Report failure without printing a normal success result
        result = self.run_tool()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

        # Keep one finished archive and include its path in the error
        saved = list(self.output.glob("*.tar.gz"))
        self.assertEqual(len(saved), 1)
        self.assertIn(str(saved[0]), result.stderr)

        # Check that the saved file still contains the original log
        self.assertEqual(
            subprocess.check_output(
                [
                    "tar",
                    "-xOzf",
                    str(saved[0]),
                    "logs/app.log",  # Path inside the saved archive
                ]
            ),
            b"started\n",
        )


# Run the same checks when this file is called directly
if __name__ == "__main__":
    unittest.main()
