# Catalog Metadata

A lightweight but comprehensive gathering of metadata for all my lab work.

## Sources of truth

1. [`sources.json`](sources.json) records registered external providers, optional collections, and any verified content-use policy once. It also labels local-work categories such as `created` and `generated` so the scripts do not guess from path names.
2. Each lab's `lab.json` records the facts worth keeping beside that work: its title, kind, status, difficulty, skills, dates, and source identity when applicable.
3. The directory hierarchy already tells us the niche, optional domain, provider, slug, path, and any numeric order. I don't store those twice.

Generated views:

- [`labs.json`](labs.json) — the machine-readable catalog.
- [`../../CATALOG.md`](../../CATALOG.md) — the human-readable catalog.

> [!WARNING]
> Do not hand-edit generated files. Regenerate them with:

```bash
python3 .meta/scripts/catalog.py
python3 .meta/scripts/catalog.py --check
```

## Why per-lab metadata?

Keeping metadata beside the work makes each lab and its data portable, and keeps the central catalog from becoming a second manually maintained database. As a die-hard automater, I wanted a generated aggregate catalog of all my lab work from the get-go.

Sure, that means manually creating and maintaining a metadata file for every lab. But that's exactly the kind of absurdity I strive for. Whatever, shh, I'm doing something.

## Schema

[`schema/lab.schema.json`](schema/lab.schema.json) defines the local metadata contract; `jsonschema` validates it. Every path provider must be registered. External labs need a source ID and URL, while local-work categories do not. A provider may have no collections; when a matching collection is defined, `ordered: true` controls whether numeric folder prefixes are required. Missing or false `ordered` means the collection has no required numeric sequence.

The lab hierarchy permits `niches/<niche>/<provider>/<lab>/` and `niches/<niche>/<domain>/<provider>/<lab>/`. A collection key in `sources.json` is the corresponding path before the provider, such as `research` or `code/devops`.

To add a provider, I add its slug as a key in `sources.json` with `type: "external"`, a name, and its homepage URL. Collections are optional. A local-work category uses `type: "local"` and needs no external URL. The path provider name and registry key must match; the scripts do not need source-specific edits.

`difficulty` is optional. When it has a meaningful normalized value, the repository-wide vocabulary is `beginner`, `intermediate`, or `advanced`. If a provider uses different labels, `difficulty_map` on its source or matching collection in `sources.json` maps those labels to the shared vocabulary; collection mappings take precedence. `lab-init` and `lab-meta` accept either the shared value or a configured source label. If no level exists or no mapping is meaningful, I leave difficulty out.

`kind` and `status` are also deliberate repository-wide vocabularies in the lab schema. Skills are open-ended lowercase kebab-case tags, not a taxonomy.

The local metadata stays authoritative. The aggregate adds the structural facts that the directory names already know.
