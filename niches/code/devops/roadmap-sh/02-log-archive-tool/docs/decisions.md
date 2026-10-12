# Archive notes

- **Started with the archive tools already in Python (2026-10-11)**
  - A shell script could call `tar`, but Python's built-in tools also handle paths and temporary files without extra commands or packages.
  - Keep the original logs. Removing or rotating them isn't needed for this tool.

- **Kept archives separate from logs (2026-10-11)**
  - An archive inside the log folder could include earlier archives or its own unfinished file.
  - Require the archive folder to be outside the log folder, including when a path uses a link.
  - Include the UTC date and time in each filename, with a short unique ending so repeated runs don't replace each other.

- **Saved the archive before recording it (2026-10-11)**
  - Write to a temporary file first. Give the finished file its final name without replacing an existing archive.
  - Used a hard link for that final step. A filesystem without hard-link support will return an error, keeping the original logs untouched.
  - Record the successful archive afterward. If that entry fails, keep the archive and report where it was saved.
  - Python's [archive tools](https://docs.python.org/3.11/library/tarfile.html) and [temporary files](https://docs.python.org/3.11/library/tempfile.html) cover the file work without another library.

- **Checked Mac paths as they actually resolve (2026-10-11)**
  - The first test run had five passes and one failure. On macOS, `/var` resolves to `/private/var`, so one path comparison was wrong.
  - Fixed the test to resolve its temporary folder too. The script already handled that path correctly.

- **Kept saved logs out of Git (2026-10-11)**
  - Review showed that the default output folder could be added to the repository.
  - Added two ignore paths for runs from the lab folder or repository root. Other labs and their files keep their existing rules.
  - Used cron for the scheduling example. A new scheduler or automatic setup wasn't needed.

## Checks, 2026-10-11

- All six tests passed on macOS with Python 3.12.10 and BSD tar 3.5.3, and on Debian 12 with Python 3.11.2 and GNU tar 1.34.
- The tests open a real archive with `tar`, check repeat runs and path errors, and test cleanup after write failures.
- Linux tests used the existing Docker image with no network access, a read-only source folder, and temporary output. No system logs were read or changed.
- [GitHub Actions](https://github.com/pradeeptathineni/labs/actions/runs/38195854988) passed at `1597696`.
- A direct command run saved a sample log. Restoring it with `tar` produced the same contents, and the original stayed in place.
