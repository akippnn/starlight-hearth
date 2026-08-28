# HSN-001 RC.2 frosted-surface field result

Date: 2026-08-28

## Authentic packaged baseline

- Target: `aki@hearth`, real niri session on the LG output.
- Booted signed OCI index:
  `sha256:dea09a20687b3f235b0dd89f817a3a63dcbc24499d1dfa6fa34a813af8f6b191`.
- Installed package: `hearth-shell-0.3.0-0.2.rc2.fc44.x86_64`.
- With `Launcher1.Visible=false`, the packaged image retained a gray frosted
  rectangle at the drawer location.
- The closed layer listing retained `hearth-launcher-drawer`; the image's
  unconditional niri xray rule blurred the complete mapped layer even after
  Quickshell cleared its shaped effect region.
- Opening the launcher replaced the artifact with the normal panel.

## Local-only correction

- Shell revision:
  `b17c1bb582090fa2aa294c29a7e97e3b2e5ac3ea`.
- Product revision:
  `30fb91dd0ddf1de2ad4afe473663ca789aea5644`.
- The normal warm surface now uses namespace
  `hearth-launcher-drawer-shaped` and Quickshell's shaped effect region.
- The compositor-wide niri fallback is isolated behind the explicit
  `hearth-launcher-drawer-xray` namespace and unmaps after closing.
- A translucent backend remains available without blur.
- The corrected closed screenshot contains no frosted rectangle. The warm
  shaped surface remains mapped so reopening does not require cold
  scene-graph construction.

## Warm workload

- Workload: 30 launcher open/close cycles with alternating Grid/List changes.
- Closed-state artifact failures: `0`.
- Rendered frames: `1587`.
- Frame time p50/p95/p99/max: `0/13/19/19 ms`.
- CPU usage delta: `1.405445 s`.
- Memory current: `159686656` bytes before, `154681344` bytes after.
- Memory peak: `164552704` bytes before and after.
- Native mesh allocations during the measured workload: `0`.
- QML warnings: `0`.

The result satisfies the local p95/p99 60 Hz limits. It is not released,
signed-image proof, audit-readiness, or owner acceptance. The packaged units
were restored after testing, so the target continues to run the published
RC.2 and therefore still contains the defect until a later owner-authorized
delivery.
