#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
STATE_FILE="${KIT_STATE_FILE:-$HOME/.local/state/engineering-governance-kit/state.json}"
python3 "$ROOT/scripts/experience/state-router.py" --state-file "$STATE_FILE" update phase=spec last_completed_step=brainstorm context_status=healthy
python3 "$ROOT/scripts/experience/state-router.py" --state-file "$STATE_FILE" next
