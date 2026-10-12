# CSV Quiz

Source: [Gophercises Quiz Game](https://github.com/gophercises/quiz/blob/82fe91a9fa4711f2c3f751fd66b2b94fd8894d0e/README.md)

## Problem

Build the quiz in the source's two parts: an untimed CSV command, then a timer that can stop while waiting for an answer.

## Solution

- Split CSV strings or use `encoding/csv`? The source warns that questions can contain commas. I chose the standard CSV reader and two fields per row.
- Start with a small parser. Reject empty quizzes, wrong column counts, and empty questions or answers. Trim answer whitespace.
- The parser's eight sample cases passed first. I then added input, scoring, and a custom CSV path.
- I used `io.Reader` and `io.Writer` so tests can check the actual prompts and score. [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests/go-fundamentals/dependency-injection) shows this simple way to pass input and output in.
- Wrong answers move straight to the next question. Spaces around answers are ignored. EOF stops input, and unanswered questions count as wrong in the total. Broken reads and writes return errors.
- The sample CSV contains three local programming questions.
- Today's stopping point is Part 1. Part 2's start prompt, timer, and interrupted-input checks stay unfinished.

```bash
cd niches/code/programming/go/gophercises/csv-quiz
go test ./...
go test -race ./...
go vet ./...
printf 'encoding/csv\nstdout\n1\n' | go run .
go run . -csv problems.csv
```

- The sample run reports `Correct: 3/3`. Four test groups cover CSV parsing, scoring, stream failures, and command behavior on Go 1.27.1.
- This small quiz loads its CSV into memory and reads one answer per line. There is no time limit yet. The lab remains in progress.
- Next: add the start prompt and a configurable timer. Check that timeout stops waiting for input, preserves the score, and does not leave a blocked worker behind. Do not add shuffle or other bonus features before that part works.
