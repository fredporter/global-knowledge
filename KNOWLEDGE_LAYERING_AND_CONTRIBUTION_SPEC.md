# Knowledge layering and contribution contract

Status: architectural target; implementation and platform qualification remain product responsibilities.

## Authority and precedence

Layer 0 is the installed immutable Global Knowledge baseline under `~/Public/global-knowledge`. Layer 1 is explicitly shared/community material under `~/Shared`. Layer 2 is personal sovereign material under `~/Vault`. Resolve personal over shared over baseline using stable identity and provenance; never overwrite baseline content when saving an overlay. UI badges, comparison and fallback behavior require tests in the consuming product before being advertised.

Only the Wizard/maintainer curates source canon through external development tools. Ordinary runtime users author overlays. uCore hosts UI/services; bundled uFlow owns workflow execution. This contract creates no separate curator service, agent tree or runtime environment.

## External review

Discover installed model inventory and qualified capability manifests. External frontier and local models may assist normalization, verification and intake review; model agreement does not establish factual accuracy. Do not embed fixed model recommendations. Verify facts, rights, provenance, privacy, links and compatibility through evidence appropriate to each proposed change.

## Planned submissions and editions

A future signed submission may nominate a public vault listing or a canon patch, with manifest, author identity, source references, content hashes and a reviewable diff. Signing and verification formats require a qualified implementation before use. Submitting a proposal does not grant canon write access or publish private content.

Wizard review occurs externally through source review and verification recipes. Accepted source changes may enter a separately verified edition. Atomic installs, rollback, signatures and delta delivery remain qualification gates; this document promises no automatic peer synchronization or in-app developer review panel. Preserve user overlays through any future baseline upgrade.
