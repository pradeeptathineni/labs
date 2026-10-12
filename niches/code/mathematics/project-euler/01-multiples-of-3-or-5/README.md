# Multiples of 3 or 5

Source: [Project Euler, problem 1](https://projecteuler.net/problem=1)

## Exercise Definition

Add the positive numbers below 1000 that are divisible by 3 or 5. Keep numbers divisible by both in the sum only once.

## Solution

### Decisions, 2026-10-12

- Start with the first problem in an ordered Project Euler collection under Mathematics.
- Link the original problem rather than copy its wording.
- Check each positive number below the limit. There are only 999 candidates for this problem, so a direct sum is enough.
- Use one function and one test file with Python's built-in tools. Avoid a command parser, a list of stored matches, and extra input rules the problem does not need.
- Use `or` for the two divisibility checks. Adding separate lists of multiples would count 15 and other shared multiples twice.
- Keep the upper limit out of the sum. A small case where the limit is divisible by 3 makes that choice easy to check.

### Run from this lab folder

```bash
# Check the small cases and the default answer
python3 -m unittest test_multiples -v

# Print the answer for the original problem
python3 multiples.py
```

The command prints `233168`. `sum_multiples(limit)` also accepts an integer limit for the smaller checks.

### A separate calculation

- Multiples of 3 below 1000 run from 3 to 999. There are 333 terms, with sum `3 * 333 * 334 / 2 = 166833`.
- Multiples of 5 run from 5 to 995. There are 199 terms, with sum `5 * 199 * 200 / 2 = 99500`.
- Multiples of 15 occur in both sums. There are 66 terms through 990, with sum `15 * 66 * 67 / 2 = 33165`.
- Subtract that shared sum once: `166833 + 99500 - 33165 = 233168`.
- This calculation checks the result without using the loop from the solution.

### Checks, 2026-10-12

- Three tests passed on macOS with Python 3.12.10. One file covers the small example, empty sums, excluded upper limits, shared multiples, and the full answer.
- Running `python3 multiples.py` printed `233168`. The separate arithmetic calculation gave the same result.
- The first test launch failed because the test file had not been created at the intended path. Corrected the path and ran the three checks.
- The function returns the sum and keeps no list of matching numbers. The direct command only prints the answer for the original limit.
- Added the existing test command to both GitHub workflows so it runs before the site can update.
- The loop is enough for 1000. A much larger limit would be a reason to replace the scan with the arithmetic calculation.
