# Controller layout planning summary

**State:** accepted defaults with unresolved global actions; not frozen
**Canonical detail:** `docs/contracts/input-navigation.md` and `docs/contracts/osk.md`

The historical Hearth Desktop v2/v3 manifests and InputPlumber profiles are
implementation evidence, not the current mapping authority. Future manifests
must be data-driven and generated or validated against the frozen contract for
their slice.

## Accepted Desktop defaults

| Physical control | Default behavior outside the OSK |
| --- | --- |
| D-pad | Semantic focus |
| Left stick | Scroll/paging |
| Right stick | Pointer |
| South | Accept |
| East | Back |
| West | Contextual alternate action; Grid/List toggle in App Menu |
| North | Open OSK immediately at active text target or primary search |
| RT / LT | Next/previous App Menu tab |
| RB / LB | Primary/secondary pointer click |
| Menu/Start | Open App Menu; selected-app actions while inside it |

West is the physical west position: Xbox X, PlayStation Square, Nintendo Y.
Guide, View, L3/R3, global media/window/workspace chords, and pointer tuning
remain open.

## Accepted keyboard defaults

| Action | Keys |
| --- | --- |
| Open App Menu | `Super+A` |
| Navigate | Arrows, `HJKL`, `WASD` |
| Search | `i`, `/`, `Ctrl+F` |
| App Menu tabs | `Ctrl+Tab`, `Ctrl+Shift+Tab` |
| Grid/List | `Ctrl+1`, `Ctrl+2` |
| Context/options | Menu key, `Shift+F10` |
| Manual OSK | `Super+I`, `F12` |

The old fake-keyboard v2 mapping, F10 launcher, trigger clicks, bumper group
navigation, and north-button hold behavior are superseded defaults. Historical
artifacts retain them for provenance.
