# Hearth Desktop v2 controller contract

InputPlumber normalizes the physical controller in both sessions.

- **Gaming Mode:** identity gamepad only; Steam Input owns game semantics.
- **Hearth Desktop:** Hearth keyboard/mouse profile only; Steam receives no
  desktop-mappable gamepad.
- **Unknown state:** gamepad-only fail-safe; Desktop mappings are never emitted.

The machine-readable fixture is
[`tests/fixtures/controller-layout-v2.json`](../tests/fixtures/controller-layout-v2.json).

| Controller input | Desktop output | Meaning |
|---|---|---|
| D-pad | Arrow keys | Directional focus |
| A / B | Enter / Escape | Accept / back |
| LB / RB | Shift+Tab / Tab | Previous / next focus group |
| Right stick | Mouse motion | Pointer |
| RT / LT | Left / right mouse button | Primary / secondary click |
| Left stick | Wheel up/down | Scrolling |
| X | Space | Toggle focused control |
| Y | F12 | Hearth on-screen keyboard |
| Menu | F10 | Hearth Home |
| View | F9 | niri overview |
| Guide | Unmapped | Reserved for Steam; never intercepted by Hearth |

Hearth Shell also accepts `h/j/k/l`, `g/G`, Page Up/Page Down, Tab, and
Shift+Tab outside text-entry fields. Opening a modal establishes one visible
focus target; closing and reopening restores a deterministic target rather than
leaving focus on an invisible control.

## Compatibility grades

- **A — native:** purpose-built semantic controller focus and actions.
- **B — focus:** complete through keyboard-style focus navigation.
- **C — pointer-assisted:** complete through pointer emulation and Hearth OSK.
- **D — unsupported:** requires a physical keyboard or cannot complete its
  primary workflow.

VS-002 core shell, OSK, power, and session transitions must be A or B. The
default-application matrix moves to VS-004.
