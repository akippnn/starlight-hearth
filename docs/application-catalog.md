# Application catalog and inventory contract

**State:** Proposed planning inventory; not frozen or implemented
**Last reconciled:** 2026-08-25

This document separates four facts that were previously conflated:

1. installed in the immutable image;
2. installed as a system or user Flatpak;
3. visible in the Menu/Start-button App Menu;
4. available on demand through Hearth Portal.

An installed recovery dependency does not automatically belong in App Menu. A
Portal-only application is absent by default and must have a typed, auditable
install action before a future inherited-base outcome removes its installation.

## Inventory identities

| Input | Immutable identity | State |
| --- | --- | --- |
| Matching clean Bazzite base | `ghcr.io/ublue-os/bazzite-deck@sha256:148c53b3858688d10ef29b571764fbdf6bbf3b6afeb56c9755096d85e46ef77f` (`stable-44.20260820`) | Historical comparison input selected for the superseded application plan |
| Deployed hearthOS | OCI index `sha256:a27e4847061b71026eba98d39de96f9db3c3b5b029282ae1601aaabe27c01296`, version `44.20260820` | Historical read-only inventory captured 2026-08-23 |
| Previous hearthOS recipe | Jellyfin Desktop, mpv, LocalSend, Warehouse, Mission Center additions | Repository baseline before roadmap repair |
| Future application-catalog candidate | Pending | Requires a new ID, exact OCI digest, and generated diff before any future audit-readiness claim |

The current upstream Bazzite KDE Flatpak manifest is a drift signal, not a
replacement for the immutable base above:
<https://raw.githubusercontent.com/ublue-os/bazzite/main/installer/kde_flatpaks/flatpaks>.

## Desired default and App Menu catalog

| Application | Package/application ID | Desired installation | App Menu | Controller mode | Rationale |
| --- | --- | --- | --- | --- | --- |
| Steam | `steam` | Default | Visible | Gaming identity | Gaming Mode and library entrypoint |
| Return to Gaming Mode | `hearth-return-gaming.desktop` | Default | Visible | Shell-native | Recovery/session transition |
| Hearth Portal | Hearth application entry | Default after its future accepted application outcome | Visible | Shell-native | Controller-native system/application management |
| Firefox | `org.mozilla.firefox` | Default | Visible | Custom bindings | Browser |
| Dolphin | `dolphin` | Default | Visible | Custom bindings | File manager |
| Ark | `ark` | Default | Visible | Custom bindings | Archive handling |
| Okular | `org.kde.okular` | Default | Visible | Custom bindings | Documents |
| Gwenview | `org.kde.gwenview` | Default | Visible | Custom bindings | Images |
| Jellyfin Desktop | `org.jellyfin.JellyfinDesktop` | Default | Visible | Native gamepad | Living-room media |
| mpv | `io.mpv.Mpv` | Default | Visible | Custom bindings | General media fallback |
| LocalSend | `org.localsend.localsend_app` | Default | Visible | Custom bindings | Local file transfer |
| Bazaar | `io.github.kolunmi.Bazaar` | Default | Visible | Custom bindings | Flatpak application store |
| Lutris | `net.lutris.Lutris` | Default | Visible | Native gamepad | Non-Steam game library |
| Bold Brew | `bbrew.desktop` | Default | Visible | Custom bindings | Homebrew manager through Terminal |
| Warehouse | `io.github.flattool.Warehouse` | Default | Visible | Custom bindings | Flatpak maintenance |
| Flatseal | `com.github.tchx84.Flatseal` | Default | Visible | Custom bindings | Flatpak permissions |
| Firmware | `org.gnome.Firmware` | Default | Visible | Custom bindings | Firmware inspection/update |
| Filelight | `org.kde.filelight` | Default | Visible | Custom bindings | Disk-usage inspection; keep one implementation |
| KCalc | `org.kde.kcalc` | Default | Visible | Custom bindings | Calculator |
| ProtonPlus | `com.vysp3r.ProtonPlus` | Default | Visible | Native gamepad | Compatibility-tool management |
| Protontricks | `com.github.Matoking.protontricks` | Default | Visible | Custom bindings | Prefix maintenance |
| Proton runtimes | Dependency-provided | Default as required | Hidden | N/A | Compatibility runtime, not launcher clutter |
| KWalletManager | `kwalletmanager5` | Default | Visible | Custom bindings | Credential recovery/inspection |
| Terminal | Ghostty | Default only after future base-curation and recovery proof | Visible as **Terminal** | Custom bindings | Proposed sole terminal emulator; selected by `xdg-terminal-exec` |

## Portal-only catalog

| Application/tool | Current deployed state | Desired state | Notes |
| --- | --- | --- | --- |
| KDE Connect | Native package installed | Portal-only | Install/enable only after niri/Hearth compatibility audit |
| Kontainer | System Flatpak installed | Portal-only | Optional container GUI |
| Waydroid | Native package installed | Portal-only | Preserve underlying requirements only when needed |
| Web Apps | Native package installed | Portal-only | Optional web-app manager |
| OpenGamepadUI | Native package installed | Portal-only | Optional alternate launcher/overlay |
| Bazzite Updater | Native package installed | Flow may move into Hearth Portal | Remove launcher only after a future Portal outcome proves update status/action parity |
| Btrfs Assistant | Native package installed | Portal maintenance action | Keep hidden if required for recovery |
| Cardwire | Native package installed | Portal maintenance action | Hardware-specific utility |
| Disks | Native package installed | Portal maintenance action | Keep hidden if dependency-safe removal is unavailable |
| Firewall | Native package installed | Portal maintenance action | Authentication-aware action required |
| ROM Properties configuration | Native package installed | Portal maintenance action | Configuration utility, not default launcher |
| Decky-Framegen | Owner plugin historically observed | Remove only in a newly identified future Gaming Mode outcome after backing up its user configuration | Retain Decky Loader, Volume Mixer, and unrelated user plugins |
| OptiScaler/Lossless Scaling | Upstream Portal actions | Portal-only | Never preinstall frame-generation plugins |

## Proposed removal or suppression in future base curation

| Surface | Current state | Required result |
| --- | --- | --- |
| Documentation | Visible inherited desktop link | Remove desktop entry and Hearth Portal link |
| Discourse | Visible inherited web link | Remove desktop entry and Hearth Portal link |
| Haruna | System Flatpak installed | Remove; mpv remains the general media fallback |
| Mission Center | hearthOS-added system Flatpak | Remove only after a proven Hearth process surface owns the workflow |
| KDE System Monitor | Native package installed | Remove when dependency-safe, otherwise hide |
| Alacritty | Native terminal installed | Remove after Ghostty passes Terminal/Bold Brew/recovery audit |
| Konsole | Native terminal installed | Remove after Ghostty passes KDE recovery audit |
| Kate, KWrite, KFind, KRDC/Krfb, Journald Browser and similar non-curated admin tools | Native packages installed | Remove when dependency-safe, otherwise hide from App Menu |

## Generated comparison requirements

The future application-catalog outcome must generate one row per launchable
desktop entry and Flatpak app for
the exact base, previous catalog, candidate, and deployed host. Each row records
desktop ID, package/app ID, provenance, scope, desired state, App Menu
visibility, Portal action, controller mode, and rationale. The generated diff
must fail on an unreviewed addition, removal, rename, duplicate implementation,
or provenance change.
