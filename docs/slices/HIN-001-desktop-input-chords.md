---
id: "HIN-001"
title: "Desktop Input Chords"
contract_version: 1
contract_state: frozen
owner: "@akippnn"
repositories:
  - "akippnn/starlight-hearth"
  - "akippnn/starlight-hearth-shell"
target: "hearthOS Desktop on the owner 8BitDo Pro 3 target"
current_status: "../status.md"
evidence: "../evidence/HIN-001.md"
updated: "2026-08-30"
---

# HIN-001 — Desktop Input Chords

This decision-complete v1 contract is owner-approved and frozen for HIN-001
implementation. Publication, deployment, audit-readiness, and acceptance
retain their independent gates.

## Owner-visible outcome

From the normal hearthOS Desktop, the owner can hold controller modifiers to
navigate and manipulate real niri windows and workspaces, and can invoke a
small capability-gated system chord set, without opening a shell surface.

## Authentic path

`physical controller -> canonical InputPlumber profile -> Rust semantic router -> real niri IPC or typed system provider -> visible compositor/system result`

Cannot prove this outcome:

- fake keyboard events, QML-emulated window/workspace state, mocked niri state,
  offscreen QML, or an InputPlumber fixture without the real action;
- a successful action on one controller family as proof of an unsupported
  hardware capability such as receiver power-off.

## Public behavior and ownership

- R3 is the default navigation hold trigger. While held, left stick or D-pad
  left/right focuses the niri column/window to the left/right and up/down
  focuses the niri workspace above/below.
- L3 is the default manipulation hold trigger. In the desktop context,
  L3+LB/RB
  swaps only the focused window left/right in its current workspace,
  L3+West requests a normal close, and L3+North toggles niri maximization.
- Base RB remains primary/left pointer click and base LB remains
  secondary/right pointer click. A registered, more-specific hearthOS context
  may override them while its modifier is active.
- In the App Menu context, L3+LB/RB emits previous/next-tab actions. HIN-001
  provides the headless state and routing; HSN-002 separately proves the tabs.
- Guide+left-stick up/down adjusts volume, left/right selects the
  previous/next media track, and Guide+L3 toggles play/pause. Held volume
  directions repeat; track and play/pause actions fire once per press.
- Guide+RT opens niri's native interactive screenshot UI. It does not capture
  through a parallel shell screenshot implementation.
- Guide+North requests controller power-off only when the discovered hardware
  provider advertises that capability. InputPlumber 0.78 and the owner 8BitDo
  receiver do not currently provide it, so the action remains unavailable and
  must not report success on that target.
- Guide+West held for 2.4 seconds requests force-quit. It is available only
  when the focused niri PID maps to a verified, user-owned application scope;
  the whole scope is terminated. Unknown PIDs, shell/compositor/session
  processes, and unverified scopes fail closed with a diagnostic.
- East remains back/cancel, West is the physical west face position, North is
  the physical north position, and South remains accept/activate.
- `Meta+H` and `Meta+L` are keyboard equivalents for focus left/right. These
  bindings call the same semantic/niri actions and remain configurable.
- Base LT/RT and Guide+LT, Guide+RS, Guide+LB, and Guide+RB are intentionally
  unassigned. View/Select is reserved for the future System Bar focus workflow,
  initially selecting Control Center; HIN-001 does not consume it.

Navigation and manipulation are stable semantic layers, not hardcoded stick
buttons. The routing model keeps physical trigger bindings separate from layer
action maps and represents hold and latch triggers independently. The packaged
defaults bind R3/L3 stick clicks as the navigation/manipulation hold triggers.
A later Controller Settings outcome may instead bind RT/LT as hold triggers
while retaining R3/L3 as latch triggers, or define additional custom modifier
layers. Custom layers may reference only registered semantic action IDs; they
cannot embed commands, D-Bus destinations, or niri request text.

HIN-001 supplies the data-driven router and packaged default binding manifest,
but not the user-facing remapping editor or final persisted user-schema. The
future editor must be able to remap every controller action, create/delete
custom modifiers, choose hold and/or latch activation per layer, detect
same-context conflicts, and retain a visible recovery path. HIN-001 must not
make that later work require replacing its state machine or public semantic
action vocabulary.

The Rust companion consumes niri's event stream as the only window/workspace
state authority and invokes typed niri actions over its IPC socket. QML does
not participate in HIN-001.

`org.starlight.HearthShell.Input1` remains the interface and keeps its existing
members, including read-only `ActiveContext:s`. It adds read-only
`ActiveModifiers:as`, `AvailableActions:as`, `Capabilities:a{sb}`, and
`BindingRevision:t`; `GetBindings()` returns `a(sssss)` records containing
`(context, layer, action, activation, trigger)`, where activation is one of
`press`, `hold`, `latch`, or `long-press` and trigger uses normalized physical
control IDs joined by `+` for a chord. `action` is empty for a layer-activation
record and otherwise names a registered semantic action. It also adds
`BindingsChanged(t revision)` and
`StateChanged(as activeModifiers, as availableActions, a{sb} capabilities,
s activeContext)`. Existing `Action(s action, s phase, d value, t monotonicUsec)`
publishes the additive semantic actions below without renaming v1 actions:

- `focus-window-west`, `focus-window-east`, `focus-workspace-north`,
  `focus-workspace-south`;
- `move-window-west`, `move-window-east`, `close-window`, `maximize-window`;
- `previous-tab`, `next-tab`;
- `volume-up`, `volume-down`, `media-previous`, `media-next`,
  `media-play-pause`;
- `screenshot`, `controller-power-off`, and `force-quit`.

