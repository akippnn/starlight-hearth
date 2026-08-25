#!/usr/bin/env bash
set -euo pipefail

readonly default_url="https://github.com/akippnn/starlight-hearth-shell/releases/download/hearth-v0.3.0-rc.1/hearth-shell-0.3.0-0.1.rc1.fc44.x86_64.rpm"
readonly default_sha256="36b30a88033a882733ffd41bfce29bb8287930c5ae12dac42a37b0940794661e"

shell_url="${HEARTH_SHELL_URL:-$default_url}"
shell_sha256="${HEARTH_SHELL_SHA256:-$default_sha256}"
curl_bin="${HEARTH_CURL:-/usr/bin/curl}"
dnf5_bin="${HEARTH_DNF5:-/usr/bin/dnf5}"
rpm_bin="${HEARTH_RPM:-/usr/bin/rpm}"
sha256_bin="${HEARTH_SHA256SUM:-/usr/bin/sha256sum}"

if [[ ! "$shell_sha256" =~ ^[0-9a-f]{64}$ ]]; then
  echo "HSN-001 requires an immutable Hearth Shell RPM URL and SHA-256" >&2
  exit 2
fi
if [[ ! "$shell_url" =~ ^https://github.com/akippnn/starlight-hearth-shell/releases/download/hearth-v0\.3\.0-rc\.[0-9]+/hearth-shell-0\.3\.0-.*\.x86_64\.rpm$ ]]; then
  echo "invalid HSN-001 Hearth Shell RPM URL: $shell_url" >&2
  exit 2
fi

workdir="$(mktemp -d /tmp/hearth-shell-install.XXXXXX)"
cleanup() {
  find "$workdir" -depth -delete
}
trap cleanup EXIT

rpm_path="$workdir/hearth-shell-0.3.0.x86_64.rpm"
"$curl_bin" --fail --location --proto '=https' --tlsv1.2 \
  --output "$rpm_path" "$shell_url"
printf '%s  %s\n' "$shell_sha256" "$rpm_path" | "$sha256_bin" --check -

"$dnf5_bin" install -y "$rpm_path"
"$rpm_bin" -q hearth-shell >/dev/null
