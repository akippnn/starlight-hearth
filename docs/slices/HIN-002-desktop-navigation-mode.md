---
id: "HIN-002"
title: "Desktop Navigation Mode"
contract_version: 1
contract_state: proposed
owner: "@akippnn"
repositories:
  - "akippnn/starlight-hearth"
  - "akippnn/starlight-hearth-shell"
target: "hearthOS Desktop on niri 26.04"
current_status: "../status.md"
evidence: "../evidence/HIN-002.md"
updated: "2026-08-29"
---

# HIN-002 — Desktop Navigation Mode

This is a decision-complete proposed contract. It depends on frozen HIN-001
headless routing and the reusable `InputHintBar` delivered by HSN-002. It does
not authorize implementation, publication, deployment, or acceptance.

## Owner-visible outcome

From the normal hearthOS Desktop, the owner can latch a visible niri-backed
Navigate or Manipulate mode, switch between them with R3/L3, understand the
available controller actions from bottom hints, and leave with the selected
real window/workspace state intact.

## Authentic path

`R3 or L3 -> HIN-001 semantic state -> Rust niri event stream/actions -> niri Overview and compositor animation -> hearthOS mode indicator + shared InputHintBar`

Cannot prove this outcome:

- QML-emulated windows/workspaces, a screenshot of static cards, fake keyboard
  state, a separate shell overview, or mocked niri actions;
- a hint overlay without physical controller, reconnect, and real niri proof.

## Public behavior and ownership

hearthOS names the surface **Desktop Navigation mode**. It uses niri's native
Overview for the zoomed-out window/workspace representation and compositor
animation. The shell supplies only a small mode indicator and bottom
`InputHintBar`; it does not reproduce window thumbnails, focus state, workspace
layout, or motion.

Two mutually exclusive modes exist:

- **Navigate (R3):** left stick or D-pad left/right focuses the niri
  column/window to the left/right; up/down focuses the workspace above/below.
  South keeps the current focus and exits. East exits without undoing focus.
  No Navigate action closes, maximizes, or moves a window.
- **Manipulate (L3):** LB/RB swaps only the focused window left/right in the
  current workspace; West requests normal close; North toggles niri
  maximization. A close or maximize action switches to Navigate if a valid
  focused window remains. East switches back to Navigate. South also returns
  to Navigate.

Pressing L3 while Navigate is active switches directly to Manipulate; pressing
R3 while Manipulate is active switches directly to Navigate. The previous mode
is fully released before the new mode activates, so both cannot be active and
no action crosses the transition.

HIN-002 extends the existing `org.starlight.HearthShell.Input1` interface
without renaming HIN-001 members. It adds read-only `DesktopMode:s` with exact
values `none`, `navigate`, and `manipulate`, plus
`DesktopModeChanged(s mode)`. Mode changes and keyboard requests emit the same
existing `Action` signal vocabulary: `toggle-navigate-mode`,
`toggle-manipulate-mode`, and `exit-desktop-mode`. QML observes this state; it
does not own or infer the latch state.

### Latch and hold

- A press activates its mode immediately and reveals hints.
- Releasing the modifier without having invoked a dependent action latches
  that mode.
- Releasing after a dependent action exits a momentary mode. If the mode was
  already latched, dependent actions do not unlatch it except for the explicit
  exit/return behavior above.
- Pressing and releasing the active mode's modifier without an action toggles
  the latch off. Pressing the other modifier switches modes seamlessly.
- East always backs out one level: Manipulate to Navigate, then Navigate to
  closed. Closing the surface also closes niri Overview.
- Disconnect, provider loss, session teardown, or shell restart closes the
  surface, closes niri Overview where reachable, and clears both modes. A
  reconnect never restores a latch automatically.

### Keyboard

- `Meta+Tab` toggles Navigate because it is unclaimed in the hearthOS niri
  configuration. `Escape` exits one level using the same rules as East.
- Classic arrows/WASD and Vim HJKL navigate while Navigate is active.
- In the Vim vocabulary, `x` closes and `f` maximizes the selected window using
  the same safe Manipulate actions, then returns to Navigate. Classic keyboard
  equivalents remain configurable and are finalized by First Setup later.
- `Meta+H` and `Meta+L` remain the HIN-001 direct focus shortcuts outside the
  visible mode. Key handling is centralized in niri/semantic configuration,
  not duplicated in QML.

### Reusable presentation

- The current mode is shown in a compact non-focusable pill above the bottom
  safe area. The shared `InputHintBar` sits below it and consumes HIN-001
  `Input1` state; HIN-002 does not fork or wrap a private hint implementation.
- Hints show R3 or L3 first, then reveal the active mode's available actions.
  They update atomically when switching modes and omit capability-gated actions
  that cannot run.
- Full motion uses shared mode/hint transitions; reduced motion uses opacity
  and immediate layout state without translation, deformation, or stagger.
