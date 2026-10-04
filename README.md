# Labs

`labs` is a working collection and showcase of problems/challenges I solve, practices/principles I employ, and ideas/curiosities I explore across different niches and domains.

A lab is synonymous with a problem, exercise, challenge, prompt, investigation, experiment, project, or case that tests my critical thinking, problem-solving, and decision-making.

## Structure

The actual work lives under [`niches/`](niches/), beside the generated [lab catalog](CATALOG.md). Repository, metadata, and catalog logic lives tucked away under [`.meta/`](.meta/).

The repository is intentionally broad at the top level. Code is one way to practice critical thinking; research, design, teaching, writing, and plenty of other areas that interest me have their own styles and requirements.

Consider a seemingly simple problem: report generation.

- How can I automate report generation for the operator's benefit?
- How can I scale report generation to serve a growing user population?
- How can I design reports for the end user's benefit?
- How can I predict when a user will need to generate a report?
- How can I maintain efficient compute usage for report generation?
- How can I properly hand off the report generation implementation to the successive maintainer?
- How can I define report generation documentation clearly?

All of those concerns fit together, but each asks for a different kind of problem-solving.

## Lab organization

A lab has one home. Every path follows one of these two shapes:

```text
niches/<niche>/<domain>/<collection>/<lab>/
niches/<niche>/<domain>/<subdomain>/<collection>/<lab>/
```

- `<niche>` — a broad style/area of problem-solving, such as `code`, `research`, `writing`, `certification`, or `architecture`.
- `<domain>` — a recognizable discipline, such as `devops`, `cloud`, `software`, `argumentation`, or `systems`.
- `<subdomain>` — one optional specialization level, such as `aws`, `kubernetes`, `backend`, `web`, or `observability`.
- `<collection>` — a coherent body of work somebody would browse together: a curriculum, challenge series, certification, topic set, course, or annual challenge.
- `<lab>` — one bounded problem, exercise, prompt, investigation, experiment, project, or case. A numeric folder prefix is used only when that collection is ordered.

For example:

```text
niches/code/devops/roadmap-sh/01-server-performance-stats/
niches/code/software/backend/devroadmaps/rest-api-with-auth/
niches/certification/cloud/aws/aws-saa-c03/saa-c03-practice-question-1-design-resilient-architectures/
niches/writing/argumentation/mit-ocw-problems-of-philosophy/24-00-problems-of-philosophy-paper-1/
```

**Hierarchy = primary human browsing identity. Metadata = provenance and cross-cutting facts.** A source can contribute work to several collections, and a collection can contain work from several sources. Source/provider is never a path level.

Each lab starts with a `README.md` and `lab.json`. The README links to external material when there is any; `lab.json` stores the details worth cataloging. Solution work gets whatever structure it actually needs, such as `src/` or `solution/`.

> [!IMPORTANT]
> Everything here is for my own education and practice, and to showcase my critical thinking, problem-solving, and decision-making. When I use someone else's work, I cite the original source and give its creators credit. I keep copied material with its license notices and attribution; some sources are link-only or need a specific review first.

## Metadata and scripts

The source registry, schemas, generated catalogs, and small maintenance tools live under [`.meta/`](.meta/README.md). The scripts work from the filesystem hierarchy and metadata; adding a niche, collection, or source does not require generic Python changes.

```bash
python3 .meta/scripts/lab_init.py --interactive
python3 .meta/scripts/lab_meta.py --interactive
python3 .meta/scripts/source_meta.py create --interactive
python3 .meta/scripts/lab_sync.py
python3 .meta/scripts/catalog.py
```

---

### Looking ahead

As I keep furnishing this repo and evolve with my interests, I can imagine more niches and disciplines: communication, argumentation, mathematics, finance, leadership, architecture, and plenty more. The hierarchy can grow without inventing another universal path level. Might eventually have to reconsider the `labs/` name with the idea having become a larger aggregation of personal critical thinking, problem-solving, decisions, patterns, and practices.
