# Container semantics and capacity planning

Status: target contract aligned with the accepted uDOS documentation; packaging, authorization and publication still require product qualification.

| Concept | Meaning | Lifecycle and authority |
| --- | --- | --- |
| Binder | Collection of materials and results linked to independent Missions | Existing Binder owner controls membership, documents and removal. |
| Capsule | Proposed portable package or edition | Format, signing, dependencies and installation must be qualified by the package owner. |
| Dispatch | Explicit selected publication or handoff | Destination, audience, permission and acknowledgement are required; local preparation cannot establish remote delivery. |
| Tomb | Public published collection | Public selection is deliberate and distinct from private storage, archive retention or deletion markers. |
| Crypt | Encrypted Tomb | Encryption, keys and recipient access require qualification; a name alone grants no protection. |

Drone supplies scoped network access. Beacons advertise presence/resources without granting access. Neither discovery nor messaging grants publication or execution authority. Human role enforcement belongs to server contracts, separately from presentation preferences.

Expiry, single-view delivery and revocation are planned adapter capabilities. Do not promise that expiry erases downloaded copies, backups or external records. A deletion tombstone is synchronization metadata and must not be confused with a public Tomb collection.

Resolve storage roots through owning settings and resource contracts. Do not introduce guessed Binder, Tomb or dispatch directories, duplicate stores or new daemons. Installed canon remains separate from selected user publications.

## Capacity evidence

Measure selected files, indexes, assets, dependencies and temporary install space on the actual target. Reserve space for host partitions, rollback and normal operation; available filesystem space differs from advertised disk capacity. Report measured bytes and an explicit safety margin. Historical per-note and device-size estimates are not installation guarantees.

Apple Silicon runs natively on macOS. Older/non-Mac hardware uses the qualified Sonic Linux live USB or dual-boot path preserving existing host data. Media writing, package compatibility and capacity checks remain Sonic/product qualification gates.
