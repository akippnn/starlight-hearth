# ADR-0001 — Controller desktop foundation

**Status:** accepted
**Date:** 2026-08-21

## Decision

Use one repository, `akippnn/starlight-hearth`, for the OCI image,
configuration, delivery records, Decky integration, and early Hearth
applications. Do not create `starlight-cli`. Split `hearth-shell` only when it
has an independent release cadence or users outside hearthOS; split a first-party
Decky plugin only if its publication model requires it.

Keep niri as an unmodified upstream Wayland compositor. Use DMS as the initial
shell and replace its responsibilities incrementally with an independently
implemented Quickshell/QML Hearth Shell backed by a Rust session/settings
service. Reserve Tauri for conventional application windows.

Steam Input is the sole desktop mapping owner for VS-001. The mapping is a
documented semantic contract selected in Steam's UI; no undocumented account
files are injected. InputPlumber may take ownership only in a future slice with
an explicit exclusivity transition.

Adapt Bazzite session switching only through installed `steamosctl` commands and
the supported steamos-manager configuration. Validate the interface and target
session before mutation; never rewrite SDDM state or retry in a restart loop.
Retain KDE until a DMS-free Hearth Shell image has passed owner acceptance.

## Consequences

- The first slice can be delivered without inventing a compositor, shell, CLI, or package release boundary.
- DMS and changing Bazzite interfaces remain upstream dependencies and therefore require recorded versions and contract checks on every candidate.
- Steam Input setup is an owner-visible onboarding step, not hidden image state.
- Recovery remains deliberately redundant: niri emergency keys, KDE, TTY, and the previous deployment.
- Future Hearth Shell surfaces must use a versioned `org.starlight.Hearth.Session1` D-Bus boundary; Quickshell must not execute privileged shell commands directly.
