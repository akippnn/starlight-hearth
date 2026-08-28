# Hearth requirements register

**Authority:** canonical product requirements
**Last reconciled:** 2026-08-28
**Freeze state:** the HSN-001 subset is frozen by its exact slice contract;
remaining requirements retain their row states

The archived handoff is source evidence. This register records its continuing
requirements together with later explicit owner decisions. Detailed accepted
interaction behavior lives in `docs/contracts/`; unresolved policy lives in
`docs/open-questions.md`.

## Governance and architecture

| ID | State | Requirement |
| --- | --- | --- |
| `GOV-001` | Accepted | `starlight-hearth` is the product-documentation, image-policy, recovery, roadmap, status, and evidence authority. |
| `GOV-002` | Accepted | Preserve immutable history, rejected owner findings, dirty-state provenance, and exact artifact revisions; never rewrite evidence to fit a new direction. |
| `GOV-003` | Accepted | Use explicit `Proposed`, `Accepted`, `Frozen-for-slice`, `Superseded`, and `Open` planning states; acceptance of an ADR is not acceptance of a product slice. |
| `GOV-004` | Accepted | Do not reuse a historical slice ID for a different outcome; the two conflicting `GM-001` meanings must receive new future IDs. |
| `ARCH-001` | Accepted | Hearth Shell is a Hearth-owned Quickshell/QML shell on unmodified niri, not a maintained DMS product. |
| `ARCH-002` | Accepted | Do not implement the shell with web technology, Electron, React, HTML, a WebView, or localhost frontend. |
| `ARCH-003` | Accepted | Reuse proven, license-compatible donors selectively; do not rebuild useful technology or import a donor wholesale without an audit. |
| `ARCH-004` | Accepted | License Hearth Shell `GPL-3.0-only` and maintain exact per-file import and attribution records. |
| `ARCH-005` | Accepted | Use one Rust companion for lifecycle, semantic routing, safe launch, diagnostics, public IPC, configuration validation/migration, and OSK supervision. |
| `ARCH-006` | Accepted | Launch applications in separate transient user-systemd units or scopes so shell failure does not terminate them. |
| `ARCH-007` | Accepted | Use layered versioned JSON configuration: packaged defaults, `/etc` policy, then XDG user configuration. |
| `ARCH-008` | Accepted | Invalid user configuration must fail visibly and fall back safely rather than preventing shell startup. |
| `ARCH-009` | Accepted | The eventual runtime performs a hard Hearth rename; DMS command, service, IPC, and config compatibility are not target contracts. |
| `ARCH-010` | Accepted | In hearthOS Desktop, `niri.service` exclusively owns companion/UI startup and teardown; the companion acquires the public D-Bus name before the UI starts, and no compositor command duplicates the systemd start path. |

## Input, focus, and glyphs

| ID | State | Requirement |
| --- | --- | --- |
| `INPUT-001` | Accepted | Controller UI actions are semantic events, not global fake keyboard keys; physical keyboard input remains independent. |
| `INPUT-002` | Accepted | Hearth-native surfaces define visible, deterministic, dynamic focus graphs that skip disabled items and restore focus on close. |
| `INPUT-003` | Accepted | Navigation Mode is the default; Text Mode begins only after deliberate text/search activation. |
| `INPUT-004` | Accepted | Arrows, `HJKL`, and `WASD` navigate Hearth surfaces outside Text Mode; printable typing does not automatically start search. |
| `INPUT-005` | Accepted | `i`, `/`, and `Ctrl+F` invoke a surface's primary search; auto-focused fields do not silently enter Text Mode. |
| `INPUT-006` | Accepted | Controller/touch text activation may open the OSK; physical keyboard entry does not and instead shows a small mode indicator. |
| `INPUT-007` | Accepted | Reusable glyphs adapt to Xbox, PlayStation, Nintendo physical positions, and a generic fallback; mappings are data-driven. |
| `INPUT-008` | Accepted | D-pad controls focus, left stick scrolls, and right stick controls the pointer outside the OSK. |
| `INPUT-009` | Proposed | Controller Settings provides a layout illustration, family-correct face labels, leader lines, action descriptions, modifier support, and a New Keybind flow. |
| `INPUT-010` | Open | Guide, View, L3/R3, global media/window/workspace chords, pointer acceleration, and controller-family precedence require later decisions. |

## Hearth Bar and shell surfaces

