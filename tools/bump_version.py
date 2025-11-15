#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


def replace_in_file(path: Path, patterns: list[tuple[str, str]]) -> int:
	text = path.read_text(encoding="utf-8")
	orig = text
	for pat, repl in patterns:
		text = re.sub(pat, repl, text)
	if text != orig:
		path.write_text(text, encoding="utf-8")
		return 1
	return 0


def main() -> int:
	if len(sys.argv) != 3:
		print("Usage: tools/bump_version.py <old_version> <new_version> (e.g., v0.4 v0.5)", file=sys.stderr)
		return 2
	old, new = sys.argv[1], sys.argv[2]
	root = Path(__file__).resolve().parents[1]
	changed = 0

	# Update artifact filenames references (markdown, makefile, docs)
	patterns = [
		(fr"spore_SpoonDiversityOntology_{re.escape(old)}\.ttl", f"spore_SpoonDiversityOntology_{new}.ttl"),
		(fr"spoon_shapes_{re.escape(old)}\.ttl", f"spoon_shapes_{new}.ttl"),
		(fr"spoon_diversity_dataset_template_{re.escape(old)}\.csv", f"spoon_diversity_dataset_template_{new}.csv"),
		(fr"spoon_experiment_workflow_{re.escape(old)}\.puml", f"spoon_experiment_workflow_{new}.puml"),
		(fr"spoon_analysis_pipeline_{re.escape(old)}\.mmd", f"spoon_analysis_pipeline_{new}.mmd"),
		(fr"ontology_hierarchy_{re.escape(old)}\.dot", f"ontology_hierarchy_{new}.dot"),
		(fr"spoon_diversity_data_dictionary_{re.escape(old)}\.md", f"spoon_diversity_data_dictionary_{new}.md"),
		(fr"spoon_spore_registry_{re.escape(old)}\.ttl", f"spoon_spore_registry_{new}.ttl"),
		(fr"guidance_spoon_{re.escape(old)}\.ttl", f"guidance_spoon_{new}.ttl"),
	]
	targets = list(root.glob("**/*.*"))
	for path in targets:
		if path.suffix.lower() in {".md", ".txt", ".yml", ".yaml", ".toml", ".puml", ".mmd", ".dot"}:
			changed += replace_in_file(path, patterns)
	print(f"Updated references in {changed} files.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())

