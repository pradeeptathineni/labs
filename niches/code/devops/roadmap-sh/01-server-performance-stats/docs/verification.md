# Verification

Observed on 2026-10-11. The reviewed implementation is
[`9984e76`](https://github.com/pradeeptathineni/labs/commit/9984e76).
Later commits refine the CI execution environment and document completion.

## What passed

| Check | Result | What it establishes |
| --- | --- | --- |
| Bash syntax and ShellCheck 0.11.0 | Passed | Shell syntax and static lint |
| macOS lab suite | 12 passed, 1 Linux test skipped | Fixture interpretation and failures, not live Linux collection |
| Debian Linux lab suite | 13 passed, no skips | Fixtures plus actual collection and a known workload |
| Repository lifecycle suite | 20 passed | Existing metadata, catalog, hook, import, and publication behavior |
| Diff and comment review | Completed by the implementing agent | Same-context review, not independent review |

The fixtures distinguish since-boot CPU from the recent sample, exercise
reordered CPU columns and invalid counters, and verify available-memory
arithmetic including free greater than available. They check a 20,000-row
process stream, fewer than five processes, missing tools, unsupported hosts,
bad arguments, and collector failures without partial output.

The live test allocates and touches 32 MiB, spins briefly, and checks that its
actual PID appears in both top-five lists with positive CPU use and the
expected resident memory. It always terminates the worker. The worker also
has its own timeout. This workload is bounded; it is not a benchmark.

## Tested environment

- Host: Intel macOS, Bash 5.3.3, Python 3.12.10, Docker Server 29.8.0.
- Linux: Debian 12 bookworm, kernel `7.0.12-linuxkit`, Bash 5.2.15,
  Python 3.11.2, procps-ng 4.0.2, GNU coreutils 9.1.
- Existing image: `node:24-bookworm`, image ID
  `sha256:367d9464824bc2fc1c5303b522c01df3b7cf33afc63785f88449798566b5c254`.
- Reproducible image reference:
  `node@sha256:6dac556d980b7f0e5498d08f08cee0ca67798b4ad6c23964a9214920e67758d0`.

The cached image already had the Linux utilities and Python. No packages,
cloud resources, or host services were installed for this lab. The stopped
home-lab VM remained stopped. Disposable containers were removed after use.

## Reproduce the checks

Inside this lab directory:

```sh
make check
```

`make test` needs Python 3. `make check` also needs Bash and ShellCheck.
On macOS the real-collector test explicitly skips. For the complete Linux
suite, run `make test-linux` from this lab directory with Docker. The target
owns this same command for local use and CI:

```sh
docker run --rm --network none --read-only \
  --cap-drop ALL --security-opt no-new-privileges \
  --pids-limit 64 --memory 256m --cpus 1 --user 65534:65534 \
  --tmpfs /tmp:rw,nosuid,nodev,exec,size=16m \
  --mount "type=bind,src=$PWD,dst=/lab,readonly" \
  --workdir /lab --entrypoint python3 \
  node@sha256:6dac556d980b7f0e5498d08f08cee0ca67798b4ad6c23964a9214920e67758d0 \
  -B -m unittest discover -s tests -v
```

Only the temporary fixture mount permits execution. Source is read-only,
network is disabled, privileges are dropped, and CPU, memory, and processes
are bounded. A missing local image will require a download before execution.

Both the metadata and Pages workflows run Bash syntax and `make test-linux`
before accepting or publishing a snapshot. The workflow checks name
this solved lab explicitly; other lab solutions do not gain CI automatically.

## Findings that changed the result

1. Live Linux showed that an overlay and backing device can both appear in
   `df`. Removed the aggregate total to avoid double counting storage.
2. Source review showed that kernel reserves can make available memory lower
   than free. Corrected the validation and added a regression test.
3. The first full Docker fixture run failed because `/tmp` was not executable.
   Corrected that disposable test configuration. The real-collector test had
   passed during that failed suite; the whole suite then passed after correction.
4. [Hosted CI](https://github.com/pradeeptathineni/labs/actions/runs/38171060367)
   failed the memory-workload assertion: five runner services had larger
   resident sizes than the worker. This was a valid ranking on a busy host.
   Publication was blocked. Moved CI to the same bounded process namespace
   through `make test-linux`, with the tested image pinned by digest.

The [decision record](decisions.md) preserves the original choices and revisions.

## Limits

The readings are collected in sequence and are not an atomic snapshot. CPU
sampling and lifetime process CPU measure different periods. A short-lived
process can disappear between rankings, and the collectors themselves can
appear in small process lists.

Container CPU and memory counters can describe the Docker VM. Process and
filesystem views follow their namespaces and mounts. Memory percentages use
the visible system total, not a cgroup limit. Filesystem rows can overlap,
and shared process pages mean resident sizes cannot be summed into system use.

The workload test expects an otherwise quiet process namespace. A busy shared
server can legitimately have five processes larger or busier than the test
worker. Test in a disposable container in that situation. No bare-metal,
every-distribution, BusyBox, or production-readiness claim is made.

No independent reviewer or human usability study was part of this attempt.
