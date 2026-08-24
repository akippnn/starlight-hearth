# Current status

**Last updated:** 2026-08-25
**Current phase:** HSN-001 ready for implementation
**Active implementation slice:** none
**New owner verdict:** pending

This is the single mutable delivery-status authority for `starlight-hearth`.

## Current work

The documentation foundation is clean at
`6b544e02c3c9a70985b886672482e92c135032f3`. The owner approved
`HSN-001 — Hearth-native Launcher Nucleus`; its frozen contract revision is
`17fedae8776ff38b53c07d4098d8ee8b13852253`.

Delivery state is `ready`; owner verdict remains `pending`. Implementation may
now begin, but no provider, consumer, package, image, or target proof exists.

## Superseded phase statement

The complete 2026-08-24 handoff and later planning decisions were
reconciled into canonical product, architecture, requirement, decision,
behavior, roadmap, and open-question documents. This work changes
documentation only.

It does **not**:

- freeze or activate a product slice;
- implement Hearth Shell, App Menu, Bar, OSK, Settings, Portal, wallpaper, or
  Gaming Mode behavior;
- change the OCI image, packages, configuration, InputPlumber, niri, deployed
  host, or `starlight-hearth-shell` repository;
- create an audit target;
- claim audit-readiness or owner acceptance.

## Historical status

| Record | Delivery state | Owner verdict | Current interpretation |
| --- | --- | --- | --- |
| VS-001 / HS-001 | Superseded | Rejected for controller-ready outcome | Boot, identity, TV-scale, niri/DMS startup, and recovery evidence remain historical facts. |
| VS-002 / HS-002 | Superseded | Not accepted | Input/session handoff and packaging evidence remain useful; it did not establish an accepted controller-native desktop. |
| HS-003 | Superseded | Pending/no owner verdict | Feature-branch implementation evidence exists; no owner-visible Hearth-native result is claimed. |

The old DMS-derived-product decision is superseded by ADR-0006. The semantic
controller architecture remains reusable under ADR-0007. Historical ADRs,
contracts, and evidence retain their original wording and must be interpreted
through these newer authorities.

## Accepted planning decisions

- Hearth-owned Quickshell/QML shell on unmodified niri.
- DMS as selective reference/donor, not maintained product.
- `GPL-3.0-only` shell governance with an exact import ledger.
- Rust companion plus QML UI, transient application launches, and layered JSON
  configuration.
- Explicit Navigation/Text modes and current semantic input defaults.
- Right-drawer App Menu with exactly Grid/List modes.
- wvkbd-derived OSK architecture and privacy/geometry/input behavior.
- Hearth Bar visible for hover, focus, or any owned open panel.
- Dolphin retained with a dormant Index/MauiKit file-manager contingency.
- Explicit decision lifecycle and owner-only product acceptance.

These are accepted and reopenable planning decisions. None is
`Frozen-for-slice`.

## Repository and deployment state

The documentation work began from `starlight-hearth` `main` at
`aec9dc874da5c4c698ca74073fc087f449454e74`. The former dirty HS-003 worktree
was preserved in its branch, a named Git stash, and an external verified
archive before switching to `main`.

`starlight-hearth-shell`, its DMS ancestry, runtime code, and the deployed host
remain unchanged. The eventual shell-history reset and hard runtime rename are
future separately authorized operations.

Existing image/build metadata may still project historical VS-002 state. No
new image may be built or presented as current until a later non-documentation
change reconciles those non-document public projections against this status.

## Next gate

Archive and verify the historical shell repository, create the clean orphan
HSN-001 branch, and begin implementation against the exact contract above. No
target or artifact proof exists yet.
