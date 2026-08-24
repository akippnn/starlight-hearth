# Exhaustive Requirements Inventory

This is an organized inventory of the owner's requirements across the original prompt and the follow-up discussion. It intentionally includes requirements that conflict with earlier implementation assumptions or with one another. `09_OPEN_QUESTIONS_AND_CONFLICTS.md` identifies the main places that require planning/reconciliation. The exact original text remains in `10_ORIGINAL_PROMPT_VERBATIM.md`.

## A. Shell architecture and project boundaries

- Dedicate focused work to `starlight-hearth-shell` and keep delivery concerns properly separated between `starlight-hearth` and `starlight-hearth-shell`.
- Use the existing vertical-slice discipline rather than treating the entire shell as one implementation task.
- Repurpose useful existing work but move toward a fully custom Hearth Shell using Quickshell/QML on niri.
- The DMS downstream threshold is crossed; DMS is no longer the product architecture. Keep it installed/available for inspiration and features worth studying.
- Avoid hardcoding and avoid collisions with upstream/system behavior where possible.
- Preserve clean branch/repository history and make upstreaming generally useful controller/keyboard improvements a separate concern from Hearth-specific product behavior when that still makes sense.
- Do not build a web-app shell or use a web frontend as a shortcut around QML/Quickshell.
- Build a solid foundation before chasing every small feature.
- Preserve recovery while the custom shell is immature.

## B. Input model and controller awareness

- The shell must know when a controller is connected.
- Controller buttons must not simply turn into global keyboard buttons.
- Controller handling must not block actual physical-keyboard input.
- Hearth-native shell apps/widgets/panels must have dedicated controller-aware navigation.
- Controller and keyboard navigation should converge on shared semantic behaviors where possible.
- Many existing applications behave unpredictably with controller input; Hearth-native surfaces should not.
- Opening a panel should choose an appropriate first focus target dynamically, not through brittle hardcoded coordinates/item identities.
- Search fields should not steal focus merely because a controller-opened panel appeared.
- A search action should focus the search field; focusing that text field should then trigger the OSK where appropriate.
- Sliders such as audio and brightness require deliberate controller interaction behavior.
- Tabs/categories/modes should be navigable through dedicated semantic actions such as previous/next group rather than accidental Tab-key behavior.
- Shell-native apps and widgets with controller support should display the relevant controller glyph/action hints.
- Modifier layers are required and should be representable in both the controller model and UI hints.
- Physical controller identity/glyph family should support Xbox, PlayStation, Nintendo, and generic face-button conventions.
- The owner wants the shell to be equally intentional for keyboard-heavy operation, including Vim-like/WASD/arrow options where appropriate.

## C. Controller Layout Settings

- Hearth Settings needs a dedicated **Controller Layout** section/page.
- Display a controller-layout visual with labels/leader lines showing what each physical control does.
- The base controller illustration can be standardized, but ABXY face-button labeling/glyphs must adapt correctly for PlayStation/Xbox/Nintendo layout families.
- Retain/equivalently recreate the existing “New Keybind” capability for assigning supported button/action types.
- Support modifier buttons/chords.
- Eventually place controller settings naturally within a broader System section when the Settings information architecture grows.
- Expose customizable keyboard shortcuts and controller layout rather than baking the owner's current mappings permanently into QML components.

## D. Controller behavior ideas from the earlier DMS phase that must be translated/reconciled

- Earlier desired behavior included LB/RB navigation between categories/tabs such as Processes `All/User/System` and App Menu `All/Apps/Files/Plugins`.
- Earlier desired face-button semantics included a dedicated search focus action and a contextual mode/action button.
- The View/Select button should be able to focus the shell bar, with a configurable preferred starting edge/item; the owner previously preferred the right-most item in the DMS layout.
- When a modifier is required, UI hints should be able to show the modifier alone until held, then reveal the secondary action buttons (for example workspace previous/next on the edges of the workspace widget).
- Earlier window controls included close/fullscreen and previous/next window/workspace actions using stick-click modifier layers.
- Earlier behavior included page scrolling from a stick axis.
- These behaviors should be preserved as product intent where still useful, but the exact current mapping must be reconciled with the later proposed Steam-like controller layout and the existing v3 manifest.

## E. On-screen keyboard and text entry

- The OSK should be smaller/compact and appear at the bottom.
- It should not destroy or obscure the shell menu/panel that initiated text entry.
- For Hearth-supported text fields, focusing a text field should be able to trigger the OSK automatically in controller mode.
- Search should be an explicit semantic focus action rather than forcing the OSK open before the search field is focused.
- Preserve physical keyboard coexistence.
- The current roadmap rejects a universal compositor-wide external-application OSK milestone; reconcile that with the owner's requirement for good text entry in Hearth-native/supported apps rather than silently expanding scope back to every arbitrary application.

