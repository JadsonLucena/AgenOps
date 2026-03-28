#!/usr/bin/env bash
set -euo pipefail

log() {
  printf '[%s] %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*"
}

repo_root() {
  git rev-parse --show-toplevel 2>/dev/null || pwd
}
