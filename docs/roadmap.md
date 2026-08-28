# hearthOS planning roadmap

**Roadmap state:** HSN-001 v2 active/pending at `43ca3393adf1dbbc2448ea8bfbfddc80761f386f`; HSN-002 proposed/pending
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
| **HSN-002 — App Menu** | Decision-complete proposed contract plus a later verified HSN-001 component baseline | Reusable `CollectionBrowser`; additive read-only `Category1` and typed `AppCatalog1`; local `Search Apps`; Favorites/Recents/By Name/By Category tabs; right index rail and Grid/List; schema-v2 migration | Proposed/pending review only; no frozen revision, candidate, evidence, or implementation authority. Opens on Favorites; clearing search restores prior context; physical keyboard composes queries until OSK; edit/reorder mode and adjacent surfaces are excluded. |
| hearthOS System Bar | Launcher/input foundation | Visibility invariant, focus return, owned-panel pinning, App Menu attachment, multi-input behavior, and owner-visible reachability; replace the temporary invisible hover edge with a generous click target around the placed App Menu button | Proposed |
| OSK and explicit Text Mode | Input foundation plus history-preserving wvkbd fork | Hearth text entry, secure-field privacy, active XKB layout, overlay/dock behavior, and bounded third-party claims | Proposed |
| hearthOS Settings foundation | Versioned config schema and shared controls | Controller/keyboard edits apply safely through the layered config model with rollback/fallback | Proposed |
| Workspace/window and control surfaces | niri IPC plus Bar foundation | Authentic niri state, no focus traps, controller-aware sliders, and coherent notifications/control center | Proposed |
| Focus Cursor | Proven focus semantics across several shell surfaces | Shell-wide animated selection-border cursor moves coherently without becoming a launcher-specific implementation | Proposed independent slice |

## Ordered successor outcomes

1. **Desktop Controller Controls** — configurable hold-by-default modifier
   layers and typed niri window/workspace actions; visible hearthOS surfaces
   override global actions.
2. **Independent Linux Search Engine** — desktop-neutral search project with a
   typed hearthOS provider adapter; HSN-002 initially keeps its app-local
   provider.
3. **hearthOS System Bar** — authentic App Menu and panel attachment points.
4. **hearthOS Control Center**.
5. **Add Controls & Widgets** — reuse `CollectionBrowser` and `Category1` as
   `ControlsCatalog`, entered from Control Center with North/Y or `i`, and use
   `Search Controls & Widgets` without a redundant title.
6. **Focus Cursor** — separate contract for the shell-wide moving selection
   border.
7. **HWP-001 Local Wallpaper** — typed local-file service, recovery wallpaper,
   per-output background, deterministic center crop, last-good retention, and
   reduced-motion handling.
8. **hearthOS Settings** — edit existing configuration and palette contracts
   rather than creating parallel state.
9. **First Setup** — explicit Classic/Vim keyboard preset selection and later
   onboarding outcomes; not HSN-002.
10. **Install hearthOS** — separately frozen installation, recovery, and
    rollback outcome.
11. **hearthOS Portal and plugin architecture** — typed privileged actions and
    explicit trust/lifecycle boundaries after their independent contracts.

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

Keep the verified HSN-001 corrections local and review the decision-complete
proposed HSN-002 contract. Do not begin HSN-002 implementation until the owner
first approves and freezes an exact contract revision, then separately
authorizes local implementation. Public push, tags, RPMs, OCI builds, target
rebases, and HSN-001 physical RB/LB reruns remain held for an explicit delivery
greenlight.

Public product naming is **hearthOS** or **HearthOS**, part of the u128
Starlight family. Repository names and the current technical bus, service,
filesystem, and package identifiers remain unchanged until a separate naming
migration is authorized.
