# ADR-0003 — Semantic controller routing and DMS-derived product

**Status:** accepted for HS-003 implementation
**Date:** 2026-08-22
**Supersedes:** ADR-0002's Desktop keyboard/mouse translation; retains its repository and session-ownership decisions

## Context

HS-002 proved that InputPlumber can hand the physical controller between Steam
Gaming Mode and Hearth Desktop and reapply ownership after reconnect. The owner
audit also proved that translating discrete controller buttons into global
keyboard events does not produce a controller-native shell. It loses semantic
context, leaks implementation keys across applications, and cannot express
modifier layers or position-stable glyphs reliably.

## Decision

Keep niri unmodified and maintain Hearth Shell as the DMS-derived product.
`master` remains a fast-forward-only upstream mirror; Hearth product work uses
`main` and `codex/hs-*` branches. After HS-003/HS-004, an explicit merge-cost
gate decides whether the fork remains sustainable. No DMS-retirement outcome is
assumed in advance.

Hearth Desktop maps discrete controller inputs to InputPlumber D-Bus events.
A Rust user-session service consumes the system-bus stream, resolves
modifiers/chords, suppresses duplicates, publishes diagnostics and glyph state,
and emits semantic actions on the user bus as
`org.starlight.HearthShell.Controller1`. QML surfaces register contexts and
available actions; they do not receive synthetic arrow, Enter, Escape, Tab, or
function-key events from the controller.

Right-stick pointer motion and left-stick scrolling remain deliberate virtual
mouse outputs. Trigger clicks are emitted only after Rust modifier resolution,
and the Hearth OSK intentionally sends keys through InputPlumber's virtual
keyboard. Physical keyboard handling remains ordinary Qt input and independent
from controller interception.

Gaming Mode continues to receive a conventional Xbox gamepad with no Hearth
interception. Steam owns game semantics and Guide there. Unknown session or
router state falls back to the gamepad-only profile rather than reactivating a
Desktop keyboard map.

Desktop readiness uses two phase- and PID-versioned markers under the user's
systemd runtime directory. After verifying the exact static image contract, the
service publishes a probe marker. The system adapter temporarily loads the
semantic profile in a known Desktop session so its D-Bus and mouse targets can
exist. The router publishes readiness only after discovering those targets and
introspecting the exact mouse-button API; until then it counts and drops
discrete events. The adapter bounds the probe and returns to the gamepad-only
profile on timeout or failure. It records requested/effective mode and router
state under `/run/hearth/input-state.json`.

The canonical mapping and glyph families live in the versioned Shell manifest
installed under `/usr/share/hearth-shell/`. `starlight-hearth` owns the matching
InputPlumber profile and validates it against the exact manifest delivered by
the checksum-pinned Shell RPM during image construction.

## Consequences

- Controller focus and hints can vary by surface without changing hardware
  mappings or emitting unsupported actions into applications.
- Modifier release order and duplicate events become testable in a small Rust
  state machine.
- Hearth-owned text fields can keep keyboard focus while the controller
  navigates a non-focus-stealing OSK. External applications use their native
  text path or an explicit HS-005 application profile; no compositor-wide
  input-method slice is planned.
- Guide can become the Desktop Hearth Quick Menu while remaining Steam-owned in
  Gaming Mode.
- The v2 image remains a recovery/development baseline, not an accepted
  controller-native release.
