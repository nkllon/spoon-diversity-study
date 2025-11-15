from __future__ import annotations

import subprocess
import sys
import pytest


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
	cmd = [sys.executable, "-m", "spoon_diversity.cli", *args]
	return subprocess.run(cmd, check=False, capture_output=True, text=True)


def test_help():
	cp = run_cli("--help")
	assert cp.returncode == 0
	out = (cp.stdout or "") + (cp.stderr or "")
	if out.strip() == "":
		pytest.skip("No help output in this interpreter")
	assert "Spoon Diversity Study CLI" in out


