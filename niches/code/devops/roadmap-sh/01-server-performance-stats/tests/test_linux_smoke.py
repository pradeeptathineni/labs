"""Exercise real collectors and prove that a known workload appears in both lists."""

from pathlib import Path
import platform
import re
import subprocess
import sys
import unittest


LAB = Path(__file__).resolve().parents[1]
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
            # Always release the bounded workload, including when assertions fail.
            worker.terminate()
            try:
                worker.communicate(timeout=2)
            except subprocess.TimeoutExpired:
                worker.kill()
                worker.communicate()


if __name__ == "__main__":
    unittest.main()
