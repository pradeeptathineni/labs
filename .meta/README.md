# Repository metadata

The schemas, source registry, generated views, and maintenance commands live here. Each lab keeps its own facts beside its work. The path supplies niche, domain, optional subdomain, any collection groupings, collection, and slug; the registered `source.provider` supplies provenance independently.

Install the generic dependency with `python3 -m pip install -r .meta/requirements.txt`. Importers also need `python3 -m pip install -r .meta/importers/requirements.txt`.

For a normal lab session, choose an existing lab and explicitly mark it `in-progress`. Add your work and reasoning under its Solution or link to your implementation. Mark it `complete` when you consider the attempt finished; editing files alone never changes status. Stage the intended files, commit, then push. The hook records content changes and refreshes the catalog; relevant pushes to main update the [web catalog](https://pradeeptathineni.github.io/labs/).

Keep upstream snapshots under `source/` separate from your work. Edit lab and collection metadata through the commands below; generated catalogs are outputs. The atlas lists options to adopt, while the catalog lists actual labs. [Site preview and publishing](site/README.md) are separate from doing a lab.

## A lab from creation to publication

| Junction | Local files and catalog | Public site |
| --- | --- | --- |
| Research an atlas opportunity | A possible future unit; no lab is created | Appears in the linked practice atlas after publication |
| Create a lab | README and metadata are created; `not-started` displays as Planned | Unchanged until a successful main deployment |
| Mark `in-progress` | Status and first start date change; In progress lists the lab | Unchanged until a successful main deployment |
| Edit your work | Status stays as selected; the catalog discovers nonempty Solution notes when regenerated | Unchanged until a successful main deployment |
| Stage and commit | The hook records staged content, updates its recording date when content changes, and includes refreshed catalogs | Unchanged; a local commit is not a deployment |
| Mark `complete` and commit | Status and first completion date change; Completed lists the lab | Unchanged until a successful main deployment |
| Push `main` | GitHub receives the committed snapshot | Pages tests, validates, builds, and deploys; the previous successful snapshot remains available meanwhile |

Here is a normal session, with a new title you can change:

```bash
git config core.hooksPath .githooks  # once per checkout
python3 .meta/scripts/lab_init.py code devops my-projects "Inspect a deployment" --summary "Check a deployment and explain its behavior." --type exercise --skill deployment --yes
lab_dir=niches/code/devops/my-projects/inspect-a-deployment
python3 .meta/scripts/lab_meta.py "$lab_dir" --status in-progress --yes
# Do the work. Record your approach, results, failures, and checks under ## Solution.
git add "$lab_dir"
git commit -m "feat(labs): record deployment investigation"
python3 .meta/scripts/lab_meta.py "$lab_dir" --status complete --yes
git add "$lab_dir/lab.json"
git commit -m "feat(labs): complete deployment investigation"
git push origin main
```

Push after any intermediate commit if you want that stage public. Push only at the end if you want the public catalog to move straight to the finished snapshot. You do not need to build the site locally for ordinary lab work. A branch push does not publish; a pull request checks its snapshot, and merging relevant changes into main triggers publication. Rapid pushes may skip an older queued snapshot when main has newer site inputs.

Completion means I consider this attempt finished. It does not prove mastery or that checks passed. The commands warn when completing a lab without a Solution link, but allow that decision. A Solution link appears as soon as meaningful notes exist under `## Solution`, even while the lab is in progress, or when you set `--link solution=PATH`. A local link is relative to the repository root; remote links use an HTTP(S) URL. An empty heading, HTML comment, or example heading inside a code fence does not count as a solution.

Dates record the first known creation, start, completion, and latest committed content recording; they are calendar dates, not hours worked. A status-only edit does not change the content recording date. Reopening with `--status in-progress` keeps the first completion date; the current status decides where the lab appears. `paused` and `abandoned` also preserve dates. Correct dates explicitly when needed; a start or completion cannot precede creation, and a start cannot follow completion. Automatic dates use the command runner's local day; explicit date flags are available for backfilled work.

The [lifecycle smoke experiment](../niches/code/devops/workflow-checks/lab-lifecycle-smoke-test/README.md) records the actual publication checks for this workflow.

## Create and edit

A write with flags needs `--yes`. `--dry-run` previews without writing or prompting. `--interactive` asks for every field and still ends with `Write these changes? [y/N]`; blank keeps the shown value and `-` clears an optional value.

```bash
python3 .meta/scripts/lab_init.py code devops my-projects "Inspect a deployment" --summary "Check a deployment and explain its behavior." --type exercise --skill deployment --yes
python3 .meta/scripts/lab_init.py code cloud my-projects "Inspect failover" --summary "Compare failover behavior across failure scenarios." --subdomain aws --yes
python3 .meta/scripts/lab_init.py study systems course-abc "Problem set 1" --summary "Explain the concepts in the first problem set." --subdomain distributed --group mit --yes
python3 .meta/scripts/lab_init.py --interactive
python3 .meta/scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats --status in-progress --yes
python3 .meta/scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats --interactive
python3 .meta/scripts/source_meta.py view roadmap-sh
python3 .meta/scripts/source_meta.py create my-source --type external --name "My source" --url https://example.com --reuse-policy review --yes
python3 .meta/scripts/source_meta.py update my-source --notes "Review each item before copying." --yes
python3 .meta/scripts/source_meta.py update my-source --interactive
```

The six lab types are `exercise`, `challenge`, `problem-set`, `question-bank`, `project`, and `experiment`. `exercise` is the default. Status and dates live under `tracking`; entering progress or completion records the first date if unknown, while reopening keeps that history. Dates can be corrected explicitly. Content edits never change status.

Use repeated `--tool` flags when creating or editing a lab; `--clear-tools` removes local tools. Collection tools still apply. A short `summary` is required. Skills describe capabilities such as `orchestration` or `log-analysis`; tools name products, services, languages and platforms such as `kubernetes`, `awk` or `aws`. A tool name belongs only in tools, even when learning that tool is the point of the lab. Goals describe intentions. The same tag cannot be a skill in one lab and a tool in another; metadata validation catches that conflict. Keep tags specific enough to help browsing, and reuse existing names.

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

The hook runs at commit time, not on each edit. It refuses unstaged lab/catalog inputs, shared metadata scripts, hooks, or hand-edited generated views when they could leak into a relevant commit. Stage the intended inputs and retry; the guard preserves unstaged work. The hook may add generated files after your initial staging, so review the resulting commit with `git show HEAD`. A structure-only commit does not change lab content dates. To sync manually or verify without writing:

```bash
python3 .meta/scripts/lab_sync.py --yes
python3 .meta/scripts/lab_sync.py --check
python3 .meta/scripts/catalog.py --check
```

The generator keeps an ignored `.meta/build/catalog-generation.json` receipt of its last output. This lets the hook safely refresh catalogs that became stale after you added Solution notes, without treating them as hand edits. The receipt is local convenience state; canonical checks and release builds do not need it or change it. If it is missing and an edited view cannot be recognized, regenerate with `catalog.py` after preserving any manual text you meant to keep in a maintained document.

`lab_sync.py` also accepts one or more lab paths. Its check mode is read-only. Untracked files enter the snapshot only after `git add`. A changed content snapshot updates `tracking.dates.updated`, which is a recording date, not time spent working; status and progress dates remain separate. The root `lab.json` is excluded from its own hash; nested fixtures, links, executable bits, and staged deletions count.

If you bypass or have not installed the hook, stage your lab content, run `lab_sync.py --yes`, stage the changed metadata and generated views, then commit. CI rejects stale fingerprints or catalogs; it does not repair them. Stage only material you intend to publish: this repository is public, including lab notes and source files.

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
