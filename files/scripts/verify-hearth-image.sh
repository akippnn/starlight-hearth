#!/usr/bin/env bash
set -euo pipefail

# shellcheck disable=SC1091
source /usr/lib/os-release

[[ "${NAME:-}" == "hearthOS" ]]
[[ "${PRETTY_NAME:-}" == "hearthOS" ]]
[[ "${VARIANT:-}" == "Hearth" ]]
[[ "${VARIANT_ID:-}" == "hearth" ]]
[[ "${LOGO:-}" == "hearth-logo" ]]
[[ "${DEFAULT_HOSTNAME:-}" == "hearth" ]]
[[ "${BOOTLOADER_NAME:-}" == "hearthOS" ]]
[[ "${IMAGE_ID:-}" == "starlight-hearth" ]]
[[ -n "${ID:-}" ]]
[[ -n "${ID_LIKE:-}" ]]
[[ -n "${VERSION_ID:-}" ]]

required_files=(
  /usr/libexec/hearth-session
  /usr/libexec/hearth-session-bootstrap
  /usr/libexec/hearth-session-mode
  /usr/libexec/hearth-shell-launch
  /usr/libexec/hearth-default-desktop-bootstrap
  /usr/libexec/hearth-display-policy
  /usr/libexec/hearth-input-adapter
  /usr/libexec/hearth-input-request
  /usr/libexec/hearth-identity-bootstrap
  /usr/lib/systemd/system/hearth-identity.service
  /usr/lib/systemd/system/hearth-input-adapter.service
  /usr/lib/systemd/user/hearth-default-desktop.service
  /usr/lib/systemd/user/hearth-display-policy.service
  /etc/xdg/autostart/org.kde.xwaylandvideobridge.desktop
  /usr/share/applications/hearth-return-gaming.desktop
  /etc/hearth-shell/config.json
  /usr/share/hearth/niri/config.kdl
  /usr/share/hearth/niri/hearth.kdl
  /usr/share/hearth/input/hearth-desktop-v4.yaml
  /usr/share/hearth/input/inputplumber-v4.json
  /usr/share/hearth/input/hearth-gaming-v2.yaml
  /usr/share/hearth/themes/hearth.json
  /usr/share/steamos-manager/user.d/config.toml
  /usr/share/inputplumber/devices/55-hearth-8bitdo-pro-3.yaml
  /usr/share/icons/hicolor/scalable/apps/hearth-logo.svg
  /usr/share/wayland-sessions/hearth.desktop
)

for path in "${required_files[@]}"; do
  [[ -s "$path" ]] || {
    echo "hearthOS final image contract missing: $path" >&2
    exit 1
  }
done

for path in \
  /usr/libexec/hearth-session \
  /usr/libexec/hearth-session-bootstrap \
  /usr/libexec/hearth-session-mode \
  /usr/libexec/hearth-default-desktop-bootstrap \
  /usr/libexec/hearth-display-policy; do
  [[ -x "$path" ]] || {
    echo "hearthOS final image contract is not executable: $path" >&2
    exit 1
  }
done

for path in /usr/libexec/hearth-input-adapter /usr/libexec/hearth-input-request /usr/libexec/hearth-identity-bootstrap; do
  [[ -x "$path" ]] || {
    echo "hearthOS input contract is not executable: $path" >&2
    exit 1
  }
done

[[ "$(readlink /usr/lib/systemd/user/niri.service.wants/hearth-shell.service)" == "../hearth-shell.service" ]]
[[ "$(readlink /usr/lib/systemd/user/niri.service.wants/hearth-shell-ui.service)" == "../hearth-shell-ui.service" ]]
[[ "$(readlink /usr/lib/systemd/user/niri.service.wants/hearth-display-policy.service)" == "../hearth-display-policy.service" ]]
[[ "$(readlink /usr/lib/systemd/user/default.target.wants/hearth-default-desktop.service)" == "../hearth-default-desktop.service" ]]
grep -Fqx 'OnlyShowIn=KDE;' /etc/xdg/autostart/org.kde.xwaylandvideobridge.desktop
grep -Fqx 'desktop = "hearth.desktop"' /usr/share/steamos-manager/user.d/config.toml
grep -Fqx 'Name=Hearth Desktop' /usr/share/wayland-sessions/hearth.desktop
grep -Fq 'namespace="^hearth-launcher-drawer$"' /usr/share/hearth/niri/hearth.kdl
grep -Fq 'blur true' /usr/share/hearth/niri/hearth.kdl
grep -Fq 'xray true' /usr/share/hearth/niri/hearth.kdl
[[ ! -e /usr/bin/starlight ]]

systemctl is-enabled tailscaled.service
systemctl is-enabled hearth-identity.service
systemctl is-enabled hearth-input-adapter.service
rpm -q --qf '%{NAME}-%{EPOCHNUM}:%{VERSION}-%{RELEASE}.%{ARCH}\n' \
  hearth-shell niri xwayland-satellite
