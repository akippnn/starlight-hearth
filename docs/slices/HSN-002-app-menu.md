---
id: "HSN-002"
title: "hearthOS App Menu"
contract_version: 1
contract_state: proposed
owner: "@akippnn"
repositories:
  - "akippnn/starlight-hearth"
  - "akippnn/starlight-hearth-shell"
current_status: "../status.md"
evidence: "../evidence/HSN-002.md"
updated: "2026-08-28"
---

# HSN-002 — hearthOS App Menu

This is a proposed contract and planning anchor. It does not authorize
implementation, publication, deployment, or an acceptance claim. Freeze a
later exact approved revision before HSN-002 implementation begins.

## Owner-visible outcome

From hearthOS Desktop, the owner can open one controller-, keyboard-, and
pointer-native App Menu, search installed applications, browse Favorites,
Recents, By Name, and By Category, switch Grid/List, invoke bounded app actions,
and launch a selected application while preserving deterministic focus and
HSN-001 recovery behavior.

## Authentic path

`approved HSN-002 contract -> clean shell package -> signed hearthOS image -> niri-owned shell -> Rust catalog/config provider -> typed Category1/Catalog operations -> Quickshell CollectionBrowser -> transient application unit`

Mocks, a QML-only catalog, offscreen rendering, schema migration tests, or a
package alone prove only their exercised surfaces. The audit target is the
complete App Menu on an exact signed image.

## Proposed public behavior and interfaces

- `CollectionBrowser` owns search mode, four tabs, Grid/List presentation,
  focus, grouping, virtualization, the right index rail, context presentation,
  and loading/empty/error states.
- Read-only `Category1` exposes typed revision/readiness/diagnostic, item,
  group, and action-description data reusable by future catalogs.
- The app-specific provider adds typed launch, Favorite/Unfavorite,
  Remove Recent, and Edit Favorites operations. QML never supplies commands or
  desktop-entry `Exec` text.
- HSN-001 `Launcher1` remains supported during this successor; any new catalog
  interface is versioned separately and must not reinterpret `Launcher1`.
- Schema v2 uses stable application and shell-item references, migrates v1 per
  layer before merge, preserves unknown keys, and writes v2 atomically on the
  first shell-owned update.
- Reusable controller and keyboard hints describe semantic actions and current
  device family without embedding physical mappings in individual components.

## Proposed behavior

- The top field says `Search Apps`, with a search icon on the left and
  controller plus `/` keyboard hints on the right; the keyboard hint is
  outermost. Search does not steal initial focus.
- Tabs are Favorites, Recents, By Name, and By Category. The active tab replaces
  a redundant content title.
- The icon-only Grid/List segmented selector is on the right and does not
  resemble an on/off switch. Grid/List mode persists across tabs and restarts.
- App-local search matches Name, GenericName, and Keywords. Exact, prefix, and
  name-word matches rank ahead of generic-name/keyword and substring matches.
- Recents contain the 12 most recent unique successful application launches.
  Shell actions never enter Recents; removal is not a blocklist.
- By Name groups by first alphabetic Unicode grapheme, with digits/symbols under
  `#`. By Category follows freedesktop main categories in registry order, lets
  an app appear in each matching category, and supplies Other as fallback.
- The right index rail morphs content into group-overview rows and restores the
  saved Grid/List mode at the chosen group.
- Initial actions are Favorite/Unfavorite, Remove Recent where applicable, and
  Edit Favorites. Uninstall is excluded.
- The temporary placement remains right/center/floating until the hearthOS
  System Bar provides the authentic attachment point.

## Scope exclusions

- First Setup, Screen Scale, keyboard-preset selection, and wallpaper onboarding;
- arbitrary placement, docking, and multi-output placement policy;
- hearthOS System Bar, Control Center, Add Controls & Widgets, and Focus Cursor;
- independent desktop/file/web search beyond the app-local provider;
- OSK implementation, Settings UI, online wallpaper providers, and plugin architecture.

## Failure and recovery

- Catalog failure remains visible and does not fabricate applications.
- Invalid schema-v2 layers fall back as a whole; migration never discards an
  intact v1 layer before a verified v2 write.
- Missing or removed entries disappear with deterministic nearest-focus recovery.
- Failed launch keeps the App Menu open, preserves selection, and shows a
  sanitized diagnostic.
- Shell failure preserves HSN-001 recovery and independently launched applications.

## Proposed non-owner gates

- [ ] Exact contract revision is approved and frozen before implementation.
- [ ] Real provider and deterministic consumer-double tests cover catalog,
      search ranking, groups, recents, actions, diagnostics, and change signals.
- [ ] Schema v1-to-v2 migration, invalid-layer fallback, unknown-key
      preservation, atomic writes, and downgrade/recovery fixtures pass.
- [ ] QML tests cover all tabs, search, right rail, Grid/List, context actions,
      hints, focus recovery, three input families, target sizes, and reduced motion.
- [ ] Clean package/image integration proves canonical/derived contracts and
      retains HSN-001 compatibility and recovery.
- [ ] The exact signed image passes authentic target workflows and produces a
      hashed audit bundle with visible limitations.

## Proposed owner audit

1. Boot the recorded signed image and enter hearthOS Desktop.
2. Open App Menu with controller, keyboard, and pointer.
3. Search and browse all four tabs; use the right index rail and Grid/List.
4. Launch an app and exercise each applicable context action.
5. Exercise an empty/missing entry, launch failure, invalid configuration, and
   shell restart without losing recovery.
6. Record `accepted` or `rejected` for HSN-002 independently of HSN-001.

Owner verdict: `pending`. No candidate exists.
