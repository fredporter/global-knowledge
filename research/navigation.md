# Navigation curation proposal

Status: source proposal for Wizard review. No installed edition change.

This batch covers [Map Reading](../navigation/map_reading.md) and
[Compass Use](../navigation/compass_use.md). The two installed articles
matched the copies on `recovery/consolidation-2026-11-10` at
`f45573ca4f36b9b4c2efbd2eadd52db3ff85c114` byte for byte. Their paths,
titles, tags and UIDs are preserved. The drafts omit old per-article
authoring instructions and the legacy spec field.

| Article | Change and evidence |
| --- | --- |
| Map Reading | Replaces an article that ended mid-warning. Uses Geoscience Australia's guide for contours, legend and orientation, and its scale explainer for the ratio. The 4 cm example is derived from the scale ratio. |
| Compass Use | Separates magnetic field bearings from bearings measured against the map grid. The cited Geoscience Australia booklet describes north references, interference and conversion. The article gives no fixed declination value or universal conversion sign. |

The drafts use original wording and retain identification metadata from
the local corpus. No legacy body text, third-party illustration or
source excerpt was imported. The two lessons are for practice on
familiar ground; route planning, emergency procedures and off-track
navigation are outside this batch.

From the uCore checkout, run the
[evidence manifest](navigation.evidence.json):

```sh
python3 scripts/audit_knowledge_evidence.py \
  --root ../global-knowledge \
  --manifest ../global-knowledge/research/navigation.evidence.json
```

For source review, compare each draft against the matching recovery
path with `git show recovery/consolidation-2026-11-10:<path>`. The audit
checks both drafts' hashes, titles, original UIDs and links to one
another.

## Reader verification

On 13 November 2026, uCore's documentation tree and content handlers
listed and served both drafts from a disposable Public library. The
reader component test followed the sibling links in both directions,
including a `./` link. A same-name file at another path and a matching
path in Shared exercised exact path and source selection. External
references rendered as offline citation chips.

The reader check used simulated API responses, with a separate check of
the API handlers against the draft files. Edition packaging and a full
browser session against a packaged edition remain open.
