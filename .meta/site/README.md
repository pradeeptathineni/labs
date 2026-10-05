# Visual workbench

The site renders the same validated records as `CATALOG.md` and `PRACTICE-ATLAS.md`. It publishes metadata and links back to GitHub for exercises and personal work. It does not publish question bodies, reference answers, source checkouts, or internal provider notes in its artifact.

## Build and preview

```bash
python3 -m pip install -r .meta/requirements.txt
python3 .meta/scripts/build_site.py --output .meta/build/pages
python3 -m http.server 8000 --bind 127.0.0.1 --directory .meta/build/pages
```

Open `http://127.0.0.1:8000`. Assets use relative URLs, so both `/` and the production `/labs/` mount work. `--base-path /labs/` records that deployment configuration. `--release` requires a clean checkout and current staged fingerprints. Normal previews are labeled local, including uncommitted changes. `build-info.json` records the commit, its timestamp, counts and file allowlist; it is not a progress timestamp.

Only `.meta/build/` is generated and ignored. The builder refuses arbitrary output paths or unmanaged existing directories. `--check-output` verifies the artifact. Rendering is offline after dependencies are available, and never updates canonical files, the Git index, lab dates or fingerprints. Hashed CSS, JS and data filenames prevent stale asset combinations.

The full work and atlas content exists in initial HTML. JavaScript enhances it with filters and URL state. Different facets combine with AND; multiple values within a facet combine with OR. Child specializations are scoped to selected subjects and incompatible choices are explicitly cleared. Sorting stays within each collection; it does not impose a curriculum order across unrelated sources. Dates are displayed as their recorded strings, with no timezone conversion.

For browser verification:

```bash
python3 -m pip install -r .meta/site/requirements-dev.txt
python3 -m playwright install chromium
python3 .meta/site/browser_smoke.py
```

Screenshots go under ignored build output, outside the publish artifact.

## Publication

The intended public address is [pradeeptathineni.github.io/labs](https://pradeeptathineni.github.io/labs/). A successful local build alone does not establish a live deployment.

The publishing workflow and exact activation/verification commands are added with the deployment configuration. The authority chain is: stage intended work → local commit hook synchronizes lab metadata and tracked views → Actions validates the committed snapshot read-only → build an isolated artifact → deploy that artifact. Website rendering never runs in pre-commit.

The `Pages` workflow runs on relevant pushes to `main`, relevant pull requests, and manual dispatch. Its path set covers `niches/`, `.meta/`, hooks, both workflows, root README/catalog/atlas, and Git attributes/ignore rules. The existing unfiltered `Lab metadata / check` remains independent; do not require the path-filtered Pages check for unrelated PRs.

Build/check has contents read and Pages read only. Only the trusted `main` deploy job receives Pages write and OIDC token write, and it deploys the successful artifact from the same run. PRs, forks, tags and feature-branch dispatches cannot publish. Checkouts use full history and do not persist credentials. Action versions were checked against official releases: configure-pages 6.0.0, upload-pages-artifact 5.0.0, deploy-pages 5.0.1; the existing checkout/setup-python v7 convention remains.

Production push and manual-main runs share `pages-production`: one active and at most one pending, without canceling an active deployment. PR groups are independent and cancel older PR checks. Before upload and again after the environment gate, a public read-only fetch compares the candidate tree with current `main` over the same relevant input paths. Relevant differences skip the stale candidate; unrelated main advances do not. There is no rollback or dispatch loop. The last good site remains if the newest build fails; the newest eligible successful run publishes once commits settle.

One-time activation (requires repository administration):

1. Settings → Pages → Build and deployment → Source: **GitHub Actions**.
2. Restrict the `github-pages` environment to deployment branches matching **main**, with no tag rule.
3. Push the validated commits. For recovery after activation, run `gh workflow run pages.yml --ref main`.
4. Use `gh run list --workflow pages.yml` and `gh run view <run-id>` to verify both jobs. Check the environment URL and compare its `/build-info.json` `source_commit` with the intended SHA. Confirm the live UI and linked lab snapshot.

The checks never install hooks or repair metadata in CI. For stale canonical inputs, repair and commit locally with `lab_sync.py --yes` and `catalog.py`, then push. A site build is never lab activity.

GitHub's [custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) and [concurrency rules](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) explain the hosting controls; the workflow uses release metadata rather than older example action tags.
