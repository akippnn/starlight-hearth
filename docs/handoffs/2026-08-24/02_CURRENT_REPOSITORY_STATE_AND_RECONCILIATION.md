# Current Repository State and Reconciliation Targets

This file describes the supplied 2026-08-24 snapshot so Codex can spend fewer tokens rediscovering obvious mismatches. Verify the actual checked-out repositories before acting; this is context, not a substitute for inspection.

## Supplied snapshot

### `starlight-hearth`

Observed HEAD in the supplied bundle/worktree:

- `2e9cb45` — `build(shell): pin Hearth Shell 0.2.0`
- Branch lineage includes `codex/hs-003-controller-app-menu`.

The current docs use the multi-track identifiers:

- `HS` — Hearth Shell
- `AP` — Applications
- `GM` — Gaming Mode
- `BR` — inherited-base retirement

`docs/status.md` currently marks **HS-003 — Controller-Aware App Menu** active/in implementation and says the deployed HS-002 image remains the development baseline.

### `starlight-hearth-shell`

Observed HEAD in the supplied bundle/worktree:

- `e7745a67` — `docs(delivery): migrate shell slices to HS track`
- Tag: `hearth-v0.2.0`

The current HS-003 branch contains potentially reusable work such as:

- Rust controller service under `controller/`.
- D-Bus API and contract tests.
- InputPlumber integration and a versioned controller manifest.
- `HearthControllerContext.qml`, `HearthControllerHint.qml`, `HearthFocusGraph.qml`, `HearthLayoutPolicy.qml`.
- Controller-aware launcher work.
- Controller Layout Settings work.
- Hearth OSK work.
- RPM/systemd/release packaging and cross-repository contract tests.

Do not assume every item should survive unchanged. Distinguish reusable contracts/primitives from UI code coupled to the DMS component hierarchy.

## Current documented assumptions that now require reconciliation

### ADR-0002

`docs/decisions/0002-hearth-shell-and-input-ownership.md` currently says `starlight-hearth-shell` is a history-preserving DMS fork, that Hearth Shell is the maintained DMS-derived product, and that there is no independent replacement-shell/DMS-retirement track.

That product assumption is stale relative to the later owner decision. Preserve the ADR as historical evidence and supersede it cleanly where necessary.

### ADR-0003

`docs/decisions/0003-semantic-controller-routing.md` retains the DMS-derived-product decision while introducing the semantic controller service. The **semantic input architecture may remain valuable even though the DMS-product assumption no longer does**. Separate those concerns instead of throwing away the whole ADR indiscriminately.

### Current roadmap maintenance gate

`docs/roadmap.md` currently says to replay upstream DMS after HS-003/HS-004 and start a clean Quickshell UI only if a merge-cost threshold is exceeded. The owner has now explicitly stated that **the threshold has been crossed**, based primarily on architectural/interaction mismatch: continuing somebody else's shell means inheriting decisions made for a desktop that was not designed for Hearth's keyboard+controller navigation model.

Document that change rather than re-running the old question as if no decision had been made.

### HS-004 and later DMS-shaped surface names

The current roadmap still includes concepts such as “Dank Bar and Hearth Quick Menu.” The new product language describes a Hearth-native **Hearth Bar**, new launcher/control-center behavior, and a custom shell. Do not merely rename symbols without checking whether the old DMS-specific implementation assumptions should be carried over.

### AP ordering

The current roadmap places Hearth Portal after broad shell coverage. The owner's newer prompt treats **Hearth Settings and Hearth Portal as the first two Hearth-native applications** and wants some Hearth applications available in Gaming Mode. Reconcile ordering/dependencies instead of assuming the old AP-001 position is still correct.

### GM ordering

The current roadmap begins GM with shader-compilation responsiveness, then latency, then Decky baseline. The owner's newer direction says early Gaming Mode work should include Hearth Portal/other Hearth apps, followed later by a Hearth-owned Decky plugin and shared features such as wallpapers. Existing shader/latency concerns must not disappear; they may need reprioritization or different slice numbering.

Do not decide the final GM order in this handoff; make the conflict explicit and plan it in the repository.

## Important runtime failure observed by the owner

A previous candidate **booted but left the shell effectively unusable**: expected visible controls were absent, the app menu could not be opened, and the owner had to use `ujust hearth-recovery-kde` to recover/inspect the system.

This changes the acceptance mindset:

- “Booted” is not equivalent to “shell works.”
- A build that removes the path to essential shell controls is a failed candidate.
- Preserve recovery during the migration.
- Add smoke/integration checks appropriate to the new shell foundation, not just source-level assertions.

## Existing semantic controller baseline to inspect

The supplied `controller-layout-v3.json` already models semantic events and glyph families for Xbox/PlayStation/Nintendo/generic controllers, including Menu/View/Guide, L3/R3 modifiers, focus directions, accept/back/action/context, group navigation, pointer routing, and scroll routing.

However, the owner's newer ideas include changes such as shoulder-button clicking and trigger-based panel/workspace navigation, plus Guide/right-stick media controls. Treat the current v3 mapping as **valuable implementation evidence and a baseline**, not automatically the final mapping.

## Reconciliation requirement

The roadmap/doc repair should answer, in repository form:

- Which current decisions are still valid as-is?
- Which decisions are still valid only in part?
- Which are explicitly superseded?
- Which current code/contracts should be retained and generalized?
- Which QML is DMS-coupled and should be replaced instead of further patched?
- Which existing tests describe enduring Hearth behavior and should be carried into the new shell?
- How should the new custom-shell foundation be sliced so owner-visible usability is never lost for long stretches?

Preserve evidence. Do not rewrite history to make the new direction look like it was always the plan.
