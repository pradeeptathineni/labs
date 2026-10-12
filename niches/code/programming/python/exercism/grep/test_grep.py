#!/usr/bin/env python3

# grep/test_grep.py - Check file-search behavior
# Usage: python3 -m unittest discover -p 'test_*.py' -v

# Use temporary files to check the real file-reading path
import itertools
import subprocess
import tempfile
import unittest
from pathlib import Path

# Import the personal solution from this directory
from grep import grep


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
