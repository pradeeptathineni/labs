# Grep in Python

Source: [Exercism](https://exercism.org/tracks/python/exercises/grep)

## Problem

Implement a fixed-string file search with composable flags and deterministic output.

Follow the linked exercise for its requirements. The checks below define what I want to verify in my attempt; extensions are my additions.

## Before starting

Python 3 and its built-in `unittest` runner are enough. The upstream tests also use `unittest`.

## Checks

- Run the source tests for multiple files, line numbers, filename-only output, case folding, inversion, and whole-line matching.
- Check combinations of flags and preserve source file order and line order.
- Explain how fixed-string matching differs from regex matching; record tests and Python version.

## Solution

- Whole-file reads, regex, or line-by-line literal search? I chose literal search and line iteration. The exercise asks for fixed text, and large unmatched files need not stay in memory.
- [Python's iterator guidance](https://docs.python.org/3/howto/functional.html#iterators) supports processing file lines as they arrive. The required string result still takes space for all returned matches.
- First step: preserve spaces, file order, and filename prefixes. One real-file test passed before adding flags.
- The flag draft included a deliberate drill: filename-only output skipped inversion. All 25 upstream tests passed anyway. A local `-l -v` check caught the wrong file being returned.
- I moved inversion ahead of both output modes. The fix is one condition change, and the local check now passes. Upstream coverage is useful, but it did not cover that interaction.
- A useful later extension would be a command that streams matches to stdout. I want that extra work to answer a real large-file question.

```bash
cd niches/code/programming/python/exercism/grep
python3 -m unittest discover -p 'test_*.py' -v
```
