# Open decision register

**Authority:** unresolved product and implementation choices
**Last reconciled:** 2026-08-25

These questions are deliberately not delegated to a future implementer. They
remain open until research resolves a discoverable fact or the owner explicitly
accepts a product tradeoff. None blocks the current documentation phase.

## Shell, repository, and configuration

| ID | Decision still needed |
| --- | --- |
| `OQ-001` | Exact private archive repository name, shell-history reset procedure, and cutover revision. |
| `OQ-002` | Public D-Bus/API successor strategy for `org.starlight.HearthShell.Controller1`. |
| `OQ-003` | Exact JSON schema/version format, unknown-key behavior, atomic writes, migration rollback, validation UX, and hot-reload semantics. |
| `OQ-004` | Exact Clavis, Caelestia, DMS, M3Shapes, and other per-file imports after packaging/performance/license audits. |
| `OQ-005` | Whether and how M3Shapes becomes a packaged foundational dependency and which Hearth wrapper API contains it. |

## Controller and global navigation

| ID | Decision still needed |
| --- | --- |
| `OQ-010` | Global Guide behavior and Guide+right-stick volume/possible brightness semantics after current Steam/Bazzite verification. |
| `OQ-011` | View behavior outside the OSK, including Hearth Bar focus and initial focus target. |
| `OQ-012` | L3/R3 modifiers, window close/fullscreen, window/workspace navigation, and interactions with stick-axis actions. |
| `OQ-013` | Right-stick pointer acceleration, dead zones, speed tiers, and click/drag behavior. |
| `OQ-014` | Controller-family detection and override precedence for Xbox, PlayStation, Nintendo, and generic glyphs. |
| `OQ-015` | Remaining global keyboard defaults and conflict policy for workspace/window switching, Bar focus, context actions, and recovery shortcuts. |

## App Menu and Hearth Bar

| ID | Decision still needed |
| --- | --- |
| `OQ-020` | Whether App Menu always opens Favorites, remembers the last tab, or uses another explicit policy. |
| `OQ-021` | Search scope, searchable fields, ranking, empty query behavior, and focus restoration after leaving search. |
| `OQ-022` | Grid density, responsive breakpoints, row/column wrapping, List/Grid card content, and empty group treatment. |
| `OQ-023` | Launch failure presentation and handling of `Hidden`, `NoDisplay`, `TryExec`, duplicate desktop IDs, and terminal applications. |
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
| `OQ-050` | Wallpaper rotation, manual navigation, history/repeat avoidance, favorites, cache retention, source attribution, and local/online mixing. |
| `OQ-051` | Shared versus per-monitor wallpaper, minimum source resolution/upscaling, crop search granularity, score weights, and tie-break order. |
| `OQ-052` | Whether representative testing proves a need for a secondary anime face/orientation detector after U²-NetP. |
| `OQ-053` | Hearth Portal's exact adapter/override format, Bazzite catalog pinning/update policy, privilege boundary, and restart contract. |
| `OQ-054` | Portal's eventual game-management scope and whether Decky-Framegen UI or ProtonPlus can be retired; ProtonTricks is not presumed replaceable. |
| `OQ-055` | Gaming Mode roadmap order, new collision-free IDs, latency/shader investigation order, and timing of Hearth apps and the Hearth Decky plugin. |

## Delivery planning

| ID | Decision still needed |
| --- | --- |
| `OQ-060` | Exact identity, owner-visible outcome, contract, and acceptance gates of the first new Hearth-native shell slice. |
| `OQ-061` | Future track/ID registry after the historical VS/HS aliases and conflicting GM-001 records. |
| `OQ-062` | Which behavior contracts become frozen together versus remain separate dependencies. |
