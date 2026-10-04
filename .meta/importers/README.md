# Source-specific importers

Importers read a local Git checkout at its resolved commit. They verify the expected origin and committed license, read committed files, and never run an upstream app or JavaScript. Cloning a checkout is a separate step; regular import runs are offline. Install their parser dependency with `python3 -m pip install -r .meta/importers/requirements.txt`.

`devroadmaps.py` uses Esprima 4.0.1 to parse the pinned JavaScript file and accepts only static literals inside `PROJECT_IDEAS`. This older parser successfully parses the reviewed file at `104d7bc31f3ade603c13ba7efa79968aca42cd15`. Expressions and duplicate object keys fail before any write. Project IDs use `project-ideas/<track>/<initial-title-slug>`; upstream reorders do not remap them, while a rename needs manual identity review.

```bash
python3 .meta/importers/devroadmaps.py --checkout /path/to/devroadmaps --list
python3 .meta/importers/devroadmaps.py --checkout /path/to/devroadmaps --track devops --all-track --destination niches/code/devops/devroadmaps --dry-run
python3 .meta/importers/devroadmaps.py --checkout /path/to/devroadmaps --track devops --all-track --destination niches/code/devops/devroadmaps --yes
python3 .meta/importers/devroadmaps.py --checkout /path/to/devroadmaps --interactive
```

`cloudcertprep.py` makes one CLF-C02 bank from explicitly selected domains or qualified question IDs. `--all-domains` adopts the four current CLF domains in one lab; AIF and SAA material are outside this adapter. The JSON keeps original IDs, choice keys, explanations, and multiple-answer values. `REFERENCE-ANSWERS.md` is upstream material, never my solution.

```bash
python3 .meta/importers/cloudcertprep.py --checkout /path/to/cloudcertprep --list
python3 .meta/importers/cloudcertprep.py --checkout /path/to/cloudcertprep --all-domains --destination niches/study/cloud/aws/clf-c02 --subdomain aws --dry-run
python3 .meta/importers/cloudcertprep.py --checkout /path/to/cloudcertprep --all-domains --destination niches/study/cloud/aws/clf-c02 --subdomain aws --yes
python3 .meta/importers/cloudcertprep.py --checkout /path/to/cloudcertprep --interactive
```

Both importers use the initializer's destination parser: `niches/<niche>/<domain>/[<subdomain>/][<group>/...]<collection>`. For a new collection with a subdomain, pass `--subdomain` matching the first directory after the domain. It is recorded as `has_subdomain: true` in the collection descriptor. Existing descriptors supply that boundary on later runs. Interactive mode asks for it explicitly. Any directories after the subject organize collections; they do not establish source provenance.

Both importers preview the exact plan, including new collection descriptors, and require `--yes` for flag writes. Interactive writes always ask for confirmation. Rerunning the same selection and revision is a no-op. A changed source needs an explicit `--refresh` with the same selection and a reviewed preview. Importer-owned snapshots are checked for local edits before refresh. My README Solution, responses, status, history, and manual metadata are preserved. If a source definition changes, the importer reports that the README definition needs manual review; it does not rewrite that section automatically.

TidyTuesday datasets and other registered sources remain selective future choices. Kananinirav study notes are linked in an active problem set; its linked practice-exam content is deferred pending specific provenance and permission review.
