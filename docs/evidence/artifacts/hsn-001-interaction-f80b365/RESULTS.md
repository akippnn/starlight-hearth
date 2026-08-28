# HSN-001 unified-selection repair result

Date: 2026-08-28

## Exact local candidate

- Shell revision:
  `f80b365ebda1d4f226918f76328375e25cb52969`.
- Product evidence base:
  `156e8f60e075e6e2dd6596ac32b9417d5c355fb9`.
- Target: `aki@hearth`, Fedora 44, real niri at 3840x2160.
- The target continued to boot the published signed RC.2 image. The exact local
  shell source was staged under
  `/home/aki/.local/share/hearth-dev/hsn001-interaction-20260828`; neither the
  installed RPM nor the booted deployment was changed.

The repair gives controller, keyboard, and pointer one canonical selected
index. Immediate pointer hover retargets the existing native rounded selection
surface. Activation from all three input paths drives the same bounded press
deformation and at most one clipped ripple. The Grid/List selector follows the
same contained press rule. Reduced-motion mode suppresses the animations.

## Automated verification

- macOS `cargo test --all-targets --locked`: 13 passed.
- macOS `python3 tests/test_contracts.py`: 6 passed.
- macOS `python3 tests/test_qml_static.py`: 17 passed.
- Fedora 44 native CMake compile/install: passed.
- Fedora 44 QML offscreen/qmllint suite: 14 passed, 0 failed.
- Fedora 44 native QML bridge suite: 3 passed, 0 failed.
- Real-niri diagnostics: 0 QML warnings and one startup mesh allocation; no
  measured workload allocation occurred.

## Real-niri workloads

Fifty rapid selection changes rendered 166 frames at p50/p95/p99/max
`0/16/16/16 ms`. Memory current changed from `151900160` to `153468928`
bytes; memory peak remained `166219776` bytes.

Thirty panel open/close plus Grid/List cycles rendered 634 frames at
p50/p95/p99/max `0/16/16/16 ms`. Memory current changed from `152104960` to
`155140096` bytes; memory peak remained `166219776` bytes. The closed
screenshot also reconfirms that the local blur correction leaves no frosted
drawer artifact.

## Restoration and lifecycle

All temporary development services were stopped and the packaged service was
restored before explicitly invoking Return to Gaming Mode. The final direct
inspection recorded an active Wayland login on `tty1` with
`Desktop=gamescope`; gamescope and Steam `-gamepadui` were running. Niri, the
Hearth companion, the packaged UI, both temporary UI units, and the temporary
ydotool daemon were inactive. This is a clean Desktop-to-Gaming teardown.

The earlier snapshot discussed with the owner was taken before the owner had
actually invoked Return to Gaming Mode. Its active Desktop units therefore
were expected and are not evidence that Gaming Mode was running concurrently
in the background. A resident Steam process in Desktop mode is likewise not
sufficient to establish an active Gaming Mode session.

## Scope and remaining gate

This bundle proves a clean local source revision in development staging. It is
not a pushed tag, published RPM, signed-image candidate, formal recovery audit,
owner motion verdict, or HSN-001 acceptance. Under the retained delivery hold,
the correction must be incorporated into the exact HSN-002-stage combined
candidate, published and signed only after explicit owner authorization, then
rechecked on the booted immutable image. HSN-001 and HSN-002 retain separate
owner verdicts.
