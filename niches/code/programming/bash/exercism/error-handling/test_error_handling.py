#!/usr/bin/env python3

# error-handling/test_error_handling.py - Check the greeting command
# Usage: python3 -m unittest discover -p 'test_*.py' -v

# Use the real script and the local Bash for each check
import subprocess
import unittest
from pathlib import Path

# Locate the script beside this test
SCRIPT = Path(__file__).with_name("error_handling.sh")


# Check the first working case before adding edge cases
class GreetingTests(unittest.TestCase):

    # Run a normal name through the real command
    def test_name(self):
        result = subprocess.run(
            ["bash", str(SCRIPT), "Alice"],
            capture_output=True,
            text=True,
        )

        # Check the output, error stream, and exit code together
        self.assertEqual(
            (result.stdout, result.stderr, result.returncode),
            ("Hello, Alice\n", "", 0),
        )
