# CSV Quiz

Source: [Gophercises Quiz Game](https://github.com/gophercises/quiz/blob/82fe91a9fa4711f2c3f751fd66b2b94fd8894d0e/README.md)

## Problem

Build the quiz in the source's two parts: an untimed CSV command, then a timer that can stop while waiting for an answer.

## Solution

- Split CSV strings or use `encoding/csv`? The source warns that questions can contain commas. I chose the standard CSV reader and two fields per row.
- Start with a small parser. Reject empty quizzes, wrong column counts, and empty questions or answers. Trim answer whitespace.
- The parser's eight sample cases pass on Go 1.27.1. There is no runnable quiz command yet. Input, scoring, and a custom CSV path are the next step.
- Today's stopping point is Part 1. Part 2's start prompt, timer, and interrupted-input checks stay unfinished.

```bash
cd niches/code/programming/go/gophercises/csv-quiz
go test ./...
```
