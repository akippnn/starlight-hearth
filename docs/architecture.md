# hearthOS architecture foundation

**Decision state:** Accepted architecture; HSN-001 active, HIN-001/HSN-002/HIN-002 proposed
**Last reconciled:** 2026-08-29

## Repository ownership

`starlight-hearth` is the product authority. It owns the OCI image, Bazzite and
niri integration policy, InputPlumber/session policy, recovery, cross-repository
contracts, roadmap, status, and evidence.

`starlight-hearth-shell` owns the independently released hearthOS Shell UI and
its implementation-facing documentation.

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
Quickshell/QML hearthOS surfaces
├── hearthOS System Bar and owned panels
├── App Menu
├── focus graphs, shared input hints, and input contexts
├── Settings/Portal shared controls
└── native QML modules only where justified
```

The Rust companion is the tested public service boundary. QML does not execute
privileged commands or invent application launch shell strings. C++ is limited
to native QML modules such as expressive-shape integration when required.

Applications launched from hearthOS run in separate transient user-systemd
units or scopes so a shell restart does not terminate them. niri remains the
source of truth for windows, outputs, workspaces, and active XKB state.
Headless input actions use niri's real IPC event stream and typed actions;
visible Desktop Navigation uses niri Overview. QML must not emulate a parallel
window or workspace model.

`niri.service` is the sole Desktop-session lifecycle owner for the companion
and UI. Image-owned `niri.service.wants` links start both units; the companion
acquires its D-Bus name before the UI starts, and `PartOf=niri.service` tears
them down when Desktop Mode ends. The compositor configuration does not issue
a duplicate shell start. See ADR-0009.

## Configuration ownership

Hearth uses one documented, versioned JSON configuration model with these
layers, from lowest to highest precedence:

1. packaged defaults;
2. image/administrator policy under `/etc`;
3. XDG user configuration edited by hearthOS Settings.

`starlight-hearth-shell` owns the schema and migrator. `starlight-hearth` pins
the exact shell artifact and supplies image policy. Invalid user configuration
must fail visibly and fall back to known-good values rather than preventing the
shell from starting. HSN-001 freezes the schema-v1 subset. Proposed HSN-002
defines per-layer v1→v2 migration, unknown-key preservation, whole-layer
rejection, and atomic first-write migration; those v2 details remain
non-normative until its exact contract revision is owner-approved and frozen.

## Input and OSK boundaries

InputPlumber normalizes physical controllers and preserves fail-safe session
ownership. A Rust semantic router resolves contexts and chords and exposes
Hearth actions; QML consumes those actions through surface contexts and focus
graphs. Deliberate pointer, scrolling, and text injection remain virtual-device
operations rather than semantic UI key emulation.

The router owns modifier, precedence, repeat, reconnect, and capability state.
Semantic layers/actions are independent from physical trigger data; every
controller action remains remappable, and hold/latch triggers may differ. The
router accepts only registered semantic actions, never arbitrary commands from
a custom binding.
The shell has one reusable `InputHintBar` driven by semantic action data;
individual surfaces do not hardcode physical mappings or fork hint state.
HIN-001 proposes the headless state, HSN-002 the first visual component, and
HIN-002 reuse of that component for its visible latched niri mode.

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

Built-in plugins are first-party packaged and audited components. Third-party
plugins are explicitly trusted user-installed code and carry no hearthOS
guarantee of security, correctness, privacy, maintenance, or compatibility.
GPL-3.0-compatible plugins may be written with or without LLM assistance, but
generated code is not inherently safe: human review, provenance/license
verification, visible first-/third-party labeling, and explicit installation
consent remain required. The host must provide failure containment, diagnostics,
disable/recovery paths, and version compatibility checks.

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