- Niri's existing focus ring/Overview selection is sufficient proof for this
  outcome. A shell-wide animated focus visualization remains the later Focus
  Cursor outcome.
- The indicator and hints are top/overlay-layer surfaces that remain visible
  over niri Overview but do not take keyboard focus or block pointer access to
  niri's Overview.

| Responsibility | Canonical owner | Contract/version | Independent proof |
| --- | --- | --- | --- |
| Window/workspace/Overview state and animation | niri 26.04 | niri IPC | Real event stream and action tests |
| Latch state, switching, reconnect, precedence | Rust companion | HIN-002 additive `Input1.DesktopMode` and actions | State-machine and user-bus tests |
| Mode indicator and hints | Shared shell components | `InputHintBar` + mode model | QML tests with provider double |
| Keyboard bindings | Product niri configuration | Semantic action mapping | niri validation and authentic keyboard test |

## Context precedence

- A focused, more-specific hearthOS surface prevents HIN-002 from opening and
  consumes its own registered actions. For example, App Menu L3+LB/RB changes
  tabs and does not move a desktop window.
- Opening App Menu or another exclusive hearthOS surface while HIN-002 is
  latched first closes Desktop Navigation mode and niri Overview, then
  transfers context. No held button is replayed into the new surface.
- Pointer use does not silently close the mode, but East/Escape, modifier
  toggle, successful South exit, or context transfer does.

## Scope

In:

- visible mutually exclusive R3 Navigate and L3 Manipulate latches;
- momentary hold behavior using the same modes;
- niri Overview, real focus/swap/close/maximize actions, bottom reusable hints,
  reduced motion, keyboard access, context transfer, and recovery.

Out:

- App Menu implementation, a new overview/window model, window previews owned
  by QML, arbitrary workspace/window reordering, moving apps to another
  workspace, whole-column movement, multi-select, drag/drop, or tiling editor;
- Focus Cursor, System Bar, Control Center, Settings, OSK, and controller
  remapping UI;
- acceptance of HIN-001 or HSN-002 merely because their implementation is
  reused.

## Failure and recovery

- If niri Overview or its event stream fails, the shell closes the mode and
  shows a bounded diagnostic through the existing shell recovery path; it does
  not present stale windows.
- A window disappearing during navigation selects niri's resulting focus. If
  none remains, mutation actions disable and East/Escape still exits.
- Close is a normal compositor close request. Force-quit remains the separate
  capability-gated HIN-001 Guide chord and is never substituted silently.
- No mode surface may create a focus trap, intercept emergency keyboard
  shortcuts, survive desktop teardown, or remain visually stuck after niri
  Overview closes externally.

## Non-owner readiness gates

- [ ] Contract is frozen and its exact approved revision is recorded externally.
- [ ] HIN-001 exact candidate passes its independent routing/reconnect gates;
      HSN-002's exact `InputHintBar` API passes reusable component tests.
- [ ] State-machine tests cover tap latch, action-aware release, same-modifier
      toggle, cross-modifier switch, East/South behavior, context transfer,
      disconnect, reconnect, provider failure, and duplicate events.
- [ ] Real niri tests prove Overview state synchronization and directional,
      workspace, swap, close, and maximize actions without QML state emulation.
- [ ] QML tests prove non-focusable contained surfaces, modifier-first hints,
      controller-family glyphs, reduced motion, accessibility text, and no
      private hint implementation.
- [ ] Authentic controller and keyboard tests exercise both modes, rapid
      navigation, window disappearance, external Overview close, reconnect,
      shell restart, desktop teardown, and recovery.
- [ ] HSN-001, HIN-001, and HSN-002 evidence remain separately attributable;
      the combined package/image does not combine owner verdicts.

## Owner audit

1. Boot the recorded signed image with several windows across at least two
   niri workspaces.
2. Tap R3 to latch Navigate; use D-pad and held left stick across windows and
   vertical workspaces and confirm niri animates the real layout.
3. Switch directly with L3, move one focused window left/right, close a
   disposable window, maximize another, and return to Navigate.
4. Exercise action-aware momentary holds, same-modifier exit, East/South,
   `Meta+Tab`, HJKL, `x`, and `f`.
5. Open App Menu while latched and verify context precedence and clean hint
   transfer; disconnect/reconnect and restart the shell during each mode.
6. Confirm no stuck layer, focus trap, stale action, QML-emulated state, or
   shell-wide Focus Cursor claim.

Owner verdict: `pending`. No candidate exists.

## Contract amendments

| Version | Supersedes | Reason / source finding | Approved by/date | Material change |
| --- | --- | --- | --- | --- |
| 1 | — | Owner separated visible latched navigation from HIN-001 on 2026-08-29 | Pending | Initial proposed contract |

Canonical evidence: [HIN-002 evidence](../evidence/HIN-002.md)
