# HS-003 — Controller-Aware App Menu

**Status:** active; implementation in progress; not audit-ready
**Owner:** @akippnn
**Repositories:** `akippnn/starlight-hearth`, `akippnn/starlight-hearth-shell`
**Target:** x86_64 AMD/Intel living-room Hearth PC; Pro 3 receiver `2dc8:310b`

## Owner-visible outcome

From Hearth Desktop, the owner presses Menu and operates the normally sized App
Menu using raw controller semantics rather than global keyboard emulation.
Visible button hints, deterministic focus, category and layout switching,
search, the compact bottom OSK, intentional pointer input, and a physical
keyboard coexist without corrupting one another.

## Authentic path

`Pro 3 receiver → InputPlumber v3 Desktop profile → system-bus D-Bus events → Rust org.starlight.HearthShell.Controller1 service → QML App Menu context → selected application`

The accepted path must use the released Shell RPM inside a signed hearthOS OCI
image. Source assertions, mocked input, or a manually launched development
binary cannot satisfy the owner-visible outcome by themselves.

## Public contracts

- `starlight-hearth-shell` owns the canonical
  `/usr/share/hearth-shell/controller-layout-v3.json` manifest and the user-bus
  service `org.starlight.HearthShell.Controller1` at
  `/org/starlight/HearthShell/Controller`.
- `starlight-hearth` owns the matching InputPlumber hardware and session
  profiles. The complete built image fails when the profile and pinned Shell
  manifest differ.
- Desktop face buttons, D-pad, bumpers, triggers, Menu, View, Guide, L3, and R3
  emit D-Bus events, never global keyboard events.
- Right stick remains pointer motion, left stick remains scrolling, trigger
  clicks are emitted intentionally after modifier resolution, and OSK keys use
  InputPlumber's virtual keyboard.
- InputPlumber 0.78's mouse D-Bus API lacks button injection. The image carries
  the isolated `SendButton` extension frozen in ADR-0004; its exact package
  marker and live introspection must both pass before the router advertises
  readiness.
- Unknown session/router state uses the conventional gamepad-only fail-safe.
  Gaming Mode presents a conventional Xbox gamepad with no Hearth interception.
- Gaming→Desktop starts from that safe profile. The Desktop service publishes a
  versioned probe only after checking the exact image contract; the adapter
  applies semantic v3 for a bounded validation window; and the service
  publishes readiness only after discovering the real D-Bus target and
  introspecting the exact mouse-button target. Discrete semantic events are
  dropped until readiness. Probe timeout or router loss restores the gamepad
  profile without blocking recovery.
- Controller glyph positions do not change across Xbox, PlayStation, Nintendo,
  and generic families; the owner may override only the displayed family.
- Ordinary Qt keyboard handling remains independent. The compact OSK does not
  take Wayland keyboard focus from its Hearth-owned target field.

## App Menu behavior

- Menu opens the App Menu with the best visible result selected, not the search
  field.
- D-pad navigates visible results; South accepts and East closes the topmost
  interaction layer.
- LB/RB cycles All, Apps, Files, and Plugins.
- West cycles a supported result section between list and grid.
- North focuses search and opens the compact OSK; holding North explicitly
  toggles the OSK.
- East closes OSK, then leaves text focus, then closes App Menu on successive
  presses.
- The rest of the Desktop darkens while the active panel and Dank Bar remain
  visually active.
- Only valid current-context hints are visible. L3/R3 show modifier intent;
  child hints replace them while held.
- Disconnect/reconnect restores the visible semantic result when possible and
  otherwise selects the first visible result.

## In scope

- Rust semantic router, versioned user-bus API, diagnostics, modifier/chord
  resolution, glyph detection/override, and systemd user service;
- v3 InputPlumber Desktop/Gaming profiles and fail-safe session ownership;
- reusable QML context, hint, and focus-graph primitives;
- App Menu focus/search/category/layout behavior, compact Hearth OSK, normal
  App/Power panel sizing, dimming, and non-battery bar cleanup;
