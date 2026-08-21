# VS-001 — Hearth Desktop Foundation

**Status:** superseded; owner audit failed the controller-ready outcome; not accepted
**Owner:** @akippnn
**Repository:** `akippnn/starlight-hearth`
**Target:** x86_64 AMD/Intel living-room Hearth PC

## Observable outcome

Historical outcome only: the signed image booted niri and DMS on the target
television with scaling and recovery. The controller-ready outcome below was
not achieved. VS-002 replaces its Steam-Input-only ownership model.

The owner boots a signed hearthOS image into Steam Gaming Mode, switches through
Steam's Power menu to a warm niri+DMS Hearth Desktop, completes the essential
desktop and default-application workflows with a controller, returns to Gaming
Mode, and retains KDE, TTY, and previous-deployment recovery.

## Authentic end-to-end path

`signed OCI image → Gaming Mode → steamos-manager → niri → DMS → Hearth Desktop v1 Steam Input layout → controller-operated application → Gaming Mode`

No mocked runtime service or injected Steam account file may satisfy this path.

## Scope

In scope:

- repair the BlueBuild recipe and define the hearthOS identity;
- install upstream niri and DMS through the official Fedora packaging path;
- provide the `Hearth Desktop` session, warm defaults, DMS service integration, and emergency bindings;
- provide a frozen Steam Input semantic contract without writing user Steam state;
- adapt the supported Bazzite `steamosctl` interface and fail closed on contract drift;
- preserve Gaming Mode, KDE, Flatpaks, Tailscale policy, signing, TTY, and atomic rollback;
- record controller compatibility and automated versus owner evidence.

Out of scope:

- Decky Loader, CSS Loader, Framegen, Hearth Shell, Quickshell or Rust runtime code;
- Tauri applications, InputPlumber desktop ownership, CLI/TUI diagnostics;
- Ember, NVIDIA, telemetry, cloud APIs, administrative update actions, or KDE removal.

## Public contracts

- Steam Power → Switch to Desktop selects `Hearth Desktop`.
- A large 4K television receives readable living-room scaling automatically;
  explicit owner/DMS scale configuration always wins.
- The launcher contains **Return to Gaming Mode**.
- `ujust hearth-return-gaming` returns to Steam Gaming Mode.
- `ujust hearth-recovery-kde` switches to KDE Plasma recovery.
- `Hearth Desktop v1` has the mapping in [controller-layout.md](../controller-layout.md).
- Existing user-edited niri and DMS configuration is preserved.
- Unknown `steamosctl` behavior exits with code 2 before a session mutation.

## Failure contracts

- DMS failure leaves niri and emergency terminal, DMS-restart, and logout bindings available.
- Missing Steam Input falls back to keyboard/mouse and is recorded as unsupported controller state.
- Missing or changed `steamosctl` commands leave the current session and SDDM state untouched.
- Offline operation remains available after image and Steam layout installation.
- Display-policy failure leaves niri's existing output scale unchanged.
- KDE's Xwayland Video Bridge never autostarts in Hearth Desktop.
- The prior atomic deployment is retained until the audit is complete.

## Automated gates

- [x] Session adapter success and fail-closed contract tests.
- [x] First-run and existing-user bootstrap tests.
- [x] Stable controller-action fixture and image content contracts.
- [x] Shell syntax and executable-mode checks.
- [x] BlueBuild schema expansion.
- [x] Complete initial image build.
- [x] Initial built-image checks for `os-release`, package versions, session files, DMS/niri services, justfiles, and stale-stub absence.
- [x] niri validation and live DMS startup inside the initial candidate.
- [x] Initial signed OCI, base digest, package versions, revision, and artifact digest recorded.
- [x] Regression fixtures for first-user Desktop selection, 4K-TV scaling,
  owner scale precedence, malformed output data, and KDE-only Video Bridge.
- [x] Complete and verify the corrected candidate containing the owner-audit fixes.

## Owner audit

1. Record the current deployment; rebase to the signed candidate by OCI digest and reboot.
2. Confirm `NAME=hearthOS`, Gaming Mode, controller operation, TTY access, and the previous deployment.
3. Configure/select `Hearth Desktop v1` in Steam controller settings.
4. Use Steam Power → Switch to Desktop; confirm niri and DMS start without a physical keyboard.
5. Complete every row in [the compatibility matrix](../controller-compatibility.md), including OSK text entry.
6. Return to Gaming Mode and repeat the transition five times, including one cycle offline.
7. Exercise KDE recovery, return to Gaming Mode, stop DMS, and verify terminal/TTY/recovery access.
8. Record the candidate digest, versions, results, limitations, and owner verdict in [the evidence record](../evidence/VS-001.md).

Agents may move this slice to `audit-ready` only after all non-owner gates pass.
Only the owner may mark it `accepted`.
