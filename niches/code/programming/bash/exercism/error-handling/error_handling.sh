#!/usr/bin/env bash

# error-handling/error_handling.sh - Greet one command-line argument
# Usage: ./error_handling.sh <person>

# Count arguments instead of treating an empty name as missing
if [[ $# -ne 1 ]]; then
    printf '%s\n' 'Usage: error_handling.sh <person>' >&2
    exit 1
fi

# Print the name as data, including spaces and format symbols
printf 'Hello, %s\n' "$1"
