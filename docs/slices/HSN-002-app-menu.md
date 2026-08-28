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
updated: "2026-08-29"
---

# HSN-002 — hearthOS App Menu

This is a proposed contract and planning anchor. It does not authorize
implementation, publication, deployment, or an acceptance claim. Freeze a
later exact approved revision before HSN-002 implementation begins.

The owner confirmed the interaction choices below during planning, then chose
to keep the complete contract proposed. Its interface names, wire shapes, and
schema therefore remain review material until an explicit freeze decision.

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

## Proposed public behavior and ownership

- `CollectionBrowser` owns search mode, four tabs, Grid/List presentation,
  focus, grouping, virtualization, the right index rail, context presentation,
  and loading/empty/error states.
- Read-only `org.starlight.HearthShell.Category1` is additive at `/Catalog` and
  exposes typed revision/readiness/diagnostic, item, group, and
  action-description data reusable by future catalogs.
- `org.starlight.HearthShell.AppCatalog1` is additive on the same object and
  owns typed activation, Favorite/Unfavorite, and Remove from Recents
  operations. No edit/reorder mode is in HSN-002. QML never supplies commands
  or desktop-entry `Exec` text.
- HSN-001 `Launcher1` remains supported during this successor; any new catalog
  interface is versioned separately and must not reinterpret `Launcher1` or
  `Config1`.
- Schema v2 uses stable application and shell-item references, migrates v1 per
  layer before merge, preserves unknown keys, and writes v2 atomically on the
  first shell-owned update.
- Reusable controller and keyboard hints describe semantic actions and current
  device family without embedding physical mappings in individual components.

| Responsibility | Canonical owner | Contract | Independent proof |
| --- | --- | --- | --- |
| Desktop-entry discovery, metadata, groups, recents, mutations, and launch | Rust companion | `Category1` / `AppCatalog1` | Rust fixtures plus real user-bus tests |
| Search, tabs, focus, index rail, Grid/List, and action presentation | Quickshell `CollectionBrowser` | Read-only snapshot and typed operations | Deterministic provider double plus QML tests |
| Layer migration and persistent user state | Rust companion | JSON schema v2 | Per-layer migration and atomic-write fixtures |
| Existing launcher compatibility | Rust companion and native QML bridge | `Launcher1`, `Config1`, schema-v1 input | Compatibility and restart tests |

### Proposed D-Bus wire contract

`Category1` exposes:

- read-only properties `Ready:b`, `Revision:t`, and `Diagnostic:s`;
- `GetSnapshot`, returning items `a(sssssasasas)`, groups `a(ssa(ss))`, and
  action descriptions `a(sss)`;
- `Changed(t revision)` after an atomic snapshot replacement.

Each item tuple is `(kind, id, name, genericName, icon, keywords, categories,
actionIds)`. Each group is `(id, label, ordered (kind,id) item references)`.
Each action description is `(id, label, icon)`. Group IDs are namespaced as
`favorites`, `recents`, `name:<key>`, or `category:<main-category>`.

`AppCatalog1` exposes `Activate(s kind, s id)`,
`SetFavorite(s kind, s id, b favorite)`, and
`RemoveRecent(s desktopId)`. Its
`OperationResult(s operation, s kind, s id, b success, s diagnostic)` signal
uses operation IDs `activate`, `set-favorite`, and `remove-recent`.
Diagnostics strip control characters and are capped at 512 UTF-8 bytes. If a
refresh fails, `Ready` becomes false, `Diagnostic` is visible, and the last
good snapshot remains available without fabricating entries.

### Proposed JSON schema v2

Schema v2 retains `appearance.motion` and `launcher.viewMode`. It represents
favorites as ordered stable references containing required `kind` and `id`
strings, and stores `launcher.recents` as ordered desktop IDs. Names and icons
come from the catalog, not configuration.

Each packaged, policy, and user layer is migrated independently before merge.
A missing version or version 1 is treated as v1; version 2 is validated
directly; other versions reject the whole layer visibly. Migration changes the
version to 2, retains `kind`/`id`, preserves unknown keys (including historical
name/icon fields), and then applies recursive object merge with array replace.
The first shell-owned mutation serializes and validates a temporary v2 file,
syncs it, and atomically replaces the user layer only after success. A failed
write leaves the intact v1 file in place.

## Proposed behavior

- The top field says `Search Apps`, with a search icon on the left and
  controller plus `/` keyboard hints on the right; the keyboard hint is
  outermost. Search does not steal initial focus.
- Every open starts on Favorites with an empty query and the first available
  favorite selected; if none exists, use the first alphabetical application.
- Entering search records the current tab, selection, and scroll position.
  Clearing the query exits search and restores that context. Tab, query,
  selection, and scroll state are transient; Grid/List remains persistent.
- Before the OSK outcome, a controller may enter/exit search and navigate
  results, but composing query text requires a physical keyboard. The UI must
  expose that limitation instead of implying controller-only text entry.
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
- Initial actions are Favorite/Unfavorite and Remove Recent where applicable.
  Favorite reorder/edit mode and Uninstall are excluded.
- The temporary placement remains right/center/floating until the hearthOS
  System Bar provides the authentic attachment point.

## Scope exclusions

- First Setup, Screen Scale, keyboard-preset selection, and wallpaper onboarding;
- arbitrary placement, docking, and multi-output placement policy;
- hearthOS System Bar, Control Center, Add Controls & Widgets, and Focus Cursor;
- independent desktop/file/web search beyond the app-local provider;
- OSK implementation, Settings UI, online wallpaper providers, and plugin architecture;
- Favorite reorder/edit mode and controller-only query composition before OSK.

## Failure and recovery

- Catalog failure remains visible and does not fabricate applications.
- Invalid schema-v2 layers fall back as a whole; migration never discards an
  intact v1 layer before a verified v2 write.
- Missing or removed entries disappear with deterministic nearest-focus recovery.
- Successful application activation moves its desktop ID to the front of
  recents, removes any prior occurrence, and truncates the list to 12. Shell
  actions and failed launches never enter recents.
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
3. Search with a physical keyboard, clear it to restore the prior context, and
   browse all four tabs with controller, keyboard, and pointer; use the right
   index rail and Grid/List.
4. Launch an app and exercise each applicable context action.
5. Exercise an empty/missing entry, launch failure, invalid configuration, and
   shell restart without losing recovery.
6. Record `accepted` or `rejected` for HSN-002 independently of HSN-001.

Owner verdict: `pending`. No candidate exists.

## Contract approval

Interaction decisions were confirmed by @akippnn during planning on
2026-08-28. On 2026-08-29 the owner directed that this technically complete
draft remain `proposed`; contract freeze and implementation authorization are
still pending and must be separate explicit decisions.
