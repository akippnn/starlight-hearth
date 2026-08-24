# hearthOS / Hearth Shell Codex Handoff Pack — 2026-08-24

This pack converts the owner's fourth-iteration shell prompt plus the follow-up design/architecture discussion into durable Codex input without intentionally hiding future requirements.

## Recommended use

Place or otherwise make the whole pack available to Codex, then give it `00_MASTER_PROMPT.md` as the entry prompt. The master file tells Codex to read the remaining files before reconciling `docs/` and planning the next vertical slices.

The key operating rule is:

> **Exhaustive roadmap, incremental implementation.**

The pack deliberately does **not** settle every engineering decision. `09_OPEN_QUESTIONS_AND_CONFLICTS.md` separates known ambiguities from settled product direction so Codex can plan them without re-deriving the entire week of discussion.

## Files

1. `00_MASTER_PROMPT.md` — entry prompt and agent behavior.
2. `01_PRODUCT_DIRECTION.md` — product identity and settled high-level direction.
3. `02_CURRENT_REPOSITORY_STATE_AND_RECONCILIATION.md` — supplied repo/doc snapshot and stale assumptions.
4. `03_EXHAUSTIVE_REQUIREMENTS_INVENTORY.md` — complete organized requirement inventory.
5. `04_INPUT_CONTROLLER_KEYBOARD_NAVIGATION.md` — input/focus/controller/keyboard details.
6. `05_SHELL_UI_SETTINGS_AND_PLUGIN_SURFACES.md` — Hearth Bar, launcher, Settings, plugins, first-party apps.
7. `06_MD3E_MOTION_AND_REFERENCE_SHELLS.md` — expressive motion and reference implementation research.
8. `07_WALLPAPER_BACKGROUND_AND_AUTOCROP.md` — wallpaper plugin, Waifu.im, U²-NetP crop pipeline.
9. `08_HEARTH_PORTAL_AND_GAMING_MODE.md` — Portal and GM direction.
10. `09_OPEN_QUESTIONS_AND_CONFLICTS.md` — intentionally unresolved planning items.
11. `10_ORIGINAL_PROMPT_VERBATIM.md` — exact original owner prompt/context.
12. `11_REFERENCES_AND_RESEARCH.md` — external technical references and license cautions.

## Source material used

- Owner's original pasted prompt/context.
- `docs.zip` supplied in the conversation.
- `starlight-hearth-20260824-222153(1).bundle`.
- `starlight-hearth-shell-20260824-222319.bundle`.
- Follow-up conversation covering Waifu.im, U²-NetP deterministic cropping, shell plugin/settings integration, Gaming Mode future Decky work, MD3E motion, Caelestia, DMS, M3Shapes, and Clavis.
- Current public documentation/reference checks performed on 2026-08-24.
