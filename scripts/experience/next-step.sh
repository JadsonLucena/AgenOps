#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
python3 "$ROOT/scripts/experience/state-router.py" --state-file "${KIT_STATE_FILE:-$HOME/.local/state/engineering-governance-kit/state.json}" next "$@"
