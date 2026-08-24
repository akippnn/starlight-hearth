# ADR-0004 — Versioned InputPlumber mouse-button contract

**Status:** accepted for HS-003 implementation; Linux x86_64 verification pending
**Date:** 2026-08-22

## Context

HS-003 must resolve L3 trigger chords before emitting a primary or secondary
click. InputPlumber 0.78 routes mouse buttons from static profiles, but its
published `org.shadowblip.Input.Mouse` D-Bus interface exposes only cursor
movement. Its composite-device interface does not expose a generic
`SendEvent` method. Mapping each trigger directly to a mouse button would make
the base click leak from L3+trigger chords, so neither upstream interface is
sufficient for the frozen v3 contract.

## Decision

`starlight-hearth` will carry the smallest possible downstream extension to the
signed InputPlumber `v0.78.0` source at
`082f67fba6aaff88441abdc482ae76b711ad2885`:
`org.shadowblip.Input.Mouse.SendButton` accepts a validated button name and
pressed state and writes through InputPlumber's existing virtual mouse target.
The patch, source identity, build inputs, RPM, URL, and SHA-256 are immutable
release evidence. No separate InputPlumber fork repository is created.

The package installs the exact versioned marker
`/usr/share/hearth/input/inputplumber-mouse-buttons-v1`. Hearth Shell checks
that static marker before publishing a probe marker. During the adapter's
bounded probe, Shell discovers the live mouse targets and selects the exact one
whose introspection contains `SendButton`; only then does it publish Desktop
readiness. A missing marker, missing method, unknown button, failed call, or
probe timeout prevents semantic Desktop promotion or revokes readiness; the
image adapter restores the gamepad-only fail-safe profile.

The extension is generic and will be kept as an isolated patch suitable for an
upstream contribution. Once an exact upstream release supplies an equivalent
audited interface, hearthOS removes the downstream patch and updates this ADR
and the controller contract together.

## Consequences

- Trigger clicks remain InputPlumber virtual-mouse events and cannot leak from
  modifier chords.
- hearthOS temporarily owns one small InputPlumber packaging delta and must
  test it against every base update.
- Shell RPMs can run elsewhere, but controller readiness remains degraded
  unless the image supplies the matching v1 output contract.
- The existing unmodified 0.78.0 package is never treated as satisfying
  controller-native Desktop readiness.
