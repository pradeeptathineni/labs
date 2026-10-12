#!/usr/bin/env python3

# tests/test_grep.py - Check file-search behavior
# Usage: python3 -m unittest discover -s tests -p 'test_*.py' -v

# Use temporary files to check the real file-reading path
import io
import itertools
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# Locate the source independently of the current folder
SOURCE = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SOURCE))
from grep import grep, iter_matches

# Use the same module for command-line checks
SCRIPT = SOURCE / "grep.py"


# Fail if the search starts loading whole files
class LineInput(io.StringIO):

    # Allow iteration, but make full-input reads visible
    def read(self, *args, **kwargs):
        raise AssertionError("Read lines instead of the whole input.")


# Start with literal text and file ordering
class GrepTests(unittest.TestCase):

    # Check matches, file prefixes, and preserved spaces
    def test_files(self):
        with tempfile.TemporaryDirectory() as directory:

            # Write inputs that distinguish literal text from regex matching
            first = Path(directory) / "first.txt"
            second = Path(directory) / "second.txt"
            first.write_text("  a.b  \naxb\n", encoding="utf-8")
            second.write_text("a.b again\n", encoding="utf-8")

            # Keep file order and add one prefix per match
            result = grep("a.b", "", [str(first), str(second)])
            self.assertEqual(
                result,
                f"{first}:  a.b  \n{second}:a.b again\n",
            )

    # Invert the match before deciding whether to return a filename
    def test_inverted_files(self):
        with tempfile.TemporaryDirectory() as directory:

            # Give one file only matches and another only nonmatches
            first = Path(directory) / "matches.txt"
            second = Path(directory) / "other.txt"
            first.write_text("alpha\nalpha\n", encoding="utf-8")
            second.write_text("beta\n", encoding="utf-8")

            # Return the file with a qualifying nonmatch, once
            self.assertEqual(
                grep("alpha", "-l -v", [str(first), str(second)]),
                f"{second}\n",
            )

    # Compare every flag combination with a separate native implementation
    def test_native_flags(self):
        with tempfile.TemporaryDirectory() as directory:

            # Include case, whitespace, blank lines, and literal punctuation
            first = Path(directory) / "first.txt"
            second = Path(directory) / "second.txt"
            first.write_text("Alpha\nalpha\n  alpha  \na.b\nBeta\n\n", encoding="utf-8")
            second.write_text("ALPHA\naxb\nomega\n", encoding="utf-8")
            files = [str(first), str(second)]
            choices = ["-n", "-l", "-i", "-v", "-x"]

            # Use three patterns and all 32 combinations of the five flags
            for pattern in ["alpha", "a.b", ""]:
                for selected in itertools.product([False, True], repeat=5):
                    flags = [flag for flag, use in zip(choices, selected) if use]
                    with self.subTest(pattern=pattern, flags=flags):

                        # Ask grep for fixed-string matching on these ASCII inputs
                        baseline = subprocess.run(
                            ["grep", "-F", *flags, "--", pattern, *files],
                            capture_output=True,
                            text=True,
                        )
                        self.assertIn(baseline.returncode, [0, 1])
                        self.assertEqual(baseline.stderr, "")
                        self.assertEqual(
                            grep(pattern, " ".join(flags), files),
                            baseline.stdout,
                        )

    # Reject unknown flags before file access and expose file errors
    def test_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = str(Path(directory) / "missing.txt")

            # Do not silently pretend that an unsupported flag worked
            with self.assertRaisesRegex(ValueError, "Unknown flags: -z"):
                grep("alpha", "-z", [missing])

            # Let the caller decide how to report an unreadable path
            with self.assertRaises(FileNotFoundError):
                grep("alpha", "", [missing])

    # Stop after one match without reading later lines or leaving the file open
    def test_lazy_rows(self):
        source = LineInput("alpha\nbeta\nalpha\n")
        with patch("grep.open", return_value=source, create=True):
            rows = iter_matches("alpha", "", ["sample.txt"])

            # One requested result should consume just its first input line
            self.assertEqual(next(rows), "alpha\n")
            self.assertEqual(source.tell(), len("alpha\n"))
            rows.close()
            self.assertTrue(source.closed)

    # Check the real command's output, errors, and statuses
    def test_command(self):
        with tempfile.TemporaryDirectory() as directory:

            # Use ordinary text and invalid UTF-8 to distinguish failure paths
            source = Path(directory) / "sample.txt"
            source.write_text("Alpha\nbeta\nStraße", encoding="utf-8")
            bad = Path(directory) / "bad.txt"
            bad.write_bytes(b"\xff")
            cases = [
                (["-i", "-n", "alpha", str(source)], 0, "1:Alpha\n", ""),
                (["-i", "-x", "STRASSE", str(source)], 0, "Straße\n", ""),
                (["absent", str(source)], 1, "", ""),
                (["alpha", str(source) + ".missing"], 2, "", "grep:"),
                (["alpha", str(bad)], 2, "", "grep:"),
                (["-z", "alpha", str(source)], 2, "", "unrecognized arguments"),
            ]

            # Exercise each path in a fresh process
            for args, code, output, error in cases:
                with self.subTest(args=args):
                    result = subprocess.run(
                        [sys.executable, str(SCRIPT), *args],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(result.returncode, code)
                    self.assertEqual(result.stdout, output)
                    if error:
                        self.assertIn(error, result.stderr)
                    else:
                        self.assertEqual(result.stderr, "")

    # A stopped pipe consumer should not cause a shutdown traceback
    def test_closed_pipe(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "many.txt"
            source.write_text("alpha\n" * 10000, encoding="utf-8")

            # Close the pipe before the command can finish its output
            process = subprocess.Popen(
                [sys.executable, str(SCRIPT), "alpha", str(source)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            process.stdout.close()
            errors = process.stderr.read()
            process.stderr.close()
            self.assertEqual(process.wait(timeout=5), 1)
            self.assertEqual(errors, b"")
