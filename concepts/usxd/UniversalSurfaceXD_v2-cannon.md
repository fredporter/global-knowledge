# UniversalSurfaceXD v2 — Grid, graphics, and portable surface canon

**Status:** locked (aligned with **uDOS v3**, 2026-04-09)  
**Scope:** cross-project surface declaration, grid–graphics contract, and transportable view model for uDOS v3  
**Implementation mirror:** [uDOS-v3 `docs/GRID-GRAPHICS-CANON.md`](https://github.com/fredporter/uDOS-v3/blob/main/docs/GRID-GRAPHICS-CANON.md) (web) · sibling path [`../../uDOS-v3/docs/GRID-GRAPHICS-CANON.md`](../../uDOS-v3/docs/GRID-GRAPHICS-CANON.md) when both repos are checked out side by side  
**Integrated checklist:** [usxd_udos_integrated_template.md](usxd_udos_integrated_template.md)

**Family:** uDOS-core, uDOS-thinui, uDOS-themes, uDOS-dev, browser GUI surfaces, TUI surfaces, Markdown export, SVG export

⸻

1. Purpose

UniversalSurfaceXD is the portable surface declaration format for uDOS.

It defines how a surface is composed semantically, spatially, and graphically across:
	•	TUI
	•	ThinUI
	•	browser GUI
	•	Markdown exports
	•	SVG/vector exports

It does not define runtime business logic.
It does not replace core state contracts.
It does not hardcode one renderer, theme, or framework.

UniversalSurfaceXD exists to let uDOS design once, then wire and render consistently across projects. It formalises the shared display grammar already implied by the spatial system, the canonical 80×30 canvas, the 16×24 tile raster, the teletext graphics bridge, the ThinUI/theme adapter split, and the emerging surface family for feeds, forms, story, workflow, tables and related views.          

⸻

2. Core statement

uDOS v3 defines all interactive and document-linked surfaces through a shared grid-graphics model.

That model is:
	•	canonical surface grid: 80 × 30
	•	canonical tile raster: 16 × 24
	•	canonical graphics encoding: teletext 2×3 mosaic masks
	•	required fallback ladder: Teletext → ASCII Block → Shades → ASCII
	•	portable surface spec: UniversalSurfaceXD
	•	transport rule: themes may change appearance, but not semantics

This follows the locked spatial/text-graphics baseline and the current rendering contract.        

⸻

3. Design goals

UniversalSurfaceXD must be:
	•	portable across runtimes
	•	renderer-neutral
	•	theme-neutral
	•	deterministic in canonical mode
	•	Markdown-friendly
	•	graphics-capable
	•	location-aware where needed
	•	safe to degrade in low-resource and recovery conditions

It must support the current family split where core owns semantics, ThinUI owns the low-resource takeover runtime, and themes own appearance, tokens, skins, fonts, loaders, and adapter mappings.      

⸻

4. Non-goals

UniversalSurfaceXD must not become:
	•	a second command engine
	•	a business logic layer
	•	a theme repo
	•	a React-only component schema
	•	a terminal-only drawing format
	•	a replacement for core state packets
	•	a replacement for spatial IDs or PlaceRef contracts

ThinUI already has a clear boundary: it renders state from core and emits events back, but does not own workflow logic or semantic truth. UniversalSurfaceXD follows the same boundary discipline.  

⸻

5. Canonical stack

The canonical v3 display stack is:

Core Semantic State
  -> Surface Definition (UniversalSurfaceXD)
  -> Canonical Grid Layout
  -> Graphics / Tile Encoding
  -> Theme Adapter Mapping
  -> Runtime Renderer
  -> Interaction Events back to Core

That extends the existing Core → ThinUI → Render → Event → Core loop into a portable cross-runtime surface model.  

⸻

6. Canonical geometry

6.1 Surface grid

The canonical surface grid is:

80 columns × 30 rows

The mini surface grid is:

40 columns × 15 rows

Canonical mode is fixed and deterministic. Adaptive mode may respond to runtime width, but canonical exports do not probe terminal size.    

6.2 Cell addressing

Cell coordinates follow the locked spatial cell scheme:
	•	columns: AA–DC
	•	rows: 10–39

Examples:

AA10
BJ10
DC39

This keeps surface-space and world-space mentally aligned, even when a surface is not a map.    

6.3 Tile raster

Each grid cell uses the canonical internal tile raster:

16 × 24 px

This is locked by the historical graphics spec and is the correct fit for rectangular text/block display while still supporting square subpixel logic via the teletext bridge.  

6.4 Teletext bridge

The canonical graphics encoding uses a teletext 2×3 occupancy mask.

Each teletext subcell can map cleanly to:

8 × 8 px

inside the 16 × 24 tile.

That gives a consistent bridge between:
	•	teletext masks
	•	block graphics
	•	text renderers
	•	SVG/vector renderers
	•	theme preview systems

The teletext mask model and its 64-pattern table are the source of truth; glyph lookup is an implementation detail.      

⸻

7. Canonical graphics contract

7.1 Encoding ladder

UniversalSurfaceXD graphics must support the locked fallback ladder:

Teletext -> ASCII Block -> Shades -> ASCII

This is mandatory for transportability and recovery-safe rendering.  

7.2 Character families

UniversalSurfaceXD may reference these families:
	•	strict ASCII
	•	Unicode box drawing
	•	Unicode shades
	•	Unicode block glyphs
	•	teletext masks

These are already defined in the consolidated graphics document and should remain the canonical family ladder for text-first rendering.  

7.3 Wide glyphs and emoji

Width-2 glyphs occupy a 2×1 tile footprint.

Canonical size:

32 × 24 px

This applies to emoji, wide glyph sprites, and other explicitly wide objects.  

⸻

8. Spatial and place model

UniversalSurfaceXD must support spatial awareness without forcing every surface to be map-like.

8.1 LocId

L{layer}-{cell}[-Z{z}]

8.2 PlaceRef

<ANCHOR>:<SPACE>:<LOCID>[:D<n>][:I<id>]

Examples:

L305-DA11
L305-DA11-Z2
EARTH:SUR:L305-DA11
GAME:skyrim:SUB:L402-CC18:D5:Iblackreach

These formats are already formalised in the spatial reference docs and should be reused directly, not forked.  

8.3 Surface relationship to place

A surface may be:
	•	non-spatial
	•	spatially anchored
	•	place-aware but not map-rendered
	•	directly map-rendered

Examples:
	•	a feed can be place-aware
	•	a story can start at a place
	•	a step-form can verify presence at a place
	•	a map surface can render place overlays directly

⸻

9. Surface kinds

UniversalSurfaceXD defines the following first-class surface kinds for v0.1:
	•	launcher
	•	panel
	•	table
	•	list
	•	board
	•	timeline
	•	feed
	•	story
	•	step-form
	•	slide
	•	map
	•	workflow
	•	recovery
	•	handoff

This formalises the current trajectory across rendering modes, feeds/spools, workflow panels, and step-form/presentation rules.      

⸻

10. Story, step-form, and slide family

UniversalSurfaceXD treats story, step-form, and slide as one related family with three render modes.

10.1 Story

Narrative-first.
May include prose, media, calls to action, and optional choices.

10.2 Step-form

Input-first.
Must follow the current rules:
	•	preferred for multi-field setup
	•	one primary action per step
	•	secondary actions remain visible but subordinate
	•	progress must be shown when more than one step exists

These rules come directly from the current step-form and presentation-flow canon.  

10.3 Slide

Presentation-first.
Read-mostly.
Pagination/frame-based.
Compatible with Markdown presentation patterns such as Marp-style flows by design, though slide syntax compatibility is an adapter concern rather than the canonical source structure.

10.4 Shared attributes

All three may share:
	•	title
	•	subtitle
	•	lede
	•	steps[]
	•	frames[]
	•	prompt
	•	choices
	•	input
	•	progress
	•	confirm
	•	notes
	•	media
	•	adapterHints

⸻

11. Feed family

Feeds are a first-class surface kind, not a derivative of logs.

The current feed/spool direction already separates:
	•	logs as execution records
	•	feeds as meaningful change streams
	•	spools as local feed retention/transformation

UniversalSurfaceXD should represent feed surfaces directly rather than deriving them from raw logs.    

Recommended feed-oriented surface patterns:
	•	feed browser
	•	digest view
	•	spool manager
	•	feed builder

These already appear as candidate UI surfaces in the feed/spool pathway notes.  

⸻

12. Region grammar

All surfaces should be composed from a shared region grammar.

12.1 Canonical region roles
	•	header
	•	nav
	•	primary
	•	secondary
	•	status
	•	footer
	•	overlay
	•	modal
	•	canvas
	•	legend
	•	inspector
	•	timeline
	•	queue
	•	controls

12.2 Examples

Feed
	•	header
	•	primary
	•	optional inspector
	•	status

Step-form
	•	header
	•	primary
	•	controls
	•	status

Slide
	•	canvas
	•	optional notes
	•	optional controls

Map
	•	canvas
	•	legend
	•	status

Workflow
	•	header
	•	timeline
	•	inspector
	•	status

This keeps all renderers working from the same layout grammar.

⸻

13. Object families

UniversalSurfaceXD should recognise the minimum object families already implied by the current rendering docs:
	•	location
	•	task
	•	schedule_item
	•	workflow_step
	•	event
	•	object/sprite

These are directly aligned with the grid/text rendering spec.  

It should additionally formalise surface-level families:
	•	tile.object
	•	tile.sprite
	•	tile.marker
	•	tile.ui
	•	surface.panel
	•	surface.table
	•	surface.list
	•	surface.feed
	•	surface.story
	•	surface.slide

The first four match the locked tile taxonomy in the spatial/text-graphics baseline.    

⸻

14. Theme mapping rule

Themes are render dialects, not alternate app architectures.

That is already consistent with the current repo boundaries:
	•	core owns semantics
	•	ThinUI owns the low-resource GUI runtime
	•	themes own appearance, tokens, adapters, fonts, loaders, and skins

UniversalSurfaceXD must preserve that split.    

14.1 Canonical theme families

Initial families include:
	•	thinui-c64
	•	thinui-teletext
	•	thinui-nes-sonic
	•	udos-default
	•	material3-surface
	•	minimal-safe

The retro ThinUI lanes are already explicitly named in the ThinUI runtime and adapter docs.    

14.2 Theme responsibilities

Themes may map:
	•	typography
	•	spacing and density
	•	borders and surfaces
	•	focus treatment
	•	status treatment
	•	loaders
	•	safe fallbacks

Themes must not alter:
	•	business logic
	•	semantic meaning
	•	interaction identity
	•	state truth

⸻

15. Runtime targets

UniversalSurfaceXD must support at least these target lanes:
	•	tui
	•	thinui
	•	browser
	•	markdown
	•	svg

15.1 TUI

Text-first.
Width-safe.
Deterministic in canonical mode.  

15.2 ThinUI

Single-window, fullscreen-capable, low-resource, recovery-safe GUI runtime.    

15.3 Browser

Rich GUI lane.
May use Material 3 or other theme adapters.

15.4 Markdown

Canonical documentation and binder export lane.
Must preserve fenced text/diagram integrity.  

15.5 SVG

Optional vector export lane.
Useful for diagrams, graphics generation and higher-fidelity output, but not the canonical source of truth for surface semantics.  

⸻

16. Transportability rule

A UniversalSurfaceXD surface is only valid if it is transportable.

Transportable means:
	•	semantics survive theme changes
	•	layouts survive renderer changes
	•	actions survive density changes
	•	recovery mode preserves meaning
	•	Markdown export preserves readable intent
	•	canonical mode is deterministic

This rule follows directly from the broader family boundary discipline and the deterministic render contract.    

⸻

17. Canonical schema shape

The following is the proposed v0.1 schema shape.

surface:
  id: "feed-main"
  version: "usxd/0.1"
  title: "System Feed"
  kind: "feed"
  mode: "canonical"

  grid:
    cols: 80
    rows: 30
    tile_px:
      w: 16
      h: 24
    graphics:
      canonical: "teletext-2x3"
      fallback:
        - "ascii-block"
        - "shades"
        - "ascii"

  place:
    place_ref: "EARTH:SUR:L305-DA11"

  theme:
    family: "thinui-c64"
    density: "compact"

  regions:
    - id: "header"
      rect: { x: 0, y: 0, w: 80, h: 3 }
      role: "header"

    - id: "stream"
      rect: { x: 0, y: 3, w: 56, h: 24 }
      role: "primary"

    - id: "inspector"
      rect: { x: 56, y: 3, w: 24, h: 24 }
      role: "secondary"

    - id: "status"
      rect: { x: 0, y: 27, w: 80, h: 3 }
      role: "status"

  bindings:
    source: "feeds.fetch"
    params:
      spool: "local/default"

  objects:
    - id: "feed-list"
      type: "surface.feed"
      region: "stream"
      item_template: "feed-card"

    - id: "digest"
      type: "surface.panel"
      region: "inspector"

  actions:
    - id: "refresh"
      label: "Refresh"
      kind: "primary"

    - id: "open-spool"
      label: "Open Spool"
      kind: "secondary"

  adapters:
    tui: "tui-default"
    thinui: "thinui-default"
    browser: "material3-surface"
    markdown: "markdown-diagram"
    svg: "svg-surface"

  fallback:
    safe_mode_theme: "minimal-safe"
    reduced_view: "list"

This schema is a synthesis of the locked grid, graphics, feed, form, and runtime contracts rather than a verbatim existing file. It is intended as the first formal UniversalSurfaceXD declaration shape.

⸻

18. Graphics object block

UniversalSurfaceXD may include graphics objects for tile-accurate render assets.

graphics_objects:
  - id: "logo"
    type: "tile.sprite"
    loc: "L305-DA11"
    footprint: "2x1"
    encoding:
      type: "teletext-mask"
      frames:
        - ["0x30", "0x3C", "0x3F", "0x0C"]

  - id: "divider"
    type: "rule"
    encoding:
      type: "line"
      style: "single"

This keeps teletext masks canonical while allowing later SVG/vector export or theme-resolved rendering.

⸻

19. Step-form example

surface:
  id: "setup-runtime"
  version: "usxd/0.1"
  title: "Setup Runtime"
  kind: "step-form"
  mode: "canonical"

  grid:
    cols: 80
    rows: 30
    tile_px: { w: 16, h: 24 }
    graphics:
      canonical: "teletext-2x3"
      fallback: ["ascii-block", "shades", "ascii"]

  theme:
    family: "thinui-teletext"
    density: "comfortable"

  progress:
    current: 2
    total: 5
    label: "Runtime Name"

  steps:
    - id: "choose-mode"
      type: "choice-grid"
      prompt: "Choose runtime mode"
      choices:
        - "local"
        - "browser"
        - "hybrid"

    - id: "name-runtime"
      type: "input-field"
      prompt: "Name this runtime"
      placeholder: "uDOS Station"

  actions:
    - id: "continue"
      label: "Continue"
      kind: "primary"

    - id: "back"
      label: "Back"
      kind: "secondary"

This is aligned with the current canonical step-form posture and adapters.  

⸻

20. Story/slide example

surface:
  id: "welcome-story"
  version: "usxd/0.1"
  title: "Welcome to uDOS"
  kind: "story"
  mode: "canonical"

  frames:
    - id: "intro"
      title: "A system of surfaces"
      lede: "Design once, render everywhere."
      body:
        - "uDOS uses a shared grid-graphics model."
        - "Themes are render dialects, not separate apps."

    - id: "handoff"
      title: "Choose your lane"
      body:
        - "TUI for text-first control"
        - "ThinUI for local low-resource panels"
        - "Browser for rich workspace views"
      cta:
        label: "Start"
        action: "continue"

A slide version of the same surface would mostly differ by adapter treatment, frame pacing, and presenter semantics.

⸻

21. Feed example

surface:
  id: "ops-feed"
  version: "usxd/0.1"
  title: "Operations Feed"
  kind: "feed"

  bindings:
    source: "feeds.fetch"
    params:
      feed_type: "event"
      spool: "ops"

  regions:
    - id: "header"
      rect: { x: 0, y: 0, w: 80, h: 3 }
      role: "header"
    - id: "primary"
      rect: { x: 0, y: 3, w: 80, h: 24 }
      role: "primary"
    - id: "status"
      rect: { x: 0, y: 27, w: 80, h: 3 }
      role: "status"

  objects:
    - id: "events"
      type: "surface.feed"
      region: "primary"

This gives feeds a proper surface identity and avoids collapsing them into raw log output.

⸻

22. Wiring rule for uDOS-dev

UniversalSurfaceXD should be wired through uDOS-dev using this pathway:

Designer / Author
  -> UniversalSurfaceXD file
  -> schema validation
  -> surface compile / resolve
  -> adapter mapping
  -> runtime render
  -> event contract back to core

Recommended responsibilities:
	•	uDOS-core
	•	semantic truth
	•	state contracts
	•	event semantics
	•	uDOS-dev
	•	schema validation
	•	compile checks
	•	cross-repo wiring
	•	adapter installation
	•	pathway verification
	•	uDOS-thinui
	•	ThinUI runtime rendering
	•	low-resource fallback handling
	•	uDOS-themes
	•	theme families
	•	token mappings
	•	surface adapters

This keeps ownership aligned with current repo boundaries.    

⸻

23. Validation rules

A UniversalSurfaceXD document must validate:

Required
	•	surface.id
	•	surface.version
	•	surface.kind
	•	surface.grid.cols
	•	surface.grid.rows
	•	surface.grid.tile_px.w
	•	surface.grid.tile_px.h
	•	surface.grid.graphics.canonical
	•	at least one runtime adapter target

Canonical constraints
	•	cols = 80 and rows = 30 in canonical mode
	•	tile_px = 16 × 24
	•	canonical graphics encoding must be teletext-2x3
	•	fallback ladder must include ascii
	•	region rectangles must be integer-aligned
	•	actions must have stable IDs
	•	step IDs must not duplicate within a story/step-form/slide surface

The no-duplicate-step rule is already explicit in the current step-form rules.  

⸻

24. Anti-patterns

Do not allow UniversalSurfaceXD to become:
	•	a dumping ground for renderer-specific CSS
	•	a JSX tree in disguise
	•	a duplicate core state schema
	•	a theme-specific branch explosion
	•	a free-form coordinate system unrelated to the canonical grid
	•	a slide/story/form split with incompatible data models
	•	a feed surface that is secretly just raw logs

These anti-patterns would break transportability and cross-project alignment.

⸻

25. Immediate lock recommendations

The following rules should be locked now for v3:
	1.	Canonical viewport = 80×30
	2.	Canonical tile raster = 16×24
	3.	Canonical graphics encoding = teletext 2×3
	4.	Fallback ladder = Teletext → ASCII Block → Shades → ASCII
	5.	UniversalSurfaceXD = canonical portable surface format
	6.	Story, step-form, and slide = one family
	7.	Feed = first-class surface kind
	8.	Themes = render dialects, not alternate architectures

These are either directly specified in the current docs or are the cleanest formal synthesis of them.          

⸻

26. Closing statement

UniversalSurfaceXD should now become the formal bridge between:
	•	the historical spatial/grid canon
	•	the locked text-graphics model
	•	ThinUI runtime surfaces
	•	theme adapter families
	•	browser Material 3 surfaces
	•	feed, workflow, story, step-form, and slide views
	•	transportable uDOS design files

It gives uDOS one display universe instead of several parallel ones.

⸻

27. UX designer default theme (2026-04-09)

The **UniversalSurfaceXD** `browser-mockup` default dark shell uses the same **reference palette** and **`--udos-*` grid CSS variables** as uDOS v3 [style-guide.md](https://github.com/fredporter/uDOS-v3/blob/main/docs/style-guide.md) §2. Mapping table: [../udos-v3-style-bridge.md](../udos-v3-style-bridge.md). Lab reference: `/lab/grid-canon`.

⸻
