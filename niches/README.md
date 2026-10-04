# Niches

### Welcome to my problem-solving corpus.

The corpus is split into different problem-solving niches because code is only one part of the much broader practice of critical thinking—also known as using your noggin.

Every lab lives in one of these shapes:

```text
niches/<niche>/<domain>/<collection>/<lab>/
niches/<niche>/<domain>/<subdomain>/<collection>/<lab>/
```

- `<niche>` — a broad problem-solving area, such as `code`, `research`, or `writing`.
- `<domain>` — a recognizable discipline, such as `devops`, `cloud`, or `argumentation`.
- `<subdomain>` — one optional stable specialization, such as `aws`, `backend`, or `web`.
- `<collection>` — a curriculum, challenge series, certification, course, topic set, or other browseable body of work.
- `<lab>` — one bounded piece of practice, optionally numbered when its collection is ordered.

Source/provider is provenance in `lab.json`, never a path level. One collection may have multiple sources, and one source may appear in multiple collections.

Every lab begins with a problem README and a `lab.json` file. Solution work gets the structure it needs; there is no need to pre-fill `src/` or `solution/` before anything exists.

Code is the obvious first niche. Architecture, decisions, design, mathematics, research, and teaching are among the others I want to practice.
