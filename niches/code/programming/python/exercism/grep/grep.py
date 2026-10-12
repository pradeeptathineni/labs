#!/usr/bin/env python3

# grep/grep.py - Search files for fixed text

# Search in file order and return the required text result
def grep(pattern, flags, files):

    # Read flags once and reject unsupported behavior
    options = set(flags.split())
    unknown = options - {"-n", "-l", "-i", "-v", "-x"}
    if unknown:
        raise ValueError(f"Unknown flags: {' '.join(sorted(unknown))}")

    # Fold both sides only when ignoring case
    needle = pattern.casefold() if "-i" in options else pattern

    # Read one line at a time and close each file after use
    matches = []
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
                    matches.append(f"{filename}\n")
                    break

                # Add file and line prefixes without changing the original text
                prefix = f"{filename}:" if len(files) > 1 else ""
                if "-n" in options:
                    prefix += f"{number}:"
                matches.append(f"{prefix}{line}\n")

    # Join only matched output, rather than loading all input
    return "".join(matches)
