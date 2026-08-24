---
id: "HSN-001"
title: "Hearth-native Launcher Nucleus"
contract_version: 1
contract_state: frozen
owner: "@akippnn"
repositories:
  - "akippnn/starlight-hearth"
  - "akippnn/starlight-hearth-shell"
target: "Bazzite/Fedora 44 x86_64; niri 26.04; LG 3840x2160 at logical 1920x1080; Pro 3 receiver"
current_status: "../status.md"
evidence: "../evidence/HSN-001.md"
updated: "2026-08-25"
---

# HSN-001 — Hearth-native Launcher Nucleus

After approval, record this file's exact repository revision in current status
and task packets. Do not edit this frozen file merely to embed its own commit
hash.

## Owner-visible outcome

From a real Hearth Desktop session, controller, keyboard, or pointer opens a
Hearth-native right drawer, switches between Grid and List, launches an
available core favorite outside the shell lifecycle, and retains Gaming Mode,
KDE, TTY, and previous-deployment recovery.

## Authentic path

`signed immutable OCI digest -> Hearth session -> unmodified niri -> Rust companion + Quickshell UI -> InputPlumber/keyboard/pointer -> launcher -> transient user-systemd application unit`

Cannot prove this outcome:

- offscreen QML, mocked D-Bus, an RPM alone, or nested niri;
- an unsigned or moving image reference;
- a shell-owned child application that terminates with the shell;
- a shortcut that bypasses the public typed launch contract.

Those mechanisms may provide independent evidence, but not authentic-path
acceptance.

## Public behavior and ownership

- Hearth Shell is a `GPL-3.0-only` native package: a Rust companion,
  Quickshell/QML UI, and a generated or contract-checked QtDBus bridge.
- The user-bus name is `org.starlight.HearthShell`.
- `/Input` implements `org.starlight.HearthShell.Input1`: context registration,
  connection/glyph/readiness properties, and typed
  `Action(action, phase, value, monotonic_usec)` events.
- `/Launcher` implements `org.starlight.HearthShell.Launcher1`: `Open`, `Close`,
  `Toggle`, `ListFavorites`, `ActivateDesktopEntry`, `InvokeAction`, visibility,
  and activation-result signals. Favorite records are `(kind,id,name,icon)`.
- `/Config` implements `org.starlight.HearthShell.Config1`: view, motion, and
  configuration-state properties plus `SetViewMode`.
- Canonical D-Bus XML and the semantic-action manifest live in the shell
  repository. Rust and QtDBus representations are generated or checked against
  them; the image pins their version.
- JSON schema v1 layers packaged defaults, `/etc/hearth-shell/config.json`, then
  `$XDG_CONFIG_HOME/hearth-shell/config.json`. Objects merge recursively and
  arrays replace. Unknown keys survive with warnings. One invalid known value
  rejects that entire layer and visibly falls back to lower layers. Shell-owned
  writes are atomic and hot-reloaded.
- QML supplies only a validated desktop ID or allowlisted action. Desktop
  entries launch through a transient user-systemd service invoking `gtk-launch`
  without a shell. `return-gaming` is a separate allowlisted action.
- A successful activation closes the drawer. Failure keeps it open, preserves
  focus, and shows an inline diagnostic.

| Responsibility | Canonical owner | Contract/version | Independent proof |
| --- | --- | --- | --- |
| Semantic input and readiness | Rust companion | `Input1` + semantic actions v1 | Rust router tests, real user-bus contract tests, deterministic InputPlumber fixtures |
| Favorite resolution and activation | Rust companion | `Launcher1` | desktop-ID allowlist, transient-unit, failure mapping, and restart-survival tests |
| Layered configuration | Rust companion | schema v1 + `Config1` | invalid-layer fallback, preservation, atomic-write, and hot-reload tests |
| Drawer interaction and presentation | Quickshell/QML | `Launcher1`, `Config1`, shared QML primitives | QML lint/offscreen focus, layout, motion, and reduced-motion tests |
| Session input and recovery | OCI image | semantic profile v4 + service units | schema fixtures, built-image checks, signed-image and physical-target audit |

## Scope

In:

- a warm Hearth dark right drawer at about 38% width, clamped to 520–760
  logical pixels, with a right-edge pointer anchor;
- Menu/Start and `Super+A` global toggles;
- configured favorites in this order: Return to Gaming Mode, Steam, Firefox,
  Dolphin, Ghostty; unavailable entries are hidden and focus reflows;
