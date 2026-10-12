# tests/test_report.py - Check sample reports and one real Linux run
# Usage: python3 -m unittest discover -s tests -v
#
# Skip the real run when Linux is not available

# Load the tools used to build sample commands and check their output
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

# Find the lab command from the test folder
LAB = Path(__file__).resolve().parents[1]

# Give vmstat a startup row and a later row with different CPU use
CPU = (
    "procs -----------memory---------- ---swap-- "
    "-----io---- -system-- ------cpu-----\n"
    " r  b swpd free buff cache si so bi bo in cs us sy id wa st\n"
    " 1  0 0 100 0 0 0 0 0 0 0 0 90 5 5 0 0\n"
    " 1  0 0 100 0 0 0 0 0 0 0 0 20 10 60 7 3\n"
)

# Make available memory larger than free memory
MEMORY = """               total used free shared buff/cache available
Mem: 104857600 83886080 10485760 0 73400320 73400320
Swap: 0 0 0
"""

# Each sample command reads its output and records its arguments
SHIM = r'''
# Load tools for the sample commands
import json, os, sys
from pathlib import Path

# Read the sample values and find which command was called
fixture = json.loads(Path(os.environ["STATS_FIXTURE"]).read_text())
name = Path(sys.argv[0]).name

# Save the arguments for the checks to read later
with open(os.environ["STATS_CALLS"], "a") as log:
    log.write(json.dumps([name, *sys.argv[1:]]) + "\n")

# Print process rows when requested, or use the given text
item = fixture[name]
if name == "ps" and "rows" in item:
    print("PID COMMAND CPU% MEM% RSS_KiB")
    for index in range(item["rows"]):
        print(f"{100 + index} worker 20.0 0.1 {20000 - index}")
else:
    sys.stdout.write(item.get("stdout", ""))

# Return any given error message and exit code
sys.stderr.write(item.get("stderr", ""))
sys.exit(item.get("exit", 0))
'''


# Check calculations and errors using known command output
class ReportTests(unittest.TestCase):
    # Create sample commands in a folder removed after each test
    def setUp(self):
        # Keep each test's files separate
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bin = self.root / "bin"
        self.bin.mkdir()

        # Provide known output for every command the report uses
        self.fixture = {
            "uname": {"stdout": "Linux\n"},
            "vmstat": {"stdout": CPU},
            "free": {"stdout": MEMORY},
            "df": {
                "stdout": (
                    "Filesystem Size Used Avail Use% Mounted on\n"
                    "/dev/root 10G 2G 8G 20% /\n"
                ),
            },
            "ps": {"rows": 12},
        }

        # Write a small executable for each sample command
        for name in self.fixture:
            command = self.bin / name
            command.write_text(f"#!{sys.executable}\n" + SHIM)
            command.chmod(0o755)

        # Keep only awk from the host so a missing tool stays missing
        (self.bin / "awk").symlink_to(shutil.which("awk"))
        self.calls = self.root / "calls.jsonl"

    # Run the report using this test's command output and arguments
    def run_report(self, *args):
        # Save the current sample values for the commands to read
        fixture_path = self.root / "fixture.json"
        fixture_path.write_text(json.dumps(self.fixture))
        env = dict(
            os.environ,
            PATH=str(self.bin),
            STATS_FIXTURE=str(fixture_path),
            STATS_CALLS=str(self.calls),
        )

        # Capture the report and any error without waiting indefinitely
        return subprocess.run(
            [shutil.which("bash"), str(LAB / "src" / "server-stats.sh"), *args],
            env=env,
            text=True,
            capture_output=True,
            timeout=10,
        )

    # A failed run should print an error and no partial report
    def assert_failed(self, result, message):
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(
            result.stdout,
            "",
            "A failed collection must not print a report",
        )
        self.assertIn(message, result.stderr)

    # Use the later CPU row and count cached memory as available
    def test_recent_stats(self):
        # Check the report's numbers from the known samples
        result = self.run_report("--interval", "2")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Non-idle: 40.0%", result.stdout)
        self.assertIn("I/O wait: 7.0% | Stolen: 3.0%", result.stdout)
        self.assertIn(
            "Used: 30.0 MiB (30.0%) | Available: 70.0 MiB | Free: 10.0 MiB",
            result.stdout,
        )

        # Check the actual options sent to each Linux command
        calls = [
            json.loads(line)
            for line in self.calls.read_text().splitlines()
        ]
        self.assertIn(["vmstat", "-n", "2", "2"], calls)
        self.assertIn(["free", "--bytes"], calls)
        self.assertIn(
            [
                "df",
                "-h",
                "--local",
                "--exclude-type=tmpfs",
                "--exclude-type=devtmpfs",
            ],
            calls,
        )
        self.assertIn(
            [
                "ps",
                "-eo",
                "pid=PID,comm=COMMAND,pcpu=CPU%,pmem=MEM%,rss=RSS_KiB",
                "--sort=-rss,-pcpu,pid",
            ],
            calls,
        )

    # Find CPU columns by name, even when their order changes
    def test_cpu_columns(self):
        self.fixture["vmstat"]["stdout"] = (
            "r b gu st wa id sy us\n"
            "1 0 0 0 0 99 1 0\n"
            "1 0 2 3 7 60 10 20\n"
        )

        # Check the same result with moved columns and a guest column
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Non-idle: 40.0%", result.stdout)

    # Reject missing rows, missing columns, and bad CPU values
    def test_bad_cpu(self):
        for output in (
            CPU.rsplit("\n", 2)[0] + "\n",
            "r b us sy id wa\n1 0 20 10 60 7\n1 0 20 10 60 7\n",
            CPU.replace("20 10 60 7 3", "20 10 101 7 3"),
            CPU.replace("20 10 60 7 3", "20 10 ? 7 3"),
        ):
            with self.subTest(output=output):
                self.fixture["vmstat"]["stdout"] = output
                self.assert_failed(self.run_report(), "CPU statistics")

    # Reject missing memory fields and values outside the total
    def test_bad_memory(self):
        for output in (
            "",
            "Mem: 0 0 0 0 0 0\n",
            "Mem: 100 0 10 0 0 101\n",
            "Mem: 100 0 101 0 0 80\n",
            "Mem: 100 0 10 0 0\n",
            "Mem: 100 0 10 0 0 ?\n",
        ):
            with self.subTest(output=output):
                self.fixture["free"]["stdout"] = output
                self.assert_failed(self.run_report(), "memory statistics")

    # Allow Linux to reserve some free memory for its own use
    def test_reserved_memory(self):
        self.fixture["free"]["stdout"] = (
            "Mem: 104857600 20971520 94371840 0 0 83886080\n"
        )

        # Available memory can be lower than free memory
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "Used: 20.0 MiB (20.0%) | Available: 80.0 MiB | Free: 90.0 MiB",
            result.stdout,
        )

    # Read all process output while printing only the first five rows
    def test_many_processes(self):
        self.fixture["ps"]["rows"] = 20000
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)

        # Both process lists should stop at the fifth worker
        sections = result.stdout.split("Top 5 processes")
        for section in sections[1:]:
            rows = [line for line in section.splitlines() if "worker" in line]
            self.assertEqual(len(rows), 5)
            self.assertTrue(rows[-1].startswith("104 "))

    # Accept a process list shorter than five rows
    def test_few_processes(self):
        self.fixture["ps"]["rows"] = 2
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("worker"), 4)

    # A command failure must not leave a partial report
    def test_command_errors(self):
        for tool in ("vmstat", "free", "df", "ps"):
            with self.subTest(tool=tool):
                # Restore the command's values before trying the next one
                original = dict(self.fixture[tool])
                self.fixture[tool]["exit"] = 2
                self.assert_failed(self.run_report(), "Could not")
                self.fixture[tool] = original

    # Stop when a required Linux command is missing
    def test_missing_tool(self):
        (self.bin / "free").unlink()
        self.assert_failed(
            self.run_report(),
            "Required command is missing: free",
        )

    # Reject other operating systems before collecting statistics
    def test_wrong_host(self):
        self.fixture["uname"]["stdout"] = "Darwin\n"
        self.assert_failed(self.run_report(), "Linux is required")

    # Show help without checking the host or running collectors
    def test_help(self):
        self.fixture["uname"]["stdout"] = "Darwin\n"
        result = self.run_report("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Usage:", result.stdout)
        self.assertFalse(self.calls.exists())

    # Reject bad arguments before running any collector
    def test_bad_args(self):
        for args in (
            ("--interval",),
            ("--interval", "0"),
            ("--interval", "61"),
            ("--interval", "1.5"),
            ("--interval", "01"),
            ("--interval", "9999999999999999"),
            ("--help", "extra"),
            ("surprise",),
            ("",),
        ):
            with self.subTest(args=args):
                self.assert_failed(self.run_report(*args), "server-stats:")

        # Argument errors must not call even the host check
        self.assertFalse(self.calls.exists())


