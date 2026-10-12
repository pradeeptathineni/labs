# Search notes

## 2026-10-12

- Chose line-by-line literal search over whole-file reads or regex.
  - The exercise asks for fixed text. Preserve spaces, file order, and filename prefixes.
  - [Python's iterator guidance](https://docs.python.org/3/howto/functional.html#iterators) covers processing lines as they arrive.
  - The required string result still retains all returned matches.
- Apply inversion before either output mode.
  - A deliberate drill skipped inversion for filename-only output. All 25 upstream tests passed.
  - A local `-l -v` check caught the wrong file. One condition change fixed it.
- Case-insensitive comparisons use `casefold()`. Output keeps the original text.
  - All 32 flag combinations matched native `grep -F` for three ASCII patterns: 96 comparisons.
  - That comparison does not cover every Unicode rule. A separate test checks Unicode case folding.
- Four local tests and all 25 [upstream tests](https://github.com/exercism/python/blob/6105f6d9d3ef66ce3d5c8f529d2882af3d76b706/exercises/practice/grep/grep_test.py) passed on Python 3.12.10.
  - Unknown flags raise `ValueError`. File errors reach the caller.
- Added a streaming command for log-processing scripts, rather than recursion or an index.
  - `iter_matches()` yields rows. `grep()` joins them for the exercise API. The CLI writes rows as they arrive.
  - Close a stopped iterator and handle a closed output pipe without a shutdown traceback.
    - [Python's broken-pipe guidance](https://docs.python.org/3/library/signal.html#note-on-sigpipe) covers the final flush trap.
  - Seven local tests passed after this addition, including command runs, invalid UTF-8, iterator cleanup, and a stopped pipe. All 25 upstream tests still passed.
- Compared allocations with 250,000 matching lines on Python 3.12.10.
  - Input: 9,250,000 bytes. Both paths produced 9,250,000 output characters.
  - Peak traced Python allocations:
    - String API: 30,806,028 bytes.
    - Streamed iteration: 23,092 bytes.
  - This measured Python allocations, not total process memory or speed. A single huge line still needs memory in the streaming path.
