# Multiples of 3 or 5

## Exercise definition

[Project Euler, problem 1](https://projecteuler.net/problem=1)

Add the positive numbers below 1000 divisible by 3 or 5, counting shared multiples once.

## Solution

From this lab folder:

```bash
python3 src/multiples.py
python3 -m unittest discover -s tests -v
```

Prints `233168`. `sum_multiples(limit)` accepts an integer limit and excludes that upper limit.

[Choices and arithmetic check](docs/decisions.md)
