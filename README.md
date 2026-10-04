# Labs

> Showcasing my problem-solving through code, design, research, analysis, and experimentation.

`labs` is a working collection of problems I solve, ideas I explore, and things I build across computing and beyond.

## Structure

The repository separates the work itself from the metadata and tooling that describe it:

- [`domains/`](domains/) — the actual body of work, organized by the primary kind of problem-solving being demonstrated.
- [`CATALOG.md`](CATALOG.md) — generated index of all individual labs.
- [`.meta/`](.meta/) — repository metadata, schemas, generated machine-readable indexes, and the tooling that maintains them.
- [`.github/`](.github/) — GitHub-specific automation.

## Lab domains

The repository was intentionally designed to be generic at the top-level, as problem-solving goes beyond code, such as research, design, teaching, and numerous other niches I have interest in and strive to keep practice within.

Consider the following concerns:

- How do I automate report generation for the operator's benefit?
- How do I scale report generation for the user population's benefit.
- How do I design reports for the end-user's benefit?
- How do I predict when a user will need to generate a report?
- How can I ensure efficient compute usage when reports are generated?

All mutually relevant, yet require problem-solving in different ways.

## Lab organization

A lab is organized as:

```text
labs/niches/<niche>/<domain>/<lab-source>/<lab-name>/<lab-content>
```

- `<niche>` — a problem-solving niche; i.e. `code`
- `<domain>` — a discipline; i.e. `devops`
- `<lab-source>` — an online source; i.e. `roadmap-sh`
  - or `created` for personally synthesized problems
  - or `generated` for AI-generated problems
  - or `other` for anything else
- `<lab-name>` — name of the lab, often numbered; i.e. `01-server-performance-stats`
- `<lab-content>`— content of the lab
  - Problem definition file; `README.md`
  - Lab metadata file; `lab.json`
  - Solution work when in progress or completed; i.e. `src/` or `solution/`

> [!IMPORTANT] This repository cites original sources when used for which all original labs/problems credit is markedly given. All contents of this repository are strictly for personal education, personal practice, and showcasing my personal abilities of critical thinking, problem-solving, and decision-making.

## Catalog

Repository-level metadata lives under [`.meta/`](.meta/):

- `.meta/catalog/sources.json` — manually maintained registry of external providers and source collections.
- `domains/**/lab.json` — manually maintained metadata local to each individual lab.
- `.meta/catalog/labs.json` — generated aggregate machine-readable catalog.
- `CATALOG.md` — generated human-readable catalog.

Regenerate the catalog:

```bash
python3 .meta/scripts/catalog.py
```

Validate metadata and confirm generated outputs are current:

```bash
python3 .meta/scripts/catalog.py --check
```
