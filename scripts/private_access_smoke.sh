#!/usr/bin/env bash
set -euo pipefail

host="${1:?usage: private_access_smoke.sh HOST USER}"
user="${2:?usage: private_access_smoke.sh HOST USER}"

if [[ ! "$host" =~ ^[A-Za-z0-9][A-Za-z0-9.-]*$ ]]; then
  echo "Target must be a Tailscale DNS name or hostname; received an invalid value." >&2
  exit 2
fi
if [[ ! "$user" =~ ^[a-z_][a-z0-9_-]*[$]?$ ]]; then
  echo "Target user must be a valid non-root local account name." >&2
  exit 2
fi
if [[ "$user" == "root" ]]; then
  echo "Direct root access is intentionally not supported." >&2
  exit 2
fi

printf 'Checking tailnet connectivity to %s as %s…\n' "$host" "$user"
tailscale ping --timeout=10s "$host"

# Tailscale SSH authenticates the runner node under the tailnet policy; no SSH key
# or public inbound SSH port is needed. This command intentionally makes no changes.
tailscale ssh "${user}@${host}" 'printf "private access OK: "; hostname; id'
