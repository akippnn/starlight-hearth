# Hearth architecture foundation

**Decision state:** Accepted architecture direction; not implemented or frozen
**Last reconciled:** 2026-08-25

## Repository ownership

`starlight-hearth` is the product authority. It owns the OCI image, Bazzite and
niri integration policy, InputPlumber/session policy, recovery, cross-repository
contracts, roadmap, status, and evidence.

`starlight-hearth-shell` owns the independently released Hearth Shell UI and
its implementation-facing documentation. It will be reconciled only after its
separate history reset; the current documentation pass does not mutate it.

A future `starlight-hearth-keyboard` repository will preserve the upstream
wvkbd history and own Hearth's OSK fork. File-manager work remains a dormant
contingency and receives a repository only if its activation gate is met.

## Runtime topology

```text
InputPlumber / Wayland / niri events
                │
                ▼
Rust hearth-shell companion
├── lifecycle and readiness
├── semantic controller routing
├── safe application launch
├── diagnostics and public IPC
├── configuration validation/migration
└── OSK child supervision
                │
                ▼
Quickshell/QML Hearth surfaces
├── Hearth Bar and owned panels
├── App Menu
├── focus graphs and input contexts
├── Settings/Portal shared controls
└── native QML modules only where justified
```

The Rust companion is the tested public service boundary. QML does not execute
privileged commands or invent application launch shell strings. C++ is limited
to native QML modules such as expressive-shape integration when required.

Applications launched from Hearth run in separate transient user-systemd
units or scopes so a shell restart does not terminate them. niri remains the
source of truth for windows, outputs, workspaces, and active XKB state.

## Configuration ownership

Hearth uses one documented, versioned JSON configuration model with these
layers, from lowest to highest precedence:

1. packaged defaults;
2. image/administrator policy under `/etc`;
3. XDG user configuration edited by Hearth Settings.

`starlight-hearth-shell` owns the schema and migrator. `starlight-hearth` pins
the exact shell artifact and supplies image policy. Invalid user configuration
must fail visibly and fall back to known-good values rather than preventing the
shell from starting. Atomic writes, hot reload, unknown-key policy, and exact
schema/version wire shapes remain open design work.

## Input and OSK boundaries

InputPlumber normalizes physical controllers and preserves fail-safe session
ownership. A Rust semantic router resolves contexts and chords and exposes
Hearth actions; QML consumes those actions through surface contexts and focus
graphs. Deliberate pointer, scrolling, and text injection remain virtual-device
operations rather than semantic UI key emulation.

The future wvkbd-derived child owns Wayland input-method, virtual-keyboard, and
layer-shell behavior. The companion remains the sole public API and supervises
the child. Hearth-owned fields are reliable; third-party Wayland fields are
best effort; unsupported and XWayland clients retain an explicit manual
fallback. Universal application compatibility is not claimed.

## Reuse and migration

Clavis is the primary niri-native architectural donor. Caelestia is the main
motion/visual reference. DMS supplies selected mature niri/system integration
and existing Hearth implementation evidence. M3Shapes is the leading native
shape-morph candidate. Every direct import requires an exact revision,
per-file license audit, change record, and attribution entry.

The canonical Hearth shell history will eventually be separated from the full
DMS ancestry. The old graph and dirty states must be retained in a private
archive before that later operation. Runtime DMS commands, service names, IPC,
and configuration compatibility are not part of the target architecture;
license attribution remains mandatory.

## Recovery and release boundary

Shell, image, Gaming Mode, applications, and base retirement remain independent
delivery tracks. One track's failure does not mask another's status. Immutable
artifact revisions and checksums are required before integration. KDE recovery
cannot be removed until display, networking, authentication, terminal, file
recovery, rollback, TTY, and diagnostics pass a dedicated owner audit.
