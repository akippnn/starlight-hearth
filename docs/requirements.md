# hearthOS requirements register

**Authority:** canonical product requirements
**Last reconciled:** 2026-08-29
**Freeze state:** the HSN-001 subset is frozen by its exact v2 slice contract;
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
| `ARCH-001` | Accepted | hearthOS Shell is a hearthOS-owned Quickshell/QML shell on unmodified niri, not a maintained DMS product. |
| `ARCH-002` | Accepted | Do not implement the shell with web technology, Electron, React, HTML, a WebView, or localhost frontend. |
| `ARCH-003` | Accepted | Reuse proven, license-compatible donors selectively; do not rebuild useful technology or import a donor wholesale without an audit. |
| `ARCH-004` | Accepted | License Hearth Shell `GPL-3.0-only` and maintain exact per-file import and attribution records. |
| `ARCH-005` | Accepted | Use one Rust companion for lifecycle, semantic routing, safe launch, diagnostics, public IPC, configuration validation/migration, and OSK supervision. |
| `ARCH-006` | Accepted | Launch applications in separate transient user-systemd units or scopes so shell failure does not terminate them. |
| `ARCH-007` | Accepted | Use layered versioned JSON configuration: packaged defaults, `/etc` policy, then XDG user configuration. |
| `ARCH-008` | Accepted | Invalid user configuration must fail visibly and fall back safely rather than preventing shell startup. |
| `ARCH-009` | Accepted | The eventual runtime performs a hard Hearth rename; DMS command, service, IPC, and config compatibility are not target contracts. |
| `ARCH-010` | Accepted | In hearthOS Desktop, `niri.service` exclusively owns companion/UI startup and teardown; the companion acquires the public D-Bus name before the UI starts, and no compositor command duplicates the systemd start path. |
| `ARCH-011` | Accepted | Before creating a new system component, inspect and extend the current shared primitive or record why reuse is impossible; HSN-001, HSN-002, HIN-001/HIN-002, later outcomes, and selectively salvaged pre-HSN work must not accumulate duplicate focus, hint, catalog, motion, configuration, or provider implementations. |

## Input, focus, and glyphs

