from __future__ import annotations

from pathlib import Path
import json
import pytest

from spoon_diversity import validators
from .test_cli import run_cli


FIX = Path(__file__).parent / "fixtures"


def test_ttl_and_shacl_validation_ok():
	ttl = FIX / "valid.ttl"
	shapes = FIX / "valid_shapes.ttl"
	validators.validate_ttl(ttl)
	# SHACL shapes may not target any data here; should still conform
	validators.validate_shapes(ttl, shapes)


def test_ttl_parse_fails():
	with pytest.raises(Exception):
		validators.validate_ttl(FIX / "invalid.ttl")


def test_csv_validation_ok():
	ttl = FIX / "valid.ttl"
	csv_path = FIX / "valid.csv"
	validators.validate_csv(csv_path, ttl)


@pytest.mark.parametrize("col,msg", [
	("HandSize_cm", ">= 0"),
	("TaskID", "controlled"),
	("Time_s", ">= 0"),
	("NumOperations", "integer"),
	("ErrorRate_pct", "between 0 and 100"),
	("SwitchCount", "integer"),
	("SwitchTime_s", ">= 0"),
	("PerceivedCognitiveCost", "1–7"),
	("PerceivedDiscomfort", "1–7"),
])
def test_csv_validation_bad_values(col: str, msg: str):
	ttl = FIX / "valid.ttl"
	csv_path = FIX / "invalid.csv"
	with pytest.raises(ValueError) as ei:
		validators.validate_csv(csv_path, ttl)
	assert col in str(ei.value)


def test_diagram_validations_ok():
	validators.validate_puml(FIX / "valid.puml")
	validators.validate_mermaid(FIX / "valid.mmd")
	validators.validate_dot(FIX / "valid.dot")


def test_diagram_validations_fail():
	with pytest.raises(ValueError):
		validators.validate_puml(FIX / "invalid.puml")
	with pytest.raises(ValueError):
		validators.validate_mermaid(FIX / "invalid.mmd")
	with pytest.raises(ValueError):
		validators.validate_dot(FIX / "invalid.dot")


def test_cli_validate_json_ok(tmp_path: Path):
	# Use repo top-level real artifacts for an end-to-end smoke with JSON output
	root = Path(__file__).resolve().parents[1]
	cp = run_cli(
		"validate",
		"--ttl", str(root / "spore_SpoonDiversityOntology_v0.3.ttl"),
		"--csv", str(root / "examples" / "spoon_diversity_sample_v0.3.csv"),
		"--puml", str(root / "spoon_experiment_workflow_v0.3.puml"),
		"--mmd", str(root / "spoon_analysis_pipeline_v0.3.mmd"),
		"--dot", str(root / "ontology_hierarchy_v0.3.dot"),
		"--shapes", str(root / "spoon_shapes_v0.3.ttl"),
		"--json",
	)
	assert cp.returncode == 0
	out = json.loads(cp.stdout)
	assert out["ok"] is True
	assert out["results"]["ttl"] == "ok"


def test_cli_validate_failure_returns_nonzero():
	root = Path(__file__).resolve().parents[1]
	cp = run_cli(
		"validate",
		"--ttl", str(FIX / "invalid.ttl"),
		"--csv", str(FIX / "valid.csv"),
		"--puml", str(FIX / "valid.puml"),
		"--mmd", str(FIX / "valid.mmd"),
		"--dot", str(FIX / "valid.dot"),
	)
	assert cp.returncode != 0


