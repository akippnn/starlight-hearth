# hearthOS

hearthOS is the controller-first living-room PC operating system in the
Starlight family. Steam Gaming Mode remains the console experience. **Hearth
Desktop** combines the upstream niri compositor with **Hearth Shell**, the
Starlight-maintained DMS fork built for televisions, controllers, and keyboard
navigation.

The repository and OCI image remain `starlight-hearth` and
`ghcr.io/akippnn/starlight-hearth`. Bazzite and Fedora remain the compatible
base platform; they are not the visible product identity. The discontinued
`starlightOS` name is retained only in historical material.

## Starlight family

```text
Starlight
├── hearthOS
│   └── Living-room gaming and controller-first desktop operating system
└── Ember
    └── Future independent always-on hardware-management service
```

Arcturus may share Ember hardware, but it is independent of Starlight. This
repository contains no Ember or Arcturus placeholder interfaces or data.

## Delivery state

VS-001 proved the signed niri/DMS image, TV scaling, and recovery foundation,
but its owner audit disproved the controller-ready claim. It is preserved as
**superseded and not accepted**.

[VS-002 — Controller Handoff and Hearth Home](docs/slices/VS-002-controller-handoff-and-hearth-home.md)
is active. The current source of truth is [docs/status.md](docs/status.md), with
the remaining slices in [docs/roadmap.md](docs/roadmap.md).

## Architecture

```text
Steam Gaming Mode
├── Steam Input owns game semantics
└── InputPlumber exposes an identity gamepad
        │
        ▼
Bazzite steamos-manager / steamosctl
        │
        ▼
Hearth Desktop
├── niri (unmodified upstream compositor)
├── Hearth Shell (`starlight-hearth-shell` RPM)
└── InputPlumber exposes only Hearth keyboard/mouse semantics

KDE Plasma
└── Recovery desktop retained until a later accepted retirement slice
```

Input ownership is fail-safe: an unknown session gets a conventional gamepad,
never simultaneous Steam and Desktop mappings. The state is visible at
`/run/hearth/input-state.json`.

## Controller contract

`Hearth Desktop v2` is image-owned and documented in
[docs/controller-layout.md](docs/controller-layout.md). Its essential actions
are directional focus, accept/back, focus-group traversal, pointer/click,
scroll, Home, niri overview, and the Hearth on-screen keyboard. Guide remains
Steam-owned and is never intercepted by Hearth.

Hearth Shell also supports `h/j/k/l`, `g/G`, and page navigation outside text
entry fields. Emergency keyboard bindings remain available:

- `Ctrl+Alt+Enter` — open Konsole;
- `Ctrl+Alt+D` — restart Hearth Shell through `dms.service`;
- `Ctrl+Alt+Shift+E` — exit niri.

Session recovery commands are:

```bash
ujust hearth-return-gaming
ujust hearth-recovery-kde
```

## Installation and rollback

Install only an immutable signed OCI digest recorded in the active evidence
record. Do not rebase to a moving tag.

```bash
sudo rpm-ostree rebase \
  ostree-image-signed:docker://ghcr.io/akippnn/starlight-hearth@sha256:<recorded-digest>
systemctl reboot
```

Keep the previous deployment until the owner audit is complete. Hearth Desktop,
the controller profiles, and session switching require no network after the
image is installed.

## Configuration ownership and failure behavior

Versioned defaults are installed for new users without overwriting owner-edited
niri or DMS-compatible configuration. Hearth Shell retains `/usr/bin/dms`,
`dms.service`, existing IPC names, and configuration paths during the fork
transition.

If Hearth Shell fails, niri and its emergency bindings remain available. If
InputPlumber is unavailable or Bazzite's session interface changes, the adapter
blocks the transition instead of guessing. KDE, TTY, Tailscale, the current
Gaming session, and the previous atomic deployment remain recovery paths.

## Development

The source repository contains image policy and integration; Hearth Shell is
released independently from `akippnn/starlight-hearth-shell` and installed by
an exact RPM URL plus SHA-256, never `latest`.

Run local contracts with:

```bash
python3 -m unittest discover -s tests -v
```

Linux x86_64 is the only build target. Authoritative package and integration
checks run through CI and `ssh aki@bazzite`.
