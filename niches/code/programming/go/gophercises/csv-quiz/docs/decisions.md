# Quiz notes

## 2026-10-12

- Chose `encoding/csv` over splitting strings. Questions can contain quoted commas.
  - Require two fields per row. Reject empty quizzes and blank questions or answers.
  - Load the rows into memory and trim answer whitespace.
- Pass input and output as `io.Reader` and `io.Writer`.
  - [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests/go-fundamentals/dependency-injection) uses this approach to check prompts without a real terminal.
  - Wrong answers advance immediately. EOF ends input. Read and write errors reach the caller.
- Four test groups passed on Go 1.27.1, covering eight CSV cases, scoring, stream failures, and command behavior. Race checks and `go vet` passed too.
- Three programming questions in `problems.csv`. The piped sample scored `3/3`.
- Timer work:
  - Start on Enter, with a configurable limit.
  - Interrupt blocked input and retain the score.
  - Check worker cleanup after timeout.
