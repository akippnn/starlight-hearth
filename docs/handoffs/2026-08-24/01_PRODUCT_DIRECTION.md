# Product Direction — hearthOS and Hearth Shell

## Product identity

hearthOS is primarily a living-room gaming operating system, not a conventional general-purpose desktop distribution whose desktop happens to support a controller. Gaming Mode remains important, but Hearth Desktop/Hearth Shell should become good enough to be a credible alternative surface rather than merely an emergency configuration screen.

The desktop does not need to reproduce every traditional Linux desktop feature immediately. It **does** need to be usable enough with a controller and with mouse+keyboard that routine operation does not require another laptop over SSH. SSH remains a useful power-user/development path, not the expected way to compensate for an unusable local shell.

The longer-term opportunity is broader than controller support: the same semantic focus/navigation work that makes a desktop usable from a controller can also make it unusually good for keyboard-heavy users who prefer predictable shortcuts and Vim-like navigation. Avoid treating keyboard accessibility as an afterthought.

## Settled shell direction

- Target a Hearth-native shell built with **Quickshell/QML** on **niri**.
- niri remains the compositor; shell UX should not casually leak compositor responsibilities into the shell.
- The previous DMS-derived product path has crossed its maintenance/replacement threshold because Hearth needs architectural ownership of focus, navigation, input semantics, hints, shell surfaces, and application integration.
- Keep DMS installed/available as a reference and inspiration source. Existing DMS integration work may still be valuable, especially niri/system integration and selected MD3E animation work, but DMS is no longer the architectural destination.
- Preserve useful proven work from the current repositories where it remains compatible with the new shell direction.
- Do not substitute a web-app shell, Electron, React, HTML, WebView, or localhost frontend for native Quickshell/QML UI.

## Input philosophy

Mouse, physical keyboard, and controller are first-class peers. Controller navigation must not be implemented by globally translating buttons into fake keyboard keys. Physical keyboard events must continue to work independently. Hearth-native surfaces should operate on semantic actions and predictable focus graphs so controller and keyboard navigation can share behavior without one impersonating the other.

## Visual identity

Use **Material 3 Expressive (MD3E)** as an actual interaction/motion language, not merely a palette and rounded-corner style. The owner specifically values the lively button interactions, morphing shapes, responsive press/release states, animated focus, expressive transitions, and high visual variety associated with MD3E and Caelestia Shell.

High-quality iconography, controller glyphs, typography, motion, state transitions, and coherent shell-wide theming are product requirements. Avoid the stereotypical low-variety “vibecoded shell” look where every surface is the same rounded card with generic fades.

## Configuration philosophy

Hearth Shell needs a coherent configuration standard and a Settings application that edits it. Do not scatter unrelated persistence formats through individual QML components. Non-default shell settings should be represented in the configuration model, and changes should be observed/applied automatically where practical. The exact configuration format and service architecture are planning decisions for Codex/repository ADRs rather than decisions made in this handoff.

## Documentation philosophy

`starlight-hearth` remains the durable top-level product documentation location for shell-visible behavior, controller layout, roadmap/status, Gaming Mode, applications, base retirement, and cross-repository contracts. `starlight-hearth-shell` should carry the implementation-facing shell documentation it needs as well. Keep the two synchronized where contracts cross repository boundaries.

Future features should be documented even when not yet implemented. Do not make the roadmap artificially narrow to simplify the current coding turn.

## Gaming Mode philosophy

Gaming Mode is an independent product track, not an afterthought and not something that should block an otherwise valid shell slice. Selected Hearth applications/features should eventually be available naturally in Gaming Mode without maintaining separate duplicate application instances. Future GM work includes a Hearth-owned Decky plugin and shared wallpaper/background functionality, but those should be planned as GM vertical slices rather than quietly embedded in shell work.

## Reference philosophy

Caelestia Shell is currently the closest visual/motion reference to the desired feeling. DMS remains useful for mature niri/system integration and its own recent Material/animation work. M3Shapes and other QML implementations are candidates for direct dependency/reuse if technically and legally appropriate. Clavis and niri ports of Caelestia are useful existence proofs/reference material. **Do not assume from this document alone that Hearth must fork or directly copy any of them.** Inspect architecture and licenses and decide deliberately in the roadmap/ADR process.
