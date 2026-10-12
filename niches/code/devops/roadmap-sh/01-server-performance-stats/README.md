# Server Performance Stats

## Exercise definition

[Server Performance Stats on roadmap.sh](https://roadmap.sh/projects/server-stats)

## Solution

From this lab folder, on Linux with Bash, procps, GNU coreutils, and `awk`:

```sh
./src/server-stats.sh
./src/server-stats.sh --interval 2
./src/server-stats.sh --help
make test
make check
make test-linux
```

- CPU is sampled over one second by default. `--interval` accepts whole seconds from 1 to 60.
- Reports memory, disk rows, and the five busiest processes by CPU and memory. No root access or service needed.
- Invalid arguments or failed commands stop the script before printing a partial report.
- Help works on macOS. The report needs Linux.
- Docker can report VM-wide CPU and memory alongside container-only processes and disks.

[Decisions](docs/decisions.md) · [Readings and test results](docs/verification.md)

## Takeaways

## Applications
