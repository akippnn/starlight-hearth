# Planning behavior contracts

These documents preserve accepted owner-visible behavior before any future
vertical slice is defined. They are **not frozen slice contracts** and do not
authorize implementation, deployment, audit-readiness, or acceptance.

Each contract separates accepted behavior from open decisions. When a future
slice depends on one, the relevant subset must be reviewed and frozen at an
exact revision in `docs/slices/`; implementation evidence then belongs in
`docs/evidence/`.

- `input-navigation.md` — shared semantic input, modes, focus, keyboard, and glyphs
- `app-menu.md` — App Menu presentation, grouping, focus, recents, and actions
- `hearth-bar.md` — visibility, panel ownership, focus return, and overlay behavior
- `osk.md` — wvkbd-derived text-entry architecture and interaction
- `file-manager-contingency.md` — dormant Dolphin/Nautilus/Index decision gate
