# hearthOS System Bar behavior

**State:** Accepted planning contract; not frozen for implementation

## Visibility invariant

For each output, the System Bar is visible when any applicable reason is true:

```text
configured always-visible
OR pointer hovering/revealing the System Bar
OR keyboard focus within the System Bar
OR controller focus within the System Bar
OR any System Bar-owned panel is open
```

System Bar-owned panels explicitly include App Menu. An inherited
strict-auto-hide setting cannot hide the System Bar while an owned panel is
open.

## Pointer reveal and hide timing

When fully hidden, an invisible edge sensor covers only the System Bar's configured
span on its configured output edge. It does not turn the entire screen edge
into a reveal target and does not require a persistent visible handle.

Reveal is immediate. Once hover, System Bar focus, and every owned-panel state are
all false, start a configurable 250 ms hide grace. Renewed hover, focus, or
panel state cancels the pending hide. The eventual implementation must avoid
flicker while the input region changes during reveal/hide animation.

## Focus and panel ownership

- Keyboard and controller System Bar focus are equally visible.
- Opening a panel records its opening System Bar item and marks that item active.
- Moving focus into the panel does not break the System Bar's visible/open state.
- Closing a panel through keyboard/controller returns focus to its opening
  item, keeping the System Bar visible until System Bar focus is explicitly exited.
- Pointer scrim close may return focus to the previously active application,
  but must clear the panel's ownership state consistently.
- Nested/transient child surfaces count as part of the owned panel while they
  are active.

## Visual relationship

Hover, focus, press, release, and open states use the shared expressive motion
system. Opening a System Bar surface coordinates the System Bar, originating
item, panel, desktop dim, and subtle blur as one transition. The System Bar and active surface are
not dimmed as unrelated background content.

## Proposed layout and customization

The current information-architecture proposal places system tray/control
center toward the left, the clock in the center, and workspace/App Menu
controls toward the right. Widget placement, pointer drag/drop, and
keyboard/controller context editing remain requirements, but their exact
workflow and final left/right placement are open.

Battery/power controls appear only when applicable hardware exists.

## Open boundary

Initial focus item, final control-center/notification placement, output policy,
edit mode, widget schema, and motion constants remain in
`docs/open-questions.md`.
