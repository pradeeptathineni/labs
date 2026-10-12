# CSV Quiz

## Exercise definition

[Gophercises Quiz Game](https://github.com/gophercises/quiz/blob/82fe91a9fa4711f2c3f751fd66b2b94fd8894d0e/README.md)

Build a CSV quiz, then add a timer that interrupts an unanswered question.

## Solution

From this lab folder:

```bash
go run ./src -csv problems.csv
printf 'encoding/csv\nstdout\n1\n' | go run ./src
go test -race ./...
go vet ./...
```

- Each CSV row contains a question and answer. Quoted commas work, and answer whitespace is ignored.
- One answer per line. EOF ends the quiz, with unanswered questions included in the total.
- The sample answers above print `Correct: 3/3`.
- No timer yet.

[Decisions](docs/decisions.md)
