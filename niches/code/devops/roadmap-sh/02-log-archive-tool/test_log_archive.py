"""Check saved files, repeated runs, and important write failures."""

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


SCRIPT = Path(__file__).with_name("log-archive")
main = runpy.run_path(str(SCRIPT))["main"]


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.source = self.root / "sample logs"
        self.source.mkdir()
        (self.source / "app.log").write_bytes(b"started\n")
        self.output = self.root / "saved archives"

    def run_tool(self, source=None, output=None):
        return subprocess.run([sys.executable, str(SCRIPT), str(source or self.source),
                               str(output or self.output)], capture_output=True, text=True, timeout=10)

    def test_archive_opens_with_tar_and_keeps_originals(self):
        self.output = self.root / "archives"
        (self.source / ".hidden").write_bytes(b"hidden\n")
        (self.source / "nested").mkdir()
        (self.source / "nested/error.log").write_bytes(b"error\n")
        outside = self.root / "outside.txt"
        outside.write_bytes(b"outside\n")
        (self.source / "linked.log").symlink_to(outside)
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.source)], cwd=self.root,
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        saved = Path(result.stdout.strip())
        self.assertEqual(saved.parent, self.output)
        content = subprocess.check_output(["tar", "-xOzf", str(saved), "logs/app.log"])
        self.assertEqual(content, b"started\n")
        with tarfile.open(saved) as archive:
            self.assertIn("logs/.hidden", archive.getnames())
            self.assertIn("logs/nested/error.log", archive.getnames())
            self.assertTrue(archive.getmember("logs/linked.log").issym())
        self.assertEqual((self.source / "app.log").read_bytes(), b"started\n")
        self.assertEqual(stat.S_IMODE(saved.stat().st_mode), 0o600)
        self.assertRegex((self.output / "archive.log").read_text(),
                         r"^\d{8}_\d{6} UTC " + saved.name.replace(".", r"\.") + r"\n$")

    def test_two_runs_in_the_same_second_keep_both_archives(self):
        clock = Mock()
        clock.now.return_value = datetime(2026, 10, 11, 12, 0, 0, tzinfo=timezone.utc)
        with patch.dict(main.__globals__, datetime=clock), redirect_stdout(io.StringIO()):
            first = main([str(self.source), str(self.output)])
            original = first.read_bytes()
            second = main([str(self.source), str(self.output)])
        self.assertNotEqual(first, second)
        self.assertTrue(first.name.startswith("logs_archive_20261011_120000_"))
        self.assertTrue(second.name.startswith("logs_archive_20261011_120000_"))
        self.assertEqual(first.read_bytes(), original)
        self.assertEqual(len((self.output / "archive.log").read_text().splitlines()), 2)

    def test_bad_paths_do_not_write_an_archive(self):
        for source in (self.root / "missing", self.source / "app.log"):
            with self.subTest(source=source):
                result = self.run_tool(source=source)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertFalse(self.output.exists())
        self.output.mkdir()
        outside = self.root / "history.txt"
        outside.write_text("keep this\n")
        (self.output / "archive.log").symlink_to(outside)
        result = self.run_tool()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(outside.read_text(), "keep this\n")
        self.assertEqual(list(self.output.glob("*.tar.gz")), [])

    def test_archive_folder_cannot_be_inside_logs_even_through_a_link(self):
        alias = self.root / "alias"
        alias.symlink_to(self.source, target_is_directory=True)
        for output in (self.source, self.source / "archives", alias / "archives"):
            with self.subTest(output=output):
                result = self.run_tool(output=output)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("outside the log folder", result.stderr)
        self.assertEqual(list(self.source.iterdir()), [self.source / "app.log"])

    def test_failed_archive_removes_unfinished_file(self):
        def failed_write(path, *args, **kwargs):
            Path(path).write_bytes(b"unfinished")
            raise OSError("disk full")

        with patch("tarfile.open", side_effect=failed_write):
            with self.assertRaisesRegex(OSError, "disk full"):
                main([str(self.source), str(self.output)])
        self.assertEqual(list(self.output.iterdir()), [])

    def test_log_failure_keeps_the_finished_archive_and_reports_it(self):
        self.output.mkdir()
        (self.output / "archive.log").mkdir()
        result = self.run_tool()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        saved = list(self.output.glob("*.tar.gz"))
        self.assertEqual(len(saved), 1)
        self.assertIn(str(saved[0]), result.stderr)
        self.assertEqual(subprocess.check_output(["tar", "-xOzf", str(saved[0]), "logs/app.log"]),
                         b"started\n")


if __name__ == "__main__":
    unittest.main()
