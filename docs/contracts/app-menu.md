# App Menu behavior

**State:** Accepted planning contract; not frozen for implementation
**Surface:** Hearth Bar-owned right drawer

## Presentation

- Open from controller Menu/Start or keyboard `Super+A`.
- Render as a right-side drawer at approximately 38% of logical output width,
  clamped near 520–760 logical pixels with safe margins.
- Use near-full width only where a narrow output cannot satisfy the clamp.
- Dim and subtly blur the desktop while keeping the Hearth Bar and opening item
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

Initial tabs, in order:

1. Favorites
2. Recent
3. By Name
4. By Category

RT moves to the next tab and LT to the previous. Keyboard equivalents are
`Ctrl+Tab` and `Ctrl+Shift+Tab`.

## Grouping and index rail

By Name groups applications under letter headings. By Category uses
freedesktop Main Categories. An application may appear in every matching main
category; applications without a match appear under Other.

A separate left vertical index rail lists the current letters or categories.
Moving left into the rail morphs the content into overview rows. Each row shows
its label and up to two stacked app-card previews. Moving right at a selected
group restores the persisted Grid/List presentation positioned at that group.

Empty groups are not invented. Exact treatment of a group becoming empty while
focused remains open.

## Focus and navigation

- Opening chooses the first favorite; if none exists, it chooses the first
  alphabetically visible application.
- Search never receives initial focus automatically.
- D-pad moves card/list/index focus.
- Left stick scrolls; it does not duplicate D-pad focus.
- Right stick remains pointer motion.
- South accepts, East backs out, and Menu/Start opens the selected app's
  actions.
- Menu key and `Shift+F10` are keyboard context equivalents.
- Pointer use and mode/tab changes preserve a valid deterministic focus target.

## Favorites and recents

Default core favorites are:

1. Return to Gaming Mode
2. Steam
3. Firefox
4. Dolphin
5. Ghostty

Favorites are user configuration. Initial context actions are
Favorite/Unfavorite and Remove from Recent.

Recents record successful launches made through App Menu only. They are unique
MRU entries ordered newest first and capped at 12. Removing an entry is not a
blocklist; a later successful launch may add it again.

## Catalog and launch boundary

Use freedesktop desktop-entry data. Manual `.desktop` entries are acceptable
for the initial catalog. The Rust companion resolves typed desktop IDs and
launches applications in separate transient user-systemd units/scopes.

Category reassignment, drag/drop management, Clear All Recents, exact search,
desktop-entry edge cases, launch failure behavior, and multi-output persistence
remain open in `docs/open-questions.md`.
