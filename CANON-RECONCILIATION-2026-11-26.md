# Canon reconciliation decision — 2026-11-26

**Decision:** `origin/main` is the canonical lineage for this repository. The
divergent local lineage is retained as a curation candidate, not merged.

**Authority:** Wizard/owner approval, 2026-11-26 (D2).

## What was true before

- Local `main` (`1a64f69`, 11 commits) and `origin/main` (`3790759`, 7 commits)
  shared **no merge base**; they are unrelated histories.
- Local `main` carried 519 tracked files, of which **508 existed only there** —
  the contributor corpus (communication, community, contributor, food, making,
  medical, shelter, skills and related trees) — plus eight uncommitted
  standards/index edits.
- `origin/main` carried 20 tracked files of published canon, including nine that
  existed only there: `EDITION_PLAN.md`, `VERSION`,
  `datasets/length_conversions.json` and the `research/` set.

## What was checked

The five commits on `plan/selective-canon-reconciliation` were reviewed for
re-landing. Their content is **already present** on `origin/main`: every file from
`5ef7c6b` is byte-identical there (`datasets/length_conversions.json`,
`navigation/compass_use.md`, `navigation/map_reading.md`, `research/core-scope.md`,
`research/navigation.md`), and the two documentation commits (`c3d69e2`,
`1b19557`) touch files that are identical on `origin/main`. Re-landing would
therefore have duplicated published canon, so it was not performed.

## What this repository now holds

- `main` = `3790759` (published canon), tree clean.
- `candidate/contributor-corpus-2026-11-26` = `5bb1c45` — the full corpus lineage
  with the pending standards edits, pushed for selective curation.
- Tags: `preserve/contributor-corpus-2026-11-26`,
  `preserve/canon-local-main-2026-11-24`, and the earlier
  `preserve/*`/`recovery/*` references.

Nothing was reset, rebased or discarded without a reference. To reproduce the
previous working tree: `git switch candidate/contributor-corpus-2026-11-26`.

## Open curation item

The installed baseline at `~/Public/global-knowledge` currently reflects the
corpus lineage, so the installed tree and published canon still differ. Under the
Wizard/submission doctrine, corpus content enters canon through reviewed
submissions; the candidate branch is the source for those reviews. Deciding which
of the 508 corpus files belong in Layer 0 is a curation decision, not a merge.
