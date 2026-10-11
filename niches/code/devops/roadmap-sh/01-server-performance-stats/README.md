# Server Performance Stats

Source: [roadmap.sh](https://roadmap.sh/projects/server-stats)

## Exercise Definition

Read the [original exercise definition](https://roadmap.sh/projects/server-stats).

## Solution

Run on Linux with Bash, procps (`vmstat`, `free`, `ps`), GNU coreutils (`df`),
and `awk`. No root privileges or background service are required.

```sh
./server-stats.sh
./server-stats.sh --interval 2
./server-stats.sh --help
```

CPU sampling takes one second by default. `--interval` accepts an integer
between 1 and 60 seconds. Invalid inputs and collection failures return a
nonzero exit code. A failed collection prints an error instead of a partial
report. The help command also works on macOS, but collection requires Linux.

CPU non-idle time includes I/O wait and stolen time. Process CPU percentages
are lifetime averages, so they need not match the system sampling window.
Memory used is total minus available, which accounts for reclaimable cache.
Process memory is resident size, not an allocation limit.

```sh
make test   # Python 3 standard-library tests
make check  # Also requires ShellCheck; checks Bash syntax and lint
```

The tests exercise controlled collector output. Live Linux verification is
still in progress. Linux containers can expose VM-wide CPU and memory counters
alongside namespaced processes and filesystems; this is not a container-usage
report.

The [decision record](docs/decisions.md) explains the scope and metric choices.
