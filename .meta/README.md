# Repository metadata

The schemas, source registry, generated views, and maintenance commands live here. Each lab keeps its own facts beside its work. The path supplies niche, domain, optional subdomain, any collection groupings, collection, and slug; the registered `source.provider` supplies provenance independently.

Install the generic dependency with `python3 -m pip install -r .meta/requirements.txt`. Importers also need `python3 -m pip install -r .meta/importers/requirements.txt`.

For a normal lab session, choose an existing lab and explicitly mark it `in-progress`. Add your work and reasoning under its Solution or link to your implementation. Mark it `complete` when you consider the attempt finished; editing files alone never changes status. Stage the intended files, commit, then push. The hook records content changes and refreshes the catalog; relevant pushes to main update the [web catalog](https://pradeeptathineni.github.io/labs/).

Keep upstream snapshots under `source/` separate from your work. Edit lab and collection metadata through the commands below; generated catalogs are outputs. The atlas lists options to adopt, while the catalog lists actual labs. [Site preview and publishing](site/README.md) are separate from doing a lab.

## Create and edit

A write with flags needs `--yes`. `--dry-run` previews without writing or prompting. `--interactive` asks for every field and still ends with `Write these changes? [y/N]`; blank keeps the shown value and `-` clears an optional value.

```bash
python3 .meta/scripts/lab_init.py code devops my-projects "Inspect a deployment" --type exercise --skill deployment --yes
python3 .meta/scripts/lab_init.py code cloud my-projects "Inspect failover" --subdomain aws --yes
python3 .meta/scripts/lab_init.py study systems course-abc "Problem set 1" --subdomain distributed --group mit --yes
python3 .meta/scripts/lab_init.py --interactive
python3 .meta/scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats --status in-progress --yes
python3 .meta/scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats --interactive
python3 .meta/scripts/source_meta.py view roadmap-sh
python3 .meta/scripts/source_meta.py create my-source --type external --name "My source" --url https://example.com --reuse-policy review --yes
python3 .meta/scripts/source_meta.py update my-source --notes "Review each item before copying." --yes
python3 .meta/scripts/source_meta.py update my-source --interactive
```

The six lab types are `exercise`, `challenge`, `problem-set`, `question-bank`, `project`, and `experiment`. `exercise` is the default. Status and dates live under `tracking`; entering progress or completion records the first date if unknown, while reopening keeps that history. Dates can be corrected explicitly. Content edits never change status.

Use repeated `--tool` flags when creating or editing a lab; `--clear-tools` removes local tools. Collection tools still apply. Skills describe competencies, tools name technologies, and goals describe intentions.

`--subdomain` adds the optional subject level immediately after the domain. Repeat `--group` for provider or collection groupings between that subject and the final collection. Interactive mode accepts the groupings as a slash-separated path. These examples show valid layouts; they are not imported course assignments.

An optional `collection.json` can name a collection, link its source with `source_url`, mark `has_subdomain: true`, and set `ordered: true`. The initializer records `has_subdomain` automatically when `--subdomain` is used, including it in the preview before writing. Without that declaration, the domain is the whole subject and all intermediate folders are collection groupings. The same domain/subdomain boundary must be used consistently across niches. A directory cannot both contain labs as a collection and contain other collections.

Only an explicitly ordered collection interprets a numeric folder prefix as order. The initializer appends after the highest existing number and leaves gaps alone; creating a descriptor never overwrites a collection README. Names and hierarchy stay out of individual `lab.json` files.

## Record staged content

Enable the repository's pre-commit hook once per checkout:

```bash
git config core.hooksPath .githooks
```

Stage the lab content you want to record and commit it. The hook runs `lab_sync.py` against the staged Git snapshot, then stages any changed `lab.json`, `CATALOG.md`, and `.meta/catalog/labs.json` in the same commit:

```bash
git add niches/code/devops/roadmap-sh/01-server-performance-stats
git commit -m "feat(labs): record server performance work"
```

The hook runs at commit time, not on each edit. It refuses unstaged lab/catalog inputs or hand-edited generated views when they could leak into a commit. A structure-only commit does not change lab content dates. To sync manually or verify without writing:

```bash
python3 .meta/scripts/lab_sync.py --yes
python3 .meta/scripts/lab_sync.py --check
python3 .meta/scripts/catalog.py --check
```

`lab_sync.py` also accepts one or more lab paths. Its check mode is read-only. Untracked files enter the snapshot only after `git add`. A changed content snapshot updates `tracking.dates.updated`, which is a recording date, not time spent working; status and progress dates remain separate. The root `lab.json` is excluded from its own hash; nested fixtures, links, executable bits, and staged deletions count.

Run the small suite with `python3 -m unittest discover -s .meta/tests`. Import commands and source-specific limits are in [the importer guide](importers/README.md).

## Choose future practice

`.meta/catalog/atlas.json` is the editable plan; `sources.json` owns provider and reuse facts. Proposed paths create no directories. Use the atlas to select a meaningful unit, review its exact source permissions and environment requirements, then adopt it deliberately. Current adoption is calculated from lab metadata, never from the plan's priority.

```bash
python3 .meta/scripts/atlas.py --list --priority next
python3 .meta/scripts/atlas.py
python3 .meta/scripts/atlas.py --check
python3 .meta/scripts/catalog.py
```

Catalog generation refreshes all tracked views. `catalog.py --check` and `atlas.py --check` are offline and read-only. An opportunity's checked date changes only when that review actually happens again. An unknown personal goal remains valid and displays its slug.
