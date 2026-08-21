# hearthOS controller desktop roadmap

Each checkpoint delivers one reversible, owner-observable outcome with a fresh
contract and evidence record. Details are not silently inherited.

| Slice | User-visible outcome | Principal gate |
|---|---|---|
| **VS-001 — Hearth Desktop Foundation** | Historical signed niri+DMS image boots on the television with recovery available. Superseded after its controller audit failed. | Preserve evidence and owner findings; never accepted. |
| **VS-002 — Controller Handoff and Hearth Home** | Gaming Mode switches to a responsive Hearth Desktop where the controller reconnects, opens Home, operates essential controls, enters text, performs session actions, and returns to Gaming Mode. | Deterministic InputPlumber/Steam ownership, pinned Hearth Shell RPM, A/B core surfaces, five transitions, offline and recovery audits. |
| **VS-003 — Hearth Shell Controller Coverage** | Settings, notifications, clipboard, launcher results, overview, lock surface, polkit prompts, and retained DMS surfaces are controller/keyboard navigable. | Complete focus graph, no focus traps, responsive TV layouts, visible focus, controller-only audit. |
| **VS-004 — Controller-Friendly Applications** | Every default GUI application has an A–C workflow through focus, pointer assistance, and Hearth OSK. | Firefox, Dolphin, Jellyfin, mpv, LocalSend, Warehouse, Mission Center, and recovery tools contain no D result. |
| **VS-005 — Hearth Gaming Integration** | A controller-friendly setup surface installs, repairs, or removes pinned Decky Loader, CSS Loader, and the Hearth Gaming theme. | Exact manifest/digests, explicit consent, rollback, and unchanged Gaming Mode when declined. |
| **VS-006 — Upstream Framegen Pilot** | The owner installs pinned upstream Decky-Framegen v0.17 and patches/unpatches Cyberpunk 2077 without copying commands. | Commit `96eb17b…`, ZIP SHA-256 `3300b617e3d979b483d03f995c75c829d6d54beaa4ac8dfae300c2560e4fc60f`, external preflight backup, restored files/options, owner verdict. |
| **VS-007 — Hearth Framegen Hardening** | Conditional transactional, hash-verified patch recovery and optional Steam Properties integration. | Created only if VS-006 safety or UX is rejected; then fork v0.17 as `akippnn/decky-framegen`. |
| **VS-008 — Secure Session Lifecycle** | Locking, idle handling, authentication, suspend, logout, and shutdown are controller-safe and security-audited. | Lock bypass, crash recovery, secret handling, polkit exclusivity, physical audit. |
| **VS-009 — KDE Retirement** | KDE is removed only after Hearth Shell and every recovery path are owner-accepted. | TTY, Tailscale, previous deployment, Gaming Mode, and shell recovery remain proven. |

There is no DMS-retirement slice: Hearth Shell is the maintained DMS-derived
product. Ember and NVIDIA remain independent future work.
