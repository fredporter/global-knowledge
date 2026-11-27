---
title: "uDos Prose Typography & Presentation Standard"
version: "1.0.0"
status: "canonical"
tags: [standards, prose, typography, usx]
---

# uDos Prose Typography & Presentation Standard

The Prose standard governs document authoring, longform reading, and markdown rendering across all uDos surfaces (Local Wikipedia reader, binders, documentation, and notebooks).

## 1. Line Measure & Spatial Hierarchy

- **Maximum Line Measure**: 70ch to 72ch (approx. 680px–740px wide), carried by `--usx-prose-width`. Reading lines exceeding 75 characters induce visual fatigue and break reading rhythm.
- **Line Height**:
  - Headings: `1.25` to `1.35` (`--usx-line-height-tight`)
  - Body Text: `1.65` to `1.75` (`--usx-line-height-relaxed`)
  - Code Blocks: `1.45` (`--usx-line-height-code`)
- **Paragraph Spacing**: `1.0em` bottom margin. Never use consecutive `<br>` tags to fake paragraph rhythm.
- **Implementation**: [usx-prose.css](../uCore/packages/usx-tokens/usx-prose.css) is the only Prose stylesheet. It uses `--usx-*` tokens exclusively.

## 2. Typography Stacks (bundled)

Three families ship with the workspace. Each maps to one USX token, and contract
styles must reference the token rather than a font name.

| Role | Bundled stack | Token |
| --- | --- | --- |
| **Reader Serif** (Wiki / Book / Longform) | `Merriweather, Georgia, serif` | `--usx-font-family-serif`, surfaced as `--usx-font-family-reading` |
| **Modern Sans** (UI chrome / system panels / headings) | `Inter, system-ui, -apple-system, sans-serif` | `--usx-font-family-sans` |
| **Technical Mono** (uCode, BASIC, terminal, datasets) | `JetBrains Mono, "SF Mono", monospace` | `--usx-font-family-mono` |

Bundled families come first so a reader works offline and identically on macOS,
Linux and revived hardware. Platform-only faces such as Charter or Berkeley Mono
must not be referenced by contract styles: they are absent on CMMint targets.

## 3. Strict Offline Citation Protocol

Under the sovereign uDos contract, the reader is a peaceful, self-contained local library:
- **Internal Wiki Links**: `[[Article Name]]` or `[Display Title](relative/path.md)` navigate directly between local vault documents without page reloads.
- **External Web References**: External URLs (`https://...`) do **NOT** link out to the live web. They render as static **citation chips**:
  ```html
  <span class="wiki-citation" data-source="web" title="Captured via BrowserUI">Source: example.com/article</span>
  ```
- **Web Intake**: `BrowserUI` is the designated tool for scraping and snapshotting external web content into `~/Vault/Clips` or `~/Public/Research`. Once clipped, the document lives locally forever.
