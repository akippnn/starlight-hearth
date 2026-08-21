# hearthOS

hearthOS is the controller-first living-room PC operating system in the
Starlight family. It keeps Bazzite Gaming Mode as the console experience and
adds **Hearth Desktop**, an upstream niri session with DankMaterialShell (DMS)
as its initial desktop shell.

The repository and OCI image remain `starlight-hearth` and
`ghcr.io/akippnn/starlight-hearth`. The retired name `starlightOS` is not the
operating-system identity.

## Starlight family

```text
Starlight
├── hearthOS
│   └── Living-room gaming and controller-first desktop operating system
└── Ember
    └── Future independent always-on hardware-management service
```

Arcturus may share Ember hardware, but it is independent of both Ember and
Starlight. This repository contains no Ember or Arcturus placeholder UI, data,
or protocol.

## Current delivery slice

[VS-001 — Controller-Ready Hearth Desktop](docs/slices/VS-001-controller-ready-hearth-desktop.md)
is active. It delivers the image/session foundation and preserves recovery;
controller compatibility and the signed candidate still require the owner
hardware audit recorded in [the evidence record](docs/evidence/VS-001.md).

The authoritative project state is [docs/status.md](docs/status.md). Later work
is sequenced in [docs/roadmap.md](docs/roadmap.md).

## Desktop architecture

```text
Steam Gaming Mode
        │
        ▼
Bazzite steamos-manager / steamosctl
        │
        ▼
Hearth Desktop
└── niri
    ├── DMS shell and control surfaces
    ├── Hearth controller bindings
    └── Return to Gaming Mode action

KDE Plasma
└── Retained as a recovery desktop
```

niri and DMS are upstream packages. Hearth-owned code currently consists only
of image configuration, a fail-closed session adapter, user-default bootstrap,
recovery recipes, tests, and delivery records. A future Hearth Shell will
replace DMS responsibility by responsibility; it will not replace niri or
Wayland.

## Installation

Only install an image candidate whose immutable OCI digest is recorded in the
active [evidence record](docs/evidence/VS-001.md). Do not rebase to `latest`.
Once a candidate exists, the form of the command is:

```bash
sudo rpm-ostree rebase \
  ostree-image-signed:docker://ghcr.io/akippnn/starlight-hearth@sha256:<recorded-digest>
systemctl reboot
```

The digest is intentionally not filled with a moving tag. Keep the prior atomic
deployment until the owner audit is complete.

## Controller setup

Steam owns the initial desktop mapping. In Steam's controller settings, create
or select **Hearth Desktop v1** and configure the semantic mapping in
[docs/controller-layout.md](docs/controller-layout.md). hearthOS does not write
undocumented per-account Steam files.

From Gaming Mode, use **Power → Switch to Desktop**. The system-wide
`steamos-manager` configuration selects `Hearth Desktop`; the adapter validates
the installed `steamosctl` interface before any transition request.

The launcher contains **Return to Gaming Mode**. Recovery commands are also
available from a terminal:

```bash
ujust hearth-return-gaming
ujust hearth-recovery-kde
```

Emergency keyboard bindings in Hearth Desktop are:

- `Ctrl+Alt+Enter` — open Konsole;
- `Ctrl+Alt+D` — restart DMS;
- `Ctrl+Alt+Shift+E` — exit niri.

## Defaults and user ownership

On first Hearth Desktop start, Hearth installs its minimal niri baseline, warm
theme, and controller bindings only where settings are absent. An existing niri
configuration is backed up once and extended with one optional Hearth include;
existing DMS settings are never overwritten. The interactive and potentially
privileged `dms setup` command is never run automatically.

The warm profile uses charcoal-plum surfaces, cream text, dusty-rose accents,
amber warnings, sage supporting accents, and soft-red failures.

## Offline and failure behavior

No network is required to start Hearth Desktop, use installed applications, or
switch sessions after the image and Steam layout are installed. Tailscale keeps
the existing Bazzite service policy but is not a Desktop dependency.

If DMS fails, niri continues running and the emergency terminal/logout bindings
remain available. If the installed Bazzite session interface is absent or no
longer advertises the requested session, the adapter exits without touching
SDDM state or guessing at upstream internals. KDE, TTY access, and the previous
atomic deployment remain recovery paths.

## Scope

VS-001 does not install Decky Loader, Framegen, Hearth Shell, Tauri applications,
or InputPlumber desktop mappings. It does not remove KDE. Those changes have
separate future slices so each can be tested and reversed independently.

## Development

Run the repository-local contracts with:

```bash
python3 -m unittest discover -s tests -v
```

The GitHub workflow runs these contracts before BlueBuild. A complete image
build and the living-room PC audit are still required before the slice can be
accepted.
