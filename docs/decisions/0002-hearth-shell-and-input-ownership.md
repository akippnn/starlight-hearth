# ADR-0002 — Hearth Shell fork and controller ownership

**Status:** accepted for VS-002 implementation
**Date:** 2026-08-22
**Supersedes:** ADR-0001

## Decision

Maintain two immediate repositories:

1. `akippnn/starlight-hearth` owns the OCI image, niri/session integration,
   InputPlumber policy, branding, recovery, and evidence.
2. `akippnn/starlight-hearth-shell` is a history-preserving DMS fork that owns
   the Hearth user interface and RPM release.

niri remains an unmodified upstream compositor. Hearth Shell is the maintained
DMS-derived product; there is no independent replacement-shell or
DMS-retirement track. Compatibility interfaces `/usr/bin/dms`, `dms.service`,
existing IPC names, and existing configuration paths remain until an explicit
later contract removes them.

InputPlumber owns physical-controller normalization in both sessions. Gaming
Mode receives only an identity gamepad and leaves game semantics to Steam
Input. Hearth Desktop receives only Hearth keyboard/mouse semantics. Unknown
session state receives the gamepad fail-safe profile. Session mutation is
blocked until the input adapter acknowledges the requested ownership state.

Hearth Shell's OSK calls InputPlumber's system D-Bus virtual keyboard through
the existing unprivileged DMS D-Bus bridge. QML does not invoke privileged
shell commands. Guide remains unmapped and Steam-owned.

## Consequences

- The shell has an independent signed RPM release and upstream tracking cadence.
- hearthOS pins one exact release URL and SHA-256 and never consumes `latest`.
- Controller reconnection can reapply the active profile without relying on
  per-account Steam files.
- A failure leaves a visible `/run/hearth/input-state.json` diagnostic and does
  not activate both mapping owners.
- KDE remains recovery until VS-009; Decky and Framegen remain later slices.
