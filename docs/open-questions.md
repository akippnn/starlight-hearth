# Open decision register

**Authority:** unresolved product and implementation choices
**Last reconciled:** 2026-08-28

These questions are deliberately not delegated to a future implementer. They
remain open until research resolves a discoverable fact or the owner explicitly
accepts a product tradeoff. HSN-001 resolved only the rows listed below; other
questions remain outside that slice.

## Resolved for HSN-001

| ID | Resolution |
| --- | --- |
| `OQ-001` | Private archive `starlight-hearth-shell-dms-archive`; verified mirror/bundle; clean orphan `codex/hsn-001-launcher-nucleus`; public cutover only after owner acceptance. |
| `OQ-002` | New typed `Input1`, `Launcher1`, and `Config1` contracts on `org.starlight.HearthShell`; no `Controller1` compatibility import. |
| `OQ-003` | JSON schema v1, recursive object merge/array replace, unknown-key preservation with warnings, whole-layer rejection for invalid known values, atomic writes, and hot reload. |
| `OQ-005` | Use Caelestia-pinned M3Shapes `bdc327b…` behind Hearth card wrappers with Apache-2.0 notices. |
| `OQ-020` | HSN-001 has Favorites only and opens the first available favorite; later tab policy remains out of scope. |
| `OQ-022` | HSN-001 requires responsive Grid/List at 1280x720 and logical 1920x1080; unavailable favorites hide and focus reflows. Later catalog density/wrapping policy remains open. |
| `OQ-023` | Validate desktop IDs, hide missing entries, retain focus/drawer and show inline diagnostics on launch failure. Broader catalog policy remains open. |
| `OQ-060` | `HSN-001` — hearthOS Launcher Nucleus, frozen in its slice contract. |
| `OQ-061` | `HSN` prefix registers new hearthOS-native shell outcomes without colliding with historical VS/HS/GM IDs. |
| `OQ-062` | HSN-001 freezes only launcher-nucleus input, config, launch, visual, package, image, and recovery behavior; tabs/search/OSK/Bar and adjacent contracts remain separate. |
| `OQ-063` | HSN-001 v2 sets RB to primary/left click, LB to secondary/right click, and niri as exclusive companion/UI lifecycle owner. |

## Defined by the proposed HSN-002 contract

These choices are stable planning inputs but do not freeze or authorize
HSN-002: `Search Apps` covers Name, GenericName, and Keywords with explicit
ranking; tabs are Favorites, Recents, By Name, and By Category; the index rail
and icon-only Grid/List selector are on the right; recents retain 12 unique
successful launches; categories use freedesktop main categories with Other.

## Shell, repository, and configuration

| ID | Decision still needed |
| --- | --- |
| `OQ-004` | Exact Clavis, Caelestia, DMS, M3Shapes, and other per-file imports after packaging/performance/license audits. |

## Controller and global navigation

| ID | Decision still needed |
| --- | --- |
| `OQ-010` | Global Guide behavior and Guide+right-stick volume/possible brightness semantics after current Steam/Bazzite verification. |
| `OQ-011` | View behavior outside the OSK, including hearthOS System Bar focus and initial focus target. |
| `OQ-013` | Right-stick pointer acceleration, dead zones, speed tiers, and click/drag behavior. |
| `OQ-014` | Controller-family detection and override precedence for Xbox, PlayStation, Nintendo, and generic glyphs. |
| `OQ-015` | Remaining global keyboard defaults and conflict policy for workspace/window switching, Bar focus, context actions, and recovery shortcuts. |

## App Menu and hearthOS System Bar

| ID | Decision still needed |
| --- | --- |
| `OQ-021` | HSN-002 empty-query behavior, focus restoration after leaving search, and whether the default/last tab is remembered. |
| `OQ-024` | Per-output App Menu placement, remembered state, and behavior when focus/output changes. |
| `OQ-025` | Clear All Recents, category-editing workflow, and whether later manual application additions remain `.desktop` based. |
| `OQ-026` | Final Bar left/center/right layout, merged control-center/notification placement, initial focus item, and multi-output visibility. |
| `OQ-027` | Bar edit mode, drag/drop details, widget persistence, and keyboard/controller equivalents. |

## OSK and external applications

| ID | Decision still needed |
| --- | --- |
| `OQ-030` | Private companion↔OSK protocol, failure/restart policy, diagnostics fields, and version negotiation. |
| `OQ-031` | Physical-keyboard input-method grab implementation and verification while the OSK is visibly open. |
| `OQ-032` | Exact unsupported/XWayland manual targeting UX without implying universal compatibility. |
| `OQ-033` | XKB invalid-layout recovery flow, language ordering, and owner-visible diagnostics presentation. |

## Shell surfaces, Settings, and plugins

| ID | Decision still needed |
| --- | --- |
| `OQ-040` | Workspace/window switcher workflow, default shortcuts, controller semantics, and multi-output behavior. |
| `OQ-041` | Initial control-center controls, grid-density meaning/default, controller slider mechanics, and notification history behavior. |
| `OQ-042` | Steam notification behavior and whether it is fixable in Hearth, niri, Steam, or not at all. |
| `OQ-043` | Settings information architecture beyond the accepted initial areas and how Gaming Mode-only system settings are linked. |
| `OQ-044` | Built-in versus user plugin trust, render/service capabilities, sandboxing, updates, failure containment, and immutable-image installation. |

## Wallpaper, Portal, and Gaming Mode

| ID | Decision still needed |
| --- | --- |
| `OQ-050` | Later online-provider selection, rotation, history/repeat avoidance, favorites, cache retention, source attribution, and local/online mixing after HWP-001. |
| `OQ-051` | Later palette extraction and advanced saliency/subject-aware crop policy; HWP-001 uses deterministic center crop and per-output rendering. |
| `OQ-052` | Whether a later provider/cropping outcome needs model-based detectors or a broader wallpaper plugin architecture. |
| `OQ-053` | hearthOS Portal's exact adapter/override format, Bazzite catalog pinning/update policy, privilege boundary, and restart contract. |
| `OQ-054` | Portal's eventual game-management scope and whether Decky-Framegen UI or ProtonPlus can be retired; ProtonTricks is not presumed replaceable. |
| `OQ-055` | Gaming Mode roadmap order, new collision-free IDs, latency/shader investigation order, and timing of Hearth apps and the Hearth Decky plugin. |
