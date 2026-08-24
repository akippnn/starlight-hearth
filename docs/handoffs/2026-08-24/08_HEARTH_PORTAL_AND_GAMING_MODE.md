# Hearth Portal and Gaming Mode Direction

## Hearth Portal

Hearth Portal remains an important first-party application and must not disappear while shell work is reorganized.

Product intent from the owner:

- Hearth Portal is Hearth's take on Bazzite Portal, presented through Hearth's MD3E/controller-first UI.
- It should stay maintainable against Bazzite rather than hard-copying a moving action catalog and diverging forever.
- Prefer an adapter/override model where Hearth can retain compatible upstream actions, replace/override entries when hearthOS needs differ, add Hearth-specific entries, and hide/remove incompatible entries deliberately.
- Do not let arbitrary QML strings become privileged commands; preserve typed/safe action boundaries from the current Portal planning where still appropriate.
- It should be controller-native and keyboard-native.
- It may become a management surface for games and gaming-adjacent tweaks.
- If a tweak requires Steam to restart, Portal should detect/communicate that and use an appropriate safe mechanism to restart Desktop Steam or Gaming Mode Steam as applicable.
- Explore whether Portal can replace Decky-Framegen's UI and perhaps reduce the need for ProtonPlus; do not assume ProtonTricks can or should be replaced.
- Add appropriate controller-adjacent Hearth apps/tools into Steam so they can be launched naturally from Gaming Mode.

The older prompt references a prior “Fix Bazzite app roadmap” discussion that is not included in this pack. Codex should inspect repository docs/history for any surviving Portal requirements before declaring the Portal plan complete. Do not invent missing details if they are not present.

## Same app, different context

Where practical, Hearth applications should not be duplicated into separate Desktop and Gaming Mode installations.

Desired behavior:

- same installed application can be registered as a Steam/Non-Steam entry;
- application can detect/receive enough launch/session context to adapt controller navigation, scaling, window behavior, or restart handling;
- core settings/state remain shared where appropriate;
- UI remains MD3E/Hearth rather than becoming a completely unrelated Gaming Mode theme.

Exact context-detection/launch contracts are planning decisions.

## Gaming Mode controller behavior

The owner wants Desktop controls to feel familiar to Gaming Mode and wants Gaming Mode behavior verified rather than guessed.

Specific ideas to investigate:

- right stick pointer on Hearth Desktop;
- Guide + vertical right stick for volume;
- whether Guide + horizontal right stick should map to brightness and whether Steam already behaves that way;
- shoulder buttons for clicking;
- triggers for panel/workspace/category navigation on Desktop.

Do not copy Steam's bindings from memory. Inspect current Steam/Bazzite behavior and reconcile it with Hearth's configurable semantic controller model.

## Existing GM concerns that must not be lost

Current repository roadmap contains:

- shader compilation responsiveness;
- perceived/measureable Gaming Mode latency / async-flip-style investigation;
- Decky baseline and Decky-Framegen retirement/isolation.

The owner also directly reported perceived controller latency being worse than before.

These concerns remain valid backlog/roadmap material even if the GM ordering/slice IDs are reworked around Hearth Portal/apps and the future Hearth Decky plugin.

## Future Hearth Decky plugin

After the shell foundation/appropriate earlier GM slices, build a Hearth-owned Decky plugin rather than relying indefinitely on unrelated plugins for Hearth product surfaces.

Potential scope mentioned by the owner:

- selected Hearth features already built for Desktop;
- the same wallpaper/provider system;
- deterministic auto-crop output/shared cache/core;
- MD3E-inspired presentation adapted to Gaming Mode;
- future game/tweak management integration as appropriate.

Do **not** build this merely as part of the Desktop wallpaper slice. Keep it in `GM-*` planning and share core logic intentionally.

## Independence of tracks

Gaming Mode failures should not silently block unrelated Shell progress, and Shell failures should not force unproven Gaming Mode changes into a release. Maintain independent rollback/evidence where the existing multi-track delivery model remains useful.
