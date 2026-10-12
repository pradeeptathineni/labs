# Grep in Python

## Exercise definition

[Exercism Grep](https://exercism.org/tracks/python/exercises/grep)

Search files for fixed text, with line numbers, filename-only output, case folding, inversion, and whole-line matching.

## Solution

From this lab folder, with Python 3:

```bash
python3 src/grep.py -n -- 'def test_' tests/test_grep.py
python3 -m unittest discover -s tests -v
```

- `grep(pattern, flags, files)` returns the exercise's string result. `iter_matches()` yields matching rows.
- File order, line order, original case, and spaces are preserved.
- The CLI streams UTF-8 files and exits 0 for matches, 1 for no matches, or 2 for file, decoding, or argument errors.
- An early pipe close exits 1. Output written before a later file error stays visible.
- Literal matching, without regex, recursion, or stdin input.
- The native comparison test needs `grep` on PATH. No extra Python packages.

[Decisions and checks](docs/decisions.md)

## Takeaways

## Applications
