# Web catalog

One static page with four expandable sections: Completed, In progress, Browse labs, and All labs. Browse offers skill, tool, goal and subject choices with a searchable selector. Collections start collapsed. Search, filtering and sorting work in the browser. Exercises, solutions and the practice atlas link to GitHub. Aptos is used where installed, with system fallbacks; no external fonts or frontend framework.

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

This checks desktop/mobile layout, filtering, saved links, reload/back, and HTML without JavaScript. Screenshots stay in ignored build output. Browser installation is not part of each deploy.

## Publish

[pradeeptathineni.github.io/labs](https://pradeeptathineni.github.io/labs/) is the public URL.

1. Set Settings → Pages → Source to **GitHub Actions**.
2. Restrict the `github-pages` environment to branch **main**.
3. Commit and push. Check `gh run list --workflow pages.yml`; compare the live `/build-info.json` commit with the intended SHA. A manual retry is `gh workflow run pages.yml --ref main`.

Relevant pushes to `main` publish automatically. Relevant pull requests build without deployment permissions. Paths cover labs, metadata/tooling, hooks, workflows and root documentation; unrelated changes do not rebuild. The existing unfiltered metadata check remains independent.

The workflow checks canonical files read-only and builds a six-file artifact. Only the trusted main deploy job gets Pages/OIDC write permissions. Production runs serialize without cancelling an active deployment. A check before upload and deployment skips snapshots whose relevant inputs no longer match main; an unrelated newer commit is allowed. The last successful site remains available if a new build fails.

Local commit hooks synchronize lab fingerprints and generated Markdown; they never build the website. CI never repairs metadata or creates bot commits. See GitHub's [custom Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) and [concurrency documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).
