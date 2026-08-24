# Input and navigation behavior

**State:** Accepted planning contract; not frozen for implementation
**Authority:** Hearth-owned surface interaction shared by controller and keyboard

## Input model

Controller actions are normalized by InputPlumber and resolved by a Hearth
semantic router. Hearth QML surfaces consume actions such as focus, accept,
back, search, context, group navigation, scrolling, and panel commands. They do
not receive fake global Arrow, Enter, Escape, Tab, or function-key events.

Physical keyboard events remain normal Qt keyboard events. Intentional pointer,
wheel, and text-injection paths may use virtual devices where their behavior is
actually pointer, scrolling, or text entry.

## Navigation and Text modes

Every Hearth-owned surface starts in Navigation Mode unless it is restoring an
explicit active text session.

- Arrows, bare `HJKL`, and `WASD` move semantic focus in Navigation Mode.
- Printable characters do not automatically start search.
- `i`, `/`, and `Ctrl+F` invoke the surface's primary search and enter Text
  Mode at its field.
- Enter/Accept on a text field deliberately enters Text Mode.
- Merely auto-focusing a field never enters Text Mode.
- Physical-keyboard entry shows a small Text Mode indicator and does not open
  the OSK.
- Controller or touch text activation opens the OSK when the field supports it.
- Leaving Text Mode restores the owning navigational control rather than an
  invisible internal text cursor.

## Focus invariants

- Opening a surface chooses the best currently enabled target from its content;
  it never hardcodes an application or network control name.
- Search does not steal initial focus.
- Disabled, invisible, and inapplicable controls are skipped.
- Dynamic list/grid changes preserve a sensible target or select the nearest
  valid replacement.
- Back closes the deepest active layer first and returns focus to the opener.
- A focus graph cannot trap controller or keyboard users.
- Pointer use does not erase the last valid navigational target; later
  controller/keyboard use restores a visible focus state.

## Accepted default controls

Mappings are data-driven and contextual. A more specific visible context such
as the OSK overrides the global meaning.

| Physical control | Default semantic behavior outside the OSK |
| --- | --- |
| D-pad | Focus left/right/up/down |
| Left stick | Scroll/paging, not focus emulation |
| Right stick | Pointer motion |
| South face | Accept/activate |
| East face | Back/cancel |
| West face | Surface alternate action; toggles Grid/List in App Menu |
| North face | Open OSK immediately and target the active field or surface primary search |
| RT / LT | App Menu next/previous tab; other contexts remain to be specified |
| RB / LB | Primary/secondary pointer click in Desktop/App Menu contexts |
| Menu/Start | Open App Menu globally; open selected-item actions inside App Menu |
| Guide | Open decision outside Gaming Mode |
| View | Open decision outside OSK |
| L3 / R3 | Open decision outside OSK |

West refers to physical position, not printed letter: Xbox X, PlayStation
Square, and Nintendo Y.

## Accepted keyboard controls

| Action | Keyboard default |
| --- | --- |
| Open App Menu | `Super+A` |
| Move focus | Arrow keys, `HJKL`, or `WASD` |
| Primary search | `i`, `/`, or `Ctrl+F` |
| Next/previous App Menu tab | `Ctrl+Tab` / `Ctrl+Shift+Tab` |
| Grid/List direct selection | `Ctrl+1` / `Ctrl+2` |
| Context/options | Menu key or `Shift+F10` |
| Accept/back | Enter / Escape where not in Text Mode-specific handling |
| Manual OSK fallback | `Super+I` or `F12` |

The old global F10 launcher binding is superseded. Remaining window,
workspace, Bar-focus, media, and recovery shortcuts require conflict review
before acceptance.

## Glyphs and configuration

Hints represent semantic actions through one reusable component. Controller
family changes update Xbox, PlayStation, Nintendo, or generic physical glyphs
without rewriting surface code. Modifier hints may show the modifier first and
reveal dependent controls only while it is active.

The controller manifest and keyboard shortcuts are versioned configuration,
not hardcoded QML policy. Existing v3 service/state-machine work is reusable
evidence, but its trigger-click, bumper-group, north-hold, and other superseded
defaults are not current behavior.

## Third-party applications

Hearth does not promise native semantic focus inside arbitrary applications.
The supported strategy remains native gamepad when available, explicit
application profiles where later justified, right-stick pointer fallback, and
the best-effort OSK path described in `osk.md`. Application capability claims
require candidate-specific evidence.

## Open boundary

Guide, View, L3/R3, global media/window/workspace actions, pointer
acceleration, glyph-family precedence, and remaining keyboard conflicts are
tracked in `docs/open-questions.md`.
