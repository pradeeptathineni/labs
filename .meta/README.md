# Repository Metadata

Machine-readable lab metadata and the small tools that maintain it live here.

- [`catalog/`](catalog/) — source registry, JSON Schemas, and generated lab index.
- [`scripts/`](scripts/) — generic lab creation, metadata, source, sync, and catalog tools.
- [`importers/`](importers/) — only small scripts with useful knowledge of one source format.
- [`tests/`](tests/) — standard-library tests for the generic rules and tracking behavior.
- [`requirements.txt`](requirements.txt) — the one runtime dependency: `jsonschema`.

The hierarchy has exactly two shapes:

```text
niches/<niche>/<domain>/<collection>/<lab>/
niches/<niche>/<domain>/<subdomain>/<collection>/<lab>/
```

Hierarchy is for browsing. The source provider belongs in `lab.json` and points to `.meta/catalog/sources.json`.

## Usage

Install dependencies:

```bash
python3 -m pip install -r .meta/requirements.txt
```

Create interactively, or pass values for automation:

```bash
python3 .meta/scripts/lab_init.py --interactive
python3 .meta/scripts/lab_init.py code software devroadmaps "REST API with Auth" --subdomain backend --source devroadmaps --item-id backend-rest-api-with-auth --source-url https://github.com/rudra496/devroadmaps/blob/master/js/project-ideas.js --kind project --difficulty beginner --skill api-design --yes
```

View or update a lab. Blank interactive inputs preserve current values; use `-` to clear optional difficulty or all skills:

```bash
python3 .meta/scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats
python3 .meta/scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats --status in-progress --add-skill process-management
python3 .meta/scripts/lab_meta.py --interactive
```

Create/view/update source records without free-form schema drift:

```bash
python3 .meta/scripts/source_meta.py create --interactive
python3 .meta/scripts/source_meta.py view roadmap-sh
python3 .meta/scripts/source_meta.py update roadmap-sh --reuse-policy link-only
```

Synchronize actual lab content and check generated catalogs:

```bash
python3 .meta/scripts/lab_sync.py
python3 .meta/scripts/lab_sync.py --check
python3 .meta/scripts/catalog.py
python3 .meta/scripts/catalog.py --check
python3 -m unittest discover -s .meta/tests
```

Only interactive runs ask for a final preview confirmation. Flag-driven commands do not prompt; `--yes` is available when an interactive write should be confirmed explicitly.
