# ADR-0006 — Hearth-native shell, reuse, and licensing

**Status:** accepted architecture decision; no implementation slice authorized
**Date:** 2026-08-25
**Supersedes:** ADR-0002 and ADR-0003 only where they define DMS as the maintained product or require DMS compatibility surfaces

## Decision

Build Hearth Shell as a Hearth-owned Quickshell/QML shell on unmodified niri.
DMS remains a reference and selective code donor, not the product foundation.
The target runtime performs a hard Hearth rename and does not preserve
`/usr/bin/dms`, `dms.service`, DMS IPC names, or DMS configuration paths as
compatibility contracts.

Adopt `GPL-3.0-only` for Hearth Shell so the project may deliberately combine
compatible GPLv3 donors such as Clavis and Caelestia while also using
compatible MIT and Apache-2.0 work. Preserve upstream histories when forking,
and maintain a per-file import ledger with exact revisions, licenses,
modifications, and notices.

Use Clavis as the primary niri-native architectural donor, Caelestia as the
primary visual/motion donor, DMS for selected system integrations and existing
Hearth work, and M3Shapes where its packaging and performance pass later
evaluation. Do not import a donor wholesale merely because its license is
compatible.

## Retained decisions

- niri remains unmodified upstream compositor infrastructure.
- `starlight-hearth` and `starlight-hearth-shell` retain separate release and
  ownership boundaries.
- Exact shell artifacts are pinned by revision and checksum.
- Semantic controller routing remains valuable independently of DMS.
- KDE recovery remains until a separate owner-accepted retirement outcome.

## Consequences

The existing DMS ancestry and feature branches are historical/salvage sources.
They are not merged wholesale into the new foundation. A later repository
maintenance operation will archive the full graph before establishing clean
canonical shell history. This ADR does not perform that operation or authorize
runtime implementation.
