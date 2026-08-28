# App Menu behavior

**State:** Decision-complete proposed HSN-002 v1; not frozen or authorized for implementation
**Surface:** Temporary right/center/floating placement until the hearthOS System Bar exists

## Presentation

- Open from controller Menu/Start or keyboard `Super+A`.
- Render as a right-side drawer at approximately 38% of logical output width,
  clamped near 520–760 logical pixels with safe margins.
- Use near-full width only where a narrow output cannot satisfy the clamp.
- Dim and subtly blur the desktop while keeping any hearthOS System Bar opener
  active and visually connected.
- Close from the scrim, Back, the opening control, or successful launch
  according to the later launch-failure policy.

## Modes and tabs

Exactly two presentation modes exist:

- Grid
- List

The selected mode is global across tabs and persisted between sessions. West
face toggles the two modes. `Ctrl+1` directly selects Grid and `Ctrl+2`
directly selects List.

Every opening starts on Favorites with an empty query. Place `Search Apps`
above the tabs. Initial tabs, in order:

1. Favorites
2. Recents
3. By Name
4. By Category

While L3 is held in App Menu, RB moves to the next tab and LB to the previous;
the modifier context suppresses their base pointer clicks. Keyboard
equivalents are `Ctrl+Tab` and `Ctrl+Shift+Tab`. RT/LT are not tab controls.

## Grouping and index rail

By Name groups applications under letter headings. By Category uses
freedesktop Main Categories. An application may appear in every matching main
category; applications without a match appear under Other.

A separate right vertical index rail lists the current letters or categories.
Moving right into the rail morphs the content into overview rows. Each row
shows its label and up to two stacked app-card previews. Moving left at a
selected group restores the persisted Grid/List presentation positioned at
that group.

Empty groups are not invented. The icon-only Grid/List selector is on the
right. The active tab does not repeat a redundant content title.

The reusable `CollectionBrowser` consumes a read-only `Category1` provider.
App Menu supplies that provider, while future catalogs may reuse the same
component without acquiring App Menu-specific policy.

## Focus and navigation

- Opening chooses the first favorite; if none exists, it chooses the first
  alphabetically visible application.
- Search never receives initial focus automatically.
- Entering search records the current tab, selection, and scroll position;
  clearing the query exits search and restores all three.
- Tab, query, selection, and scroll state are transient across closes.
- Until the OSK outcome, controller can enter/exit search and navigate results,
  but composing query text requires a physical keyboard and is labeled as such.
- D-pad and left stick move card/list/tab/index focus. Both emit immediately,
  repeat after 260 ms at 90 ms, and accelerate to 55 ms after one second. Left
  stick engages at 0.55, releases at 0.35, and locks to the strongest axis
  until recentered so diagonal jitter cannot alternate focus.
- Right stick remains pointer motion.
- South accepts, East backs out, and Menu/Start opens the selected app's
  actions.
- Menu key and `Shift+F10` are keyboard context equivalents.
- Pointer use and mode/tab changes preserve a valid deterministic focus target.
- The bottom `InputHintBar` is a shared shell primitive driven by semantic
  action/modifier/capability state. App Menu does not maintain a private glyph
  or modifier-hint implementation.

## Bounded Blob transition

HSN-002 may adapt the exact Caelestia Blob files and revision named by its
slice contract only for the contained transition between ordinary content and
right-index overview. It never replaces the canonical selection surface,
changes pixels outside the App Menu containment boundary, or runs continuously.
Reduced motion disables deformation. Source, package, license, allocation,
memory, frame-time, and containment claims require candidate-specific proof.

## Favorites and recents

Default core favorites are:

1. Return to Gaming Mode
2. Steam
3. Firefox
4. Dolphin
5. Ghostty

Favorites are user configuration. Initial typed context actions are Favorite,
Unfavorite, and Remove from Recents. QML never supplies arbitrary commands.
Favorite reorder/edit mode is outside HSN-002.

Recents record successful app launches made through App Menu only. They are unique
MRU entries ordered newest first and capped at 12. Removing an entry is not a
blocklist; a later successful launch may add it again.

## Catalog and launch boundary

Use freedesktop desktop-entry data. `Search Apps` matches Name, GenericName,
and Keywords. Rank exact name, then name prefix, then name-word matches, then
GenericName/Keywords, then remaining substrings, with stable alphabetical
tie-breaking. Manual
`.desktop` entries are acceptable for the initial catalog. The Rust companion resolves typed desktop IDs and
launches applications in separate transient user-systemd units/scopes.

HSN-002 migrates configuration to schema v2 while preserving schema-v1 input
compatibility and the existing D-Bus boundary. Exact additive `Category1` and
`AppCatalog1` wire shapes are owned by the proposed slice contract.
Category reassignment, drag/drop
management, Clear All Recents, desktop-entry edge cases, launch failure
details, and multi-output persistence remain open in `docs/open-questions.md`.

First Setup, wallpaper, arbitrary placement/docking, the hearthOS System Bar,
and broad independent search are excluded from HSN-002.