| ID | State | Requirement |
| --- | --- | --- |
| `BAR-001` | Accepted | The Hearth Bar is normally unobtrusive and becomes visible while hovered, keyboard/controller focused, or any bar-owned panel—including App Menu—is open. |
| `BAR-002` | Accepted | Hidden pointer reveal uses the configured bar-span edge sensor; reveal is immediate and hide uses a configurable 250 ms grace after all visibility reasons clear. |
| `BAR-003` | Accepted | Closing a bar-owned panel with controller/keyboard returns focus to its opening bar item and keeps the bar visible while that focus remains. |
| `BAR-004` | Proposed | Bar items are customizable and support pointer drag/drop/context actions with keyboard/controller equivalents. |
| `BAR-005` | Proposed | Hardware-inapplicable controls, such as battery/power on a desktop, remain hidden. |
| `BAR-006` | Open | Final left/center/right information architecture, initial focus item, multi-output policy, and edit workflow remain undecided. |
| `SURFACE-001` | Accepted | Opening a shell panel coordinates dim/blur with its originating bar item; the active bar and surface stay visually connected. |
| `SURFACE-002` | Accepted | Do not restore the inherited enlarged-panel treatment merely by renaming DMS components. |
| `WORKSPACE-001` | Proposed | Workspace and window surfaces use real niri IPC/state and expressive directional overlays rather than a duplicate shell model. |
| `CONTROL-001` | Proposed | Start with a small customizable control-center/notification surface, controller-aware sliders, and conditional hardware controls. |
| `CONTROL-002` | Open | Merged notification/control-center behavior and final placement remain unresolved; Steam notification behavior requires investigation. |

## App Menu

| ID | State | Requirement |
| --- | --- | --- |
| `LAUNCH-001` | Accepted | App Menu is a right drawer, approximately 38% logical width and clamped near 520–760 logical pixels with safe margins; narrow outputs may use near-full width. |
| `LAUNCH-002` | Accepted | The drawer dims/subtly blurs the desktop, leaves the Hearth Bar active, and closes from its scrim. |
| `LAUNCH-003` | Accepted | Exactly two persistent modes exist: Grid and List. West face toggles them; `Ctrl+1` selects Grid and `Ctrl+2` selects List. |
| `LAUNCH-004` | Accepted | Initial tabs are Favorites, Recent, By Name, and By Category; RT/LT move next/previous tab and `Ctrl+Tab`/`Ctrl+Shift+Tab` are keyboard equivalents. |
| `LAUNCH-005` | Accepted | By Name groups letters; By Category uses freedesktop Main Categories, allows all matching groups, and has an Other fallback. |
| `LAUNCH-006` | Accepted | A left index rail morphs into group overview rows with a label and up to two stacked app-card previews, then restores the saved Grid/List view at the chosen group. |
| `LAUNCH-007` | Accepted | Opening focuses the first favorite or, if none exists, the first alphabetically visible application. Search never steals initial focus. |
| `LAUNCH-008` | Accepted | Core favorites are Return to Gaming Mode, Steam, Firefox, Dolphin, and Ghostty. |
| `LAUNCH-009` | Accepted | Recents contain successful drawer launches only, are unique MRU entries capped at 12, and permit removed applications to reappear after a later launch. |
| `LAUNCH-010` | Accepted | Menu/Start opens App Menu globally and opens selected-app actions while inside it; Menu key or `Shift+F10` is the keyboard context equivalent. |
| `LAUNCH-011` | Accepted | `Super+A` is the sole accepted global keyboard launcher shortcut; the former F10 proposal is superseded. |
| `LAUNCH-012` | Open | Default/remembered tab, search scope/ranking, grid density, edge wrapping, metadata, failure handling, and multi-output state remain undecided. |

## On-screen keyboard

| ID | State | Requirement |
| --- | --- | --- |
| `OSK-001` | Accepted | Preserve and fork wvkbd v0.20 commit `6b41504a0cb58fd1163fa44692398fbd61f8905f` in a separate upstream-history repository. |
| `OSK-002` | Accepted | The Rust companion supervises the OSK child; the child is not an unrelated system service and does not become another public API. |
| `OSK-003` | Accepted | Use input-method-v2, text-input-v3, virtual-keyboard-v1, and layer shell; support exact active XKB layout and variant. |
| `OSK-004` | Accepted | Provide four-row Letters, Numbers, and Symbols layers; emoji and handwriting are deferred. |
| `OSK-005` | Accepted | Overlay is default; visible Pin/Dock toggles a per-output remembered docked mode that reserves an exclusive bottom zone. |
| `OSK-006` | Accepted | Balanced geometry is about 72% width by 34% height, capped near 1100×360 logical pixels with at least 48 logical-pixel key targets. |
| `OSK-007` | Accepted | North face opens the OSK immediately outside it and targets the active field or surface primary search; `Super+I` and `F12` are manual keyboard fallbacks. |
| `OSK-008` | Accepted | Back closes the OSK and exits Text Mode in one action, restoring navigational focus to the field's owning control. |
| `OSK-009` | Accepted | Secure fields disable character popups, content feedback/retention, suggestions, and all content logging while preserving visible focus. |
| `OSK-010` | Accepted | Hearth fields are reliable; third-party Wayland text input is best effort; unsupported and XWayland clients retain manual fallback without a universal-support claim. |
| `OSK-011` | Accepted | OSK controller mapping and caret-repeat constants are canonical in the OSK behavior contract. |
| `OSK-012` | Open | Public IPC version, private child protocol, unsupported-client UX, and physical-keyboard grab implementation require later design. |

