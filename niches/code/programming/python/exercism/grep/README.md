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
- All 25 [upstream tests](https://github.com/exercism/python/blob/6105f6d9d3ef66ce3d5c8f529d2882af3d76b706/exercises/practice/grep/grep_test.py) pass at the pinned source version. Four local tests also pass on Python 3.12.10.
- I compared all 32 flag combinations with native `grep -F`, using three ASCII patterns. All 96 comparisons matched. Unknown flags raise `ValueError`, and file errors reach the caller.
- Review choice: preserve each line's spaces and original case in output. Case-insensitive matching uses `casefold()`. The native comparison covers the saved ASCII examples, not every Unicode rule or grep feature.
- A useful later extension would be a command that streams matches to stdout. I want that extra work to answer a real large-file question.

```bash
cd niches/code/programming/python/exercism/grep
python3 -m unittest discover -p 'test_*.py' -v
```

The native comparison test needs `grep` on PATH. The solution uses only Python's standard library.
