# Engineering decisions

This record follows the development order. It explains choices and revisions
that a reader can check against the code, tests, and Git history.

## 1. Start with the existing Linux tools — 2026-10-11

The [exercise](https://roadmap.sh/projects/server-stats) asks for a script with
CPU, memory, disk, and top-process statistics. I chose the first project in the
roadmap.sh collection because its behavior can be checked on a real Linux
runtime without provisioning a server.

Use Bash to compose `vmstat`, `free`, `df`, and `ps`. These utilities already
own collection and sorting. Python is useful for the tests, but a Python
collector or monitoring dependency would add little to this exercise.

Keep the report to the required measurements. A dashboard, historical storage,
privileged login-log access, and cloud deployment would make this harder to
operate without improving the required behavior.

## 2. Explain what the numbers measure — 2026-10-11

Use the second `vmstat` report for a recent CPU interval. Its first report
describes time since boot. Report non-idle time and show wait and stolen time
separately so that the headline is not mistaken for time executing work.

Calculate memory used as total minus available. Available includes memory the
kernel can reclaim for applications. Also show literal free memory so that
cache does not look like a leak. Calculate this explicitly because `free`
versions have changed the meaning of their used column.

Let `df` report mounted local filesystems and its total, excluding in-memory
filesystems. Label that scope. Filesystem capacity is not raw-device capacity,
and reserved space means used plus available can differ from total.

Use `ps` sorting for the top five processes. Its CPU percentage is a lifetime
average, not the CPU sampling interval above. Rank memory by resident size and
show that size because small percentages can round to zero. Print command
names, not full argument lists, which may contain credentials.

These choices follow the upstream manuals for
[vmstat](https://gitlab.com/procps-ng/procps/-/raw/master/man/vmstat.8),
[free](https://gitlab.com/procps-ng/procps/-/raw/master/man/free.1), and
[ps](https://gitlab.com/procps-ng/procps/-/raw/master/man/ps.1), and the kernel's
[proc documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html).
The verification record will distinguish the tested versions from current manuals.

## 3. Keep evidence and operation separate — 2026-10-11

Use standard-library Python tests with controlled command output for edge
cases, then run the script against real Linux tools with a bounded workload.
A fixture proves interpretation; it cannot prove Linux collection works.

An existing Debian Docker image provides Linux without new cloud resources or
starting the stopped home-lab VM. Its kernel-wide counters can describe the
Docker VM while process and filesystem views depend on namespaces. This is
Linux compatibility evidence, not a measurement of the Mac or a container
resource dashboard.

The public lab will contain operation instructions, decisions, and evidence.
Reusable autonomous-development guidance belongs in private Planning AI.
Normal manual use of this script must not depend on that private repository.

## 4. Remove a misleading disk total after running Linux — 2026-10-11

The first implementation passed 11 fixture tests and ShellCheck. A live Debian
12 run then showed an overlay mount, its backing device, and the host bind
mount. `df --total` summed those rows and could count the same storage twice.

Remove the aggregate rather than building a device-deduplication engine.
Each filesystem still has size, used, available, and percentage columns.
This satisfies the exercise's disk information and gives readers a useful
mount-level view without pretending to measure unique physical storage.

Revise the option assertion and add a real-Linux test that starts a bounded
CPU and memory workload, finds its PID in both rankings, and cleans it up even
when an assertion fails. Fixtures alone did not reveal the mount topology.

## 5. Revise an overly strict memory assumption during review — 2026-10-11

Reviewing the validation exposed an assumption that available memory must be
at least free memory. The kernel's estimate accounts for reserves and zone
watermarks. On a system with little reclaimable cache, available can be less
than free. The [kernel documentation](https://www.kernel.org/doc/html/v6.1/filesystems/proc.html)
explains the estimate, and an [Oracle Linux engineering example](https://blogs.oracle.com/linux/memavailable-less-than-memfree)
demonstrates this case.

Validate both quantities against total memory instead of comparing them to
each other. Replace the incorrect failure fixture and add a regression test
for free greater than available. This is a source-backed edge case, not a
claim that the live Debian run reproduced that memory state.

The Linux test attempt also failed because its disposable `/tmp` mount was
not executable. The fixtures create command shims there. Allow execution only
on that temporary container mount, retain `nosuid` and `nodev`, and keep the
source mount read-only. With that correction, all 12 tests then passed on
Linux. No product fix was needed for this test-environment failure.

## 6. Make the workload test independent of runner services — 2026-10-11

The first hosted CI attempt failed the known-worker memory assertion. Its
top five correctly contained runner services with resident sizes from about
50 to 128 MiB, all larger than the test's 32 MiB allocation. The locally
tested container had an isolated process namespace; the CI host did not.

Add `make test-linux` as the shared local and CI command. It runs the complete
suite in the same Debian environment, pinned by image digest, with a bounded
read-only container and an executable disposable fixture directory.

This preserves a meaningful assertion without depending on which services
the hosted runner starts. It costs a Docker image download on a fresh runner.
Revisit the image choice if that cost becomes significant. The cached image
already supplies all required tools, so no Dockerfile or installation script
is needed today.

The new CI gate prevented this failed attempt from replacing the public site.
Local commits and pushes did not themselves establish successful publication.

## 7. Keep the test organization proportionate — 2026-10-11

The human clarified that one test file is normally enough, until a real need
justifies splitting it. The fixtures and live Linux check are small enough to
read together, so consolidate them into `tests/test_report.py`. Separate test
classes still distinguish controlled output from real collection.

Retain the tests that discriminate metric meaning and failure behavior.
Stop expanding or repeating checks once those pass unless a new change,
failure, or unresolved concern justifies more work. A growing test structure
would add navigation without helping this lab today.
