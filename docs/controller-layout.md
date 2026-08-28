# Controller layout validation summary

**State:** accepted defaults with unresolved global actions; not frozen
**Canonical detail:** `docs/contracts/input-navigation.md` and `docs/contracts/osk.md`

The historical Hearth Desktop v2/v3 manifests and InputPlumber profiles are
implementation evidence, not the current mapping authority. Future manifests
must be data-driven and generated or validated against the frozen contract for
their slice.

## Validated summary

The canonical behavior is defined only in
[`contracts/input-navigation.md`](contracts/input-navigation.md). The current
physical profile and machine-readable contract must preserve these validated
facts:

- right stick is pointer motion and left stick is scrolling;
- RB is primary/left click and LB is secondary/right click;
- an active, more-specific hearthOS surface overrides broader/global actions;
- West is the physical west position, independent of printed controller label;
- future Classic/Vim presets and First Setup remain outside HSN-002.

The old fake-keyboard v2 mapping, F10 launcher, trigger clicks, bumper group
navigation, and north-button hold behavior are superseded defaults. Historical
artifacts retain them for provenance.
