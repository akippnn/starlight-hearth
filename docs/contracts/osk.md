# On-screen keyboard behavior

**State:** Accepted planning contract; not frozen for implementation
**Proposed upstream base:** wvkbd v0.20 at `6b41504a0cb58fd1163fa44692398fbd61f8905f`

## Process and protocol boundary

Create a separate `starlight-hearth-keyboard` fork preserving wvkbd history.
The Rust shell companion spawns and supervises it as a child; it is not an
unrelated standalone service. The companion remains hearthOS's sole public API.
The private child protocol is not yet specified.

Use Wayland input-method-v2, text-input-v3, virtual-keyboard-v1, and layer
shell. Add input-method keyboard grab support only while the OSK has been
explicitly shown for physical-keyboard navigation. A hidden OSK never captures
application keyboard events.

## Activation and mode flow

- Controller/touch deliberate activation of a text field opens the OSK.
- Mouse, right-stick pointer, and physical-keyboard activation do not auto-open
  it.
- North face outside the OSK opens it immediately with no hold delay.
- Target the active text field; if none exists on a hearthOS surface, target its
  primary search. In App Menu this means focus search.
- `Super+I` and `F12` are manual physical-keyboard fallbacks.
- Back closes the OSK and exits Text Mode in one action, restoring focus to the
  field's owning navigational control. A later Back may close the parent.

hearthOS-owned fields are reliable. Supported third-party Wayland fields are
best effort through text-input/input-method protocols. Unsupported and
XWayland clients retain an explicit manual fallback; universal support is not
claimed.

## Geometry and layers

- Four-row paged keyboard.
- Initial layers: Letters, Numbers, Symbols.
- Emoji and handwriting deferred.
- Overlay default, remembered per output.
- Visible Pin/Dock action toggles docked mode.
- Docked mode reserves an exclusive bottom zone so niri reflows applications.
- Balanced overlay geometry: about 72% width by 34% height, capped near
  1100×360 logical pixels with safe-edge clamping.
- Minimum key target: 48 logical pixels.

Qt/Quickshell logical geometry is authoritative across output scales.

## Layout and language

Render the exact active XKB layout and variant and follow niri's active-layout
event stream. The language control changes niri's active layout rather than
maintaining an unrelated OSK-only language. Invalid keymap configuration shows
a visible warning, records the exact non-content error, and uses a US QWERTY
fallback.

## Controller mapping while visible

| Input | OSK action |
| --- | --- |
| D-pad | Navigate keys |
| South/A | Activate selected key |
| East/B | Close and leave Text Mode |
| West | Delete |
| North | Space |
| RT | Enter |
| LT held | Shift; hold-only |
| L3 | Caps Lock synchronized with seat/physical LED state |
| Menu | Toggle symbol/page mode |
| View | Toggle Overlay/Docked |
| LB / RB | Previous/next keyboard layer |
| Right stick | Four-way caret movement; vertical movement is ignored in single-line fields |

Right-stick caret repeat uses a 55% threshold, immediate first step, about
350 ms initial delay, 90 ms repeat, and acceleration to about 45 ms after
1.5 seconds.

## Privacy

For secure fields, retain visible focus but disable character popups, key
content feedback, surrounding-text retention, suggestions, and content
logging. Diagnostics never record entered text, surrounding text, passwords,
or key content.

## Visual phase

The first implementation may use a functional hearthOS skin with correct color,
typography, focus, hints, privacy, and responsive geometry. Full expressive
motion refinement is later work and cannot delay correct input behavior.

Public/private IPC shapes, child restart policy, physical-keyboard grab details,
and unsupported-client UX remain open.
