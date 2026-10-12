#!/usr/bin/env python3

# src/grep.py - Search files for fixed text
# Usage: python3 src/grep.py [-n] [-l] [-i] [-v] [-x] -- pattern file...

# Use standard command-line parsing and close stopped searches
import argparse
import os
import sys
from contextlib import closing


# Yield matches in file order without keeping the full result
def iter_matches(pattern, flags, files):

    # Read flags once and reject unsupported behavior
    options = set(flags.split())
    unknown = options - {"-n", "-l", "-i", "-v", "-x"}
    if unknown:
        raise ValueError(f"Unknown flags: {' '.join(sorted(unknown))}")

    # Fold both sides only when ignoring case
    needle = pattern.casefold() if "-i" in options else pattern

    # Read one line at a time and close each file after use
    for filename in files:
        with open(filename, encoding="utf-8") as source:
            for number, raw in enumerate(source, start=1):
                line = raw.rstrip("\n")
                candidate = line.casefold() if "-i" in options else line
                matched = needle == candidate if "-x" in options else needle in candidate

                # Invert the match before choosing either output mode
                if "-v" in options:
                    matched = not matched
                if not matched:
                    continue

                # Return a matching filename only once
                if "-l" in options:
                    yield f"{filename}\n"
                    break

                # Add file and line prefixes without changing the original text
                prefix = f"{filename}:" if len(files) > 1 else ""
                if "-n" in options:
                    prefix += f"{number}:"
                yield f"{prefix}{line}\n"


# Preserve the exercise's string-returning interface
def grep(pattern, flags, files):
    return "".join(iter_matches(pattern, flags, files))


# Stream command output and report match, no-match, or error status
def main(argv=None):

    # Parse the exercise flags without building another parser
    parser = argparse.ArgumentParser(description="Search UTF-8 files for fixed text.")
    flag_help = {
        "-n": "show line numbers",
        "-l": "show matching filenames once",
        "-i": "ignore case",
        "-v": "select nonmatching lines",
        "-x": "match the whole line",
    }
    for flag, help_text in flag_help.items():
        parser.add_argument(flag, action="store_true", help=help_text)
    parser.add_argument("pattern")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args(argv)
    flags = " ".join(flag for flag in flag_help if getattr(args, flag[1:]))

    # Write matches as they arrive and close files if output stops
    found = False
    try:
        with closing(iter_matches(args.pattern, flags, args.files)) as rows:
            for row in rows:
                sys.stdout.write(row)
                found = True
        sys.stdout.flush()

    # Avoid a second flush error when a pipe consumer exits early
    except BrokenPipeError:
        target = os.open(os.devnull, os.O_WRONLY)
        try:
            os.dup2(target, sys.stdout.fileno())
        finally:
            os.close(target)
        return 1

    # Keep file and decoding errors separate from a clean no-match result
    except (OSError, UnicodeError) as error:
        print(f"grep: {error}", file=sys.stderr)
        return 2

    # Match the usual grep statuses for normal text input
    return 0 if found else 1


# Run the command only when called as a script
if __name__ == "__main__":
    raise SystemExit(main())
