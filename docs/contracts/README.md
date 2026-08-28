# Planning behavior contracts

These documents preserve accepted owner-visible behavior before any future
vertical slice is defined. They are **not frozen slice contracts** and do not
authorize implementation, deployment, audit-readiness, or acceptance.

Each contract separates accepted behavior from open decisions. When a future
slice depends on one, the relevant subset must be reviewed and frozen at an
exact revision in `docs/slices/`; implementation evidence then belongs in
`docs/evidence/`.

- `input-navigation.md` — authoritative shared semantic input, modes, focus, keyboard, contextual precedence, and reusable hints
- `app-menu.md` — proposed HSN-002 App Menu presentation, grouping, search, recents, and actions
- `system-bar.md` — hearthOS System Bar visibility, panel ownership, focus return, and overlay behavior
- `osk.md` — wvkbd-derived text-entry architecture and interaction
- `file-manager-contingency.md` — dormant Dolphin/Nautilus/Index decision gate

The decision-complete proposed slice contracts for the headless hold/chord
layer, App Menu, and visible latched niri mode live under `docs/slices/` as
HIN-001, HSN-002, and HIN-002. Their common primitives are shared contracts;
their owner-visible outcomes and acceptance records remain independent.