| ID | State | Requirement |
| --- | --- | --- |
| `INPUT-001` | Accepted | Controller UI actions are semantic events, not global fake keyboard keys; physical keyboard input remains independent. |
| `INPUT-002` | Accepted | hearthOS-native surfaces define visible, deterministic, dynamic focus graphs that skip disabled items and restore focus on close. |
| `INPUT-003` | Accepted | Navigation Mode is the default; Text Mode begins only after deliberate text/search activation. |
| `INPUT-004` | Accepted | Arrows, `HJKL`, and `WASD` navigate Hearth surfaces outside Text Mode; printable typing does not automatically start search. |
| `INPUT-005` | Accepted | `i`, `/`, and `Ctrl+F` invoke a surface's primary search; auto-focused fields do not silently enter Text Mode. |
| `INPUT-006` | Accepted | Controller/touch text activation may open the OSK; physical keyboard entry does not and instead shows a small mode indicator. |
| `INPUT-007` | Accepted | Reusable glyphs adapt to Xbox, PlayStation, Nintendo physical positions, and a generic fallback; mappings are data-driven. |
| `INPUT-008` | Accepted | D-pad controls focus, right stick controls the pointer, and left stick is context-sensitive: base Desktop scroll remains available, while registered Hearth navigation surfaces such as App Menu consume its axis as semantic focus with hysteresis and repeat. |
| `INPUT-009` | Proposed | Controller Settings provides a layout illustration, family-correct face labels, leader lines, action descriptions, and a New Keybind flow. Every action is remappable; users may create custom semantic modifier layers and assign hold and/or latch triggers independently, with conflict diagnostics and recovery. |
| `INPUT-010` | Accepted | Active specific-context actions override broader/global actions and suppress the losing action completely. Base RB/LB remain primary/secondary pointer clicks. Proposed HIN-001 uses R3 navigation and L3 manipulation as packaged defaults; historical L3-window/R3-workspace bumper defaults are superseded planning. |
| `INPUT-011` | Proposed | First Setup offers Classic and Vim keyboard presets while preserving shared search, activation, and context commands; this is future work outside HSN-002. |
| `INPUT-012` | Proposed | HIN-001 provides an always-available headless hold/chord layer backed by real niri IPC: packaged R3 plus D-pad/left stick focuses windows/workspaces; packaged L3 plus LB/RB/West/North moves, closes, or maximizes the focused window. Semantic layers remain independent from these defaults. |
| `INPUT-013` | Proposed | HIN-001 adds Guide+left-stick media, Guide+RT niri screenshot, capability-gated controller power-off, and a 2.4-second capability-gated force-quit that targets only a verified user application scope. |
| `INPUT-014` | Proposed | Disconnect, reconnect, provider loss, context transfer, and session teardown release all dependent actions, clear modifiers/repeat timers, and never replay stale input. |
| `INPUT-015` | Proposed | HIN-002 provides mutually exclusive visible Navigate and Manipulate latches with packaged R3/L3 defaults, switches directly between them, uses niri Overview/state/animation, and never emulates windows or workspaces in QML. |
| `INPUT-016` | Proposed | `Meta+Tab` toggles HIN-002 Navigate; `Meta+H/L` directly focuses left/right; Vim HJKL navigates and `x`/`f` close/maximize through the same semantic actions. Bindings remain configurable and future First Setup owns preset choice. |
| `INPUT-017` | Proposed | `InputHintBar` is a first-class shared primitive with semantic action sourcing, context precedence, modifier-first expansion, controller-family glyphs, bottom-safe placement, accessibility text, reduced motion, and reuse across HSN-002, HIN-002, OSK/Text Mode, System Bar, and later surfaces. HIN-001 supplies headless state; HSN-002 supplies the first visual implementation. |
| `INPUT-018` | Accepted | Physical bindings are defaults, not immutable behavior. Stable semantic layers/actions are separate from trigger data; hold and latch triggers may differ, including RT/LT hold with R3/L3 latch, and custom modifiers may reference only registered semantic actions rather than arbitrary commands. |
| `INPUT-019` | Accepted | View/Select is reserved for future System Bar controller focus, initially selecting Control Center. Base LT/RT and Guide+LT, Guide+RS, Guide+LB, and Guide+RB remain unassigned. |

## hearthOS System Bar and shell surfaces

| ID | State | Requirement |
| --- | --- | --- |
| `BAR-001` | Accepted | The hearthOS System Bar is normally unobtrusive and becomes visible while hovered, keyboard/controller focused, or any System Bar-owned panel—including App Menu—is open. |
| `BAR-002` | Accepted | Hidden pointer reveal uses the configured bar-span edge sensor; reveal is immediate and hide uses a configurable 250 ms grace after all visibility reasons clear. |
| `BAR-003` | Accepted | Closing a bar-owned panel with controller/keyboard returns focus to its opening bar item and keeps the bar visible while that focus remains. |
| `BAR-004` | Proposed | Bar items are customizable and support pointer drag/drop/context actions with keyboard/controller equivalents. |
| `BAR-005` | Proposed | Hardware-inapplicable controls, such as battery/power on a desktop, remain hidden. |
| `BAR-006` | Open | Final left/center/right information architecture, unavailable-default fallback, multi-output policy, and edit workflow remain undecided. |
| `BAR-007` | Accepted | View/Select enters System Bar focus and initially selects Control Center; later customization may change its remembered/default target without changing the semantic focus action. |
| `SURFACE-001` | Accepted | Opening a shell panel coordinates dim/blur with its originating bar item; the active bar and surface stay visually connected. |
| `SURFACE-002` | Accepted | Do not restore the inherited enlarged-panel treatment merely by renaming DMS components. |
| `WORKSPACE-001` | Proposed | Workspace and window surfaces use real niri IPC/state and expressive directional overlays rather than a duplicate shell model. |
| `WORKSPACE-002` | Proposed | HIN-001/HIN-002 focus niri columns left/right and workspaces up/down; manipulation swaps only the focused window left/right in the same workspace. Moving apps between workspaces, moving whole columns, and workspace reordering remain later scope. |
| `CONTROL-001` | Proposed | Start with a small customizable control-center/notification surface, controller-aware sliders, and conditional hardware controls. |
| `CONTROL-002` | Open | Merged notification/control-center behavior and final placement remain unresolved; Steam notification behavior requires investigation. |

