# Reuse, licensing, and provenance ledger

**License direction:** hearthOS Shell `GPL-3.0-only`
**Ledger state:** HSN-001 imports packaged in RC.1; HSN-002 Blob subset proposed only
**Last reconciled:** 2026-08-29

Design inspiration is not source reuse. Before copying source, assets, shaders,
fonts, icons, models, or generated artifacts, record the exact upstream object,
license, local modifications, notice obligations, and destination.

## Researched donors

| Project | Inspected revision | License observed | Planning disposition |
| --- | --- | --- | --- |
| Clavis | `8a7b1989d8995bd49a0b00cf9c19650f22d54d7b` | GPLv3 | Primary niri-native architecture donor; exact imports remain open. |
| Caelestia Shell | `1d0e5a588c61f1d905eba5fe8446ec222d37f50c` | GPL-3.0 | Primary motion/visual donor; Hyprland assumptions prevent wholesale adoption. |
| DMS / current shell history | Hearth shell `origin/main` inspected at `16ee3a209396caba209c8604fb70eeb8ca182f7f` | Upstream MIT; submodules/files require recheck | Select system/niri services and existing Hearth work only; not the target architecture. |
| M3Shapes | `bdc327b29f95394a732baf3c9b19658ba23755b6` | Apache-2.0 | HSN-001 dependency pin inherited from the selected Caelestia build; expose only through Hearth card wrappers. |
| Caelestia CLI | `d512bc1e3607c52c5e1fb4477b9c7f31d9216760` | Verify per file | Candidate service/config patterns; no import selected. |
| wvkbd | `6b41504a0cb58fd1163fa44692398fbd61f8905f` (`v0.20`) | GPLv3 core; MIT/X compatibility files and MIT `wld` notices | Accepted OSK fork base; no fork created in this phase. |
| niri | `8ed0da44d974c32c6877d2f4630c314da0717ecb` (`v26.04`) | GPL-3.0 | Upstream compositor and protocol behavior reference; remain unmodified. |
| Smithay | `ff5fa7df392cecfba049ffed55cdaa4e98a8e7ef` | Verify exact crates/files | Protocol implementation reference used by inspected niri. |
| Plasma Keyboard | `6d64d99b7fc0500ac21db84e75b1fc222d326db3` | KDE per-file licenses | Rejected as unchanged base because inspected code uses input-method-v1 rather than niri's v2 path. |
| Index | Research snapshot `ebb31be…`; exact full revision must be repinned if activated | GPLv3 | File-manager contingency only. |
| MauiKit FileBrowsing | `4c51bff2e8b106501cd67fc6ff5b907068c14cd7` | Mixed per-file, predominantly LGPL | Candidate dependency for the Index contingency. |
| COSMIC Files | `7cebbef82f59a5fc020e4bcb369abc542e5e1cd6` | Verify exact files before use | Reference only; not selected as the contingency base. |
| U²-Net / U²-NetP | Exact model/conversion artifact not selected | Official source Apache-2.0 | Historical research input only; HWP-001 uses deterministic center crop. Any model-based saliency belongs to a later proposed outcome with fresh provenance and license review. |

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

## HSN-001 selected import boundary

| Upstream | Exact identity | Selected source surface | Excluded surface | Required notice |
| --- | --- | --- | --- | --- |
| Caelestia Shell | `1d0e5a588c61f1d905eba5fe8446ec222d37f50c` | animation/CAnim, state layer, button, variable Material icon, typography/font builder, motion/rounding tokens | Hyprland services, Caelestia product shell, Blob engine | GPL-3.0 source attribution and adaptation ledger |
| M3Shapes | `bdc327b29f95394a732baf3c9b19658ba23755b6` | native shape dependency behind Hearth wrappers | direct QML product API and unrelated examples | Apache-2.0 LICENSE/NOTICE preservation |
| Google Sans Flex | Caelestia `1d0e5a588c61f1d905eba5fe8446ec222d37f50c`; asset SHA-256 `2510a8b7a24beb1fe8163e9a49813ccfe96b5453444b9443d42665ca4fa320c9` | pinned typeface asset | mutable font download | OFL-1.1 text and reserved-name compliance |
| Material Symbols Rounded | npm `material-symbols@0.46.0`; archive SHA-256 `f8511ad410460f345c7f9dbb2467da9dae982d949c77dca8ef3508f54bad6017` | pinned Rounded variable icon font | mutable font download | Apache-2.0 license/notice |
| Hearth controller glyphs | original HSN-001 QML | face/control glyphs | donor product glyph set | GPL-3.0-only project source |

Historical candidate `e7745a672edc868f693826cf3c1f9cd5f7128deb` may supply only
reviewed Rust routing/focus logic and tests. Its DMS launcher UI and
`org.starlight.HearthShell.Controller1` wire contract are explicitly excluded.

## Proposed HSN-002 Blob boundary

No Blob source has been imported by this documentation reconciliation. If the
HSN-002 contract is approved, frozen, and separately authorized, the maximum
direct-import set is pinned to Caelestia Shell
`1d0e5a588c61f1d905eba5fe8446ec222d37f50c`:

- `plugin/src/Caelestia/Blobs/blobgroup.hpp` and `.cpp`;
- `blobshape.hpp` and `.cpp`;
- `blobrect.hpp` and `.cpp`;
- `blobmaterial.hpp` and `.cpp`;
- `shaders/blob.vert` and `shaders/blob.frag`.

Each adapted file must carry `GPL-3.0-only` SPDX identification, the upstream
project, exact commit and source path, and a concise adaptation note. Packaged
GPL notices must identify the same files. The adaptation removes inverted-rect
support and unrelated module dependencies and is bounded to the App Menu
content↔index-overview transition. `BlobPopup.qml`, `BlobInvertedRect`,
Hyprland-specific services, the Caelestia product shell, continuously animated
effects, and all unrelated Blob consumers remain excluded.

## Shared-component rule

HSN-001 and pre-HSN implementation may be reused only after contract and
license review. HIN-001 owns shared headless semantic input state; HSN-002 is
planned to deliver the one reusable `InputHintBar` and `CollectionBrowser`;
HIN-002 must consume the same hint component. Later OSK/Text Mode, System Bar,
Settings, Portal, and plugin surfaces improve those primitives instead of
creating behaviorally duplicate private components. Reuse never transfers
evidence or an owner verdict between outcomes.
