# GridCore Dot Lattice & Vector-to-Bitmap (V2B) Specification

- **Version**: 1.1.0
- **Authority**: Wizard (System Architect / Canonical Standards)
- **Status**: Canonical Standard (Layer 0 Base Canon)
- **Standards data**: [GRIDCORE-STANDARDS.json](GRIDCORE-STANDARDS.json)

---

## 1. Geometric Invariant: The Atomic Dot

All GridCore 2D rendering, mosaic mapping, typography, and sprite blitting are anchored on a single atomic invariant:

$$\mathbf{1\text{ dot}} = 4\times 4\text{ logical raster pixels}$$

Quantize positions in logical raster coordinates. Viewport fitting and device pixel ratio govern the final display scale. Preserve the selected cell register and keep raster glyphs and mosaics crisp when scaling.

---

## 2. Cell Registers & Pitches

| Register | Dimensions (Dots) | Dimensions (Pixels) | Aspect Ratio | Primary Target |
|---|---|---|---|---|
| **Dot** | $1\times 1$ | $4\times 4$ | 1:1 | Atomic coordinate step |
| **Square Cell** | $2\times 2$ | $8\times 8$ | 1:1 | Gaming, Nethack, roguelike, retro tilemaps |
| **Tall Cell** | $3\times 5$ | $12\times 20$ | 3:5 | Teletext Mode 7 and character-grid reading |
| **Super Cell** | $6\times 10$ | $24\times 40$ | 3:5 | Universal column/row pitch container |

### Super Cell Invariant
A single **Super Cell** ($24\times 40\text{ px}$) harmonizes square and tall grids:
- Accommodates exactly **$3\times 5$ Square Cells** ($3 \times 8\text{ px} = 24\text{ px}$; $5 \times 8\text{ px} = 40\text{ px}$).
- Accommodates exactly **$2\times 2$ Tall Cells** ($2 \times 12\text{ px} = 24\text{ px}$; $2 \times 20\text{ px} = 40\text{ px}$).
- **Column Pitch**: 24 px (6 dots). 3 square columns equal 2 tall columns (3:2 ratio).
- **Row Pitch**: 40 px (10 dots). 5 square rows equal 2 tall rows (5:2 ratio).

---

## 3. Recipe display profiles

| Recipe | Canvas | Glyphs | Composition |
| --- | --- | --- | --- |
| `teletext-mode7` | 40 columns × 25 rows | Bedstead, tall register | Header at row 0, up to 23 body rows, Fastext at row 24 |
| `terminal-ansi` | 42 columns × 27 rows | Press Start 2P, square register | 40 × 25 active area with a one-cell border |

The Mode 7 matrix has a 480 × 500 logical raster before fitting. The traditional 4:3 presentation describes the display, and the matrix retains 40 × 25 addressable cells. G1 mosaics divide a cell into a 2 × 3 mask. Use the canonical bit mapping and glyph or mosaic renderer. Derive boundaries within each cell to avoid accumulated rounding and use the existing character mapping for text export.

GridCore colors are palette indices. Both gallery canvases use the default eight-color palette. In the Teletext fixture, SGR 30–37 select foreground indices 0–7, SGR 1 enables bold, and SGR 0 resets the style. Escape sequences occupy no cells. This preview input is distinct from native Mode 7 control codes, and the terminal preview is a fixed composition rather than a full ANSI emulator.

The canonical palette and the lattice geometry live in [GRIDCORE-STANDARDS.json](GRIDCORE-STANDARDS.json). `gridcore.css` mirrors them as `--gridcore-palette-0..7` and `--gridcore-dot`, `--gridcore-cell-*`, `--gridcore-pitch-*`, `--gridcore-teletext-*`. The palette is theme-independent: a lattice does not recolour when the Prose theme changes, and the checker fails if the code drifts from the standards data.

Scaling is integer-only. A lattice declares `[data-lattice]` with a `--gridcore-zoom` step of `1`, `2` or `3` and is never scaled fractionally by a display profile, because fractional scaling blurs the 4px dot and the glyph raster.

Use the terminal renderer dimensions above when reviewing the gallery. The sample payload advertises 80 × 25 and pane widths, but the renderer uses the fixed 42 × 27 canvas and its own pane truncation. Check that content stays within its cells, the Teletext footer remains visible and the terminal border survives resizing. Use [USX surface style](USX-STYLE-SPEC.md) for the buttons and navigation around the viewport.

---

## 4. Vector-to-Bitmap (V2B) Quantizer Pipeline

Vector curves and SVG paths are snapped and quantized to the dot lattice using three algorithms:

1. **Lattice Snapping**: Snaps arbitrary floating-point 2D coordinates and SVG path `d="..."` commands (`M`, `L`, `C`, `Q`, `Z`) to nearest dot step ($4\text{ px}$) boundaries.
2. **Teletext G1 Quantization**: Renders SVG geometry into a $40\times 25$ character grid, mapping each cell's sub-pixel raster to its canonical G1 Teletext character code.
3. **BOB Blitter Rasterization**: Generates Amiga-inspired Blitter Objects (BOBs) with planar mask bitplanes and bounding boxes snapped to whole $8\times 8$ or $16\times 16$ tile registers.

---

## 5. REST API Endpoints (uCore)

- `GET  /api/vector/lattice/spec`: Read-only JSON definition of the Dot Lattice.
- `POST /api/vector/quantize/lattice`: Snap coordinates or SVG paths to the dot lattice.
- `POST /api/vector/quantize/teletext-g1`: Quantize vector graphics into 40x25 Teletext Mode 7 lines.
- `POST /api/vector/quantize/bob`: Quantize vector graphics into BOB blitter sprite definitions.
