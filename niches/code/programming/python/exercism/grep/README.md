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

```bash
cd niches/code/programming/python/exercism/grep
python3 -m unittest discover -p 'test_*.py' -v
```

The native comparison test needs `grep` on PATH. The solution uses only Python's standard library.

## Extra work

- I chose a streaming command over recursion, regex, or a search index. It fits log-processing scripts and keeps this exercise small.
- `iter_matches()` yields rows. The original `grep()` still returns the string required by the exercise. The CLI writes each row as it arrives.
- The command returns 0 for matches, 1 for no matches, and 2 for file, decoding, or argument errors. Output already written before a later file error stays visible.
- An early pipe close returns 1 without a shutdown traceback. [Python's broken-pipe guidance](https://docs.python.org/3/library/signal.html#note-on-sigpipe) explains the final flush trap. The command also closes a stopped search.
- Seven local tests now pass, including early iterator close, real command runs, invalid UTF-8, a stopped pipe, and Unicode case folding. All 25 upstream tests still pass.
- I tried 250,000 matching lines, totaling 9,250,000 input bytes. Both paths produced the same 9,250,000 output characters. Peak traced Python allocations were 30,806,028 bytes for the required string API and 23,092 bytes for streamed iteration on Python 3.12.10.
- That is one local allocation check, not total process memory or a speed result. The string API must retain its answer. The streaming path uses space for the current line, so a single huge line still needs memory.
- Stopping here: useful as a UTF-8 file command, without recursion, stdin input, regex, or the rest of grep's options.

```bash
python3 grep.py -n -- 'def test_' test_grep.py
```
