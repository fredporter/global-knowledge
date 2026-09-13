---
title: "uDos Prose Typography & Presentation Standard"
version: "1.0.0"
status: "canonical"
tags: [standards, prose, typography, usx]
---

# uDos Prose Typography & Presentation Standard

The Prose standard governs document authoring, longform reading, and markdown rendering across all uDos surfaces (Local Wikipedia reader, binders, documentation, and notebooks).

## 1. Line Measure & Spatial Hierarchy

- **Maximum Line Measure**: 70ch to 72ch (approx. 680px–740px wide). Reading lines exceeding 75 characters induce visual fatigue and break reading rhythm.
- **Line Height**:
  - Headings: `1.25` to `1.35`
  - Body Text: `1.65` to `1.75`
  - Code Blocks: `1.45`
- **Paragraph Spacing**: `1.0em` bottom margin. Never use consecutive `<br>` tags to fake paragraph rhythm.

## 2. Typography Stacks

1. **Reader Serif (Default for Wiki / Book / Longform)**:
   `Charter, "Bitstream Charter", "Sitka Text", Cambria, Georgia, serif`
2. **Modern Sans (UI Chrome / System Panels)**:
   `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
3. **Technical Mono (uCode, BASIC, Terminal, Datasets)**:
   `"Berkeley Mono", "SF Mono", Menlo, Monaco, "Courier Prime", monospace`

## 3. Strict Offline Citation Protocol

Under the sovereign uDos contract, the reader is a peaceful, self-contained local library:
- **Internal Wiki Links**: `[[Article Name]]` or `[Display Title](relative/path.md)` navigate directly between local vault documents without page reloads.
- **External Web References**: External URLs (`https://...`) do **NOT** link out to the live web. They render as static **citation chips**:
  ```html
  <span class="wiki-citation" data-source="web" title="Captured via BrowserUI">Source: example.com/article</span>
  ```
- **Web Intake**: `BrowserUI` is the designated tool for scraping and snapshotting external web content into `~/Vault/Clips` or `~/Public/Research`. Once clipped, the document lives locally forever.
