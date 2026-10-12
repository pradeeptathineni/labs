#!/usr/bin/env python3

# grep/grep.py - Search files for fixed text

# Search in file order and return the required text result
def grep(pattern, flags, files):

    # Keep unfinished flag handling visible
    if flags:
        raise NotImplementedError("Flag handling is the next step.")

    # Read one line at a time and close each file after use
    matches = []
    for filename in files:
        with open(filename, encoding="utf-8") as source:
            for raw in source:
                line = raw.rstrip("\n")
                if pattern in line:
                    prefix = f"{filename}:" if len(files) > 1 else ""
                    matches.append(f"{prefix}{line}\n")

    # Join only matched output, rather than loading all input
    return "".join(matches)