## F. Hearth Bar and overlays

- Replace the old DMS/Dank Bar product concept with a Hearth-native bar direction.
- The Hearth Bar should be highly customizable.
- Desired behavior: normally unobtrusive/invisible, becoming visually present through MD3E-style blur/interaction when hovered, focused, or an item is selected.
- Support mouse drag-and-drop philosophy where appropriate.
- Support contextual/right-click menus; controller Start/Menu and keyboard shortcuts such as `Ctrl+I` / `Shift+I` were proposed as non-pointer equivalents and should be reconciled rather than blindly hardcoded.
- Controller View/Select should focus the bar.
- The bar should provide very visible expressive feedback when focused/pressed and indicate when a related panel/surface remains open.
- Earlier DMS work used enlarged panels; the owner wants to remove that approach and instead emphasize the active surface by dimming/graying the rest of the desktop while keeping the bar and selected widget/app visually active.
- Power/battery-specific surfaces should be conditional on hardware context; do not show a laptop-oriented power widget on a desktop simply because the upstream shell had one.
- Widgets should be placeable/customizable on the Hearth Bar.

## G. App Menu / launcher

- A simple App Menu lives at/near the right side of the Hearth Bar in the newer concept.
- Controller navigation: D-pad + left stick are candidate directional inputs.
- Keyboard navigation: WASD, Vim-style `hjkl`, and arrow keys were requested as possible supported schemes.
- Category navigation should have controller and keyboard equivalents; proposals include LT/RT and keyboard alternatives such as `q/e`, `Shift+h/l`, or `Shift+Left/Right`.
- Search should have controller and keyboard shortcuts; the owner proposed the north/left face-button position depending controller family plus `Ctrl+F`/backtick-like keyboard behavior. Resolve exact bindings through the configurable semantic layout.
- App options/context menu should be available via pointer right-click and non-pointer equivalents such as controller Menu/Start and keyboard context shortcuts.
- App categories should be user-manageable, including mouse drag/drop and context-menu-based reassignment usable from keyboard/controller.
- Default category should be configurable.
- App grid density/number of columns/items should be configurable in Hearth Settings.
- Opening the App Menu should deterministically focus a useful first item, but not hardcode a particular application name.

## H. Workspaces and switching

- A workspace button should be located near the App Menu in the proposed Hearth Bar layout.
- It should expose niri workspace behavior rather than implementing a fake workspace model in the shell.
- `Meta+F3` was proposed as a default keyboard shortcut and should be treated as a proposed/configurable default, not an immutable contract unless retained by the final plan.
- Provide a window/workspace switcher with an expressive blurred overlay.
- Proposed keyboard defaults: `Meta+Tab` for windows and `Meta+\`` for workspaces.
- Controller window/workspace navigation should be predictable and use the shared semantic routing layer.

## I. Center clock and control center / notifications

- The center of the Hearth Bar should show time/clock initially; it does not need a large feature set yet.
- A system-tray/control-center area is proposed on the left side of the newer Hearth Bar concept.
- The control center should be simple initially and customizable rather than reproducing every desktop control immediately.
- The control center should support movable/placeable widgets.
- Grid density should be configurable; the owner proposed a default around 3 columns/items depending interpretation.
- Earlier DMS requirements proposed merging notifications and control center into one widget/surface and replacing separate upstream widgets.
- Earlier placement put the merged notification/control widget at the far right with the notification icon right-most; the newer Hearth Bar layout moves App Menu/workspaces to the right and tray/control center left. Preserve the merged-surface idea as a requirement to evaluate, but reconcile placement in planning.
- Steam notifications were observed behaving more like windows than normal desktop notifications; investigate whether Hearth can improve integration rather than assuming the previous failed attempt was the final answer.

## J. Hearth Settings

- Hearth Settings is one of the first Hearth-native applications.
- Initially focus it on modifying Hearth Shell rather than duplicating all system settings already reachable elsewhere/Gaming Mode.
- Do not overpopulate it early.
- All non-default shell settings should be represented in the configuration model.
- Settings changes should apply automatically where possible.
- External/config-file edits should also be detected/applied where practical.
- Determine and document a configuration-file/configuration-schema standard.
- Include controller layout/shortcuts, Hearth Bar behavior/layout, launcher behavior/density/categories, control-center behavior/density, motion/animation preferences, Starlight color tones/custom tones, wallpaper/background, and later relevant system/controller sections.
- Replace inherited DMS identity/about information with Hearth information while properly attributing DMS, niri, Bazzite, Steam, Quickshell, and other upstream/reference projects where appropriate.

## K. Hearth-native applications

