"""Check report calculations with sample output, then run on Linux."""

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


LAB = Path(__file__).resolve().parents[1]
CPU = """procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b swpd free buff cache si so bi bo in cs us sy id wa st
 1  0 0 100 0 0 0 0 0 0 0 0 90 5 5 0 0
 1  0 0 100 0 0 0 0 0 0 0 0 20 10 60 7 3
"""
MEMORY = """               total used free shared buff/cache available
Mem: 104857600 83886080 10485760 0 73400320 73400320
Swap: 0 0 0
"""

# Each test command reads sample output and records its arguments
SHIM = r'''
import json, os, sys
from pathlib import Path
fixture = json.loads(Path(os.environ["STATS_FIXTURE"]).read_text())
name = Path(sys.argv[0]).name
with open(os.environ["STATS_CALLS"], "a") as log:
    log.write(json.dumps([name, *sys.argv[1:]]) + "\n")
item = fixture[name]
if name == "ps" and "rows" in item:
    print("PID COMMAND CPU% MEM% RSS_KiB")
    for index in range(item["rows"]):
        print(f"{100 + index} worker 20.0 0.1 {20000 - index}")
else:
    sys.stdout.write(item.get("stdout", ""))
sys.stderr.write(item.get("stderr", ""))
sys.exit(item.get("exit", 0))
'''


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.fixture = {
            "uname": {"stdout": "Linux\n"},
            "vmstat": {"stdout": CPU},
            "free": {"stdout": MEMORY},
            "df": {"stdout": "Filesystem Size Used Avail Use% Mounted on\n/dev/root 10G 2G 8G 20% /\n"},
            "ps": {"rows": 12},
        }
        for name in self.fixture:
            command = self.bin / name
            command.write_text(f"#!{sys.executable}\n" + SHIM)
            command.chmod(0o755)
        # Keep only awk from the host so a missing tool stays missing
        (self.bin / "awk").symlink_to(shutil.which("awk"))
        self.calls = self.root / "calls.jsonl"

    def run_report(self, *args):
        fixture_path = self.root / "fixture.json"
        fixture_path.write_text(json.dumps(self.fixture))
        env = dict(os.environ, PATH=str(self.bin), STATS_FIXTURE=str(fixture_path),
                   STATS_CALLS=str(self.calls))
        return subprocess.run([shutil.which("bash"), str(LAB / "server-stats.sh"), *args],
                              env=env, text=True, capture_output=True, timeout=10)

    def assert_failed(self, result, message):
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "", "A failed collection must not print a report")
        self.assertIn(message, result.stderr)

    def test_recent_cpu_and_available_memory(self):
        result = self.run_report("--interval", "2")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Non-idle: 40.0%", result.stdout)
        self.assertIn("I/O wait: 7.0% | Stolen: 3.0%", result.stdout)
        self.assertIn("Used: 30.0 MiB (30.0%) | Available: 70.0 MiB | Free: 10.0 MiB", result.stdout)
        calls = [json.loads(line) for line in self.calls.read_text().splitlines()]
        self.assertIn(["vmstat", "-n", "2", "2"], calls)
        self.assertIn(["free", "--bytes"], calls)
        self.assertIn(["df", "-h", "--local", "--exclude-type=tmpfs", "--exclude-type=devtmpfs"], calls)
        self.assertIn(["ps", "-eo", "pid=PID,comm=COMMAND,pcpu=CPU%,pmem=MEM%,rss=RSS_KiB", "--sort=-rss,-pcpu,pid"], calls)

    def test_cpu_columns_can_move_and_include_guest(self):
        self.fixture["vmstat"]["stdout"] = "r b gu st wa id sy us\n1 0 0 0 0 99 1 0\n1 0 2 3 7 60 10 20\n"
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Non-idle: 40.0%", result.stdout)

    def test_missing_or_invalid_cpu_sample(self):
        for output in (CPU.rsplit("\n", 2)[0] + "\n", "r b us sy id wa\n1 0 20 10 60 7\n1 0 20 10 60 7\n",
                       CPU.replace("20 10 60 7 3", "20 10 101 7 3"), CPU.replace("20 10 60 7 3", "20 10 ? 7 3")):
            with self.subTest(output=output):
                self.fixture["vmstat"]["stdout"] = output
                self.assert_failed(self.run_report(), "CPU statistics")

    def test_missing_or_invalid_memory(self):
        for output in ("", "Mem: 0 0 0 0 0 0\n", "Mem: 100 0 10 0 0 101\n",
                       "Mem: 100 0 101 0 0 80\n", "Mem: 100 0 10 0 0\n", "Mem: 100 0 10 0 0 ?\n"):
            with self.subTest(output=output):
                self.fixture["free"]["stdout"] = output
                self.assert_failed(self.run_report(), "memory statistics")

    def test_available_can_be_less_than_free_due_to_kernel_reserves(self):
        self.fixture["free"]["stdout"] = "Mem: 104857600 20971520 94371840 0 0 83886080\n"
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Used: 20.0 MiB (20.0%) | Available: 80.0 MiB | Free: 90.0 MiB", result.stdout)

    def test_top_five_drains_large_process_output(self):
        self.fixture["ps"]["rows"] = 20000
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        sections = result.stdout.split("Top 5 processes")
        for section in sections[1:]:
            rows = [line for line in section.splitlines() if "worker" in line]
            self.assertEqual(len(rows), 5)
            self.assertTrue(rows[-1].startswith("104 "))

    def test_fewer_than_five_processes(self):
        self.fixture["ps"]["rows"] = 2
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("worker"), 4)

    def test_collector_failures_do_not_print_partial_reports(self):
        for tool in ("vmstat", "free", "df", "ps"):
            with self.subTest(tool=tool):
                original = dict(self.fixture[tool])
                self.fixture[tool]["exit"] = 2
                self.assert_failed(self.run_report(), "Could not")
                self.fixture[tool] = original

    def test_missing_dependency(self):
        (self.bin / "free").unlink()
        self.assert_failed(self.run_report(), "Required command is missing: free")

    def test_unsupported_host(self):
        self.fixture["uname"]["stdout"] = "Darwin\n"
        self.assert_failed(self.run_report(), "Linux is required")

    def test_help_does_not_collect_or_require_linux(self):
        self.fixture["uname"]["stdout"] = "Darwin\n"
        result = self.run_report("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Usage:", result.stdout)
        self.assertFalse(self.calls.exists())

    def test_invalid_arguments_do_not_collect(self):
        for args in (("--interval",), ("--interval", "0"), ("--interval", "61"),
                     ("--interval", "1.5"), ("--interval", "01"), ("--interval", "9999999999999999"),
                     ("--help", "extra"), ("surprise",), ("",)):
            with self.subTest(args=args):
                self.assert_failed(self.run_report(*args), "server-stats:")
        self.assertFalse(self.calls.exists())


