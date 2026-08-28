# hearthOS

> [!WARNING]
> **Pre-alpha — owner testing only.**
>
> hearthOS is not ready for general installation. HSN-001 is active at its
> exact v2 frozen contract revision. Signed RC.2 boots, but has recorded
> closed-launcher blur and presentation defects. It is not audit-ready or
> owner-accepted.
>
> Existing GHCR images are historical development artifacts; download counts
> do not imply a supported release. Do not rebase to `latest` or infer current
> support from an older candidate.

hearthOS is a living-room gaming operating system in the Starlight family.
Steam Gaming Mode remains the console experience. hearthOS Desktop is intended
to become a controller-, keyboard-, and pointer-native alternative that is
usable locally without requiring another computer over SSH.

The target hearthOS Shell is a hearthOS-owned Quickshell/QML shell on unmodified
niri. DMS remains useful as a reference and selective source, but it is no
longer the product architecture. The target is not a web, Electron, React,
WebView, or localhost shell.

## Current phase

**HSN-001 active/pending; work is local-only until the owner explicitly greenlights delivery at the HSN-002 stage.**

The signed RC.2 image booted and starts hearthOS Shell automatically, but
field testing found an unconditional compositor-blur artifact while the
launcher is closed and competing selection/press shapes. Both corrections
pass local real-niri staging and remain unpublished. HSN-002 is proposed only,
with no candidate or implementation claim. Do not treat RC.2 or the local
corrections as an audit candidate.

Historical VS/HS work, including HS-003, is retained as implementation and
audit evidence without being promoted to current support. No documentation
decision by itself authorizes shell code, packaging, configuration, image,
deployment, or owner-audit work.

Current authority:

- [Product direction](docs/product-direction.md)
- [Architecture foundation](docs/architecture.md)
- [Repository reconciliation record](docs/repository-reconciliation.md)
- [Requirements register](docs/requirements.md)
- [Open decisions](docs/open-questions.md)
- [Planning behavior contracts](docs/contracts/README.md)
- [Roadmap](docs/roadmap.md)
- [Current status](docs/status.md)
- [Reuse/licensing ledger](docs/reuse-ledger.md)
- [Handoff coverage matrix](docs/coverage-matrix.md)
- [Immutable 2026-08-24 handoff](docs/handoffs/2026-08-24/INDEX.md)

## Architecture direction

```text
InputPlumber / niri / Wayland
              │
              ▼
Rust hearth-shell companion
├── lifecycle and semantic controller routing
├── safe application launch and diagnostics
├── configuration validation/migration
└── supervised wvkbd-derived OSK child
              │
              ▼
Quickshell/QML hearthOS surfaces
```

Applications launch outside the shell's lifecycle in transient user-systemd
units/scopes. Configuration is one versioned JSON model layered from packaged
defaults through `/etc` policy to XDG user overrides. HSN-001 v2 freezes the
launcher subset, public typed service boundary, RB/LB ordering, and niri-owned
shell lifecycle at product revision
`43ca3393adf1dbbc2448ea8bfbfddc80761f386f`.

hearthOS Shell's accepted license direction is `GPL-3.0-only`, enabling deliberate
license-compatible reuse from Clavis, Caelestia, DMS, M3Shapes, wvkbd, and
other audited donors. Every import requires exact revision and per-file
attribution records.

## Historical delivery and recovery

- VS-001/HS-001 proved signed boot, niri/DMS startup, TV scaling, and recovery,
  but its controller-ready claim was rejected.
- VS-002/HS-002 proved useful session/input-handoff behavior but did not produce
  an accepted controller-native desktop.
- HS-003 contains reusable semantic-routing and UI test evidence but was never
  owner-accepted and is now superseded by the hearthOS-native direction.

Historical identifiers are mapped in
[docs/identifier-migration.md](docs/identifier-migration.md). Historical files
retain their original wording and must be read through current status.

KDE Plasma, TTY, Tailscale, Gaming Mode, and previous atomic deployments remain
recovery paths. KDE retirement requires a later dedicated owner-accepted
outcome; it is not authorized by the shell direction change.

## Development

This repository owns image policy, integration, recovery, cross-repository
contracts, and delivery truth. `starlight-hearth-shell` remains a separate
release boundary and will be reconciled only against the exact HSN-001
contract revision.

Existing repository checks can be run with:

```bash
python3 -m unittest discover -s tests -v
```

Linux x86_64 remains the build target. Only exact source, artifact, image, and
target identities recorded in HSN-001 evidence count toward this candidate.
