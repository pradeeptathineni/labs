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

- I compared `echo`, `printf`, and an external greeting command. I chose Bash's built-in `printf` with a fixed format. Names should stay data, even when they contain `%` or backslashes.
- The first step handles a normal name and checks output, errors, and exit status with one test.
- This is an unfinished deliberate error drill. Its argument check also rejects an empty name. The broader argument tests have not run yet. I will check and correct that boundary next.

```bash
python3 -m unittest discover -s niches/code/programming/bash/exercism/error-handling -p 'test_*.py' -v
```
