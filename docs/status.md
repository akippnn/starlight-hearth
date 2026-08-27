# Current status

**Last updated:** 2026-08-28
**Current phase:** HSN-001 RC.2 clean local candidate and owner visual gate
**Active implementation slice:** HSN-001
**New owner verdict:** pending

This is the single mutable delivery-status authority for `starlight-hearth`.

## Current work

The documentation foundation is clean at
`6b544e02c3c9a70985b886672482e92c135032f3`. The owner approved
`HSN-001 — hearthOS Launcher Nucleus`; its frozen contract revision is
`17fedae8776ff38b53c07d4098d8ee8b13852253`.

Delivery state is `active`; owner verdict remains `pending`. RC.1 remains
released at signed tag `hearth-v0.3.0-rc.1`, source revision
`a3503dc734cab9111b065691609bc339918bd779`. Fedora package, real user-bus,
native QtDBus/M3Shapes, and source/static checks pass. Product integration
revision `87faf5525fc8de4b39e7a1241eca04b05bb05823` pins its immutable RPM URL and
SHA-256. BlueBuild run `32813973301` passed at clean build head
`ae04d4fe93ce8c65cb928b30229099c1f6766f99`, producing signed OCI index
`sha256:e1791f4ba537c0d052b704d4aaff2f168244b63f3d013f372952c8fd90765372`.
Independent Cosign verification passed on `aki@hearth`, and the owner later
booted that exact index. The RC.1 field smoke proved controller and keyboard
navigation plus Return to Gaming Mode, but found packaged UI startup, pointer,
application-launch lifecycle, layout, scrim, icon, and performance defects.
The local shell commits through `3bfe0f4c` and product commit `ee6b158` are
unreleased RC.2 inputs only. RC.2 implementation and local target staging are
the current gate; recovery, exact signed-image proof, and owner audit remain
pending.

The preserved v11 checkpoint met its performance target but failed Launcher
Presentation because the selection contour remained faceted and its fade was
sequenced incorrectly. It is explicitly recorded as a visual failure rather
than a successful candidate.

The replacement RC.2 staging tree now proves the corrected transient
application lifecycle, closed-state activation rejection, service-restart
survival, visible invalid-config fallback, visible launch failure, real icons,
and bounded two-endpoint icon behavior. One preallocated native scene-graph
surface uses M3Shapes device-pixel antialiasing, morphs the compact contour to a
rounded rectangle before tone/bounds expansion, and owns one dark restrained
elevation. Real-niri screenshots cover Grid/List at logical 1920x1080 and
1280x720. Fifty rapid changes rendered at p95/p99/max `16/16/17 ms`; 30
panel/view cycles rendered at `1/16/17 ms`, with a `182.7 MiB` peak.

A task-labeled Fedora 44 build passed Rust, user-bus, QML/offscreen, native
bridge, contract, payload, dependency, license, no-DMS, and network-disabled
offline-install checks. Its local RPM SHA-256 is
`463f6409247eafecd9a13e5226bb27f08192cc03cd541db0ccafa1d85f0d5cf9`.
It is local evidence only, not a published RC.2 identity.

The source-identical shell tree is clean at
`a67c014c8f9278b02ced45f3b52799746cab1014` on
`codex/hsn-001-launcher-nucleus`. No tag or remote publication was created.
The local product integration is clean at image-changing commit `dc6e746`,
with the hashed evidence checkpoint recorded through
`ddffa30ebff25b832468816b0a2b547d4b06512f` on the matching feature branch.

The subsequent RC.2 build/package gate was intentionally interrupted at the
owner's request before a new build process or container was running. Inspection
confirmed that no task-labeled builder required termination; caches, build
artifacts, and unrelated processes were left untouched. The requested shared
native selection increment and resumed local package gate are complete at an
evidence-recorded engineering checkpoint. Owner visual approval and exact clean
source identities are the current gate.

## Superseded phase statement

The complete 2026-08-24 handoff and later planning decisions were
reconciled into canonical product, architecture, requirement, decision,
behavior, roadmap, and open-question documents. This work changes
documentation only.

It does **not**:

- freeze or activate a product slice;
- implement hearthOS Shell, App Menu, Bar, OSK, Settings, Portal, wallpaper, or
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

The historical DMS refs and dirty state remain preserved in the private archive
recorded by repository reconciliation. Public shell and product `main` branches
remain unchanged; HSN-001 work lives on dedicated feature branches and the
signed RC.1 tag. Preflight is recorded, but the deployed host has not been
rebased to HSN-001 because remote rpm-ostree authorization is unavailable; its
booted and rollback deployments remain unchanged.

Existing image/build metadata may still project historical VS-002 state. No
new image may be built or presented as current until a later non-documentation
change reconciles those non-document public projections against this status.

## Next gate

Present the real-niri Grid/List screenshots, selected-corner crops, and motion
recording for owner visual approval. Do not create `hearth-v0.3.0-rc.2`, publish
the RPM, or build/pin a new OCI until that approval is recorded. Formal rebase,
recovery, and owner validation remain later gates.
