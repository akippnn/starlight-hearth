#!/usr/bin/env bash
set -euo pipefail

readonly default_url="https://github.com/akippnn/starlight-hearth-shell/releases/download/hearth-v0.1.0-7/starlight-hearth-shell-0.1.0-1.fc44.x86_64.rpm"
readonly default_sha256="22f38a85e78928fb00fbe7b59467b2a0c0794ae887687f34fc87c55c02d72603"

shell_url="${HEARTH_SHELL_URL:-$default_url}"
shell_sha256="${HEARTH_SHELL_SHA256:-$default_sha256}"
curl_bin="${HEARTH_CURL:-/usr/bin/curl}"
dnf5_bin="${HEARTH_DNF5:-/usr/bin/dnf5}"
rpm_bin="${HEARTH_RPM:-/usr/bin/rpm}"
sha256_bin="${HEARTH_SHA256SUM:-/usr/bin/sha256sum}"

if [[ ! "$shell_sha256" =~ ^[0-9a-f]{64}$ ]]; then
  echo "invalid Hearth Shell SHA-256: $shell_sha256" >&2
  exit 2
fi

workdir="$(mktemp -d /tmp/hearth-shell-install.XXXXXX)"
cleanup() {
  find "$workdir" -depth -delete
}
trap cleanup EXIT

rpm_path="$workdir/starlight-hearth-shell-0.1.0-1.fc44.x86_64.rpm"
"$curl_bin" --fail --location --proto '=https' --tlsv1.2 \
  --output "$rpm_path" "$shell_url"
printf '%s  %s\n' "$shell_sha256" "$rpm_path" | "$sha256_bin" --check -

"$dnf5_bin" install -y "$rpm_path"
"$rpm_bin" -q starlight-hearth-shell >/dev/null
"$rpm_bin" -q --whatprovides dms >/dev/null
