# Bash Error Handling

## Exercise definition

[Exercism Error Handling](https://exercism.org/tracks/bash/exercises/error-handling)

Handle argument counts, quoting, and failure exit codes.

## Solution

From this lab folder:

```bash
./src/error_handling.sh 'Alice and Bob'
python3 -m unittest discover -s tests -v
BASH_UNDER_TEST=/usr/local/bin/bash python3 -m unittest discover -s tests -v
shellcheck src/error_handling.sh
```

- Exactly one argument prints `Hello, <name>` and exits 0, including an empty name.
- Other argument counts print usage on stderr and exit 1.
- `BASH_UNDER_TEST` selects another Bash installation. The tests otherwise use `bash` on PATH.

[Decisions and checks](docs/decisions.md)