WORKER = """
import signal, time
signal.alarm(12)
memory = bytearray(32 * 1024 * 1024)
print('ready', flush=True)
deadline = time.monotonic() + 10
while time.monotonic() < deadline:
    memory[0] = (memory[0] + 1) % 256
"""


@unittest.skipUnless(platform.system() == "Linux", "Real collectors require Linux")
class LinuxSmokeTests(unittest.TestCase):
    def test_real_report_finds_cpu_and_memory_workload(self):
        worker = subprocess.Popen([sys.executable, "-c", WORKER], text=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            self.assertEqual(worker.stdout.readline().strip(), "ready")
            result = subprocess.run(["bash", str(LAB / "server-stats.sh")], text=True,
                                    capture_output=True, timeout=8)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertRegex(result.stdout, r"Non-idle: \d+\.\d%")
            self.assertIn("Available:", result.stdout)
            self.assertIn("Mounted on", result.stdout)
            cpu = result.stdout.split("Top 5 processes by CPU (lifetime average)\n")[1].split("\n\n")[0]
            memory = result.stdout.split("Top 5 processes by memory (resident size)\n")[1]
            for section in (cpu, memory):
                rows = [line.split() for line in section.splitlines()
                        if re.match(r"\s*\d+\s", line)]
                self.assertLessEqual(len(rows), 5)
                matching = [row for row in rows if row[0] == str(worker.pid)]
                self.assertEqual(len(matching), 1, section)
                self.assertGreaterEqual(int(matching[0][-1]), 32 * 1024)
                self.assertGreater(float(matching[0][-3]), 0)
        finally:
            # Always stop the test process, even when a check fails
            worker.terminate()
            try:
                worker.communicate(timeout=2)
            except subprocess.TimeoutExpired:
                worker.kill()
                worker.communicate()


if __name__ == "__main__":
    unittest.main()
