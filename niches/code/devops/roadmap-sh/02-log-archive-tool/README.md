# Log Archive Tool

## Exercise definition

[Log Archive Tool on roadmap.sh](https://roadmap.sh/projects/log-archive-tool)

## Solution

- Use Python 3.9 or newer on macOS or Linux. No extra Python packages are needed.

```sh
./log-archive /path/to/logs
./log-archive /path/to/logs /path/to/saved-archives
./log-archive --help
```

- The default output folder is `archives` in the current folder. It must be outside the log folder.
- Git ignores that output when running from this lab folder or the repository root. Keep other archive folders outside the repository.
- Each archive is named `logs_archive_DATE_TIME_ID.tar.gz`, with UTC time and a short unique ending.
- The command prints the saved file's full path and appends its date, time, and filename to `archive.log` in the output folder.
- Original logs stay in place. Hidden files and subfolders are included, and links are saved as links.
- New archive files are readable only by their owner. Use an archive folder you control.
- The archive folder must allow hard links (two names for one file). This lets the finished file get its final name without replacing another archive.
- An error returns a nonzero exit code. Unfinished archive files are removed.
- If writing `archive.log` fails after the archive is saved, the error includes its path. The archive is kept, and the command still returns an error.
- Pause log writes for a consistent copy. Files are read one after another, so this is not a backup of one exact moment.

```sh
python3 -m unittest test_log_archive -v
```

- An existing cron setup can run it each night at 1 AM in the machine's local time. Replace these paths with the installed Python, script, logs, and archive folder.

```cron
0 1 * * * /path/to/python3 /path/to/log-archive /path/to/logs /path/to/saved-archives
```

- No schedule is installed by the script. Archive filenames still use UTC.

## Decisions

1. **Started with the archive tools already in Python (2026-10-11)**
   - A shell script could call `tar`, but Python's built-in tools also handle paths and temporary files without extra commands or packages.
   - Keep the script small and keep the tests in one file. The commands, choices, and results fit in this README.
   - Keep the original logs. Removing or rotating them isn't needed for this tool.

1. **Kept archives separate from logs (2026-10-11)**
   - An archive inside the log folder could include earlier archives or its own unfinished file.
   - Require the archive folder to be outside the log folder, including when a path uses a link.
   - Include the UTC date and time in each filename, with a short unique ending so repeated runs don't replace each other.

1. **Saved the archive before recording it (2026-10-11)**
   - Write to a temporary file first. Give the finished file its final name without replacing an existing archive.
   - Used a hard link for that final step. A filesystem without hard-link support will return an error, keeping the original logs untouched.
   - Record the successful archive afterward. If that entry fails, keep the archive and report where it was saved.
   - Python's [archive tools](https://docs.python.org/3.11/library/tarfile.html) and [temporary files](https://docs.python.org/3.11/library/tempfile.html) cover the file work without another library.

1. **Checked Mac paths as they actually resolve (2026-10-11)**
   - The first test run had five passes and one failure. On macOS, `/var` resolves to `/private/var`, so one path comparison was wrong.
   - Fixed the test to resolve its temporary folder too. The script already handled that path correctly.

1. **Kept saved logs out of Git (2026-10-11)**
   - Review showed that the default output folder could be added to the repository.
   - Added two ignore paths for runs from the lab folder or repository root. Other labs and their files keep their existing rules.
   - Used cron for the scheduling example. A new scheduler or automatic setup wasn't needed.

1. **Finished after checking the working command (2026-10-11)**
   - The Mac and Linux checks passed, and the public site showed the working version in progress after GitHub Actions passed.
   - Ran the executable directly and restored a sample log with `tar`. The restored file matched, and the original stayed in place.
   - Marked the lab complete. No extra files, features, or tests were needed.

## Checks

- All six tests passed on macOS with Python 3.12.10 and BSD tar 3.5.3, and on Debian 12 with Python 3.11.2 and GNU tar 1.34.
- The tests open a real archive with `tar`, check repeat runs and path errors, and test cleanup after write failures.
- Linux tests used the existing Docker image with no network access, a read-only source folder, and temporary output. No system logs were read or changed.
- Code and comments were reviewed during development. There was no separate reviewer.
- [GitHub Actions and deployment](https://github.com/pradeeptathineni/labs/actions/runs/38195854988) passed at `1597696`. The site's exact version and in-progress status were checked afterward.
