# Repository Metadata

Machine-readable metadata for the lab corpus and the small tools that maintain it live here.

- [`catalog/`](catalog/) — the source registry, metadata schemas, and generated lab index.
- [`scripts/`](scripts/) — tools for creating labs, updating metadata, and rebuilding the catalog.
- [`requirements.txt`](requirements.txt) — the one dependency those tools need.

This is mostly upkeep and automation. The labs themselves live under [`niches/`](../niches/).

## Usage

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Create a lab. For an ordered collection, the next available number is assigned automatically:

```bash
python3 scripts/lab_init.py code roadmap-sh "Server Performance Stats" --domain devops --kind project --difficulty beginner --skill bash --skill linux --skill performance-monitoring --source-id server-stats --source-url https://roadmap.sh/projects/server-stats
```

View or update a lab's metadata:

```bash
python3 scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats
python3 scripts/lab_meta.py niches/code/devops/roadmap-sh/01-server-performance-stats --status in-progress --add-skill process-management
```

Regenerate or check the catalog corpus:

```bash
python3 scripts/catalog.py
python3 scripts/catalog.py --check
```
