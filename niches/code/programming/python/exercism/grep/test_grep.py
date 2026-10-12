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
