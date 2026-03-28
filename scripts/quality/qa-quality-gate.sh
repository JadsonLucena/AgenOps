#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
source "$ROOT/scripts/lib/common.sh"

log "Quality gate started"

"$ROOT/scripts/quality/run-lint.sh"
"$ROOT/scripts/quality/run-tests.sh"

if [ -n "${SONAR_COMMAND:-}" ]; then
  "$ROOT/scripts/quality/run-sonar.sh"
else
  log "Skipping sonar because SONAR_COMMAND is not set"
fi

log "Quality gate passed"
