# Codex Master Handoff — hearthOS / starlight-hearth-shell fourth-iteration direction

You are working on the `starlight-hearth` and `starlight-hearth-shell` repositories. Treat this handoff pack as the complete current product-direction update, not as a narrow feature request for whatever slice happens to be active right now.

## How to use this pack

Read all numbered files in this pack before restructuring the roadmap or making architectural changes. The exact original owner prompt is preserved in `10_ORIGINAL_PROMPT_VERBATIM.md`; the other files organize it, add the later discussion, identify current-repository conflicts, and collect research/reference material. Do **not** omit a requirement merely because it belongs to a later vertical slice. The goal is exhaustive documentation and bounded implementation, not bounded knowledge.

The repositories already use `docs/` as durable project memory. Preserve that model. Reconcile the entire direction into the canonical documentation, ADRs, roadmap, slice contracts, status, and evidence system so future Codex turns can continue from repository state without requiring this giant prompt again. Keep chat narration concise; spend effort on repository inspection, durable docs, implementation, and tests instead of repeatedly re-explaining the plan in prose.

## Product-direction authority

Use chronology and explicitness carefully. Existing docs and ADRs describe what was true when they were written; they are not automatically authoritative when the owner later changed direction. Preserve old evidence and history, but explicitly supersede stale decisions rather than silently editing history or pretending they were never made. Likewise, earlier exploratory statements in the owner's prompt may be superseded by later explicit decisions in the same prompt.

One product decision is already resolved and must not be reopened as if it were undecided: **the downstream DMS maintenance/replacement threshold has been crossed.** The reason is not merely merge-conflict volume. Hearth's controller-first + keyboard-first semantic interaction model conflicts with assumptions distributed throughout a shell designed primarily around conventional pointer/keyboard desktop interaction. Continuing as a maintained DMS product means repeatedly inheriting and working around someone else's interaction decisions. DMS should remain available as a reference/inspiration and possible source of selectively reusable, license-compatible implementation ideas, but the target is a Hearth-native shell direction.

The later owner direction to repurpose useful existing work and build a custom Hearth Shell with **Quickshell/QML on niri** is authoritative over earlier uncertainty about whether to remain a DMS fork. Do not turn the shell into React, Electron, HTML, an embedded browser/WebView, or a localhost web application as an implementation shortcut. Native helper/services are allowed where QML should not own the operation; do not decide their language or architecture from this prompt alone when the repository and existing proven work can inform that choice.

Everything else that is genuinely open should remain open until you inspect the repositories, references, constraints, and existing work. Do not use this prompt as an excuse to prematurely decide plugin ABI, configuration format, exact source-reuse strategy, every controller chord, implementation language for every backend, or exact slice numbering. Plan those deliberately and record meaningful decisions in the appropriate docs/ADR when needed.

## Planning and delivery behavior

1. Inspect both repositories, including current branches, commit history, `docs/`, ADRs, current roadmap/status, evidence, tests, packaging, Quickshell/QML code, controller service, InputPlumber integration, recovery path, and any relevant current implementation.
2. Compare the current documented architecture to this handoff. Identify what remains valid, what is useful but coupled to the DMS-based implementation, what is stale, and what is directly contradicted by later owner direction.
3. Reconcile the complete product direction into `docs/`. **All requirements belong in the roadmap/backlog/docs even when they are not in the next slice.** Do not hide future requirements from Codex merely to reduce current scope.
4. Preserve historical evidence and accepted/rejected owner-audit results. Supersede obsolete ADRs/slices explicitly rather than deleting or rewriting their history.
5. Decompose the work into dependency-aware, reversible, testable vertical slices using the repository's existing delivery conventions. The roadmap can be broad; each implementation slice should have a bounded blast radius and a real user-visible outcome.
6. Reuse existing proven work when it still fits the new architecture. Do not preserve DMS-specific UI code merely because effort was spent on it, and do not discard valuable controller contracts/services/tests merely because the UI direction changed.
7. After roadmap reconciliation, follow through via the project's normal vertical-slice workflow. Avoid asking the owner to restate information already present in this pack or repository. Ask only when a genuine owner/product decision cannot be inferred or safely delegated.
8. Self-test implementation changes and fix ordinary implementation errors before returning. A shell that compiles or boots but loses essential visible controls/navigation is not a successful slice.
9. Owner/hardware acceptance gates remain owner-only. Do not self-approve an owner verdict.
10. Keep the recovery path intact while the new shell foundation is immature.

A concise rule for the whole project: **exhaustive roadmap, incremental implementation.**

## Required companion files

- `01_PRODUCT_DIRECTION.md` — product goals, non-goals, settled direction, and design philosophy.
- `02_CURRENT_REPOSITORY_STATE_AND_RECONCILIATION.md` — snapshot of the supplied repositories/docs and known architectural conflicts.
- `03_EXHAUSTIVE_REQUIREMENTS_INVENTORY.md` — organized inventory of the owner's requirements without hiding later work.
- `04_INPUT_CONTROLLER_KEYBOARD_NAVIGATION.md` — semantic input, focus, mappings, OSK, glyphs, and unresolved mapping questions.
- `05_SHELL_UI_SETTINGS_AND_PLUGIN_SURFACES.md` — Hearth Bar, launcher, workspaces, control center, Settings, apps, plugins, and shell behavior.
- `06_MD3E_MOTION_AND_REFERENCE_SHELLS.md` — expressive motion requirements and Caelestia/DMS/M3Shapes/Clavis reference strategy.
- `07_WALLPAPER_BACKGROUND_AND_AUTOCROP.md` — default background plugin, Waifu.im provider, settings, and deterministic U²-NetP crop pipeline.
- `08_HEARTH_PORTAL_AND_GAMING_MODE.md` — Portal, Gaming Mode integration, Decky future work, and existing GM concerns.
- `09_OPEN_QUESTIONS_AND_CONFLICTS.md` — deliberately unresolved items Codex should plan/reconcile rather than having this handoff decide.
- `10_ORIGINAL_PROMPT_VERBATIM.md` — the owner's original prompt/context exactly as supplied.
- `11_REFERENCES_AND_RESEARCH.md` — current external references and licensing/architecture notes to verify before reuse.

## Completion expectation for this handoff

Do not respond to this pack by reducing it to a tiny feature checklist. The first meaningful result should be a repository-aware reconciliation: update the durable documentation so the fourth-iteration product direction, future work, superseded assumptions, and reusable existing work are all represented. Then let the roadmap and status docs drive implementation in manageable slices. The owner wants fewer back-and-forth turns caused by forgotten context, not fewer documented requirements.
