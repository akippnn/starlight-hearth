# Input and navigation behavior

**State:** Accepted planning contract; not frozen for implementation
**Authority:** Canonical hearthOS surface interaction shared by controller and keyboard

## Input model

Controller actions are normalized by InputPlumber and resolved by a hearthOS
semantic router. hearthOS QML surfaces consume actions such as focus, accept,
back, search, context, group navigation, scrolling, and panel commands. They do
not receive fake global Arrow, Enter, Escape, Tab, or function-key events.

Physical keyboard events remain normal Qt keyboard events. Intentional pointer,
wheel, and text-injection paths may use virtual devices where their behavior is
actually pointer, scrolling, or text entry.

## Navigation and Text modes

Every hearthOS-owned surface starts in Navigation Mode unless it is restoring an
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

Mappings are data-driven and contextual. An active, more-specific hearthOS
surface always overrides a broader or global controller action. For example,
the OSK layer overrides desktop-wide bumper and face-button meanings while it
is visible.

| Physical control | Default semantic behavior outside the OSK |
| --- | --- |
| D-pad | Focus left/right/up/down; registered surfaces may apply bounded repeat |
| Left stick | Base Desktop scroll/paging; registered Hearth surfaces may override it with semantic focus, hysteresis, axis lock, and bounded repeat |
| Right stick | Pointer motion |
| South face | Accept/activate |
| East face | Back/cancel |
| West face | Surface alternate action; toggles Grid/List in App Menu |
| North face | Open OSK immediately and target the active field or surface primary search |
| RT / LT | Base controls unbound by default; Guide+RT is the proposed HIN-001 native screenshot chord |
| RB | Primary/left pointer click in Desktop/App Menu contexts |
| LB | Secondary/right pointer click in Desktop/App Menu contexts |
| Menu/Start | Open App Menu globally; open selected-item actions inside App Menu |
| Guide | Proposed HIN-001 system-chord modifier outside Gaming Mode |
| View/Select | Future System Bar focus; initially select Control Center |
| R3 + D-pad / left stick | Proposed HIN-001 focus window left/right and workspace up/down |
| L3 + LB / RB | Proposed HIN-001 swap focused window left/right; App Menu overrides with previous/next tab |
| L3 + West / North | Proposed HIN-001 close/maximize focused window |
| Guide + left stick / L3 | Proposed volume, track, and play/pause media actions |
| Guide + West hold / North / RT | Proposed capability-gated force-quit, power-off, and native screenshot |
| Guide + LT / RS / LB / RB | Unassigned and reserved for later remappable actions |

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

The old global F10 launcher binding is superseded. System Bar-focus, media,
Guide/View, and recovery shortcuts require conflict review before acceptance.

## Future keyboard presets and First Setup

First Setup will offer explicit Classic and Vim presets. These are future
outcomes and are not part of HSN-002. During setup both vocabularies may work
temporarily; pointer/WASD usage recommends Classic, HJKL usage recommends Vim,
and controller-only setup asks for an explicit choice.

| Intent | Classic | Vim |
| --- | --- | --- |
| Navigate | Arrows, `WASD`, `Tab` | Arrows, `HJKL` |
| Previous/next tab | `Shift+A` / `Shift+D` | `Shift+H` / `Shift+L`, `gT` / `gt` |
| First/last item | Home / End | `gg` / `G` |
| Remove selected item | Delete | `dd` |
| Undo | `Ctrl+Z` | `u` |

Both presets retain `/` for search, `o` or Enter for activation, and Menu or
`Shift+F10` for context actions.

## Glyphs and configuration

`InputHintBar` is the one reusable visual source for shell action hints. HIN-001
provides headless `Input1` context, action, modifier, capability, and glyph
state; HSN-002 delivers the first visual implementation. HIN-002, OSK/Text
Mode, System Bar, and later surfaces reuse that component rather than creating
surface-specific hint systems.

HIN-001 reuses the existing `Input1.ActiveContext` member and adds modifier,
available-action, capability, and read-only active-binding snapshot/revision
state. HIN-002 separately proposes additive
`Input1.DesktopMode` state for `none`, `navigate`, and `manipulate`; QML does
not infer or own that latch. An active specific surface suppresses unregistered
desktop modifier actions as well as overriding registered conflicts, so an
App Menu chord cannot close or move the window behind the menu.

The component consumes ordered semantic action descriptions rather than
physical mappings. Controller-family changes update Xbox, PlayStation,
Nintendo, or generic physical glyphs without rewriting surface code. An
inactive modifier is shown first by itself; while active it expands in place to
reveal only actions valid in the winning context. Unsupported capability-gated
actions are absent or visibly disabled. The default host places hints in its
bottom safe area with accessible text equivalents.

Full motion uses shared insertion/expansion tokens and never delays dispatch.
Reduced motion uses opacity/state changes with no translation, deformation, or
stagger. Context transfer updates hints atomically and cannot replay an input.

The controller manifest and keyboard shortcuts are versioned configuration,
not hardcoded QML policy. Every controller action is intended to be remappable.
Semantic layers and actions remain stable while physical triggers are data:
hold and latch triggers are independent and may be the same or different
controls. Packaged R3/L3 navigation/manipulation defaults therefore allow a
later mapping such as RT/LT for hold while R3/L3 remain latch triggers.

The later Controller Settings editor owns user-facing remapping, custom
modifier creation, per-layer hold/latch choice, conflict diagnostics, and
recovery. Custom bindings may select only registered semantic actions and must
never become arbitrary command execution. HIN-001/HIN-002 must use an
extensible binding/state model now so that editor does not require a parallel
router or hint implementation. Existing v3 service/state-machine work is
reusable evidence, but its trigger-click, bumper-group, north-hold, and other
superseded defaults are not current behavior.

## Third-party applications

hearthOS does not promise native semantic focus inside arbitrary applications.
The supported strategy remains native gamepad when available, explicit
application profiles where later justified, right-stick pointer fallback, and
the best-effort OSK path described in `osk.md`. Application capability claims
require candidate-specific evidence.

## Open boundary

Final System Bar focus-return details, pointer acceleration, final glyph-family
override precedence, controller-power implementation for unsupported hardware,
the persisted custom-binding schema, and remaining keyboard conflicts are
tracked in `docs/open-questions.md`.
