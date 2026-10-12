# Bash Error Handling

Source: [Exercism](https://exercism.org/tracks/bash/exercises/error-handling)

## Problem

Handle command-line argument counts, quoting, and failure exit codes in a Bash script.

Follow the linked exercise for its requirements. The checks below define what I want to verify in my attempt; extensions are my additions.

## Before starting

Bash and the track’s documented Bats runner for a local attempt, or an Exercism account. Use the linked track files for exact expected output and tests; no test or starter files are copied here.

## Checks

- Check zero, one, and multiple arguments; distinguish an empty argument from no argument.
- Test a name containing spaces and capture both printed output and exit status.
- Run the upstream tests and record the Bash version; explain the boundary checks used.

## Solution

- `echo` or `printf`? I chose Bash's built-in `printf` with a fixed format. [Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls#printf_.22.24foo.22) explains why input should not become the format string.
- The first step handles a normal name and checks output, errors, and exit status with one test.
- The first local draft included a deliberate error drill: its argument check rejected an empty name. Only the normal-name test had run.
- The broader check caught the planted empty-name error. One empty argument is still one argument. I removed the value check and kept the count check.
- I put usage errors on stderr and return status 1. A valid name returns status 0 and only the greeting on stdout.
- Local checks cover nine inputs on Bash 3.2.57 and 5.3.3. All five upstream Bats tests passed at `a043c6997769640440cdbb9356800e67392cf8b9`, using Bats 1.14.0 with skipped cases enabled. ShellCheck passed too.
- I also tried names with spaces, newlines, Unicode, a leading dash, and format symbols. This small command should preserve them exactly. No extra flags or greeting library seemed useful.

```bash
cd niches/code/programming/bash/exercism/error-handling
./error_handling.sh 'Alice and Bob'
python3 -m unittest discover -p 'test_*.py' -v
BASH_UNDER_TEST=/usr/local/bin/bash python3 -m unittest discover -p 'test_*.py' -v
shellcheck error_handling.sh
```

The second test command needs that Bash path. Set it to the Bash installation being checked.
