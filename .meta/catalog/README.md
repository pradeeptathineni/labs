# Catalog metadata

`lab.json` keeps maintained facts beside each lab: title, optional summary, type, optional difficulty, skills, optional cross-cutting goals, source, optional solution/demo links, and tracking. Status and the four lifecycle dates live under `tracking`. Paths supply niche, domain, optional subdomain, a list of collection groupings, collection, and lab slug. There is no provider-derived path level.

A source record has a name and one of `external`, `organization`, or `local`. External sources have a canonical URL and reuse policy. An organizational source can omit its public URL; local sources need neither. `copy`, `link-only`, and `review` are operational policies for these tools, with evidence scoped to the source material reviewed. A registered provider name does not make every linked asset safe to copy.

A collection may have `collection.json` with a display title, a collection-level `source_url`, `ordered: true`, or shared goals. Its title names the collection itself; the catalog supplies subject and niche context. Without `ordered: true`, numeric-looking lab names are ordinary slugs. Ordered collections require unique positive prefixes and append after the highest number.

`has_subdomain: true` in that same descriptor declares that the directory immediately after the domain is a subject specialization. With no declaration, only the domain identifies the subject. Every remaining directory before the collection is a grouping, at any depth. This distinguishes `systems/mit/course-abc` from `systems/distributed/mit/course-abc` without guessing what a provider name means. Conflicting interpretations of a domain/subdomain across niches are rejected.

The generated records expose `subdomain` as a name or null and `groups` as an ordered list, alongside the other path-derived fields. No copy of a subject name is maintained in a lab or descriptor. Only the boundary is declared.

Browse all groups collections by the exact domain/subdomain pair across niches. Plain subject headings, such as AWS Cloud and DevOps, sit above closed collection dropdowns. Each summary shows the collection hierarchy followed by the niche. Its next line uses `<small>` for the full path as inline code, the calculated lab count, and a notes link when a collection README exists. A final `ref` links to `source_url` when supplied. Each lab's title opens its local exercise and its final `ref` links to its exact source. Completed and In progress use the same collection labels and paths with counts for the displayed status.

Every lab uses the same metadata line: type, status, update date, skills, optional goals, and a source `ref` when available. Question counts and resolved provider names remain available in `labs.json`; they do not add extra fields to individual catalog rows.

Provider spelling comes from the existing source registry where a hierarchy label matches a registered ID; that lookup only formats a name. A few spelling and subject-title exceptions live in the generator, with readable slug-based fallbacks for new names. These labels never determine grouping. The generator keeps styles together and uses HTML links and `<code>` inside summaries because Markdown link syntax and backticks stay literal there.

As a die-hard automater, I wanted the aggregate catalog generated from the get-go. Keeping metadata beside the work makes each lab portable and prevents the central index from becoming another hand-maintained database. Sure, I maintain a metadata file for each lab. That's the particular absurdity I've chosen.

Generated views are [`labs.json`](labs.json) and [the readable catalog](../../CATALOG.md). Regenerate them with `python3 .meta/scripts/catalog.py`; check without writing with `python3 .meta/scripts/catalog.py --check`. The index is deterministic and offline. Its counts describe registered labs and current status; imported questions and target skills are not evidence of personal practice.

> [!WARNING]
> Do not hand-edit generated views. Edit the neighboring metadata or source registry, then regenerate.
