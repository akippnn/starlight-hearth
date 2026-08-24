# References and Research Notes — Verify Before Direct Reuse

These are current reference points gathered during the planning discussion. They are provided to reduce rediscovery cost, not to substitute for fresh repository inspection when implementation begins.

## Caelestia Shell

- Repository: https://github.com/caelestia-dots/shell
- Current project description: a fluid/morphing Quickshell/QML desktop shell.
- Current README identifies Hyprland as its window manager/integration target.
- Current upstream license: GPL-3.0.
- Current CMake build can fetch/build M3Shapes as a QML module.
- Current upstream niri-support request history includes closed/not-planned requests; treat compositor coupling as something to audit rather than assuming a trivial port.

Use it primarily to study:

- motion abstractions;
- MD3E interaction quality;
- shape morphing;
- component composition;
- animated states/elevation;
- Material theming;
- plugin/background architecture where useful.

Do not copy GPL code into a differently licensed Hearth project without an explicit licensing decision.

## DankMaterialShell (DMS)

- Repository: https://github.com/AvengeMedia/DankMaterialShell
- Quickshell/QML + Go shell/backend architecture.
- Explicitly supports/optimizes for niri among other Wayland compositors.
- Upstream license: MIT.
- Mature references for network, audio, notifications, processes, system tray, launcher, plugins, niri integration, and desktop services.
- Recent project direction includes Material/expressive animation work worth studying.

Hearth is no longer continuing DMS as its product foundation, but the implementation remains valuable reference material.

## M3Shapes

- Repository: https://github.com/soramanew/m3shapes
- Caelestia currently pins it in its build for Material 3 Expressive shapes/morphing.
- Reference projects list it as Apache-2.0.

Re-verify the exact pinned revision and license before adopting.

## Clavis Shell

- Repository: https://github.com/StatIndet/quickshell
- Describes itself as a niri shell using Quickshell/QML/Qt 6/native modules.
- Explicitly acknowledges/integrates inspiration or components from DMS, Caelestia, `qml-niri`, M3Shapes, and others.
- Useful reference for independent niri shell architecture and third-party-license bookkeeping.
- Current repository license shown by GitHub: GPL-3.0; copied components retain their own notices.

## Community niri Caelestia port

- Example: https://github.com/jutraim/niri-caelestia-shell

Use this type of project to identify practical Hyprland→niri integration replacement points. Do not assume community ports meet Hearth's maintenance/security/quality requirements.

## Quickshell

- Documentation: https://quickshell.org/

When Codex works in QML/Quickshell, consult actual installed/current APIs and working upstream examples. Do not infer APIs from generic Qt/QML knowledge when a Quickshell type/IPC/compositor integration detail is uncertain.

## U²-Net / U²-NetP

- Official repository: https://github.com/xuebinqin/U-2-Net
- Task: salient object detection.
- Official README/reference code describes `u2netp` as the small ~4.7 MB model.
- Reference inference resizes inputs to ~320 px.
- Repository license: Apache-2.0.

Hearth intends to use U²-NetP only to estimate saliency/subject regions; deterministic Hearth code selects the crop.

Before shipping an ONNX model, identify the exact conversion/model artifact, source revision, model license, checksum, input normalization, tensor shape, output semantics, and runtime dependency. Do not download an arbitrary third-party ONNX blob at runtime without provenance.

## Waifu.im

- API documentation: https://docs.waifu.im/
- API base: https://api.waifu.im
- Current docs state basic image fetching does not require authentication.
- Current API version at time of research: `v7`.
- Production integration should use the `Accept-Version` header and have an upgrade plan.
- `/images` supports image browsing/filtering.
- `/tags` lists tags.
- Current tag semantics:
  - repeated `IncludedTags` = AND;
  - repeated `ExcludedTags` = OR;
  - `IsNsfw=False` is the SFW default;
  - `IsNsfw=True` is NSFW only;
  - `IsNsfw=All` includes both.
- `oppai` is a real accepted tag and can appear on SFW images, which is why it is explicitly excluded from Hearth's conservative default.

Use an HTTP library/query builder rather than hand-concatenating/over-encoding query strings.

## Licensing note

Do not rely on this handoff as legal advice. Before direct reuse, re-open the exact upstream license, inspect per-file/submodule notices, and record attribution/reuse in Hearth's repository. Design inspiration and independent implementation are different from copying source code.
