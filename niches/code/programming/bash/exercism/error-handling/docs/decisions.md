# Greeting notes

## 2026-10-12

- Chose the built-in `printf` over `echo`.
  - A fixed format keeps spaces, newlines, Unicode, leading dashes, and format symbols intact.
  - [Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls#printf_.22.24foo.22) covers the mistake of using input as the format string.
- Check argument count, not whether the name has text.
  - The deliberate error drill rejected an empty name. The first normal-name test missed it.
  - A broader check caught it. Removed the value check: one empty argument is still one argument.
- Usage goes to stderr with status 1. The greeting goes to stdout with status 0.
- Local checks passed for nine inputs on Bash 3.2.57 and 5.3.3. ShellCheck passed.
- All five upstream Bats tests passed at `a043c6997769640440cdbb9356800e67392cf8b9`, using Bats 1.14.0 with skipped cases enabled.
