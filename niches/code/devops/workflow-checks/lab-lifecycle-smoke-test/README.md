# Lab lifecycle smoke test

This is a repository workflow experiment, not a DevOps exercise completion.

## Exercise Definition

Create a lab through the initializer, move it from planned to in progress to complete, and verify the local catalog and public Pages snapshot at each stage. Inspect automatic content tracking, solution discovery, lifecycle dates, commit safeguards, and deployment failures. Fix observed weaknesses and preserve enough evidence to repeat the workflow.

Finish when all three statuses have been observed publicly, meaningful regression checks pass, and the workflow guide explains what changes at each boundary.

## Solution

I used the real initializer, metadata editor, pre-commit hook, main branch, GitHub Actions, and public Pages catalog. This experiment exercised the repository workflow only; it did not provision infrastructure or solve any of the imported exercises.

### Observed boundaries

| Stage | What changed | Publication evidence |
| --- | --- | --- |
| Planned | The initializer added one experiment with `not-started` status, null start/completion dates, and an empty Solution section. The hook recorded the staged README. | Commit `f99a162`; [Pages run 38164955733](https://github.com/pradeeptathineni/labs/actions/runs/38164955733) succeeded. The live build and catalog payload matched that commit, showed Planned, and had no Solution link. |
| In progress | The metadata command set `in-progress` and the first start date to 2026-10-11. The status-only commit kept the content fingerprint unchanged. | Commit `6647f42`; [Pages run 38165049526](https://github.com/pradeeptathineni/labs/actions/runs/38165049526) succeeded. The live build and payload matched, showed In progress, and still had no Solution link. |
| Completed | I added these worked notes and explicitly selected `complete`. The hook records the new content fingerprint, and the completion command records the first completion date. | Final public verification is recorded below after deployment. |

At each local edit or metadata change, the public site retained its last published snapshot until the main deployment succeeded. The corpus grew from 76 to 77 labs; the original 76 labs and 49 atlas opportunities kept their existing lifecycle state. This completed experiment is distinct from those still-planned exercises.

### Weaknesses found and fixed

- Pages previously validated canonical files but could deploy independently of the test workflow. Its build now runs the regression suite before publishing.
- Starting a lab and then adding Solution notes could make the earlier generated views stale. The commit hook incorrectly treated that normal sequence as hand editing. The generator now records hashes of its last output in ignored local build state; the hook recognizes and refreshes those stale outputs while preserving and rejecting actual manual edits.
- The commit guard covered only some metadata scripts. It now includes all shared scripts and hooks, preventing unstaged tooling from influencing a relevant commit.
- Start and completion dates could precede creation. Validation now rejects that chronology before writing any files.
- A comment-only Solution section or a `## Solution` example inside a code fence could create a misleading Solution link. Discovery now skips comments and example headings while recognizing actual text or code in the section.
- Completion without worked notes remains an explicit personal decision; commands now explain that no Solution link is recorded. Creation and editing also explain the remaining stage/commit/push boundary.
- The browser smoke check formerly used local counts without proving the live deployment was the expected snapshot. It now compares the commit and complete catalog payload, checks lifecycle sections and Solution links, and rejects a different deployment.

### Validation

The original 16 tests passed before changes. The expanded 20-test suite passed locally, including the full planned → in-progress → complete → reopened → complete workflow through real commit hooks and clean release builds in disposable repositories. Those checks also preserve manual generated-view edits, reject unstaged shared tooling without altering the index, reject invalid dates without writes, and prove release verification does not depend on local generator receipts.

The browser check passed for the local catalog at both `/` and `/labs/`, covering status sections, Solution links, filtering, saved URLs, reload/back, desktop and narrow layouts, and usable links with JavaScript disabled. A deliberate mismatch in the expected commit made the live check fail as intended; the local artifact was restored afterward.

The [maintenance guide](../../../../../.meta/README.md) explains everyday creation, progress, completion, reopening, staged content, and first-date semantics. The [publishing guide](../../../../../.meta/site/README.md) explains deployment verification, stale snapshots, and recovery from failed checks.