## Settings, applications, plugins, and visual system

| ID | State | Requirement |
| --- | --- | --- |
| `SETTINGS-001` | Proposed | Hearth Settings is a first Hearth-native application and initially configures Hearth rather than duplicating every system settings page. |
| `SETTINGS-002` | Proposed | Settings covers controller/shortcuts, Bar, App Menu, control center, motion/reduced motion, Starlight tones, wallpaper, plugins, and About/attribution. |
| `APP-001` | Proposed | Hearth Portal is the other first Hearth-native application; later MPV UI remains separate future work. |
| `APP-002` | Proposed | Hearth-native apps share shell interaction primitives and use the same installation/state in Desktop and Gaming Mode where practical. |
| `APP-003` | Accepted | Dolphin remains the default file manager while existing application/profile approaches are evaluated. |
| `MOTION-001` | Accepted | Use a central motion/token system for effects/spatial durations, easing, springs, deformation, state layers, and reduced-motion policy. |
| `MOTION-002` | Accepted | Default interaction remains lively; reduced motion is a deliberate alternate path, not a reason to make default feedback timid. |
| `PLUGIN-001` | Proposed | Provide a secure but powerful plugin model with explicit trust, service, state, failure-containment, and lifecycle boundaries. |
| `PLUGIN-002` | Proposed | The default wallpaper system is an early real plugin use case and must not be buried entirely in a Settings QML page. |

## Wallpaper and provider system

| ID | State | Requirement |
| --- | --- | --- |
| `WALL-001` | Proposed | Support local wallpapers and an online-provider abstraction; Waifu.im is the first provider and uses its API rather than scraping. |
| `WALL-002` | Proposed | Ship visible conservative SFW defaults: waifu included; oppai/selfies excluded; landscape; non-animated; minimum near 1920×1080. |
| `WALL-003` | Proposed | Do not feature a dedicated NSFW mode; knowledgeable users may edit generic valid provider parameters. |
| `WALL-004` | Proposed | Use a real query encoder supporting repeated keys and pin the production API version through `Accept-Version`. |
| `WALL-005` | Proposed | Use U²-NetP only for reduced-resolution saliency inference; deterministic Hearth scoring selects and caches original-resolution crops. |
| `WALL-006` | Proposed | Crop scoring preserves salient subjects and useful negative space, avoids awkward cuts, and uses deterministic fallback/tie-breaking. |
| `WALL-007` | Proposed | Network/model failure retains the last known-good or safe local wallpaper and never blocks the shell render thread. |
| `WALL-008` | Open | Rotation, history, favorites, cache retention, attribution UI, per-monitor policy, minimum resolution, scoring constants, and need for a second detector remain undecided. |

## Portal, Gaming Mode, and inherited-base retirement

| ID | State | Requirement |
| --- | --- | --- |
| `PORTAL-001` | Proposed | Hearth Portal adapts and overrides the Bazzite Portal catalog rather than copying it; QML selects typed actions and never supplies arbitrary privileged commands. |
| `PORTAL-002` | Proposed | Portal may manage games/tweaks and must communicate and safely perform required Steam restarts in the correct session context. |
| `PORTAL-003` | Open | Exact catalog adapter, privilege boundary, update strategy, and potential Decky-Framegen/ProtonPlus replacement scope remain undecided. |
| `GM-REQ-001` | Proposed | Preserve independent shader-responsiveness and measured controller/input-to-display latency investigations without assuming Hearth caused either issue. |
| `GM-REQ-002` | Proposed | Register selected Hearth apps as Steam entries and later build a Hearth-owned Decky plugin using shared core features rather than duplicate implementations. |
| `GM-REQ-003` | Proposed | Preserve unrelated owner Decky plugins and isolate any Decky-Framegen retirement. |
| `GM-REQ-004` | Open | Gaming Mode roadmap order and replacement IDs for both collided `GM-001` records remain undecided. |
| `BASE-001` | Accepted | Retain KDE recovery until a separate owner audit proves display, network, authentication, terminal, file recovery, rollback, TTY, and diagnostics without Plasma. |
| `BASE-002` | Proposed | Remove or hide inherited applications only after a proven replacement or Portal action exists; dependency-required libraries may remain. |

## File-manager contingency

| ID | State | Requirement |
| --- | --- | --- |
| `FM-001` | Contingency | Test Dolphin and Nautilus before authorizing custom file-manager work. |
| `FM-002` | Contingency | If both fail owner requirements, activate a new `FM-*` track before KDE recovery retirement and fork Index directly rather than building from scratch. |
| `FM-003` | Contingency | Reuse MauiKit FileBrowsing, KF6, KIO, and useful KDE libraries where appropriate; Plasma-shell retirement does not require removing those libraries. |
| `FM-004` | Contingency | Dolphin remains default until an Index-derived candidate receives explicit owner acceptance. |
