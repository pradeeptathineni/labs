# Log Archive Tool

## Exercise definition

[Log Archive Tool on roadmap.sh](https://roadmap.sh/projects/log-archive-tool)

## Solution

- Use Python 3.9 or newer on macOS or Linux. No extra Python packages are needed.

```sh
./src/log-archive /path/to/logs
./src/log-archive /path/to/logs /path/to/saved-archives
./src/log-archive --help
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
python3 -m unittest discover -s tests -v
```

### Nightly archive

At 1 AM in the machine's local time, using installed paths:

```cron
0 1 * * * /path/to/python3 /path/to/log-archive /path/to/logs /path/to/saved-archives
```

- No schedule is installed by the script. Archive filenames still use UTC.

[Decisions and checks](docs/decisions.md)
