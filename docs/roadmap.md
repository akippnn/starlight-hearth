# hearthOS planning roadmap

**Roadmap state:** HSN-001 v2 active/pending at `43ca3393adf1dbbc2448ea8bfbfddc80761f386f`; HIN-001, HSN-002, and HIN-002 proposed/pending
**Last updated:** 2026-08-29

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

## Candidate hearthOS Shell outcomes

| Candidate outcome | Dependency | Principal future gate | Planning state |
| --- | --- | --- | --- |
| **HSN-001 — hearthOS Launcher Nucleus** | Frozen v2 contract plus exact clean shell/image inputs | From a real hearthOS Desktop session, controller/keyboard/pointer opens the right drawer, switches Grid/List, launches a separate available core favorite, and retains recovery | Active/pending at exact v2 revision `43ca3393…`; signed RC.2 boots and its functional field paths pass, but it retains blur and duplicate-selection presentation defects. Both corrections pass local real-niri proof and remain deliberately unpublished. RB/LB physical and cross-repository mapping proof must be rerun on the next signed candidate. |
| **HIN-001 — Desktop Input Chords** | Repaired HSN-001 input/lifecycle baseline | Headless navigation/manipulation with R3/L3 packaged defaults, binding-independent semantic layers, context precedence, media/screenshot, safe capability gates, real niri IPC, and reconnect recovery | Proposed/pending; implement first after documentation, exact owner freeze, and separate authorization. No UI and no candidate. |
| **HSN-002 — App Menu** | HIN-001 semantic state plus a verified HSN-001 component baseline | Reusable `CollectionBrowser` and binding-aware `InputHintBar`; additive read-only `Category1` and typed `AppCatalog1`; local search/tabs/index/Grid/List; schema-v2 migration; bounded attributed Blob transition | Proposed/pending review only; no frozen revision, candidate, evidence, or implementation authority. D-pad and left stick navigate with rapid repeat; the manipulation modifier plus LB/RB changes tabs (L3 packaged default); physical keyboard composes queries until OSK. |
| **HIN-002 — Desktop Navigation Mode** | Exact HIN-001 routing plus HSN-002 shared `InputHintBar` | Mutually exclusive visible Navigate/Manipulate latches with R3/L3 defaults, independently remappable hold/latch triggers, real niri Overview state/animation, keyboard access, hints, and recovery | Proposed/pending; implement after HSN-002 in this train. No candidate, evidence, or implementation authority. |
| hearthOS System Bar | Launcher/input foundation | Visibility invariant, View/Select focus with Control Center initially selected, focus return, owned-panel pinning, App Menu attachment, multi-input behavior, and owner-visible reachability; replace the temporary invisible hover edge with a generous click target around the placed App Menu button | Proposed |
| OSK and explicit Text Mode | Input foundation plus history-preserving wvkbd fork | Hearth text entry, secure-field privacy, active XKB layout, overlay/dock behavior, and bounded third-party claims | Proposed |
| hearthOS Settings foundation | Versioned config schema and shared controls | Controller/keyboard edits apply safely through the layered config model with rollback/fallback | Proposed |
| Workspace/window and control surfaces | niri IPC plus Bar foundation | Authentic niri state, no focus traps, controller-aware sliders, and coherent notifications/control center | Proposed |
| Focus Cursor | Proven focus semantics across several shell surfaces | Shell-wide animated selection-border cursor moves coherently without becoming a launcher-specific implementation | Proposed independent slice |

## Ordered successor outcomes

1. **HIN-001 Desktop Input Chords** — headless hold/chord routing and real niri
   actions.
2. **HSN-002 App Menu** — full application catalog plus the first shared
   `InputHintBar` and bounded Blob adaptation.
3. **HIN-002 Desktop Navigation Mode** — visible latches and niri Overview,
   reusing HIN-001 state and HSN-002 hints.
4. **hearthOS System Bar** — authentic App Menu and panel attachment points.
5. **hearthOS Control Center**.
6. **Add Controls & Widgets** — reuse `CollectionBrowser` and `Category1` as
   `ControlsCatalog`, entered from Control Center with North/Y or `i`, and use
   `Search Controls & Widgets` without a redundant title.
7. **Focus Cursor** — separate contract for the shell-wide moving selection
   border.
8. **hearthOS Settings and Controller Settings** — edit existing configuration,
   palette, and binding contracts rather than creating parallel state; remap
   every action and author custom hold/latch modifiers with conflict recovery.
9. **Plugin architecture** — first-party packaged/audited built-ins, explicitly
   trusted user-installed third-party code, compatibility, containment,
   diagnostics, disable/recovery, and provenance/consent requirements.
10. **HWP-001 Local Wallpaper built-in plugin** — typed local-file service,
    recovery wallpaper, per-output background, deterministic center crop, and
    last-good retention.
11. **Independent Linux Search Engine built-in plugin** — desktop-neutral
    search with a typed hearthOS provider adapter; HSN-002 initially keeps its
    app-local provider.
12. **hearthOS Portal** — typed privileged actions and Bazzite catalog adapter.
13. **First Setup** — explicit Classic/Vim keyboard preset selection and later
    onboarding outcomes; not HSN-002.
14. **Install hearthOS** — separately frozen installation, recovery, and
    rollback outcome.
15. **Later shell surfaces and applications** — bounded owner-visible outcomes
    using established shared providers and controls.

## Candidate application and plugin outcomes

| Candidate outcome | Dependency | Principal future gate | Planning state |
| --- | --- | --- | --- |
| hearthOS Portal foundation | Safe typed action adapter and shared hearthOS app controls | Maintainable Bazzite catalog alignment, privilege isolation, Desktop/Gaming context, and recovery | Proposed |
| **HWP-001 — Local Wallpaper** | Independent local-file contract plus config/background service | Typed local-file selection, packaged recovery background, deterministic center crop, last-good retention, and nonblocking per-output rendering | Reserved for a small independent contract; online providers, palette extraction, advanced saliency/cropping, and plugin architecture are later proposed/Open outcomes. |
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

Complete and commit the decision-complete HIN-001, HSN-002, and HIN-002
documentation, then obtain explicit owner approval and freeze each contract at
its own exact product revision. After separate implementation authorization,
the train order is HIN-001, HSN-002, then HIN-002. Public push, tags, RPMs, OCI
builds, deployment, target rebases, and HSN-001 physical RB/LB reruns remain
held for a later explicit delivery greenlight.

Public product naming is **hearthOS** or **HearthOS**, part of the u128
Starlight family. Repository names and the current technical bus, service,
filesystem, and package identifiers remain unchanged until a separate naming
migration is authorized.
