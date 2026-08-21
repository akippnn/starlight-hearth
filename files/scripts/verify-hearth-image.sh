#!/usr/bin/env bash
set -euo pipefail

# shellcheck disable=SC1091
source /usr/lib/os-release

[[ "${NAME:-}" == "hearthOS" ]]
[[ "${PRETTY_NAME:-}" == "hearthOS" ]]
[[ "${VARIANT:-}" == "Hearth" ]]
[[ "${VARIANT_ID:-}" == "hearth" ]]
[[ -n "${ID:-}" ]]
[[ -n "${ID_LIKE:-}" ]]
[[ -n "${VERSION_ID:-}" ]]

required_files=(
  /usr/libexec/hearth-session
  /usr/libexec/hearth-session-bootstrap
  /usr/libexec/hearth-session-mode
  /usr/share/applications/hearth-return-gaming.desktop
  /usr/share/hearth/dms/settings.json
  /usr/share/hearth/niri/config.kdl
  /usr/share/hearth/niri/hearth.kdl
  /usr/share/hearth/themes/hearth.json
  /usr/share/steamos-manager/user.d/config.toml
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
  /usr/libexec/hearth-session-mode; do
  [[ -x "$path" ]] || {
    echo "hearthOS final image contract is not executable: $path" >&2
    exit 1
  }
done

[[ "$(readlink /usr/lib/systemd/user/niri.service.wants/dms.service)" == "../dms.service" ]]
grep -Fqx 'desktop = "hearth.desktop"' /usr/share/steamos-manager/user.d/config.toml
grep -Fqx 'Name=Hearth Desktop' /usr/share/wayland-sessions/hearth.desktop
[[ ! -e /usr/bin/starlight ]]

systemctl is-enabled tailscaled.service
rpm -q --qf '%{NAME}-%{EPOCHNUM}:%{VERSION}-%{RELEASE}.%{ARCH}\n' \
  dms niri xwayland-satellite
