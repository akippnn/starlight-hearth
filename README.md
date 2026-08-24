# hearthOS

> [!WARNING]
> **Pre-alpha — owner testing only.**
>
> hearthOS is not ready for general installation. No implementation slice is
> currently active, frozen, audit-ready, or owner-accepted. The project is in a
> documentation and planning reconciliation phase.
>
> Existing GHCR images are historical development artifacts; download counts
> do not imply a supported release. Do not rebase to `latest` or infer current
> support from an older candidate.

hearthOS is a living-room gaming operating system in the Starlight family.
Steam Gaming Mode remains the console experience. Hearth Desktop is intended
to become a controller-, keyboard-, and pointer-native alternative that is
usable locally without requiring another computer over SSH.

The target Hearth Shell is a Hearth-owned Quickshell/QML shell on unmodified
niri. DMS remains useful as a reference and selective source, but it is no
longer the product architecture. The target is not a web, Electron, React,
WebView, or localhost shell.

## Current phase

**Documentation foundation reconciliation; no active product slice.**

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
Quickshell/QML Hearth surfaces
```

Applications launch outside the shell's lifecycle in transient user-systemd
units/scopes. Configuration is one versioned JSON model layered from packaged
defaults through `/etc` policy to XDG user overrides. Exact wire/schema details
remain open until a future contract is frozen.

Hearth Shell's accepted license direction is `GPL-3.0-only`, enabling deliberate
license-compatible reuse from Clavis, Caelestia, DMS, M3Shapes, wvkbd, and
other audited donors. Every import requires exact revision and per-file
attribution records.

## Historical delivery and recovery

- VS-001/HS-001 proved signed boot, niri/DMS startup, TV scaling, and recovery,
  but its controller-ready claim was rejected.
- VS-002/HS-002 proved useful session/input-handoff behavior but did not produce
  an accepted controller-native desktop.
- HS-003 contains reusable semantic-routing and UI test evidence but was never
  owner-accepted and is now superseded by the Hearth-native direction.

Historical identifiers are mapped in
[docs/identifier-migration.md](docs/identifier-migration.md). Historical files
retain their original wording and must be read through current status.

KDE Plasma, TTY, Tailscale, Gaming Mode, and previous atomic deployments remain
recovery paths. KDE retirement requires a later dedicated owner-accepted
outcome; it is not authorized by the shell direction change.

## Development

This repository owns image policy, integration, recovery, cross-repository
contracts, and delivery truth. `starlight-hearth-shell` remains a separate
release boundary and is intentionally untouched by the current documentation
phase.

Existing repository checks can be run with:

```bash
python3 -m unittest discover -s tests -v
```

Linux x86_64 remains the existing build target. No new build or deployment is
produced by the documentation reconciliation.
