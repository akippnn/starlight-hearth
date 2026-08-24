# Open Questions and Conflicts — Deliberately Not Decided Here

This file exists specifically so Codex does not waste tokens rediscovering ambiguities, while also preventing this handoff from pretending they are already decided.

## 1. Exact controller default layout

There are at least three layers of requirements:

- existing `controller-layout-v3.json` implementation;
- earlier DMS-era ideas (LB/RB categories, trigger clicks, L3/R3 modifiers, stick scrolling, etc.);
- newer Steam-like ideas (shoulder clicks, LT/RT navigation, Guide+right-stick volume/possibly brightness).

Codex should inspect actual current Steam Gaming Mode behavior, InputPlumber constraints, controller hardware, and the semantic routing architecture. Propose a coherent configurable default and document migration from v3. Do not assume the implemented v3 mapping wins merely because it exists.

## 2. L3/R3 modifier semantics vs stick-axis actions

The owner has discussed stick-click modifiers and stick-axis pointer/scroll/media actions. Clarify how modifier modes interact with pointer motion, volume/brightness, scroll, window/workspace actions, and accidental activation.

## 3. Control center / notifications placement

Earlier DMS direction wanted a merged control-center+notification widget on the far right. Newer Hearth Bar direction places App Menu/workspace controls on the right and tray/control center on the left. Preserve the desired merged/coherent behavior, but plan final placement from the new Hearth Bar information architecture.

## 4. Hearth Bar initial focus edge

Earlier preference was right-most because that was where the merged quick controls lived. Newer layout changes what is on each edge. Keep initial focus configurable; decide a sensible default only after the bar layout is planned.

## 5. Exact keyboard defaults

The owner has proposed several overlapping options: arrows, WASD, `hjkl`, `q/e`, shifted Vim/arrow variants, `Ctrl+F`, backtick-like search, `Ctrl+I`/`Shift+I`, `Meta+F3`, `Meta+Tab`, and `Meta+\``. Build configurable semantic actions and choose defaults deliberately rather than enabling conflicting shortcuts ad hoc.

## 6. Config format and schema

A coherent versioned config is required, but JSON/TOML/KDL/etc. and ownership boundaries are not decided here. Consider QML ergonomics, schema validation, comments, hot reload, migration, atomic writes, system defaults vs user overrides, plugin settings, and immutable-image concerns.

## 7. Native backend/service architecture

Quickshell/QML is settled for UI, but this handoff does not decree that every backend must be Rust, Go, C++, Python, or QML. Existing Rust controller service is likely valuable. Evaluate language/runtime choices per boundary and avoid rewriting proven code for aesthetic consistency alone.

## 8. Caelestia adoption level

Caelestia is the strongest visual/motion reference, but upstream is Hyprland-centric and GPL-3.0. Possible strategies range from inspiration-only, to selective independent reimplementation, to selective license-compatible reuse, to deeper porting. Do not decide from screenshots alone. Audit dependencies, compositor coupling, and licensing.

## 9. DMS reuse level

The DMS downstream-product strategy is ended, but DMS remains a mature niri/system-integration source and MIT-licensed upstream. Decide which integrations/components are worth extracting/adapting versus replacing with simpler Hearth-native services.

## 10. M3Shapes dependency

Likely attractive for MD3E shape morphing, but evaluate packaging, performance, maintenance, ABI, and wrapper/design-token needs before declaring it foundational.

## 11. Plugin sandbox/security model

“Secure but powerful” is a requirement, not an implementation. Decide what trust levels exist for built-in/system plugins vs user plugins, what APIs they receive, how updates/config/state work, and how a broken plugin is prevented from taking down the shell.

## 12. Wallpaper rotation UX

Not fully specified:

- interval vs event-driven rotation;
- manual Next/Previous;
- history/avoid repeats;
- favorites;
- local + online mixing;
- cache size/retention;
- per-monitor wallpaper vs shared wallpaper;
- offline behavior;
- artist/source attribution UI.

Document these as future/optional requirements rather than guessing all of them into V1.

## 13. Wallpaper minimum resolution / upscaling policy

The owner uses high-resolution displays and wants wallpapers, but requiring native 4K would drastically shrink the source pool. Starting discussion used >=1920x1080 or >=2560x1440. Decide defaults based on real Waifu.im result counts, crop requirements, and final renderer/upscaling quality.

## 14. Auto-crop scoring constants

The desired criteria are known, but exact numeric weights/search granularity/tie-breaking should be designed and tested on representative anime art, photography/local wallpapers, portraits, off-center subjects, and multiple aspect ratios. Do not turn brainstorming weights into unexplained magic constants.

## 15. Secondary anime detector

U²-NetP saliency is the intended first model. A second anime face/character/orientation detector is optional only if testing demonstrates a concrete failure mode. Avoid model creep.

## 16. Hearth Portal exact relationship to Bazzite Portal

The direction is maintainable alignment + Hearth overrides, but inspect Bazzite Portal's current catalog/interface and existing Hearth plans before choosing adapter format, ownership, privilege boundaries, and update strategy.

## 17. Gaming Mode roadmap order / IDs

Current docs place shader/latency first. New owner direction wants Hearth Portal/apps and future Hearth Decky work elevated. Preserve all concerns and let dependency/value planning determine final GM order; do not delete the old concerns simply because numbering changes.

## 18. Steam notification integration

The owner observed Steam notifications not behaving like expected desktop notifications. Investigate whether this is Steam/Game Mode/XDG notification behavior, window routing, current DMS/niri integration, or a non-fixable upstream choice before defining a Hearth feature.

## 19. How much “desktop” to build now

Hearth Desktop must be locally usable, but it is still primarily a gaming OS. Avoid both extremes: an unusably thin configuration shell and an endless attempt to recreate KDE/GNOME before gaming/Hearth-specific value exists. Vertical-slice planning should define the minimum coherent desktop capability per stage.

## 20. Owner questions that should still be asked when genuinely necessary

The original prompt explicitly invited questions about controller layout/default actions and missing controller interactions. Do not avoid those forever; just do not ask questions whose answers are already in the repository/handoff or questions that can be answered by implementation research/testing. Escalate genuine product choices to the owner when the roadmap reaches them.