| Responsibility | Canonical owner | Contract/version | Independent proof |
| --- | --- | --- | --- |
| Physical normalization and packaged defaults | Product image | InputPlumber desktop profile + extensible binding manifest | Schema, drift, and physical-event tests |
| Chord state, precedence, repeat, capabilities, diagnostics | Rust companion | `Input1` additive state/actions | Router/state-machine and user-bus tests |
| Window/workspace state and actions | niri 26.04 | niri IPC event stream/actions | Real-socket provider tests |
| Media and screenshot actions | Rust companion + system providers | Typed semantic actions | Provider fixtures plus authentic target |

## Input-state rules

- A modifier press becomes active immediately. Its release emits releases for
  every active dependent action before clearing modifier state.
- Trigger resolution uses the active binding manifest. Hold and latch triggers
  for one semantic layer may be the same physical control or different controls;
  changing a trigger never renames the layer or its semantic actions.
- D-pad and left-stick directions emit one action immediately, repeat after
  260 ms, repeat every 90 ms, and accelerate to 55 ms after one second.
- Left-stick direction engages at 0.55, releases at 0.35, and locks to the
  strongest axis until recentered. Diagonal jitter cannot alternate actions.
- A more-specific active hearthOS context wins over desktop/global routing.
  While such a surface is active, unregistered desktop modifier actions are
  suppressed rather than falling through to the window behind it. The losing
  action is not emitted later when the context closes.
- Duplicate press events are suppressed. Disconnect, provider loss, session
  teardown, and service restart synthesize required releases, clear every
  modifier/repeat timer, and never replay a stale action after reconnect.
- Pointer output is suppressed while RB/LB participate in an active modifier
  chord; a chord cannot leak a click.
- Capability-gated actions appear in `AvailableActions` only when safe to
  invoke. Failure is diagnostic and never silently falls back to a shell
  command or fake success.

## Scope

In:

- the headless navigation and manipulation hold layers with packaged R3/L3
  defaults and an extensible trigger/action representation;
- App Menu tab semantic actions without App Menu UI implementation;
- bounded Guide media, screenshot, capability-gated power-off, and safe
  force-quit chords;
- niri event-stream reconnect, focus/action routing, and additive `Input1`
  state needed by reusable hints.

Out:

- latched modes, niri Overview orchestration, hint UI, or any shell surface;
- App Menu implementation, OSK invocation, Controller Settings/remapping UI,
  persisted custom-binding authoring and migration,
  controller-specific HID reverse engineering, brightness, magnifier, and
  screen-reader chords;
- moving a window to another workspace, moving whole columns/workspaces, and
  shell-wide Focus Cursor animation.

## Failure and recovery

- If niri state is unavailable, all desktop window/workspace actions fail
  closed, modifiers clear, and recovery keyboard paths remain usable.
- If media or screenshot providers fail, the router emits a bounded diagnostic
  and does not reinterpret the chord.
- Unsupported controller power-off remains visibly unavailable through state
  and later hints; the owner receiver is an explicit unsupported cohort.
- Force-quit never targets niri, hearthOS Shell, the desktop session, an
  unknown PID, or an unverified cgroup.
- Controller reconnect restores only the base state. The user must press a
  modifier again.

## Non-owner readiness gates

- [ ] Contract is frozen and its exact approved revision is recorded externally.
- [ ] Canonical product mapping, installed profile, shell mirror, and semantic
      manifest agree exactly and preserve HSN-001 RB/LB behavior.
- [ ] Router tests cover precedence, modifier ordering, repeat/hysteresis,
      duplicate suppression, click suppression, disconnect, reconnect, and
      capability changes.
- [ ] Binding-model tests prove physical triggers are separate from semantic
      layers, hold/latch triggers can differ, free controls remain unclaimed,
      custom layers accept only registered actions, conflicts fail visibly,
      and `GetBindings`/`BindingsChanged` expose the exact active mapping.
- [ ] Real niri IPC tests cover event-stream bootstrap/reconnect and every
      approved focus, swap, close, maximize, and screenshot action.
- [ ] Media tests cover repeat and no-repeat actions; force-quit tests prove
      scope verification and protected-process rejection.
- [ ] Authentic physical-controller tests exercise every supported chord and
      visibly confirm that controller power-off is unavailable on the owner
      receiver rather than falsely successful.
- [ ] HSN-001 regression and amended physical RB/LB compatibility gates pass.

## Owner audit

1. Start from the recorded clean image with at least two windows on two niri
   workspaces and media playback available.
2. Hold R3 and navigate windows left/right and workspaces up/down with both the
   D-pad and left stick, including held repeat.
3. Hold L3 and move one focused window left/right, close a disposable window,
   and toggle maximize without moving a whole tabbed column.
4. Exercise base RB/LB clicks, Guide media, and the niri screenshot UI.
5. Long-hold force-quit on a disposable verified app, then confirm protected
   and unknown targets fail closed.
6. Disconnect/reconnect during each modifier and verify no stuck or replayed
   action; confirm power-off is unavailable on the owner receiver.

Owner verdict: `pending`. No candidate exists.

## Contract amendments

| Version | Supersedes | Reason / source finding | Approved by/date | Material change |
| --- | --- | --- | --- | --- |
| 1 | — | Owner separated headless hold/chord routing from visible navigation and clarified remappable hold/latch defaults on 2026-08-29 | @akippnn / 2026-08-30 | Initial frozen contract, including binding-independent semantics and free-control reservations |

Canonical evidence: [HIN-001 evidence](../evidence/HIN-001.md)
