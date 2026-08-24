# Reuse, licensing, and provenance ledger

**License direction:** Hearth Shell `GPL-3.0-only`
**Ledger state:** research candidates only; no donor source imported by this documentation change
**Last reconciled:** 2026-08-25

Design inspiration is not source reuse. Before copying source, assets, shaders,
fonts, icons, models, or generated artifacts, record the exact upstream object,
license, local modifications, notice obligations, and destination.

## Researched donors

| Project | Inspected revision | License observed | Planning disposition |
| --- | --- | --- | --- |
| Clavis | `8a7b1989d8995bd49a0b00cf9c19650f22d54d7b` | GPLv3 | Primary niri-native architecture donor; exact imports remain open. |
| Caelestia Shell | `1d0e5a588c61f1d905eba5fe8446ec222d37f50c` | GPL-3.0 | Primary motion/visual donor; Hyprland assumptions prevent wholesale adoption. |
| DMS / current shell history | Hearth shell `origin/main` inspected at `16ee3a209396caba209c8604fb70eeb8ca182f7f` | Upstream MIT; submodules/files require recheck | Select system/niri services and existing Hearth work only; not the target architecture. |
| M3Shapes | `6875533e1b459cd096e2250f54ceaad5290afc49` | Apache-2.0 | Leading expressive shape/morph candidate pending packaging and performance evaluation. |
| Caelestia CLI | `d512bc1e3607c52c5e1fb4477b9c7f31d9216760` | Verify per file | Candidate service/config patterns; no import selected. |
| wvkbd | `6b41504a0cb58fd1163fa44692398fbd61f8905f` (`v0.20`) | GPLv3 core; MIT/X compatibility files and MIT `wld` notices | Accepted OSK fork base; no fork created in this phase. |
| niri | `8ed0da44d974c32c6877d2f4630c314da0717ecb` (`v26.04`) | GPL-3.0 | Upstream compositor and protocol behavior reference; remain unmodified. |
| Smithay | `ff5fa7df392cecfba049ffed55cdaa4e98a8e7ef` | Verify exact crates/files | Protocol implementation reference used by inspected niri. |
| Plasma Keyboard | `6d64d99b7fc0500ac21db84e75b1fc222d326db3` | KDE per-file licenses | Rejected as unchanged base because inspected code uses input-method-v1 rather than niri's v2 path. |
| Index | Research snapshot `ebb31be…`; exact full revision must be repinned if activated | GPLv3 | File-manager contingency only. |
| MauiKit FileBrowsing | `4c51bff2e8b106501cd67fc6ff5b907068c14cd7` | Mixed per-file, predominantly LGPL | Candidate dependency for the Index contingency. |
| COSMIC Files | `7cebbef82f59a5fc020e4bcb369abc542e5e1cd6` | Verify exact files before use | Reference only; not selected as the contingency base. |
| U²-Net / U²-NetP | Exact model/conversion artifact not yet selected | Official source Apache-2.0 | Accepted saliency approach; model provenance/checksum remain open. |

## Required import record

Every future direct import adds one row before integration:

| Field | Required value |
| --- | --- |
| Upstream project and URL | Canonical repository/resource |
| Exact source identity | Full commit, tag, artifact digest, and submodule state |
| Source paths | Every imported file/module/asset/model |
| License | Exact file and project terms plus compatibility conclusion |
| Hearth destination | Repository and path |
| Transformation | Copied, adapted, generated, wrapped, or linked dependency |
| Local changes | Behavioral and structural changes |
| Notices | Required copyright/license attribution location |
| Verification | Build/test/visual/protocol evidence and limitations |

The archived handoff Markdown is owner-supplied project documentation, not a
third-party code import. Its checksums live in
`docs/handoffs/2026-08-24/INDEX.md`.
