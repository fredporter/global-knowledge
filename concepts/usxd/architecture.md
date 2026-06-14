# Architecture

## Objective

Create an independent UX repository that can serve MDC native apps, ThinUI browser interfaces, GitHub Pages-flavoured documentation surfaces, and terminal implementations without forcing all UI work into any one product repo.

**MDC v2.6:** Consumer MDC is now defined as the **App Store–ready Apple surface** for the uDOS family, with a three-layer split (App Store surface / orchestration core / uDOS family). See [v2.6/shared-architecture-contracts.md](v2.6/shared-architecture-contracts.md).

## Repository layers

### Spine
Canonical design layer:

- tokens
- component names
- state semantics
- layout grammar
- information hierarchy
- interaction contracts

### Staff
Support layer that helps teams consume the spine:

- Storybook setup
- token export scripts
- Swift bridge examples
- TUI bridge examples
- wireframe helpers

### Browser mockup
Low-risk SvelteKit playground for trying layout families before implementation is promoted downstream.

## Contract with product repos

This repo informs and supports:

- `mdc-ios-app`
- `mdc-mac-app`
- `UDOS-thinu`
- `uDOS-shell`
- `uHOME-client` and kiosk-oriented surfaces
