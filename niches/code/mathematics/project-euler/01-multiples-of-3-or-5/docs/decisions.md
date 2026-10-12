# Multiples notes

## 2026-10-12

- A direct sum is enough for 999 candidates. Chose a scan over an arithmetic formula.
  - One function, without storing matching numbers or adding a command parser.
  - `or` counts numbers divisible by both 3 and 5 once.
  - Exclude the upper limit. The small checks include limits divisible by 3.
- Checked the answer separately with arithmetic:
  - Multiples of 3: 333 terms through 999. `3 * 333 * 334 / 2 = 166833`.
  - Multiples of 5: 199 terms through 995. `5 * 199 * 200 / 2 = 99500`.
  - Multiples of 15: 66 terms through 990. `15 * 66 * 67 / 2 = 33165`.
  - Subtract the shared sum once: `166833 + 99500 - 33165 = 233168`.
- The first test launch used the wrong file path. Corrected it, then all three tests passed on macOS with Python 3.12.10.
  - Small sums, empty sums, excluded limits, shared multiples, and the full answer.
  - The direct command printed `233168`, matching the arithmetic result.
- For a much larger limit, the arithmetic formula would avoid scanning every number.
