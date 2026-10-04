# Repository metadata

The schemas, source registry, generated views, and maintenance commands live here. Each lab keeps its own facts beside its work. The path supplies niche, domain, optional group, collection, and slug; the registered `source.provider` supplies provenance independently.

Install the generic dependency with `python3 -m pip install -r .meta/requirements.txt`. Importers also need `python3 -m pip install -r .meta/importers/requirements.txt`.

## Create and edit

A write with flags needs `--yes`. `--dry-run` previews without writing or prompting. `--interactive` asks for every field and still ends with `Write these changes? [y/N]`; blank keeps the shown value and `-` clears an optional value.

```bash
python3 .meta/scripts/lab_init.py code devops my-projects "Inspect a deployment" --type exercise --skill deployment --yes
python3 .meta/scripts/lab_init.py --interactive
python3 .meta/scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats --status in-progress --yes
python3 .meta/scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats --interactive
python3 .meta/scripts/source_meta.py view roadmap-sh
python3 .meta/scripts/source_meta.py create my-source --type external --name "My source" --url https://example.com --reuse-policy review --yes
python3 .meta/scripts/source_meta.py update my-source --notes "Review each item before copying." --yes
python3 .meta/scripts/source_meta.py update my-source --interactive
```

The six lab types are `exercise`, `challenge`, `problem-set`, `question-bank`, `project`, and `experiment`. `exercise` is the default. Status and dates live under `tracking`; entering progress or completion records the first date if unknown, while reopening keeps that history. Dates can be corrected explicitly. Content edits never change status.

An optional `collection.json` can name a collection and set `"ordered": true`. Only an explicitly ordered collection interprets a numeric folder prefix as order. The initializer appends after the highest existing number and leaves gaps alone; creating a descriptor never overwrites a collection README.

## Record staged content

Stage the lab content you want to record, then write the fingerprint and catalog from the Git index snapshot:

```bash
git add niches/code/devops/roadmap-sh/01-server-performance-stats
python3 .meta/scripts/lab_sync.py --yes
git add niches/code/devops/roadmap-sh/01-server-performance-stats/lab.json CATALOG.md .meta/catalog/labs.json
python3 .meta/scripts/lab_sync.py --check
python3 .meta/scripts/catalog.py --check
```

`lab_sync.py` also accepts one or more lab paths. Its check mode is read-only. Unstaged edits to tracked lab content are reported so I can stage the intended bytes. Untracked files enter the snapshot only after `git add`. A changed snapshot updates `tracking.dates.updated`, which is a recording date, not time spent working. The root `lab.json` is excluded from its own hash; nested fixtures, links, executable bits, and staged deletions count.

Run the small suite with `python3 -m unittest discover -s .meta/tests`. Import commands and source-specific limits are in [the importer guide](importers/README.md).
