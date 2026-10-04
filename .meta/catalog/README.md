# Catalog Metadata

A small, generated view over a human-sized practice corpus.

## Sources of truth

1. [`sources.json`](sources.json) records provenance providers independently from the folder hierarchy, along with verified source-level reuse guidance.
2. Each lab's `lab.json` records title, kind, status, optional difficulty, skills, source item, lifecycle dates, and content tracking.
3. The path supplies niche, domain, optional subdomain, collection, lab slug, and numeric order. Those derivable facts are not repeated in local metadata.

Generated views:

- [`labs.json`](labs.json) — machine-readable catalog.
- [`../../CATALOG.md`](../../CATALOG.md) — human-readable catalog.

> [!WARNING]
> Do not hand-edit generated files. Regenerate them with:

```bash
python3 .meta/scripts/catalog.py
python3 .meta/scripts/catalog.py --check
```

## Hierarchy and metadata

The only legal lab paths are:

```text
niches/<niche>/<domain>/<collection>/<lab>/
niches/<niche>/<domain>/<subdomain>/<collection>/<lab>/
```

The domain is required, subdomain is optional and exactly one level deep, and collection is required. Source/provider is never a hierarchy level. A source may appear in several collections, and one collection may contain labs from several sources.

Local metadata uses `source.provider` to reference `sources.json`. External or organizational sources also require an `item_id` and item `url`; `created` and `generated` need only their provider. Keep path-derived facts out of `lab.json`.

The kind vocabulary stays compact and covers projects, challenges, exercises, problems, prompts, questions, case studies, experiments, incidents, and katas. Difficulty is optional and normalized to `beginner`, `intermediate`, or `advanced`; source-specific labels can map through `difficulty_map`. Skills are open-ended lowercase kebab-case tags.

## Source records and reuse

Source records have `name`, `type`, and a canonical `url` where applicable. External sources and organizational sources carry `reuse` guidance:

- `copy` — reviewed source policy allows repository tooling to materialize content, subject to attribution and license notices.
- `link-only` — scripts must link to the canonical source rather than copy its content.
- `review` — no materialization until that item is reviewed.

The record may also keep a known license identifier, `license_url`, `policy_url`, verification date, and a short operational note. This is a local workflow rule, not legal advice or a legal database. Unknown permission is not treated as permission. Per-item exceptions still need review.

To add or correct records without changing generic Python:

```bash
python3 .meta/scripts/source_meta.py create --interactive
python3 .meta/scripts/source_meta.py view roadmap-sh
python3 .meta/scripts/source_meta.py update roadmap-sh --reuse-policy link-only
```

## Ordering and lifecycle

A collection is ordered when its sibling lab folders consistently use positive numeric prefixes. `lab_init.py --ordered` starts numbering a new collection; once numbering exists, later labs take the next free order. Unnumbered collections stay unordered. Mixed or duplicate ordering fails validation.

Lifecycle status changes are explicit through `lab_meta.py`. `lab_sync.py` hashes meaningful tracked and untracked files, excluding `lab.json`. A first fingerprint initializes tracking without changing the historical `updated` date; later content changes move `dates.updated` but never infer status. `--check` only reports stale metadata.
