# hearthOS planning roadmap

**Roadmap state:** HSN-001 ready/pending at exact frozen contract revision
**Last updated:** 2026-08-25

Future identifiers are intentionally unassigned. They will be reserved only
when an owner-visible contract is approved, preventing reuse of historical
VS/HS aliases or either collided `GM-001` meaning.

## Historical delivery record

| Historical slice | Delivery state | Owner verdict | Durable result |
| --- | --- | --- | --- |
| VS-001 / HS-001 — Hearth Desktop Foundation | Superseded | Rejected for controller-ready claim | Signed image boot, niri/DMS startup, TV scaling, identity, and recovery evidence remain valid within their recorded candidates. |
| VS-002 / HS-002 — Controller Handoff Prototype | Superseded | Not accepted | Session ownership, InputPlumber handoff, reconnect, packaging, and recovery evidence remain useful; controller-native shell behavior was not achieved. |
| HS-003 — Controller-Aware App Menu | Superseded | Pending/no verdict | Local semantic-router, D-Bus, focus/layout, glyph, packaging, and QML test evidence may be selectively salvaged; no deployed or owner-accepted Hearth-native outcome exists. |

Historical contracts and evidence remain under `docs/slices/` and
`docs/evidence/`. Their original state is not rewritten.

## Candidate Hearth Shell outcomes

| Candidate outcome | Dependency | Principal future gate | Planning state |
| --- | --- | --- | --- |
| **HSN-001 — Hearth-native Launcher Nucleus** | Frozen contract plus exact clean shell/image inputs | From a real Desktop session, controller/keyboard/pointer opens the right drawer, switches Grid/List, launches a separate available core favorite, and retains recovery | Ready/pending at `17fedae8776ff38b53c07d4098d8ee8b13852253` |
| Hearth Bar minimum | Launcher/input foundation | Visibility invariant, focus return, owned-panel pinning, multi-input behavior, and owner-visible reachability | Proposed |
| OSK and explicit Text Mode | Input foundation plus history-preserving wvkbd fork | Hearth text entry, secure-field privacy, active XKB layout, overlay/dock behavior, and bounded third-party claims | Proposed |
| Hearth Settings foundation | Versioned config schema and shared controls | Controller/keyboard edits apply safely through the layered config model with rollback/fallback | Proposed |
| Workspace/window and control surfaces | niri IPC plus Bar foundation | Authentic niri state, no focus traps, controller-aware sliders, and coherent notifications/control center | Proposed |
| Expressive design-system refinement | Proven functional shell surfaces | Shared motion tokens, reduced motion, performance, and consistent mouse/keyboard/controller states | Proposed |

## Candidate application and plugin outcomes

| Candidate outcome | Dependency | Principal future gate | Planning state |
| --- | --- | --- | --- |
| Hearth Portal foundation | Safe typed action adapter and shared Hearth app controls | Maintainable Bazzite catalog alignment, privilege isolation, Desktop/Gaming context, and recovery | Proposed |
| Default wallpaper plugin | Plugin boundary plus config/provider service | Local and Waifu.im sources, failure-safe cache, deterministic crop provenance, and responsive Settings | Proposed |
| Controller-friendly default applications | Input/app-profile policy and exact catalog | Required workflows graded against exact candidates; no silent unsupported defaults | Proposed |
| File-manager contingency | Dolphin and Nautilus both fail documented owner workflows | Explicit owner activation, Index history-preserving fork, MauiKit/KIO reuse, and separate acceptance | Deferred contingency |

## Candidate Gaming Mode outcomes

| Candidate outcome | Dependency | Principal future gate | Planning state |
| --- | --- | --- | --- |
| Shader-compilation responsiveness investigation | Matching unmodified Bazzite baseline | Reproduce and attribute behavior before a bounded Hearth mitigation | Proposed |
| Measured Gaming Mode latency investigation | Controlled hardware/session baselines | Input-to-display and frame-time evidence isolates Steam, Gamescope, InputPlumber, Hearth, wireless, or other causes | Proposed |
| Hearth apps in Gaming Mode | Context-aware app launch contract | Same installed apps appear as safe Steam entries with correct scale/input/state | Proposed |
| Hearth-owned Decky integration | Proven shared Desktop cores | Preserve unrelated plugins and reuse rather than duplicate provider/config logic | Deferred |

The two historical proposals both called `GM-001` receive new IDs only after
their individual contracts are approved.

## Candidate inherited-base retirement outcomes

| Candidate outcome | Dependency | Principal future gate | Planning state |
| --- | --- | --- | --- |
| Curated application surface | Portal and exact application inventory | No workflow disappears before its replacement; dependencies may remain hidden | Proposed |
| KDE recovery retirement | Accepted shell, Portal, Settings, file recovery, and recovery diagnostics | Display, network, authentication, terminal, files, rollback, TTY, and failure recovery pass owner audit without Plasma | Deferred |

## Current gate

Implement only HSN-001's provider, consumer, package, and image
responsibilities against its recorded contract revision. Owner acceptance
remains separate.
