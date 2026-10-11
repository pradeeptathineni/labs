# Server Performance Stats

## Exercise definition

[Server Performance Stats on roadmap.sh](https://roadmap.sh/projects/server-stats)

## Solution

- Run on Linux with Bash, procps (`vmstat`, `free`, `ps`), GNU coreutils (`df`), and `awk`.
- No root access or background service is needed.

```sh
./server-stats.sh
./server-stats.sh --interval 2
./server-stats.sh --help
```

- CPU is measured over one second by default. `--interval` accepts whole seconds from 1 to 60.
- Bad arguments or failed commands stop the script with an error. It won't print a half-finished report.
- Help also works on macOS. The report itself needs Linux.
- CPU time includes time waiting for disk work and time taken by other virtual machines.
- Each process's CPU percentage is an average since it started. It covers a different period from the system CPU reading.
- Memory used is total minus available. Available includes cached memory that Linux can free for programs.
- Process memory shows what it currently holds in RAM, including shared pages.
- Each disk row shows a storage location, such as `/`, with its size, used space, available space, and percentage used.
- `tmpfs` and `devtmpfs` use memory, so they are left out. Docker can show the same disk space in more than one row, so there is no combined total.
- Linux can keep some disk space aside. Used plus available may be less than the full size. `df` calculates the percentage from used plus available, and rounds the displayed sizes.
- In Docker, CPU and memory readings can describe its Linux virtual machine. The process list and disk rows can describe only the container. The report isn't a measure of the container's own resource limits.

```sh
make test        # Python 3 tests
make check       # Also checks Bash syntax and runs ShellCheck
make test-linux  # All tests in Docker, with CPU and memory limits
```

- [Decisions](docs/decisions.md)
- [Test results](docs/verification.md)
