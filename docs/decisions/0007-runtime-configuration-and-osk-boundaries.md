# ADR-0007 — Runtime, configuration, launch, and OSK boundaries

**Status:** accepted architecture decision; no implementation slice authorized
**Date:** 2026-08-25
**Supersedes:** ADR-0002's DMS OSK bridge and ADR-0005's blanket rejection of a compositor input-method path

## Decision

Quickshell/QML owns Hearth UI. One tested Rust `hearth-shell` companion owns
lifecycle/readiness, semantic controller routing, diagnostics, public IPC,
safe application launch, configuration validation/migration, and supervision
of the OSK child. C++ is used only for justified native QML modules.

Applications launch in separate transient user-systemd units or scopes so
shell failure does not terminate them. QML selects typed application/action
identifiers; it does not construct arbitrary privileged commands.

Use a versioned JSON configuration model layered as packaged defaults, `/etc`
administrator/image policy, and XDG user configuration. The shell repository
owns the schema and migrator; the image repository supplies policy and pins the
exact shell artifact. Invalid user input falls back visibly and safely.

Fork wvkbd v0.20 at
`6b41504a0cb58fd1163fa44692398fbd61f8905f` into a separate history-preserving
keyboard repository. The Rust companion supervises it as a child and remains
the sole public API. The fork uses Wayland input-method-v2, text-input-v3,
virtual-keyboard-v1, and layer shell. It may serve supported third-party
Wayland fields on a best-effort basis, but Hearth does not claim universal or
XWayland text-entry compatibility.

## Consequences

Existing Rust semantic-routing code and tests may be salvaged after contract
review. The fixed-size Hearth QML OSK and InputPlumber `SendKey` path are not
the target implementation. Exact JSON schema, IPC version, private child wire
format, and unsupported-client UX remain open and must be decided before a
future frozen slice.
