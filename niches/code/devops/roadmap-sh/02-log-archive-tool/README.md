# Log Archive Tool

## Exercise definition

[Log Archive Tool on roadmap.sh](https://roadmap.sh/projects/log-archive-tool)

## Solution

- Work is in progress. The tool will take a log folder, save a dated `.tar.gz` file, and record the date and time.

## Decisions

1. **Started with the archive tools already in Python (2026-10-11)**
   - A shell script could call `tar`, but Python's built-in tools also handle paths and temporary files without extra commands or packages.
   - Keep the script small and keep the tests in one file. The commands, choices, and results fit in this README.
   - Keep the original logs. Removing or rotating them isn't needed for this tool.

1. **Kept archives separate from logs (2026-10-11)**
   - An archive inside the log folder could include earlier archives or its own unfinished file.
   - Require the archive folder to be outside the log folder, including when a path uses a link.
   - Include the UTC date and time in each filename, with a short unique ending so repeated runs don't replace each other.
