# MD3 Expressive Motion and Reference Shells

## The requirement is motion, not just Material styling

“MD3E” must not collapse into rounded rectangles, Material colors, and generic 200 ms fades. The owner specifically likes how lively Material 3 Expressive interactions feel, especially button interactions and state changes.

Treat motion as part of the Hearth design system alongside color, typography, shape, elevation, iconography, and spacing.

Desired interaction character includes:

- visibly responsive hover/focus/press/release states;
- coordinated scale/compression and spring-back where appropriate;
- shape morphing rather than only color swaps;
- expressive state layers/ripple behavior;
- elevation/shadow changes tied to interaction;
- icons that can change fill/weight/state smoothly where the chosen icon technology supports it;
- selection indicators that can move/morph between related controls instead of being destroyed/recreated with a hard cut;
- panels/cards/widgets that reshape as they expand/collapse;
- directional transitions that reflect navigation direction where useful;
- blur/dim transitions coordinated with the originating bar item and opened surface;
- strong controller focus feedback that feels as intentional as mouse hover;
- keyboard activation driving the same semantic visual pressed/activated state as mouse/controller activation.

The default Hearth experience should be intentionally lively. Include reduced-motion/accessibility support, but do not make the normal motion language timid simply because a reduced-motion path exists.

## Central motion system

Codex should strongly consider a shared motion/token layer instead of arbitrary animation constants inside individual components. The exact implementation is open, but the design system should be able to express concepts such as:

- fast/default/slow effects transitions;
- fast/default/slow spatial transitions;
- emphasized easing;
- spring parameters;
- deformation/morph strength;
- state-layer/ripple behavior;
- reduced-motion policy;
- theme-aware motion where relevant.

Prefer Qt Quick/QML animation primitives and GPU-friendly animations over timer-driven JavaScript or manual frame stepping. Evaluate `Behavior`, `Transition`, `NumberAnimation`, `PropertyAnimation`, `ColorAnimation`, `SpringAnimation`, `SmoothedAnimation`, parallel/sequential animation groups, animators, and shader-based effects where appropriate.

## Caelestia Shell — primary visual/motion reference

Current upstream: `https://github.com/caelestia-dots/shell`

Why it matters:

- Quickshell/QML shell with a deliberately fluid/morphing visual identity.
- Strong match to the owner's desired MD3E feeling.
- Existing component/module/service organization can be studied.
- Current build integrates M3Shapes.
- Useful reference for motion abstractions, shape morphing, animated surfaces, theme changes, and button interaction quality.

Important architectural caution:

- Upstream Caelestia is currently built around **Hyprland** and its own CLI/integration assumptions.
- Do not assume it is a drop-in niri/Hearth foundation merely because the QML looks right.
- Do not automatically decide to fork it or reject it. Inspect where its compositor assumptions live and compare the cost of selective reuse, porting, or independent Hearth components.
- Direct reuse has licensing implications; upstream Caelestia Shell is GPL-3.0 as of this handoff. Re-verify before copying code.

## DMS — niri/system integration and additional MD3E reference

Current upstream: `https://github.com/AvengeMedia/DankMaterialShell`

Why it still matters even though the downstream product path is ended:

- Mature Quickshell shell with niri support and many system integrations.
- Existing DMS architecture can show how audio/network/Bluetooth/process/notification/system-tray/etc. integration is handled in QML + native/backend services.
- Recent DMS work has explicitly moved toward Material 3 Expressive-inspired animation and can be studied for proven QML interaction patterns.
- The supplied Hearth fork already contains useful DMS-derived/system integration code and Hearth controller work.

Do not resume the old strategy of endlessly patching DMS to become Hearth. Use it as a reference/source of deliberately selected implementation pieces when appropriate.

DMS upstream is MIT-licensed as of this handoff; re-verify specific files/submodules before copying.

## M3Shapes — candidate native QML dependency

Repository: `https://github.com/soramanew/m3shapes`

Caelestia currently pins/builds M3Shapes as a native QML module for Material 3 Expressive shape/morph behavior. It is a strong candidate to evaluate for Hearth rather than reimplementing all expressive shape geometry from scratch.

Available reference projects identify M3Shapes as Apache-2.0. Re-verify the exact revision/license before adopting it.

Do not force adoption solely because this handoff likes it; assess Fedora/Bazzite packaging, ABI/build integration, performance, maintenance, and whether Hearth needs a wrapper/design-token layer around it.

## Clavis — useful niri existence proof/reference

Repository: `https://github.com/StatIndet/quickshell`

Clavis describes itself as a niri shell built with Quickshell/QML/Qt 6/native modules and explicitly acknowledges/reference-integrates ideas/components from DMS, Caelestia, `qml-niri`, and M3Shapes. It is useful evidence that the “Caelestia-like expressive QML + niri integration + independent shell” direction is technically plausible.

Do not automatically fork Clavis either. Inspect it for architectural lessons, niri models, Material-shape integration, and licensing practices.

## Niri Caelestia ports

Community ports such as `jutraim/niri-caelestia-shell` can be inspected specifically to learn where Caelestia's Hyprland assumptions need replacement. They are reference material, not automatically trustworthy foundations.

## Reuse and licensing rule

Before directly copying/adapting source, assets, shaders, fonts, icons, or modules:

1. identify the exact upstream file/revision;
2. verify its license and attribution requirements;
3. document the dependency/reuse in the repository;
4. avoid accidentally imposing a licensing model on Hearth through copied GPL code without an explicit project-level decision;
5. prefer independent implementation from documented behavior/design ideas when direct copying is not appropriate.

This handoff deliberately does **not** decide how much Caelestia/DMS/Clavis code should be reused. Codex should plan that after inspecting the actual code and project licensing goals.
