# VS-002 — Controller Handoff and Hearth Home

**Status:** in implementation
**Owner:** @akippnn
**Repositories:** `akippnn/starlight-hearth`, `akippnn/starlight-hearth-shell`
**Target:** x86_64 AMD/Intel living-room Hearth PC; Pro 3 receiver `2dc8:310b`

## Observable outcome

Gaming Mode switches to a responsive Hearth Desktop where the controller
reconnects automatically, opens Home, operates essential controls, enters text,
performs power/session actions, and returns to normal Steam controller behavior
in Gaming Mode.

## Authentic path

`signed OCI → Gaming Mode identity profile → steamos-manager → niri → Hearth Shell RPM → Desktop keyboard/mouse profile → Hearth Home/OSK → Gaming Mode`

No mocked controller, simultaneous Steam/Desktop mapping, unpinned shell
artifact, or manually injected Steam account file can satisfy this path.

## In scope

- fork DMS at `20aafebd87f0340c24b585180ab36339d6b154ad` with preserved history and submodule;
- release `starlight-hearth-shell-0.1.0-1.fc44.x86_64.rpm` from signed Hearth source;
- retain DMS compatibility executable, service, IPC, and configuration paths;
- provide Home, power, OSK, quick-controls sizing, visible focus, vim
  navigation, TV breakpoints, warm-rose theme, and top-right toasts;
- use InputPlumber for deterministic Gaming/Desktop ownership and reconnect;
- expose adapter state under `/run/hearth/input-state.json`;
- complete visible hearthOS identity while preserving base compatibility;
- keep KDE, TTY, Tailscale, current-session, and prior-deployment recovery.

## Failure contracts

- Unknown session state applies the gamepad-only fail-safe profile.
- InputPlumber failure blocks a requested transition before `steamosctl`
  changes session state.
- Controller absence is a visible waiting state; reconnect applies the current
  requested profile.
- Changed or unsupported Bazzite session commands fail closed.
- Hearth Shell failure leaves niri emergency bindings and recovery available.
- No network is required after the image and RPM are installed.

## Automated gates

- [x] Frozen fork baseline and submodule recorded.
- [x] Upstream Go tests and Hearth shell contracts pass on Fedora 44 x86_64.
- [x] Nested niri/Quickshell shell startup smoke passes on Bazzite.
- [x] Fedora 44 RPM build, dependency install, ownership, embedded QML,
  compatibility provide/obsolete, permissions, and version checks pass.
- [x] Composite and profile YAML validate against InputPlumber 0.78.0 schemas.
- [x] Session/input adapter unit contracts pass on x86_64 Bazzite.
- [ ] Public shell repository and signed `hearth-v0.1.0` release exist.
- [ ] hearthOS pins the exact release URL and release-asset SHA-256.
- [ ] BlueBuild expansion and complete signed OCI build pass.
- [ ] Built image proves package replacement, services, profiles, session,
  branding, recovery, and stale-stub absence.

## Owner audit

1. Rebase to the signed candidate by immutable digest and reboot.
2. Confirm hearthOS identity, automatic TV scale, TTY, KDE, and prior deployment.
3. Enter Hearth Desktop from Gaming Mode without keyboard or mouse.
4. Power-cycle the controller and confirm Home navigation resumes.
5. Operate Home, quick controls, OSK, power menu, overview, and Return to Gaming.
6. Repeat five transitions, including offline and shell-restart cycles.
7. Confirm normal Steam controller behavior after every return to Gaming Mode.

Agents may mark this slice `audit-ready`; only the owner may mark it `accepted`.
