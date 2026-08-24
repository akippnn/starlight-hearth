# ADR-0005 — Multi-track roadmap and application strategy

**Status:** accepted
**Date:** 2026-08-23

## Decision

Use `HS`, `AP`, `GM`, and `BR` identifiers for Hearth Shell, applications,
Gaming Mode, and inherited-base retirement. Rename the existing generic
records one-to-one so their evidence remains comparable, and preserve the old
identifiers only as documented historical aliases.

Reject a standalone compositor-wide external-application OSK milestone.
External applications use a hybrid controller model: native gamepad
passthrough where supported, versioned per-application keyboard/mouse bindings
where required, and a safe pointer fallback. Application forks require a later
ADR demonstrating that this model cannot satisfy a required workflow.

Hearth Portal is the exception because application and system management are a
core hearthOS surface. Hearth Shell renders the controller-native UI while an
adapter consumes the root-owned Bazzite Portal catalog. QML may select only
typed catalog and option IDs; it never supplies an arbitrary command.

Adopt useful Bazzite applications before removing inherited surfaces. Tailscale
remains preinstalled and enabled. KDE remains the recovery desktop until the
separate BR-002 audit proves equivalent recovery without Plasma.

## Consequences

- The Menu/Start App Menu and Guide-opened Hearth Quick Menu have distinct
  names, controller ownership, and acceptance tests.
- Gaming Mode work can release beside Shell work but cannot block it.
- AP-001 must pin an immutable Bazzite base and generate an application diff;
  a moving `stable` manifest is only a drift signal.
- BR-001 cannot remove a package before its replacement or Portal action is
  proven. Dependency-required packages may remain installed but hidden.
- Ghostty becomes the sole visible terminal only after Terminal, Bold Brew,
  emergency access, and KDE recovery pass against one candidate.
- Decky Loader is preserved; Decky-Framegen retirement is isolated in GM-003
  and must not remove unrelated owner plugins.
