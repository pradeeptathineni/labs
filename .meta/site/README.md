# Web catalog

One static page with four expandable sections: Completed, In progress, Browse labs, and All labs. Browse offers skill, tool, goal and subject choices with a searchable selector. Collections start collapsed. Search, filtering and sorting work in the browser. Exercises, solutions and the practice atlas link to GitHub. Aptos is used where installed, with system fallbacks; no external fonts or frontend framework.

Explicit empty collections appear in All labs as `0 labs · Planned`, with their notes, source, and inherited goals. They stay searchable and filterable without increasing lab counts. Certification goals display their readable credential title and Certification label. Completed and In progress contain actual labs only.

## Preview

```bash
python3 -m pip install -r .meta/requirements.txt
python3 .meta/scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory .meta/build/pages
```

Open `http://127.0.0.1:8000`. Relative assets also work under `/labs/`. The complete catalog is in the HTML, so links remain usable without JavaScript. Query parameters preserve search, filter, sort and individual lab links. Collection order matches Markdown across niches; the sort control changes lab order within each collection. Tags share one compact line with the source `ref`.

The builder reads the shared catalog records and recorded lab dates. It never updates metadata, fingerprints, tracked views or the Git index. Only `.meta/build/` is generated and ignored. Hashed assets prevent mixing old data with new code. `build-info.json` identifies the source commit; `--release` requires a clean, current snapshot.

For a local browser check after changing the page:

```bash
python3 -m pip install -r .meta/site/requirements-dev.txt
python3 -m playwright install chromium
python3 .meta/site/browser_smoke.py
```

This checks the built snapshot, lifecycle section counts, Solution links, desktop/mobile layout, filtering, saved links, reload/back, and HTML without JavaScript. Screenshots stay in ignored build output. Browser installation is not part of each deploy.

## Publish

[pradeeptathineni.github.io/labs](https://pradeeptathineni.github.io/labs/) is the public URL.

1. Set Settings → Pages → Source to **GitHub Actions**.
2. Restrict the `github-pages` environment to branch **main**.
3. Commit and push. Check `gh run list --workflow pages.yml`; compare the live `/build-info.json` commit with the intended SHA. A manual retry is `gh workflow run pages.yml --ref main`.

Relevant pushes to `main` publish automatically. Relevant pull requests build without deployment permissions. Paths cover labs, metadata/tooling, hooks, workflows and root documentation; unrelated changes do not rebuild. The existing unfiltered metadata check remains independent.

The workflow runs the regression suite before publication, checks canonical files read-only, and builds a seven-file artifact. Only the trusted main deploy job gets Pages/OIDC write permissions. Production runs serialize without cancelling an active deployment. A check before upload and deployment skips snapshots whose relevant inputs no longer match main; an unrelated newer commit is allowed. The last successful site remains available if a new build fails. Repository links on the site point to the published commit, so an older catalog continues to open its matching lab notes while a newer deployment is pending.

After pushing, verify the intended commit, rather than assuming the newest run or a green metadata check means the site is current:

```bash
git rev-parse HEAD
gh run list --workflow pages.yml --limit 5
curl --fail --silent --show-error https://pradeeptathineni.github.io/labs/build-info.json
# Once source_commit matches HEAD, build the same clean snapshot and check it live:
python3 .meta/scripts/build_site.py --release --base-path /labs/
python3 .meta/site/browser_smoke.py --url https://pradeeptathineni.github.io/labs/
```

The live browser check compares the commit, complete catalog payload, status sections, and Solution links with your local release build. It fails for a stale or different snapshot. A local preview can include uncommitted edits; it does not publish them. Allow time for Actions and cached content to catch up; there is no fixed publication delay. If publication fails, inspect `gh run view RUN_ID --log-failed`, fix the reported input or test failure, and push the correction. If inputs are already valid and the failure was transient, retry the Pages workflow on main. A freshness skip is deliberate; check the newer main run before retrying an obsolete one.

Local commit hooks synchronize lab fingerprints and generated Markdown; they never build the website. CI never repairs metadata or creates bot commits. See GitHub's [custom Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) and [concurrency documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).
