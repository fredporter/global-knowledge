# Sovereign Communications Loop & Tasker Autonomy Specification

**Version**: 1.0.0
**Authority**: Wizard (System Architect / Canonical Standards)
**Status**: Canonical Standard (Layer 0 Base Canon)

---

## 1. Principles

1. **Zen Ecosystem Contract Hierarchy**:
   - Host OS Native (Apple Events / Shortcuts CLI / notify-send / say)
   - Ecosystem Service (uCore Feed / Spool / Binders / Tasker)
   - Vendor Components
   - Custom Code
2. **Offline-First & Sovereign**: No cloud dependency, no telemetry, fail-closed read-only canon, local persistence in `~/.udos/flow/tasks/` or local Vaults.
3. **Explicit Autonomy & Approval Gates**: Automation proposals must never execute destructively or autonomously without an explicit user approval step (`pending_approval` $\to$ `approved` $\to$ `executed`).

---

## 2. Inbound Communications Loop

- **Apple Mail**: Non-invasive intake via JXA (`POST /api/host/mail/intake`), filtering unread or flagged messages without auto-launching background apps.
- **Apple Messages**: Read-only conversation digest intake via JXA (`POST /api/host/imessage/intake`).
- **Apple Reminders**: Inbound querying of incomplete reminders across lists (`POST /api/workflow/sync/apple-reminders/inbound` and `GET /api/host/reminders/intake`).
- **Apple Notes**: Selective scratchpad intake by folder (`GET /api/host/notes/intake`).
- **Safari Research Tabs**: Active tab metadata extraction and capture into feed research cards (`GET /api/host/safari/active`, `POST /api/host/safari/intake`).

---

## 3. Action-to-Task & Task-to-Action Architecture

### Action-to-Task
Inbound events from Mail, Safari, or Notifications are transformed into sovereign `.tasker` Markdown notes with YAML frontmatter:
```yaml
---
id: act_20260916_review
board: inbox
status: todo
priority: high
source: apple_mail
source_id: msg_882194
binder: GridCore
due: '2026-09-17T18:00:00Z'
action_type: archive_mail
approval_status: pending_approval
---
# Review Vector Lattice Spec

## Summary
Approval request for Teletext Mode 7 quantization.
```

### Approval Gates & Task-to-Action
Tasks with associated automation actions require explicit human sign-off:
1. `pending_approval`: Actions are staged but cannot be dispatched by autonomous daemons.
2. `approved`: User clicks "Approve" in the UI or invokes `POST /api/workflow/tasks/{task_id}/approve`.
3. `executed`: Host automation is performed (Shortcuts CLI, Reminders export, Mail archival, or desktop notification) and logged to the Feed Activity Pod.
4. `rejected`: User rejects the action with an optional recorded reason.

---

## 4. Bidirectional Apple Sync

- **Reminders $\leftrightarrow$ Tasker**:
  - Inbound: Apple Reminders sync into `.tasker` inbox or binder with full due date / deadline preservation.
  - Outbound: Active tasks from a specified Binder (e.g. `uDos`, `GridCore`, or all binders `*`) are exported out to Apple Reminders (`POST /api/workflow/sync/apple-reminders/outbound`).
  - Native Host Sync: Apple Reminders automatically handles iCloud synchronization to iPhone, iPad, and Apple Watch natively.

---

## 5. Aggregated System Sync Health

`GET /api/host/sync/status` returns real-time status across:
- **Apple PIM**: Reminders, Notes, Mail, Messages availability and bidirectional readiness.
- **Google Drive Mirror**: Local `~/Vault` status and CloudStorage mount verification.
- **BitChat Mesh**: Local node ID and LAN peer count on port 53535.