- Hearth Portal and Hearth Settings are the first two Hearth-native apps.
- Hearth-native applications must be completely navigable with controller and keyboard, not just mouse.
- MPV UI is a later Hearth-native application/surface idea; do not force it into the immediate shell foundation.
- Some Hearth applications should be launchable in Gaming Mode without separate duplicate app installations/instances.
- Hearth apps should be aware of whether they are running/opened from Gaming Mode vs Desktop when behavior/scaling/navigation needs to differ.
- Preserve MD3E identity in both contexts and pay attention to Gaming Mode window scaling.

## L. Starlight theming and design

- Provide a curated set of Starlight color tones in Settings plus custom tone support.
- Use high-quality fonts and iconography.
- Use high-quality controller glyphs/button hints.
- Favor the high-variety expressive character of MD3E rather than a uniform generic-card UI.
- Animation behavior should be theme-aware and customizable.
- Reduced-motion/accessibility behavior should exist without making the default experience timid.

## M. Secure plugin system

- Hearth Shell needs a secure but powerful plugin system.
- Do not prematurely invent a huge ABI in this handoff; Codex should inspect existing DMS/Caelestia/plugin patterns and plan an appropriately bounded first contract.
- Plugins should not require arbitrary unsafe QML/backend access merely because that is easy.
- The background/wallpaper feature should be implemented as a shell plugin installed by default, which will exercise the plugin/config/settings architecture early.

## N. Wallpaper/background

- A background wallpaper is a real product feature, not a placeholder.
- Add a dedicated Wallpaper section in Hearth Settings.
- The wallpaper/background implementation should be a shell plugin installed by default.
- Support local/static wallpapers and an online provider model.
- Use Waifu.im as the first online provider with visible/configurable API parameters.
- Ship conservative SFW wallpaper defaults, but do not expose a conspicuous dedicated “NSFW mode” toggle; advanced users may deliberately edit generic valid provider parameters/tags themselves.
- Use the previously discussed U²-NetP-based deterministic artistic auto-crop pipeline. Full details are in `07_WALLPAPER_BACKGROUND_AND_AUTOCROP.md`.
- Design fetching/cropping/caching so future Gaming Mode integration can reuse the core behavior rather than duplicating it inside Decky/QML UI.

## O. Gaming Mode and Steam integration

- Gaming Mode remains a major product focus alongside the shell.
- The owner perceived controller latency in Steam Gaming Mode becoming worse and wants it investigated without assuming Hearth is necessarily the cause.
- Existing shader-compilation responsiveness and low-latency roadmap concerns must remain documented even if their GM slice order changes.
- Hearth Portal and selected Hearth apps should become available in Gaming Mode as proper Steam/Non-Steam entries without separate app copies.
- Hearth Portal should know when changes require Steam or Gaming Mode Steam to restart and should be able to manage that through an appropriate safe mechanism.
- Hearth Portal should remain aligned with Bazzite Portal's action catalog instead of becoming an unmaintainable copy; Hearth may replace/override, add, or remove entries where hearthOS needs differ.
- Hearth Portal may become the game-management surface, potentially replacing Decky-Framegen UI and possibly reducing the need for ProtonPlus; ProtonTricks may still be necessary. Treat those as evaluation items, not already-set retirement decisions.
- Add controller-adjacent Hearth apps to Steam where useful.
- Future `GM-*` work should create a Hearth-owned Decky plugin that brings selected features into Gaming Mode, including the same wallpaper/provider/cropping system and likely MD3E-inspired presentation.

## P. Proposed Steam-like desktop controller feel

The newer prompt proposes making Hearth Desktop controls feel familiar to Steam Gaming Mode where useful:

- Right stick remains pointer/mouse control.
- Guide + vertical right-stick movement was proposed for volume.
- Horizontal Guide + right-stick behavior may be brightness; the owner explicitly asked to verify what Steam actually does rather than assume.
- Shoulder buttons were proposed for mouse clicking instead of triggers.
- LT/RT were proposed for panels/workspaces/category navigation because the new shell initially has fewer surfaces.

These proposals conflict with parts of the current v3 controller manifest. Do not silently choose one; reconcile in the controller-layout planning.

## Q. Documentation and quality

- `starlight-hearth` should continue documenting shell features and controller layout and be updated whenever the shell contract changes.
- Remove/update outdated descriptions such as DMS being the intended Hearth Shell architecture once superseded ADRs are recorded.
- Preserve the current evidence/owner-audit discipline.
- Do not call a slice successful merely because it compiles or the session starts.
- Essential shell affordances must remain visible/reachable.
- Avoid regressions that force `ujust hearth-recovery-kde` merely to inspect a candidate.
- Keep implementation maintainable, testable, and recoverable.
