# hearthOS controller desktop and shell roadmap

The roadmap uses vertical slices: each checkpoint must produce one reversible,
owner-observable outcome with its own frozen contract and evidence. Details are
not silently inherited between slices.

| Slice | User-visible outcome | Principal gate |
|---|---|---|
| **VS-001 — Controller-Ready Hearth Desktop** | Gaming Mode switches to a warm niri+DMS Desktop that can run its essential workflows with a controller and recover through KDE. | Complete signed image, A–C application matrix, repeated session transitions, and owner hardware audit. |
| **VS-002 — Hearth Gaming Integration** | A controller-friendly setup surface explicitly installs, repairs, or removes tested Decky Loader, CSS Loader, and a Hearth Gaming Mode theme. | Pinned artifact manifest, explicit consent, transactional rollback, and unchanged Gaming Mode when declined. |
| **VS-003 — Framegen Pilot** | The owner installs pinned Decky-Framegen and completes one named OptiScaler workflow on one named game/hardware combination. | Exact source/artifact digest, per-game consent, and restoration of original game files. |
| **VS-004 — Hearth Home** | A controller-native Hearth Home launches and focuses applications and returns to Gaming Mode while DMS remains available. | Independent Quickshell/Rust tests, versioned `org.starlight.Hearth.Session1` D-Bus contract, and working DMS fallback. |
| **VS-005 — Hearth Controls and Settings** | Hearth Shell manages common audio, brightness, network, Bluetooth, display, and power settings without DMS panels. | Real service adapters, degraded-state behavior, controller-only audit, and no privileged shell calls from Quickshell. |
| **VS-006 — Desktop Shell Parity** | Hearth Shell owns Home, launcher, bar, overview, OSDs, notifications, clipboard access, and session actions. | Explicit parity/failure test for every displaced DMS responsibility; DMS remains selectable. |
| **VS-007 — Secure Session Lifecycle** | Hearth supplies audited idle, lock, authentication-agent, suspend, logout, and shutdown behavior. | Lock-bypass, crash-recovery, secret-handling, polkit exclusivity, and physical security audits. |
| **VS-008 — DMS Retirement** | Normal Hearth Desktop starts without DMS while KDE remains recovery. | A DMS-free image passes every prior owner audit and preserves rollback. |
| **VS-009 — KDE Retirement** | KDE is removed only after Hearth Shell has accepted parity for ordinary and recovery workflows. | Previously accepted DMS-free deployment plus TTY, Tailscale, prior-deployment, and Gaming Mode recovery. |

Tauri remains deferred until a conventional windowed Hearth application has a
specific need for a second UI stack. Ember, NVIDIA images, telemetry, cloud
APIs, and automatic self-update are outside this roadmap.
