# Current status

Last updated: 2026-08-22

This is the single current-status source for `starlight-hearth`.

## Active slice

**VS-002 — Controller Handoff and Hearth Home** is **in implementation**.

VS-001 is **superseded and not accepted**. It proved signed image boot, niri,
upstream DMS, television scaling, hearthOS identity, KDE/TTY/atomic recovery,
and repeated build signing. Its owner audit disproved the claimed
controller-ready outcome: navigation depended on Steam's partial desktop map,
DMS was primarily pointer-oriented, and controller reconnection did not restore
deterministic Desktop ownership. The original evidence remains in
[`evidence/VS-001.md`](evidence/VS-001.md).

VS-002 replaces the failed ownership model with:

- Hearth Shell, an upstream-tracking DMS fork released as the exact
  `starlight-hearth-shell` RPM while retaining compatibility interfaces;
- InputPlumber-owned session profiles for the Pro 3 receiver `2dc8:310b`;
- a fail-safe adapter that prevents Steam Input and Desktop mappings from being
  active simultaneously and records state under `/run/hearth`;
- controller-native Home, power, on-screen keyboard, TV layouts, focus rings,
  vim navigation, and top-right notifications;
- complete visible hearthOS identity while preserving Bazzite/Fedora
  compatibility and provenance fields.

## Verification state

| Gate | State | Evidence |
|---|---|---|
| Frozen DMS fork baseline | Pass | Upstream `20aafebd87f0340c24b585180ab36339d6b154ad`; submodule `fbbdddc47b5564dcf67aa05bd7bf1d3af8f5aad5` |
| Shell Go and Hearth tests | Pass locally | Fedora 44 x86_64 on `aki@bazzite` |
| Nested niri/Quickshell smoke | Pass locally | Shell remained alive for the bounded run; one discovered QML import defect was repaired |
| Shell RPM build/install | Pass | Published Fedora 44 x86_64 RPM; package replacement, ownership, embedded QML, and non-root version checks pass on `aki@bazzite` |
| InputPlumber schema validation | Pass locally | Installed Bazzite 0.78.0 schemas validate composite and both profiles |
| hearthOS repository contracts | Pass locally | 30 tests on x86_64 Bazzite; current count recorded in VS-002 evidence |
| Public shell repository/release | Pass | Signed `hearth-v0.1.0-7` at `49456632b17ba962755c2dd18376d9a859eaf11a`; release workflow run `32517193618` passed |
| Pinned shell RPM in image | Pass | Exact release URL and SHA-256 `22f38a85e78928fb00fbe7b59467b2a0c0794ae887687f34fc87c55c02d72603`; checksum failure blocks installation |
| Complete signed OCI build | Pending | Required before audit-ready |
| Owner controller audit | Pending | Owner-only hardware proof and verdict |

No agent may mark VS-002 accepted. The highest agent-controlled state is
`audit-ready` after every non-owner gate and a signed candidate are complete.

## Scope boundaries

Decky, CSS Loader, Framegen, general application coverage, secure lock/session
lifecycle, Ember, NVIDIA support, telemetry, cloud services, Tauri, CLI
diagnostics, and KDE removal are outside VS-002.