## App Menu

| ID | State | Requirement |
| --- | --- | --- |
| `LAUNCH-001` | Accepted | App Menu is a right drawer, approximately 38% logical width and clamped near 520–760 logical pixels with safe margins; narrow outputs may use near-full width. |
| `LAUNCH-002` | Accepted | The drawer dims/subtly blurs the desktop, leaves any hearthOS System Bar opener active, and closes from its scrim. |
| `LAUNCH-003` | Accepted | Exactly two persistent modes exist: Grid and List. West face toggles them; `Ctrl+1` selects Grid and `Ctrl+2` selects List. |
| `LAUNCH-004` | Accepted | Initial tabs are Favorites, Recents, By Name, and By Category; the App Menu manipulation modifier plus RB/LB moves next/previous tab (`L3` is the packaged modifier default), and `Ctrl+Tab`/`Ctrl+Shift+Tab` are keyboard equivalents. Base RT/LT are not tab controls. |
| `LAUNCH-005` | Accepted | By Name groups letters; By Category uses freedesktop Main Categories, allows all matching groups, and has an Other fallback. |
| `LAUNCH-006` | Proposed | HSN-002 places a right index rail and right icon-only Grid/List selector around reusable `CollectionBrowser`/read-only `Category1` content; the active tab has no redundant title. |
| `LAUNCH-007` | Accepted | Opening focuses the first favorite or, if none exists, the first alphabetically visible application. Search never steals initial focus. |
| `LAUNCH-008` | Accepted | Core favorites are Return to Gaming Mode, Steam, Firefox, Dolphin, and Ghostty. |
| `LAUNCH-009` | Accepted | Recents contain successful drawer launches only, are unique MRU entries capped at 12, and permit removed applications to reappear after a later launch. |
| `LAUNCH-010` | Accepted | Menu/Start opens App Menu globally and opens selected-app actions while inside it; Menu key or `Shift+F10` is the keyboard context equivalent. |
| `LAUNCH-011` | Accepted | `Super+A` is the sole accepted global keyboard launcher shortcut; the former F10 proposal is superseded. |
| `LAUNCH-012` | Proposed | HSN-002 `Search Apps` covers Name, GenericName, and Keywords, ranked by exact name, name prefix, name-word match, GenericName/Keywords, then remaining substring with stable alphabetical ties. |
| `LAUNCH-013` | Proposed | HSN-002 migrates configuration to schema v2 and exposes typed Favorite, Unfavorite, and Remove from Recents actions while preserving schema-v1 and public D-Bus compatibility. |
| `LAUNCH-014` | Proposed | Every App Menu open starts on Favorites; clearing search restores the prior tab, selection, and scroll position; those states are transient while Grid/List persists. |
| `LAUNCH-015` | Proposed | Before OSK delivery, controller can enter/exit search and navigate results, but physical keyboard input is required to compose the query and the limitation remains visible. |
| `LAUNCH-016` | Proposed | Add read-only `Category1` and typed `AppCatalog1` at `/Catalog` without reinterpreting `Launcher1` or `Config1`; exact wire shapes are frozen only with the HSN-002 contract. |
| `LAUNCH-017` | Proposed | HSN-002 maps both D-pad and left stick to semantic focus in App Menu. A held direction repeats after 260 ms at 90 ms and accelerates to 55 ms after one second so sustained movement retargets the existing 140 ms selection surface by sliding. |
| `LAUNCH-018` | Proposed | HSN-002 delivers the shared `InputHintBar`; App Menu supplies ordered actions and placement but does not own a private glyph/modifier implementation. |
| `LAUNCH-019` | Proposed | HSN-002 may adapt only the pinned Caelestia Blob subset named in its contract for the contained right-index overview transition, with per-file GPL attribution, reduced-motion fallback, visual containment, allocation/memory/frame-time gates, and no continuous/full-screen/selection replacement. |

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
| `OSK-010` | Accepted | hearthOS fields are reliable; third-party Wayland text input is best effort; unsupported and XWayland clients retain manual fallback without a universal-support claim. |
| `OSK-011` | Accepted | OSK controller mapping and caret-repeat constants are canonical in the OSK behavior contract. |
| `OSK-012` | Open | Public IPC version, private child protocol, unsupported-client UX, and physical-keyboard grab implementation require later design. |