# Give the Linux test a process with known memory use and CPU activity
WORKER = """
# Load the clock and a backup stop signal
import signal, time

# Stop after twelve seconds even if the parent cannot clean up
signal.alarm(12)

# Reserve memory and tell the test the worker is ready
memory = bytearray(32 * 1024 * 1024)
print('ready', flush=True)

# Keep the CPU busy for up to ten seconds
deadline = time.monotonic() + 10
while time.monotonic() < deadline:
    memory[0] = (memory[0] + 1) % 256
"""


# Check real Linux tools with a short-lived worker process
@unittest.skipUnless(
    platform.system() == "Linux",
    "Real collectors require Linux",
)
class LinuxSmokeTests(unittest.TestCase):
    # Find the worker in both CPU and memory lists
    def test_live_report(self):
        # Start a worker that reports when its memory is ready
        worker = subprocess.Popen(
            [sys.executable, "-c", WORKER],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        try:
            # Wait for the worker before collecting the real report
            self.assertEqual(worker.stdout.readline().strip(), "ready")
            result = subprocess.run(
                ["bash", str(LAB / "src" / "server-stats.sh")],
                text=True,
                capture_output=True,
                timeout=8,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertRegex(result.stdout, r"Non-idle: \d+\.\d%")
            self.assertIn("Available:", result.stdout)
            self.assertIn("Mounted on", result.stdout)

            # Separate the process lists from the other report sections
            cpu = (
                result.stdout
                .split("Top 5 processes by CPU (lifetime average)\n")[1]
                .split("\n\n")[0]
            )
            memory = result.stdout.split(
                "Top 5 processes by memory (resident size)\n"
            )[1]

            # Find one worker row in each list with its memory and CPU use
            for section in (cpu, memory):
                rows = [
                    line.split()
                    for line in section.splitlines()
                    if re.match(r"\s*\d+\s", line)
                ]
                self.assertLessEqual(len(rows), 5)
                matching = [row for row in rows if row[0] == str(worker.pid)]
                self.assertEqual(len(matching), 1, section)
                self.assertGreaterEqual(int(matching[0][-1]), 32 * 1024)
                self.assertGreater(float(matching[0][-3]), 0)
        finally:
            # Always stop the worker, even when a check fails
            worker.terminate()
            try:
                worker.communicate(timeout=2)
            except subprocess.TimeoutExpired:
                # Force it to stop if it ignores the first request
                worker.kill()
                worker.communicate()


# Run the same checks when this file is called directly
if __name__ == "__main__":
    unittest.main()
