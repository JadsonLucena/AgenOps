#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
source "$ROOT/scripts/lib/common.sh"
log "Run tests"
if [ -n "${TEST_COMMAND:-}" ]; then
  eval "$TEST_COMMAND"
else
  log "TEST_COMMAND is not set"
  exit 1
fi