## Settings, applications, plugins, and visual system

| ID | State | Requirement |
| --- | --- | --- |
| `SETTINGS-001` | Proposed | hearthOS Settings is a first hearthOS-native application and initially configures hearthOS rather than duplicating every system settings page. |
| `SETTINGS-002` | Proposed | Settings covers controller/shortcuts, System Bar, App Menu, control center, motion/reduced motion, Starlight tones, wallpaper, plugins, and About/attribution. |
| `APP-001` | Proposed | hearthOS Portal is the other first hearthOS-native application; later MPV UI remains separate future work. |
| `APP-002` | Proposed | hearthOS-native apps share shell interaction primitives and use the same installation/state in Desktop and Gaming Mode where practical. |
| `APP-003` | Accepted | Dolphin remains the default file manager while existing application/profile approaches are evaluated. |
| `MOTION-001` | Accepted | Use a central motion/token system for effects/spatial durations, easing, springs, deformation, state layers, and reduced-motion policy. |
| `MOTION-002` | Accepted | Default interaction remains lively; reduced motion is a deliberate alternate path, not a reason to make default feedback timid. |
| `PLUGIN-001` | Proposed | Provide a secure but powerful plugin model with explicit trust, service, state, failure-containment, and lifecycle boundaries. |
| `PLUGIN-002` | Proposed | Online wallpaper providers and broader wallpaper plugin architecture are later independent outcomes, not HWP-001. |
| `PLUGIN-003` | Proposed | Built-in plugins such as local wallpaper and independent search are first-party packaged and audited components with clear first-party labeling. |
| `PLUGIN-004` | Proposed | Third-party plugins are explicitly trusted user-installed code; hearthOS does not guarantee their security, correctness, privacy, maintenance, or compatibility. Installation requires clear third-party labeling and explicit user consent. |
| `PLUGIN-005` | Proposed | Users and downstream developers may create GPL-3.0-compatible plugins, including with LLM assistance, but generated code is not inherently safe and still requires human review, provenance/license verification, and explicit installation consent. |
| `PLUGIN-006` | Proposed | Plugin architecture must provide version compatibility, bounded capabilities, failure containment, visible diagnostics, disable/recovery paths, and a first-party/third-party distinction before third-party loading is authorized. |
| `SETUP-001` | Proposed | First Setup configures the future Classic/Vim keyboard preset and other owner-approved onboarding choices; it is not HSN-002 scope. |
| `INSTALL-001` | Proposed | Install hearthOS remains a separate future owner-visible outcome with its own recovery and rollback contract. |

## Wallpaper and provider system

| ID | State | Requirement |
| --- | --- | --- |
| `WALL-001` | Proposed | HWP-001 selects a local wallpaper, ships a recovery background, renders per output without blocking the shell, applies deterministic center crop, and retains the last good selection. |
| `WALL-002` | Open | Online providers, provider parameters, attribution, rotation/history/favorites, and cache policy belong to later proposed outcomes. |
| `WALL-003` | Open | Palette extraction, advanced saliency/subject-aware cropping, detector/model choice, and scoring policy belong to later proposed outcomes. |
| `WALL-004` | Open | A broader wallpaper plugin architecture requires a later independent contract after the local HWP-001 baseline. |

## Portal, Gaming Mode, and inherited-base retirement

| ID | State | Requirement |
| --- | --- | --- |
| `PORTAL-001` | Proposed | hearthOS Portal adapts and overrides the Bazzite Portal catalog rather than copying it; QML selects typed actions and never supplies arbitrary privileged commands. |
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
