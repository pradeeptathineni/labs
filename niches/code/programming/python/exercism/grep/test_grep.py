#!/usr/bin/env python3

# grep/test_grep.py - Check file-search behavior
# Usage: python3 -m unittest discover -p 'test_*.py' -v

# Use temporary files to check the real file-reading path
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