- Grid/List only: West toggles, `Ctrl+1` selects Grid, `Ctrl+2` selects List,
  and the selection persists;
- D-pad/arrows/HJKL/WASD navigation, South/Enter activation,
  East/Escape/scrim close, left-stick scroll, right-stick pointer, and LB/RB
  primary/secondary clicks;
- directional drawer motion, card shape morphs, press deformation,
  ripple/state layers, elevation, animated icon fill/weight, and a reduced-motion
  path that removes spatial and shape travel;
- shaped Quickshell background effects when available, then niri xray blur,
  then translucent dimming;
- direct, reviewed adaptations of Caelestia animation, state-layer, button,
  variable-icon, typography, and token primitives from
  `1d0e5a588c61f1d905eba5fe8446ec222d37f50c`;
- Caelestia-pinned M3Shapes
  `bdc327b29f95394a732baf3c9b19658ba23755b6` behind Hearth card wrappers with
  Apache-2.0 notices;
- pinned OFL Google Sans Flex, Apache-2.0 Material Symbols Rounded, and original
  Hearth controller glyphs;
- replacement of image DMS runtime paths, exact shell RPM URL/SHA-256, semantic
  InputPlumber v4, and preservation of niri, Gaming Mode, KDE, TTY, emergency
  keyboard, and previous deployment recovery.

Out:

- tabs, search, recents, categories/index rail, and context actions;
- OSK/Text Mode, the full Hearth Bar, Settings UI, Portal, notifications, and
  control center;
- multi-output policy, wallpaper/dynamic tones, and Gaming performance work;
- KDE retirement.

## Failure and recovery

- Missing favorites are hidden rather than faked; audit-readiness requires
  Return to Gaming Mode plus at least one external application to resolve and
  launch.
- Invalid higher configuration layers expose diagnostics and fall back to the
  complete lower-layer result. They never partially apply known keys.
- Input routing fails closed until companion and UI readiness is established;
  controller reconnect restores the semantic profile without duplicate global
  keyboard events.
- Shell failure leaves niri, launched application units, emergency keyboard
  bindings, Gaming Mode return, KDE, TTY, and the previous deployment usable.
- An unreachable target or missing artifact identity is recorded as a blocker,
  never replaced by mocked target proof.

## Non-owner readiness gates

- [ ] Contract is frozen and its exact approved revision is recorded externally.
- [ ] Rust unit tests and real user-bus D-Bus contract tests pass.
- [ ] Deterministic InputPlumber v4, config fallback, desktop-ID allowlist,
      launch failure, and application-survival tests pass.
- [ ] QML lint/offscreen checks cover focus, missing-favorite reflow, persisted
      Grid/List, all three input families, 1280x720 and logical 1920x1080,
      motion endpoints, icon axes, and reduced motion.
- [ ] Exact donor import ledger, GPL/OFL/Apache notices, M3Shapes native tests,
      RPM payload/dependency, no-DMS-name, offline-install, and reproducibility
      checks pass.
- [ ] Canonical/derived contracts match; nested niri smoke, five-second service
      readiness, physical reconnect, real application launch, shell-restart
      survival, Gaming Mode return, and signed OCI verification pass.
- [ ] On the LG target after warm-up, p95 animation frame time is at most one
      output frame and p99 at most two across 30 open/close and Grid/List cycles;
      reduced motion removes spatial/shape travel.
- [ ] Clean shell and image revisions, immutable RPM URL/SHA-256, signed OCI
      digest, and hashed screenshot/recording plus D-Bus/systemd trace bundle
      are recorded.
- [ ] Evidence, current status, limitations, and guarded public claims agree.

## Owner audit

1. Boot the recorded OCI digest and switch from Gaming Mode to Hearth Desktop.
2. Open the launcher with controller, keyboard, and pointer.
3. Navigate, toggle Grid/List, and launch an application with each applicable
   input.
4. Restart Hearth Shell and confirm the launched application survives.
5. Exercise controller reconnect, launch failure, invalid-config fallback,
   return to Gaming Mode, and KDE/TTY recovery.
6. Record `accepted` or `rejected`.

`audit-ready` leaves the owner verdict pending. Agents may report at most
`audit-ready/pending`; only the product owner records acceptance.

## Contract amendments

| Version | Supersedes | Approved by/date | Material change |
| --- | --- | --- | --- |
| 1 | — | @akippnn / 2026-08-25 | Initial frozen launcher-nucleus contract |

Canonical evidence: [HSN-001 evidence](../evidence/HSN-001.md)
