#!/usr/bin/env python3

# error-handling/test_error_handling.py - Check the greeting command
# Usage: python3 -m unittest discover -p 'test_*.py' -v

# Use the real script and the local Bash for each check
import os
import subprocess
import unittest
from pathlib import Path

# Locate the script beside this test
SCRIPT = Path(__file__).with_name("error_handling.sh")
BASH = os.environ.get("BASH_UNDER_TEST", "bash")


# Check the command's input and output boundaries
class GreetingTests(unittest.TestCase):

    # Capture output and status from the real command
    def run_script(self, *names):
        return subprocess.run(
            [BASH, str(SCRIPT), *names],
            capture_output=True,
            text=True,
        )

    # Treat every single argument as data, including an empty string
    def test_names(self):
        for name in ["Alice", "", "Alice and Bob", "%s\\n", "--help", "Zoë", "A\nB"]:
            with self.subTest(name=name):
                result = self.run_script(name)

                # Check that formatting leaves the input untouched
                self.assertEqual(
                    (result.stdout, result.stderr, result.returncode),
                    (f"Hello, {name}\n", "", 0),
                )

    # Reject zero or multiple arguments without adding greeting output
    def test_usage(self):
        for names in [(), ("Alice", "Bob")]:
            with self.subTest(names=names):
                result = self.run_script(*names)

                # Keep failures out of the normal output stream
                self.assertEqual(
                    (result.stdout, result.stderr, result.returncode),
                    ("", "Usage: error_handling.sh <person>\n", 1),
                )
