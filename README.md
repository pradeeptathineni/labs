# Labs

`labs` is a working collection and showcase of problems/challenges I solve, practices/principles I employ, and ideas/curiosities I explore across different niches and domains.

A lab is synonymous to a problem, exercise, or challenge that aims to test my critical thinking, problem-solving, and decision-making.

## Structure

The actual work lives under [`niches/`](niches/), nearby a generated labs [catalog](CATALOG.md). Repository/metadata/catalog logic lives tucked away under [`.meta/`](.meta/).

The repository is intentionally broad at the top level. Code is one way to practice critical thinking; research, design, teaching, writing, and numerous other niches that interest me have differing styles and requirements.

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

A lab can live at either level defined below, depending on whether a domain helps organize it:

```text
niches/<niche>/<source>/<lab>/
niches/<niche>/<domain>/<source>/<lab>/
```

- `<niche>` — a broad problem-solving area, such as `code`.
- `<domain>` — an optional discipline within the niche, such as `devops`.
- `<source>` — the original source provider of the exercise, such as `roadmap-sh`.
  - `<registered-id>` when an external provider.
  - `created` when personally synthesized.
  - `organization` when received organizationally (company, interview, event, hackathon, etc).
  - `generated` when AI-generated.
  - All sources of all types are strictly registered under `.meta/catalog/sources.json`.
- `<lab>` — the individual exercise, optionally numbered when its collection has an order.

For example:

```text
niches/code/devops/roadmap-sh/01-server-performance-stats/
niches/code/devops/organization/eng-challenge-aws-terraform/  *A lab can solicit its own repo.*
niches/code/devops/generated/01-claude-devops-challenge/
niches/research/software/created/finding-prior-art/
niches/research/ai/created/grounding-gen-ai/
niches/research/created/conducting-research/  *A lab can be niche-level.*
```

Each lab starts with a `README.md` and `lab.json`. The README links to external material when there is any; the metadata stores the details worth cataloging. Solution work gets whatever structure it actually needs, such as `src/` or `solution/`.

> [!IMPORTANT]
> Everything here is for my own education and practice, and to showcase my critical thinking, problem-solving, and decision-making. When I use someone else's work, I cite the original source and give its creators credit.

---

### Setting up for the future:

As I consistently furnish this repo and evolve with my interests over the years, I could imagine critical thinking nuances like:

```text
niches/communication/unity/created/effective-teamwork/
niches/communication/discourse/created/effective-debate/
niches/writing/essay/created/critical-thinking-prompts/
niches/writing/essay/created/critical-thinking-prompts/
niches/writing/essay/generated/critical-thinking-prompts/
niches/life/finances/...
niches/life/investing/...
niches/leadership/...
niches/business/...
```

Hierarchy structuring and automation will also evolve as the repo grows. Might have to reconsider the labs/ name with the idea having become an aggregation of personal critical thinking, problem solving, decision making, patterns, and practices.
