# Offline knowledge editions

This repository is the developer-maintained source for the uDOS offline knowledge bank. The installed user edition lives in `~/Public/global-knowledge`; user changes belong in Shared/Vault overlays. Typical users do not update this repository or curate the canonical corpus.

The same baseline content serves uCore's knowledge views and its teletext reader. Think of it as a reusable offline encyclopedia/survival reference edition, with multiple presentations rather than copied reader-specific content.

Plan editions as manifests over one corpus: Core, Essential, Reference, Complete and optional interest packs. Declare actual sizes, file/pack hashes, dependencies, licences/provenance and reader compatibility. Use atomic validated installs and preserve user overlays. Publish only content whose distribution rights have been reviewed. Existing version.json and _index.json are historical metadata; they must not be represented as a newly verified edition manifest.

Runtime calculations and mapping algorithms remain in product code. Larger reference datasets, map layers and catalogs belong in seed packs. Existing uCode map seeds and host IANA timezone data remain their active read sources until a verified seed release migrates them. No application daemon, Python environment, service or agent configuration belongs in this data repository.

The initial checkout was relocated from the installed library without changing its readable installed files. All tracked files and three pre-existing untracked assets were verified; original Git metadata is retained in Code/ARCHIVED/cleanup-2026-11-09/installed-knowledge-git. This planning note has not been installed into the user's edition or published upstream.
