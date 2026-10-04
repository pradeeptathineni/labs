# Source-specific importers

Generic repository semantics live under `.meta/scripts/`. Source-specific knowledge is allowed only under `.meta/importers/`. An importer needs stable structured data, a registered policy that permits the intended operation, direct mapping into lab semantics, enough repeated value to justify upkeep, and a small implementation.

`cloudcertprep.py` accepts a local CloudCertPrep checkout and requires an explicit item selection by ID, bounded count, or range. It refuses `link-only` and `review` sources, requires the upstream `LICENSE`, preserves that notice beside copied question content, and creates each lab through `lab_init.create_lab()`.

No DevRoadmaps importer: its project ideas are curated in JavaScript rather than stable JSON. Parsing or executing that file would add brittle source logic without enough repeated value; generic manual initialization is enough. TidyTuesday is deferred because the repository license does not establish reuse rights for each underlying dataset. Exercism is deferred until one exact track is selected because license details vary by repository. CK-X and pwn.college stay link-based: CK-X uses a restricted BSL 1.1 license, and pwn.college asks users not to publish challenge solutions. No generic downloader or plugin framework is planned.
