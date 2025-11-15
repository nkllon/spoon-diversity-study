from __future__ import annotations

import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
	cmd = [sys.executable, "-m", "spoon_diversity.cli", *args]
	return subprocess.run(cmd, check=False, capture_output=True, text=True)


def test_help():
	cp = run_cli("--help")
	assert cp.returncode == 0
	assert "Spoon Diversity Study CLI" in cp.stdout


