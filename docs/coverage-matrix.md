# Handoff coverage matrix

**Source package:** `docs/handoffs/2026-08-24/`
**Coverage date:** 2026-08-28

Every handoff section is routed below to a canonical requirement, decision,
behavior contract, roadmap entry, or explicit open question. The archive
retains exact wording; this matrix prevents a later summary from silently
dropping it.

| Archived source | Sections covered | Canonical destinations |
| --- | --- | --- |
| `00_MASTER_PROMPT.md` | How to use; authority; planning/delivery; companion files; completion expectation | `product-direction.md`, `requirements.md`, ADR-0008, `roadmap.md`, `status.md` |
| `01_PRODUCT_DIRECTION.md` | Product identity; shell direction; input; visual identity; configuration; documentation; Gaming Mode; references | `product-direction.md`, `architecture.md`, `requirements.md`, ADR-0006/0007/0008 |
| `02_CURRENT_REPOSITORY_STATE_AND_RECONCILIATION.md` | Supplied repositories; ADR conflicts; roadmap gates; AP/GM ordering; runtime failure; controller baseline; reconciliation | `repository-reconciliation.md`, `architecture.md`, ADR-0006/0007/0008, `identifier-migration.md`, `roadmap.md`, `status.md`, `reuse-ledger.md` |
| `03_EXHAUSTIVE_REQUIREMENTS_INVENTORY.md` | A–Q: architecture; input; Controller Settings; old mappings; OSK; Bar; App Menu; workspaces; control center; Settings; apps; design; plugins; wallpaper; Gaming Mode; Steam-like controls; documentation | `requirements.md`, all five behavior contracts, `open-questions.md`, `roadmap.md` |
| `04_INPUT_CONTROLLER_KEYBOARD_NAVIGATION.md` | Core model; focus; semantic vocabulary; glyphs; existing/new mappings; launcher; OSK; external apps; latency | `contracts/input-navigation.md`, `contracts/app-menu.md`, `contracts/osk.md`, `requirements.md`, `open-questions.md` |
| `05_SHELL_UI_SETTINGS_AND_PLUGIN_SURFACES.md` | Bar; App Menu; workspaces; clock; control center/notifications; overlay; Settings; attribution; apps; plugins | `contracts/system-bar.md`, `contracts/app-menu.md`, `requirements.md`, `open-questions.md`, `roadmap.md` |
| `06_MD3E_MOTION_AND_REFERENCE_SHELLS.md` | Motion requirement; central system; Caelestia; DMS; M3Shapes; Clavis; niri ports; licensing | `product-direction.md`, `requirements.md`, ADR-0006, `reuse-ledger.md`, `open-questions.md` |
| `07_WALLPAPER_BACKGROUND_AND_AUTOCROP.md` | Historical online-provider, metadata, model, crop, orientation, performance, and Gaming Mode proposals | `requirements.md` (`WALL-*` local HWP-001 boundary), `open-questions.md` (`OQ-050`–`OQ-052` later outcomes), `reuse-ledger.md`, `roadmap.md` |
| `08_HEARTH_PORTAL_AND_GAMING_MODE.md` | Portal; same app/different context; controller behavior; existing GM concerns; Decky; track independence | `requirements.md` (`PORTAL-*`, `GM-REQ-*`), `open-questions.md`, `roadmap.md` |
| `09_OPEN_QUESTIONS_AND_CONFLICTS.md` | Questions 1–20: mappings; modifiers; placement; focus; keyboard; config; services; donors; plugins; wallpaper; Portal; GM; notifications; desktop scope | Resolved choices in ADR-0006/0007 and behavior contracts; unresolved choices in `open-questions.md` |
| `10_ORIGINAL_PROMPT_VERBATIM.md` | Complete original owner prompt and immediate context | Preserved verbatim; normalized into `requirements.md`, behavior contracts, `roadmap.md`, and `open-questions.md` |
| `11_REFERENCES_AND_RESEARCH.md` | Caelestia; DMS; M3Shapes; Clavis; niri port; Quickshell; historical wallpaper-model/provider research; licensing | `reuse-ledger.md`, ADR-0006/0007, `requirements.md`, `open-questions.md` |
| `12_PACKAGE_MANIFEST.md` | Package membership and handoff integrity | Handoff `INDEX.md` and this matrix |
| `README.md` | Recommended use; file index; source material | Handoff `INDEX.md`, root `README.md`, and this matrix |

## Later explicit decisions covered

| Decision cluster | Canonical destination |
| --- | --- |
| GPLv3 governance and maximal compatible reuse | ADR-0006, `reuse-ledger.md`, `requirements.md` |
| Clean Hearth-native history and hard DMS runtime rename | ADR-0006, `architecture.md`, `open-questions.md` |
| Rust companion, layered JSON, transient launches | ADR-0007, `architecture.md` |
| Grid/List only, west face, `Ctrl+1`/`Ctrl+2`, drawer/tabs/index/recents | `contracts/app-menu.md`, `requirements.md` |
| Navigation/Text modes and current semantic mappings | `contracts/input-navigation.md` |
| wvkbd fork, Wayland protocols, layout, privacy, controller behavior | `contracts/osk.md`, ADR-0007 |
| System Bar visible on hover/focus/owned-panel, edge span, 250 ms grace, focus return | `contracts/system-bar.md`, `requirements.md` |
| Dolphin retained and Index/MauiKit contingency | `contracts/file-manager-contingency.md`, `requirements.md` |
| Foundation documentation before frozen slice contracts | ADR-0008, `status.md`, `roadmap.md` |
