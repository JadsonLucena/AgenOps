#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
source "$ROOT/scripts/lib/common.sh"
log "Run lint"
if [ -n "${LINT_COMMAND:-}" ]; then
  eval "$LINT_COMMAND"
else
  log "LINT_COMMAND is not set"
  exit 1
fi
