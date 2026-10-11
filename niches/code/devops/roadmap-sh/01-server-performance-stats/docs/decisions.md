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
