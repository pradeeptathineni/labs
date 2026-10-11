# Test results

## Checks on 2026-10-11

- Checked the script at `9984e76`. Later changes covered the test setup, documents, and completion status.
- Bash syntax and ShellCheck 0.11.0 passed.
- On macOS, 12 tests passed. The Linux-only test was skipped.
- On Debian Linux, all 13 tests passed.
- The existing 20 repository tests passed. They cover lab records, catalogs, imports, commit checks, and site updates.
- GitHub Actions and site deployment passed at `d16cf1a` and `3b14e10`.
- Browser checks confirmed both site versions, lab status, solution links, small screens, and use with JavaScript turned off.
- Code and comments were reviewed while developing. There was no separate reviewer or usability study.

## What the tests cover

- `tests/test_report.py` contains all the tests.
- Sample command output checks the recent CPU reading, changed CPU column order, memory calculations, and invalid numbers.
- Other checks cover 20,000 process rows, fewer than five processes, missing tools, bad arguments, failed commands, and macOS refusing to run the Linux report.
- The Linux test starts a process that briefly uses CPU and 32 MiB of memory. It checks the process ID in both rankings and always stops the process afterward.
- The process also stops itself after a timeout. This test checks the report, not how fast the system is.

## Tools used

- Mac: Intel macOS, Bash 5.3.3, Python 3.12.10, Docker Server 29.8.0.
- Linux: Debian 12 bookworm, kernel `7.0.12-linuxkit`, Bash 5.2.15, Python 3.11.2, procps-ng 4.0.2, GNU coreutils 9.1.
- Docker image: `node:24-bookworm`, already installed locally.
- Image ID: `sha256:367d9464824bc2fc1c5303b522c01df3b7cf33afc63785f88449798566b5c254`.
- Fixed image reference: `node@sha256:6dac556d980b7f0e5498d08f08cee0ca67798b4ad6c23964a9214920e67758d0`.
- No new packages, cloud resources, or host services were installed. The home-lab VM stayed stopped. Test containers were removed afterward.

## Run the checks

From the lab folder:

```sh
make test
make check
make test-linux
```

- `make test` needs Python 3. Its Linux test skips on macOS.
- `make check` also needs Bash and ShellCheck.
- `make test-linux` needs Docker and runs all tests in the image listed above. Docker downloads it if it's missing.
- The Docker test has no network access. It limits CPU, memory, and processes, runs without root, and can't change the source files.
- Its temporary folder allows the sample test commands to run, with `nosuid` and `nodev` still set.
- Both GitHub Actions workflows run Bash syntax checks and `make test-linux` before the site can update. Other solved labs need their own workflow checks.

## Problems found

- Docker could show the same disk space twice. Removed the combined disk total.
- Available memory can be lower than free memory. Fixed that check and added a test.
- Temporary test commands couldn't run from `/tmp`. Changed that folder's Docker settings.
- The [first GitHub Actions check](https://github.com/pradeeptathineni/labs/actions/runs/38171060367) failed because five runner services used more memory than the test process. Moved the test into Docker with its own process list.

## Limits

- Numbers are read one after another, so they don't all come from the same moment.
- System CPU covers the chosen number of seconds. Process CPU covers time since each process started.
- A process can stop between the two rankings. The tools collecting the report can also appear in the lists.
- Docker's CPU and memory numbers can cover its whole Linux virtual machine. The process list and disk rows can cover only the container.
- Memory percentages use the visible system total, not the container's memory limit.
- Disk rows can show the same space more than once. Processes can share memory pages, so adding their memory sizes won't give system memory use.
- The Linux test expects few other programs to be running. Use `make test-linux` on a busy machine.
- Testing covered this Debian setup. It didn't cover a physical Linux server, every Linux version, or BusyBox.

## Site updates

- Failed checks left the site at `88c2b44`, where the lab was planned.
- [This Pages run](https://github.com/pradeeptathineni/labs/actions/runs/38171368719) put `d16cf1a` on the site with the lab in progress.
- [This Pages run](https://github.com/pradeeptathineni/labs/actions/runs/38171776776) put `3b14e10` on the site with the lab complete.
- Browser checks confirmed the exact code versions, status, and solution links.
- Completion is set explicitly. Adding code or passing tests doesn't set it. The site changes after a main push passes its checks and deploys.
