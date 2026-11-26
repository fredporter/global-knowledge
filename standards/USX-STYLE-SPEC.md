# USX surface style

Version 1.1.0. Universal baseline for uDOS interfaces. [USX standards data](USX-STANDARDS.json) records default scales and asset presets. The shared `@udos/usx-tokens` package implements the CSS, and the Engineering Recipe Gallery shows how the patterns fit together.

## Colour

USX colour follows the [Bootstrap 6 colour system](https://getbootstrap.com/docs/6.0/customize/color/): a 13-stop palette per hue (`025`–`975`), semantic roles assigned per colour mode, and a contrast partner for every fill.

- **Palette.** `tokens-color.css` carries the Bootstrap 6 base hues as sRGB stops (`--usx-color-{hue}-{stop}`). USX declares the stops it consumes; the formula is Bootstrap's white-tint / black-shade mix, so adding a stop stays compatible.
- **Role mapping.** `primary`=blue, `success`=green, `danger`=red, `warning`=yellow/amber, `info`=cyan, `secondary`=gray. `accent` maps to indigo once those stops are declared.
- **Roles per colour.** `--usx-color-{role}` is both the foreground on canvas and the fill for badges; `-surface` and `-border` carry containers; `on-{role}` is the contrast partner. Light mode uses the 600/700 stops with white contrast; `themes/dark.css` swaps to the 400 stops with 900-stop contrast.
- **Contrast is enforced.** `scripts/check_content_contract.py` measures every role pair against each theme's canvas. Light, dark and high-contrast must pass `4.5:1`; `c64` and `teletext` report as warnings because retro palettes belong inside the GridCore viewport.
- **Latitude.** If a colour is only ever a fill, use the `500` stop; if it carries text, use the role token. Do not improvise a hex.


- Use AppShell and GlobalToolbar for shared navigation. A hosted surface does not add a second Dashboard or back bar. Keep surface tabs for views within the surface.
- Use the shared semantic canvas, surface, text, border and status tokens. Keep body and muted text legible in light and dark. Use `--usx-color-warning` for warnings. Keep retro display palettes inside the GridCore viewport. The gallery's local theme overrides are preview styling.
- Use `UIcon` with Material Symbols for web actions and `.usx-btn` for buttons. Use links for navigation, label icon-only controls and preserve visible keyboard focus. Use an explicit label and confirmation for destructive actions. Status text must remain meaningful without color.
- Use the shared spacing, radius and typography scales. Let cards and form fields reflow in the space available. Keep the primary action reachable with a keyboard and on narrow or touch layouts. Use the shared control and touch target sizes.
- Use the Prose typography policy for document content, with a comfortable measure up to 72ch. Preserve heading hierarchy, code, tables and document navigation. Keep reader chrome and editor controls outside the prose body.

## Recipe reference

The recipe identifier selects a presentation pattern. Its version describes the recipe payload. Fixture copy, statuses and actions demonstrate layout and do not establish product behavior.

| Recipe | Use it for | Keep visible |
| --- | --- | --- |
| `task-list` | A list of work by status | Task title, status and next action |
| `authoring-workbench` | Writing and source review | Document context, editor and citation provenance |
| `prose-document` | Reading a structured document | Title, headings and navigable document content |
| `card-matrix` | Browsing a collection or opening a surface | Item label and destination, with detail as space permits |
| `settings-form` | Editing settings by section | Field labels, help, validation and save state |
| `story-form` | Guided form entry | Current step, progress and a way to return |
| `system-page` | A diagnostic or fallback page | Status, explanation and an actionable next step |
| `alerts-suite` | Feedback at the point of use | Severity in words, context and any required action |

Review each pattern at the gallery's 360, 768 and 1200 CSS pixel widths and at fluid width. Check light and dark, keyboard focus, text wrapping, long and empty content, and the relevant loading, error or confirmation state. Treat the viewport switch as a layout check. Verify touch, keyboard and assistive technology behavior in the working surface.

Use [GridCore's lattice and display profiles](GRIDCORE-LATTICE-SPEC.md) for the content inside a character canvas. Its host controls still follow the USX rules above.

[Engineering recipe source](https://github.com/fredporter/uCore/tree/c873b1fed425c3572a1c334a163fb9d4fab73c1e/frontend-vue/src/recipes) · [Shared token implementation](https://github.com/fredporter/uCore/tree/c873b1fed425c3572a1c334a163fb9d4fab73c1e/packages/usx-tokens)
