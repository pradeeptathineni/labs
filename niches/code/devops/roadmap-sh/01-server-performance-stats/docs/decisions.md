# Engineering decisions

1. **Started with the Linux tools already available (2026-10-11)**
   - Picked the first roadmap.sh project. It could be tested on Linux without setting up a server.
   - Used Bash with `vmstat`, `free`, `df`, and `ps`. These tools already collect the numbers and sort the processes.
   - Kept Python for tests. A new monitoring library wasn't needed.
   - Left out a dashboard, saved readings, login logs, and cloud setup. None was needed for the requested report.

1. **Chose what each number means (2026-10-11)**
   - Used the second `vmstat` row. The first covers time since startup, while the second covers the chosen number of seconds.
   - Included waiting and time taken by other virtual machines in the CPU total, and showed them separately.
   - Calculated memory used as total minus available. Linux can free some cached memory for programs, so free memory alone would give the wrong impression.
   - Didn't use the `free` tool's used column because its meaning has changed between versions.
   - The first version used `df --total` to show each storage location and a combined total. It left out storage held in memory.
   - Used `ps` to sort the top five processes. Its CPU percentage is an average since each process started.
   - Sorted memory by how much each process holds in RAM. Small memory percentages can round to zero.
   - Printed command names without their arguments. Arguments can contain passwords or other private values.
   - Checked the [vmstat](https://gitlab.com/procps-ng/procps/-/raw/master/man/vmstat.8), [free](https://gitlab.com/procps-ng/procps/-/raw/master/man/free.1), and [ps](https://gitlab.com/procps-ng/procps/-/raw/master/man/ps.1) manuals, and the [Linux memory notes](https://www.kernel.org/doc/html/latest/filesystems/proc.html).

1. **Tested sample output, then real Linux commands (2026-10-11)**
   - Used Python's built-in test tools with sample command output to check calculations and errors.
   - Then ran the script on Linux. Sample output couldn't prove that the real commands worked.
   - Used an existing Debian Docker image. No cloud resources or home-lab VM were needed.
   - Docker's system numbers can cover its whole Linux virtual machine while its process list covers just the container. Kept that difference in the operating notes.

1. **Removed the combined disk total after running Linux (2026-10-11)**
   - The first version passed 11 tests and ShellCheck.
   - A Debian 12 run showed Docker's file storage, the disk underneath it, and the folder shared from the Mac.
   - `df --total` could count the same space twice. Removed the total and kept each row's size, used space, available space, and percentage.
   - Checking which rows share a disk would need more code and wasn't needed for this report.
   - Added a Linux test that briefly uses CPU and 32 MiB of memory. It checks that the process appears in both top-five lists, then stops it even if the test fails.

1. **Fixed an incorrect memory check during review (2026-10-11)**
   - The script assumed available memory couldn't be lower than free memory.
   - Linux keeps some memory aside for its own needs. Available memory can therefore be lower than free memory.
   - The [Linux notes](https://www.kernel.org/doc/html/v6.1/filesystems/proc.html) and an [Oracle Linux example](https://blogs.oracle.com/linux/memavailable-less-than-memfree) showed why.
   - Changed the checks to compare both numbers with total memory. Added a test for free memory greater than available memory.
   - This case came from source review. It wasn't seen in the Debian run.
   - The first full Docker test run also failed because temporary test commands couldn't run from `/tmp`.
   - Allowed those commands to run in the container's temporary folder. Kept the source folder read-only and the `nosuid` and `nodev` protections.
   - All 12 tests then passed on Linux. The script itself didn't need a change for that folder problem.

1. **Kept the Linux test separate from the runner's own programs (2026-10-11)**
   - The first GitHub Actions run failed the memory test. Five runner services used about 50 to 128 MiB each, more than the test process.
   - The script had ranked them correctly. The test had assumed it would be running with few other programs.
   - Added `make test-linux` for local use and GitHub Actions. It runs all tests in Docker with its own process list.
   - Fixed the image version by its full ID. Set limits on CPU, memory, and process count, and kept the source read-only.
   - A new runner needs to download the image. It already has the tools needed, so no Dockerfile or install script was added.
   - The failed checks left the public site unchanged. It updated after the corrected checks and deployment passed.

1. **Kept the tests in one file (2026-10-11)**
   - The sample-output tests and Linux test fit together in `tests/test_report.py`.
   - Separate classes are enough to keep the two kinds of tests apart.
   - Kept checks for calculations and important errors. More files or repeated tests weren't needed once these passed.

1. **Finished the lab (2026-10-11)**
   - The report ran, the tests passed, and the code and comments were reviewed.
   - GitHub Actions passed, and the site showed the lab in progress with its solution link.
   - Marked the lab complete. The operating notes keep the Linux and measurement limits clear.
   - More features or tests need an actual reason. This work hasn't been tested on every Linux setup.
