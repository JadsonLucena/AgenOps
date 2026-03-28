#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
source "$ROOT/scripts/lib/common.sh"
log "Run sonar"
if [ -n "${SONAR_COMMAND:-}" ]; then
  eval "$SONAR_COMMAND"
else
  log "SONAR_COMMAND is not set"
  exit 1
fi
