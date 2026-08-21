# Hearth Desktop v1 controller layout

Steam Input is the sole desktop mapping owner in VS-001. Configure this layout
through Steam's controller UI; hearthOS intentionally does not inject
account-specific Steam files. InputPlumber must not emit a second desktop map.

The machine-readable contract is
[`tests/fixtures/controller-layout-v1.json`](../tests/fixtures/controller-layout-v1.json).

| Controller input | Steam Input output | Meaning |
|---|---|---|
| D-pad | Arrow keys | Directional focus |
| A | Enter | Accept |
| B | Escape | Back/cancel |
| LB / RB | Shift+Tab / Tab | Previous/next focus |
| Right stick | Mouse | Pointer |
| RT / LT | Left/right mouse button | Primary/secondary click |
| Left stick | Mouse wheel | Scrolling |
| X | Space | Toggle or activate focused control |
| Y | Steam “Show Keyboard” action | On-screen keyboard |
| Menu | F10 | DMS launcher/Home |
| View | F9 | niri overview |
| Guide | Steam-owned Guide action | Steam overlay; never intercepted by Hearth |

F11 is reserved as a keyboard-level diagnostic shortcut for DMS Control Center;
it is not required by the canonical controller layout.

## Compatibility grades

- **A — native:** purpose-built semantic controller focus and actions.
- **B — focus:** complete through keyboard-style focus navigation.
- **C — pointer-assisted:** complete through pointer emulation and on-screen keyboard.
- **D — unsupported:** a physical keyboard is required or the primary workflow cannot complete.

Core shell, settings, power, session-switching, and recovery workflows must be A
or B. Every default application must have an observed A–C path. Pending is not a
grade and cannot satisfy the acceptance gate.
