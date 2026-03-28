#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import runpy

# Compatibility wrapper.
# Canonical executable lives at scripts/experience/state-router.py.
runpy.run_path(str(Path(__file__).resolve().parents[2] / "scripts/experience/state-router.py"), run_name="__main__")
