# Input, Controller, Keyboard, Focus, and Navigation Requirements

## Core model

Hearth should treat the controller as a semantic input device, not as a keyboard macro pad. Preserve/extend the existing direction where physical controller events are normalized by InputPlumber, discrete actions enter a Hearth-owned semantic routing layer, and QML surfaces consume semantic actions through contexts/focus graphs. Physical keyboard input remains ordinary keyboard input; it must not be swallowed just because controller support exists.

Right-stick pointer and other deliberate pointer-like outputs can remain virtual pointer behavior where appropriate. The important distinction is that semantic UI actions such as accept/back/search/category/context/overview should not leak through the desktop as fake global `Enter`, `Escape`, arrow keys, function keys, etc.

Codex should inspect the existing Rust service, D-Bus contract, InputPlumber profiles, glyph manifest, and QML focus/context helpers before replacing or extending them. They may be among the most reusable results of the DMS-era work.

## Focus behavior

Every Hearth-native interactive surface should define predictable focus behavior:

- Opening a panel/menu should establish a useful first focus target based on current content and enabled state, not a hardcoded app/control name.
- Returning/closing should restore focus sensibly.
- Search fields should not automatically steal controller focus just because a panel opened.
- A dedicated semantic search action should focus the search field.
- When a Hearth-controlled text field gains focus in controller mode, the compact OSK may open.
- Focus must remain visible and expressive.
- Disabled/inapplicable controls should be skipped.
- Focus graphs should not trap the user.
- Dynamic lists/grids should remain navigable as content changes.
- Mouse use should not corrupt controller focus state; controller use should not disable keyboard focus/navigation.

For Settings and similarly dense Hearth apps, consider visually de-emphasizing/graying unrelated regions while controller focus is in a specific region if it improves predictability, but treat exact visual behavior as a design decision to test rather than a blanket rule.

## Semantic action vocabulary

Do not bind every component directly to physical buttons. Maintain/derive a semantic vocabulary that can represent at least:

- focus left/right/up/down
- accept/activate
- back/cancel
- search/focus search
- contextual/alternate action
- options/context menu
- previous/next group/category/tab
- focus Hearth Bar
- open App Menu
- open quick/guide menu
- previous/next window
- previous/next workspace
- overview
- scroll/paging
- pointer primary/secondary click
- window actions such as close/fullscreen/move where supported
- modifier layers/chords

The existing v3 manifest already expresses many of these. Evolve rather than bypass the semantic model.

## Glyphs and controller families

Support visible glyph families for:

- Xbox-style ABXY
- PlayStation Cross/Circle/Square/Triangle and corresponding shoulder/menu symbols
- Nintendo physical face-button labeling/order
- Generic fallback

The controller settings visual should label physical positions correctly. Avoid assuming that “A” always means the south physical button across families.

Controller hints should be reusable components and should react to configured mappings. Do not draw text like `A`, `RB`, `Y` manually in every surface.

For modifier actions, support a hint mode where the modifier can be shown first and dependent actions appear when the modifier is active. This is particularly useful for bar/workspace/window hints.

## Proposed mappings and mappings that require reconciliation

### Existing v3 baseline in the supplied repo

The current manifest includes, among other things:

- D-pad → semantic focus directions.
- South face → accept.
- East face → back.
- West/north face → alternate/search-context actions with modifier window controls.
- Bumpers → previous/next groups plus modifier window/workspace actions.
- Triggers → pointer clicks plus modifier move-window actions.
- Menu → App Menu.
- View → focus bar.
- Guide → quick menu on Desktop / Steam-owned in Gaming Mode.
- L3/R3 click → modifier layers.
- Right stick → pointer.
- Left stick → scroll.

### Newer owner proposal

The owner later proposed a more Steam-like Desktop feel:

- right stick pointer remains;
- shoulder buttons become mouse clicks;
- LT/RT become panel/workspace/category navigation;
- Guide + vertical right stick controls volume;
- possible Guide + horizontal right stick brightness, **to be verified against Steam rather than assumed**.

The owner also previously wanted stick-modifier window controls and page scrolling. These ideas can coexist only if modes/chords are designed deliberately. Do not “resolve” this by preserving whichever mapping happens to be implemented today. Model the conflict and propose a coherent configurable default during roadmap/controller-layout planning.

## Launcher/app-menu interaction requirements

Controller:

- D-pad and/or left stick for grid/list movement.
- Semantic previous/next category actions (earlier LB/RB; later LT/RT proposed).
- Dedicated search-focus action.
- Context/options action.
- Accept/back.
- Layout/mode action where the UI exposes list/grid/etc.

Keyboard equivalents should support conventional arrows plus configurable keyboard-first alternatives such as WASD/Vim-style keys. The owner's examples include `hjkl`, `q/e`, shifted variants, `Ctrl+F`, context shortcuts, `Meta+Tab`, and `Meta+\``. Treat them as desired defaults/candidates, not reasons to bake keycodes into every QML file.

## OSK

- Compact, bottom-positioned.
- Must not replace/close the initiating shell surface.
- Triggered by focused Hearth text input in controller mode rather than by the search button itself.
- Physical keyboard continues to type normally.
- Controller navigation of the OSK should be semantic and predictable.
- Do not accidentally reintroduce global controller-to-keyboard leakage to implement the OSK.

## External applications

The owner wants the system to feel coherent even when arbitrary desktop apps are imperfect with a controller, but Hearth cannot guarantee native focus graphs inside every third-party GUI.

The current docs propose a hybrid model for external apps: native gamepad where supported, application profiles/custom bindings where needed, and pointer fallback. Keep that concept available for planning. Do not expand this shell rewrite into a universal compositor-wide accessibility/input-method project unless a later ADR justifies it.

## Latency

Controller latency matters as a product property, particularly in Gaming Mode and during session handoff. Preserve existing latency/evidence gates where useful. If latency appears worse, first isolate whether the cause is Steam, Gamescope, InputPlumber, Hearth routing, compositor/session transition, wireless mode, or something else before applying a Hearth workaround.
