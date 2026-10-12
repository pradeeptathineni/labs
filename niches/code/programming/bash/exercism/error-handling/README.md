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
