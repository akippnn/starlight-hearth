#!/usr/bin/env bash
set -euo pipefail

required=(
  /usr/bin/dms
  /usr/bin/niri
  /usr/bin/niri-session
  /usr/lib/systemd/user/dms.service
  /usr/lib/systemd/user/hearth-default-desktop.service
  /usr/lib/systemd/user/hearth-display-policy.service
  /usr/lib/systemd/user/niri.service
  /usr/lib/systemd/system/hearth-input-adapter.service
  /usr/lib/systemd/system/hearth-identity.service
  /usr/libexec/hearth-default-desktop-bootstrap
  /usr/libexec/hearth-display-policy
  /usr/libexec/hearth-input-adapter
  /usr/libexec/hearth-input-request
  /usr/libexec/hearth-identity-bootstrap
  /usr/libexec/hearth-session
  /usr/libexec/hearth-session-bootstrap
  /usr/libexec/hearth-session-mode
  /usr/share/wayland-sessions/hearth.desktop
)

for path in "${required[@]}"; do
  if [[ ! -e "$path" ]]; then
    echo "hearthOS image contract missing: $path" >&2
    exit 1
  fi
done

install -d -m 0755 /usr/lib/systemd/user/niri.service.wants
ln -sfn ../dms.service /usr/lib/systemd/user/niri.service.wants/dms.service
ln -sfn ../hearth-display-policy.service \
  /usr/lib/systemd/user/niri.service.wants/hearth-display-policy.service

install -d -m 0755 /usr/lib/systemd/user/default.target.wants
ln -sfn ../hearth-default-desktop.service \
  /usr/lib/systemd/user/default.target.wants/hearth-default-desktop.service

chmod 0755 \
  /usr/libexec/hearth-default-desktop-bootstrap \
  /usr/libexec/hearth-display-policy \
  /usr/libexec/hearth-input-adapter \
  /usr/libexec/hearth-input-request \
  /usr/libexec/hearth-identity-bootstrap \
  /usr/libexec/hearth-session \
  /usr/libexec/hearth-session-bootstrap \
  /usr/libexec/hearth-session-mode

validation_root="$(mktemp -d /tmp/hearth-niri-validate.XXXXXX)"
trap 'rm -rf "$validation_root"' EXIT
install -d -m 0700 "$validation_root/niri"
install -m 0600 /usr/share/hearth/niri/config.kdl "$validation_root/niri/config.kdl"
XDG_CONFIG_HOME="$validation_root" /usr/bin/niri validate

# DMS refuses to start as root, including for its version subcommand. Image
# modules run as root, so verify the installed RPM without executing DMS.
rpm -q dms >/dev/null
