# Hearth product direction

**Decision state:** Accepted; not frozen for an implementation slice
**Last reconciled:** 2026-08-29

## Product identity

hearthOS is a living-room gaming operating system. Steam Gaming Mode remains
the console experience, while Hearth Desktop must be a credible local surface
for routine operation, recovery, and Hearth-specific applications. A second
computer over SSH is useful for development but is not an acceptable
substitute for a usable local shell.

The desktop is intentionally smaller in scope than a general-purpose KDE or
GNOME replacement. It must nevertheless be coherent and predictable with a
controller, physical keyboard, and pointer before inherited recovery surfaces
can be retired.

## Settled direction

- Build a Hearth-owned shell with Quickshell/QML on unmodified upstream niri.
- Treat controller, keyboard, and pointer as first-class peers.
- Route controller UI actions semantically; do not translate them into global
  fake keyboard events.
- Keep DMS as a reference and selective source, not the product architecture.
- Reuse proven, license-compatible code, services, libraries, tests, and
  upstream histories instead of rebuilding them without cause.
- Maintain shared semantic input, focus, catalog, hint, and surface primitives;
  an outcome may extend them but must not create a private equivalent merely
  because it ships in a separate slice.
- Treat controller mappings as remappable data over stable semantic actions.
  Hold and latch triggers may be assigned independently, custom modifier layers
  remain possible, and user bindings never become arbitrary command execution.
- Use native helpers where QML is the wrong boundary. Do not substitute a web
  frontend, Electron, React, WebView, or localhost application for the shell.
- Preserve KDE, TTY, Tailscale, Gaming Mode, and the previous atomic deployment
  as recovery paths until a later owner-accepted retirement outcome exists.

## Experience principles

- hearthOS-native surfaces have explicit focus graphs, visible focus, reliable
  return paths, and no automatic search-field focus on open.
- The same semantic actions drive controller and keyboard interaction while
  leaving physical keyboard text input independent.
- Material 3 Expressive is a motion and interaction language: responsive
  hover/focus/press/release, shape morphing, elevation, directional movement,
  coordinated blur, and lively defaults with a real reduced-motion path.
- Typography, iconography, controller glyphs, motion, and state changes must be
  deliberate and varied rather than generic rounded-card styling.
- hearthOS Settings and hearthOS Portal are the first hearthOS-native applications.
  They share shell input/design primitives and may run as the same installed
  applications in Desktop and Gaming Mode.
- Built-in plugins such as local wallpaper and independent search are
  first-party packaged/audited components. Third-party plugins are explicitly
  trusted user-installed code with visible provenance, consent, diagnostics,
  disable/recovery paths, and no hearthOS security or compatibility guarantee.
  LLM-assisted GPL-3.0-compatible plugins remain subject to human review and
  license/provenance verification; generation is never a safety claim.

## Delivery philosophy

The roadmap is exhaustive, but implementation is incremental. HSN-001 remains
active/pending under its exact frozen v2 contract. HIN-001, HSN-002, and
HIN-002 are decision-complete proposals only. After this documentation pass,
each needs explicit owner approval, an exact frozen product revision, and
separate implementation authorization. The intended implementation order is
HIN-001, HSN-002, then HIN-002; shared integration does not merge acceptance.

Historical implementation and evidence are preserved without being promoted
to current support. Compilation, boot, or partial tests never substitute for
an owner verdict.
