# Length conversion seed audit

Status: evidence for maintainer review. Scope: four values in the
installed `datasets/world_parameters.json`, under
`measurement_standards.length`.

| Seed key | Metres per unit | Definition |
| --- | ---: | --- |
| `inch_in_meters` | 0.0254 | International inch |
| `foot_in_meters` | 0.3048 | International foot |
| `yard_in_meters` | 0.9144 | International yard |
| `mile_in_meters` | 1609.344 | International mile |

These factors are exact. Historical coordinates based on the U.S.
survey foot require the original survey unit; the international foot
factor is not interchangeable with it.

Source: NIST Handbook 44 (2023), Appendix C, Section 4, “Units of
Length” table and accompanying note (p. C-10). Checked 12 November 2026.
[NIST source](https://www.nist.gov/system/files/documents/2022/11/30/2023%20NIST%20Handbook%2044.pdf).
The evidence records numerical facts and original explanatory prose;
no source table image or source text has been imported.

Run the [evidence manifest](length-conversions.evidence.json) from the
sibling uCore checkout:

```sh
python3 scripts/audit_knowledge_evidence.py \
  --root ~/Public/global-knowledge \
  --manifest ../global-knowledge/research/length-conversions.evidence.json
```

All four installed values match the evidence. Keep their keys and
values as-is. The remaining fields in the dataset, the historical
article corpus and any edition or consumer migration are outside this
review. A hash change calls for a new diff review before refreshing
the manifest.
