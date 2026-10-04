# Catalog Metadata

A lightweight but comprehensive gathering of all lab metadata.

## Sources of truth

1. **`.meta/catalog/sources.json`** describes external providers and their source collections once.
2. **Each lab's `lab.json`** describes that lab and references a registered source when applicable.

Generated views:

- `.meta/catalog/labs.json`
- `CATALOG.md`

> [!WARNING] Do not hand-edit.

Regenerate them with:

```bash
python3 .meta/scripts/catalog.py
```

## Why per-lab metadata?

Keeping metadata beside the work makes individual labs and their data portable, and prevents a central index from becoming a second manually maintained database. As a die-hard automater, I wanted a generated aggregate catalog of metadata of all my lab work from the get-go.

Sure that means manually creating and maintaining/changing/updating a metadata file for every lab. But that's exactly the kind of absurdity I strive for. Whatever, shh, I'm doing something.

## Schema

`schema/lab.schema.json` details the v1 metadata contract. The generator performs dependency-free validation of the required v1 fields and referential integrity against `sources.json`.

Yes, I manually update sources.json too.
