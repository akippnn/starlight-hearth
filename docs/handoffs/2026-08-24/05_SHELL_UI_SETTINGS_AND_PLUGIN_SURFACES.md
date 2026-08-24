# Hearth Shell UI, Settings, Apps, and Plugin Surfaces

## Hearth Bar

The newer Hearth Bar concept should guide planning instead of mechanically porting the DMS Dank Bar.

Desired characteristics:

- Customizable item/widget placement.
- Normally visually unobtrusive or effectively invisible.
- Interaction causes a clear MD3E-style background blur/state treatment so the bar becomes legible without permanently occupying the visual scene.
- Mouse hover, keyboard focus, and controller focus should all produce coherent visible states.
- Controller View/Select can focus the bar; initial focused item/edge should be configurable.
- Contextual editing via drag/drop/right-click with controller/keyboard equivalents.
- Related panel open state remains visually clear on its bar item.
- Strong expressive press/release interaction, not a tiny opacity flicker.
- Hardware-inapplicable widgets such as laptop/battery/power-specific controls should not appear blindly on desktop hardware.

## App Menu

The owner wants a simple, controller/keyboard-first launcher rather than a giant DMS panel.

Plan for:

- placement near the right side of the Hearth Bar in the current concept;
- grid/list navigation with predictable focus;
- configurable grid density;
- categories with configurable default category;
- category reassignment via mouse drag/drop and a non-pointer context menu;
- search that is explicitly invoked/focused rather than auto-focused on open;
- context/options per app;
- possible layout/mode changes;
- consistent controller glyph hints;
- keyboard schemes including conventional arrows and keyboard-power-user options;
- no hardcoded assumption that one particular app is the first focus target.

## Workspaces and switcher

- Workspace control near the App Menu in the current concept.
- Use niri's real workspace/window data/IPC rather than duplicating state.
- Window/workspace switcher should use a coherent blurred expressive overlay.
- Proposed configurable defaults include `Meta+F3`, `Meta+Tab`, and `Meta+\``.
- Controller navigation should reuse semantic input primitives.

## Clock

- Time/clock centered on the Hearth Bar initially.
- It does not need to become a complex calendar/dashboard in the foundation slice.

## Control center, tray, and notifications

Newer direction:

- system tray/control-center area toward the left of Hearth Bar;
- simple/customizable control center initially;
- widget placement and configurable grid density;
- avoid recreating every GNOME/KDE system settings page at once.

Earlier requirement still worth preserving for reconciliation:

- merge notifications and control-center concepts into a coherent surface rather than duplicating two unrelated large panels;
- notification state/icon should be clearly visible;
- investigate Steam notification behavior that was observed as a window instead of a conventional notification.

The exact left/right placement and final information architecture are deliberately not settled in this handoff because the earlier DMS-specific requirement and newer Hearth Bar layout differ.

## Overlay treatment

The owner does not want the old “everything becomes a huge enlarged panel” approach. When a shell surface opens, consider a coordinated overlay that dims/grays/de-emphasizes the rest of the desktop while keeping the Hearth Bar and active surface visually connected. This should animate as one transition and should not make the active surface feel disconnected from the control that opened it.

## Hearth Settings

Hearth Settings is a first-party application and should establish the quality bar for controller/keyboard navigation.

Early Settings should focus on Hearth-specific customization rather than duplicating every system preference:

- Controller Layout and keyboard shortcuts.
- Hearth Bar layout/interaction.
- App Menu behavior, category/default/category management, grid density.
- Control center/widget density/layout.
- Motion/animation settings including expressive intensity and reduced motion.
- Starlight color tones and custom tone input.
- Wallpaper/background provider and crop behavior.
- Plugin management as the plugin architecture matures.
- Hearth information/About attribution.

Configuration requirements:

- one coherent documented settings/config model;
- non-default settings represented in config;
- Settings writes through that model rather than storing unrelated component state;
- shell observes and applies valid changes;
- config-file edits should be observed/applied when practical;
- validation/failure should not make the shell unbootable;
- unknown/new keys should be handled with a migration/versioning strategy chosen during design.

The exact file format/schema is intentionally left for Codex to plan.

## Hearth information / attribution

Replace inherited DMS-branded Settings/About identity with Hearth information while retaining correct attribution to projects that actually contribute technology or inspiration, including as applicable:

- Quickshell
- niri
- Bazzite / Universal Blue
- Steam / Gamescope / Steam Input
- DMS
- Caelestia
- M3Shapes
- InputPlumber
- other copied/adapted libraries with license-required notices

Do not misrepresent reference inspiration as code ownership, and do not omit license notices for directly reused code/assets.

## Hearth-native applications

- Hearth Settings and Hearth Portal are the first two.
- They must be controller + keyboard navigable from the beginning.
- They should share design/input primitives with the shell rather than each rebuilding controls.
- Some should open in Gaming Mode as the same installed application, context-aware rather than duplicated.
- MD3E identity should survive Gaming Mode scaling/windowing.
- MPV UI is a later candidate.

## Plugin system

Goal: secure but powerful.

Do not solve the entire plugin ecosystem in one giant ABI. Codex should inspect DMS and Caelestia plugin designs, Quickshell extension mechanisms, process/security boundaries, configuration ownership, update/lifecycle requirements, and hearthOS's immutable packaging model.

The **background/wallpaper plugin installed by default** is a useful early real plugin use case. Use it to force a clean answer to questions such as:

- what a plugin can render;
- what services it can request;
- how plugin settings are surfaced;
- where plugin config/state/cache live;
- how plugins are enabled/disabled;
- how failures are contained;
- how default/system plugins differ from user plugins;
- how Gaming Mode can reuse non-UI plugin/core functionality later.

Those are planning questions, not predetermined answers in this handoff.
