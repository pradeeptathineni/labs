# Multiples of 3 or 5

Source: [Project Euler, problem 1](https://projecteuler.net/problem=1)

## Exercise Definition

Add the positive numbers below 1000 that are divisible by 3 or 5. Keep numbers divisible by both in the sum only once.

## Solution

### Decisions, 2026-10-12

- Start with the first problem in an ordered Project Euler collection under Mathematics.
- Link the original problem rather than copy its wording. The solution and reasoning here are original work.
- Check each positive number below the limit. There are only 999 candidates for this problem, so a direct sum is enough.
- Use one function and one test file with Python's built-in tools. Avoid a command parser, a list of stored matches, and extra input rules the problem does not need.
- Use `or` for the two divisibility checks. Adding separate lists of multiples would count 15 and other shared multiples twice.
- Keep the upper limit out of the sum. A small case where the limit is divisible by 3 makes that choice easy to check.
