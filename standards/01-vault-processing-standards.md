---
title: "Vault Processing Standards"
type: spec
status: approved
version: 1.0.0
binder: "#standards"
tags: [vault, processing, standards, binder]
created: 2026-05-04
updated: 2026-05-04
author: fred
related:
  - "../#udos/01-architecture.md"
  - "https://jsonfeed.org/version/1.1"
---

# Vault Processing Standards

This document defines the processing standards for all binder documents in the uDos Vault.

## Overview

The uDos Vault uses a **binder-based organization** where documents are grouped by topic into binder directories. Each binder has a manifest (`binder.yaml`) and follows a standard processing pipeline.

## Frontmatter Requirements

Every binder document **must** include the following frontmatter fields:

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Document title |
| `type` | Yes | One of: spec, guide, reference, tutorial, roadmap |
| `binder` | Yes | Binder topic name (e.g., `#standards`) |
| `status` | Yes | One of: draft, reviewed, approved, archived |

## Processing Pipeline

The binder processing pipeline consists of these passes:

1. **deduplicate** — SHA-256 content hashing to find duplicates
2. **frontmatter-enrich** — Auto-fill missing frontmatter fields
3. **link-validate** — Check internal and external links
4. **generate-index** — Create JSON feed and search index

## JSON Feed Output

Each processed binder produces a JSON Feed file at `~/uDos/shared/feeds/<topic>.json` following the [JSON Feed v1.1](https://jsonfeed.org/version/1.1) specification.