- read-only Controller Layout settings page;
- Fedora 44 x86_64 RPM, immutable image integration, automated evidence, and
  owner audit.

Out of scope are arbitrary-application text fields, completed Dank Bar/Quick
Menu behavior, rebinding, every other DMS surface, application compatibility,
Decky, Framegen, secure lifecycle, Ember, NVIDIA, and KDE removal.

## Failure contracts

- A missing or failed Rust router makes the system adapter apply the gamepad-only
  fail-safe profile. Physical keyboard/mouse and niri emergency bindings remain
  available; the image reports controller semantics as degraded and restores
  v3 Desktop semantics when the router returns. It never restores the v2 global
  keyboard map.
- Changed InputPlumber or Bazzite contracts fail closed to the gamepad profile.
- Missing or incompatible InputPlumber mouse-button output revokes router
  readiness before a trigger can use an undocumented composite-device method.
- Probe and readiness markers are phase- and PID-versioned. A stale or
  mislabeled marker cannot promote the Desktop profile, and the bounded probe
  cannot remain an indefinite partially active Desktop mapping.
- Modifier release order never leaks the child button's base action.
- Controller disconnect clears held buttons/modifiers. Reconnect reapplies the
  active Desktop profile and restores current surface context.
- Missing OSK virtual keyboard reports a visible error without privileged shell
  execution.
- No network is required after the image and RPM are installed.

## Automated and integration gates

- [x] Rust unit tests cover one-action presses, duplicate suppression, modifier
  release order, North short/hold exclusivity, trigger click balance, reconnect
  reset, glyph detection, and configuration validation.
- [x] Real session-bus tests call and introspect the public D-Bus contract and
  validate signal bodies; a fake ObjectManager additionally exercises the real
  InputPlumber discovery, input signal, exact mouse-target selection, and
  `SendButton` calls.
- [x] QML tests cover semantic-key focus restoration, invisible/header skips,
  wraparound, and reordered App Menu results.
- [ ] Upstream Go tests, Hearth source contracts, QML lint, 720p/logical-1080p
  layout checks, and nested niri/Quickshell smoke pass on Linux x86_64.
- [ ] Fedora 44 and Bazzite validate the RPM's package ownership, service,
  embedded QML, public manifest/schema, compatibility provide/obsolete, version,
  and SHA-256.
- [ ] InputPlumber 0.78 validates both profiles and observes no global keyboard
  output or duplicate Desktop action for every discrete input.
- [ ] The exact downstream InputPlumber RPM exposes and exercises
  `org.shadowblip.Input.Mouse.SendButton`, owns the v1 contract marker, rejects
  unknown buttons, and fails closed when either the marker or method is absent.
- [ ] Profile/manifest cross-check and complete signed OCI build pass; exact
  source, RPM, base, image, and signature identities are recorded.
- [ ] Compared with the direct receiver baseline, the added Gaming Mode path is
  at most 2 ms median and 5 ms p95 across at least 1,000 events.
## Owner audit

1. Rebase by the recorded immutable OCI digest and reboot.
2. Confirm hearthOS identity, Gaming Mode, TTY, KDE recovery, automatic TV
   scale, and the prior deployment.
3. Enter Hearth Desktop without keyboard or mouse and open App Menu with Menu.
4. Navigate, change each category and supported layout, search with the compact
   OSK, launch an application, and close each interaction layer with East.
5. Mix controller, physical keyboard, and pointer input; confirm focus remains
   visible and restores to the same semantic result.
6. Power-cycle the controller five times and confirm context/focus restoration.
7. Repeat Gaming↔Desktop five times, including offline and Shell-restart cycles;
   confirm normal Steam controller behavior after every return.
8. Record the owner verdict and limitations in `docs/evidence/HS-003.md`.

Agents may mark this slice `audit-ready` only after every non-owner gate passes.
Only the owner may mark it `accepted`.
