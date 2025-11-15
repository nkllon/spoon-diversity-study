from __future__ import annotations

import argparse
from pathlib import Path
import json
from . import validators
from . import __version__


def main() -> None:
	parser = argparse.ArgumentParser(prog="spoon-diversity", description="Spoon Diversity Study CLI")
	parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
	parser.add_argument("--quiet", action="store_true", help="Suppress non-error output")
	parser.add_argument("--json", dest="json_out", action="store_true", help="Emit JSON output summary")
	parser.add_argument("--config", help="Path to TOML config with artifact paths", default=None)
	subparsers = parser.add_subparsers(dest="command", required=True)

	p_validate = subparsers.add_parser("validate", help="Validate core study artifacts")
	p_validate.add_argument("--ttl", required=False)
	p_validate.add_argument("--csv", required=False)
	p_validate.add_argument("--puml", required=False)
	p_validate.add_argument("--mmd", required=False)
	p_validate.add_argument("--dot", required=False)
	p_validate.add_argument("--shapes", required=False, default=None)
	p_validate.add_argument("--all", action="store_true", help="Use repository defaults (v0.4) for all artifact paths")

	p_sync = subparsers.add_parser("sync", help="Generate/update data dictionary from CSV header")
	p_sync.add_argument("--ontology", required=True)
	p_sync.add_argument("--csv", required=True)
	p_sync.add_argument("--dict", required=True)

	args = parser.parse_args()
	# Optional config load (TOML)
	cfg: dict[str, str] = {}
	if args.config:
		try:
			try:
				import tomllib  # type: ignore[attr-defined]
			except Exception:
				import tomli as tomllib  # type: ignore
			cfg_data = Path(args.config).read_bytes()
			cfg = tomllib.loads(cfg_data.decode("utf-8")).get("artifacts", {})
		except Exception as exc:
			raise SystemExit(f"Failed to load config: {exc}")

	if args.command == "validate":
		# Resolve defaults
		defval = {
			"ttl": "spore_SpoonDiversityOntology_v0.4.ttl",
			"csv": "spoon_diversity_dataset_template_v0.4.csv",
			"puml": "spoon_experiment_workflow_v0.4.puml",
			"mmd": "spoon_analysis_pipeline_v0.4.mmd",
			"dot": "ontology_hierarchy_v0.4.dot",
			"shapes": "spoon_shapes_v0.4.ttl",
		}
		ttl = args.ttl or cfg.get("ttl") or (defval["ttl"] if args.all else None)
		csv = args.csv or cfg.get("csv") or (defval["csv"] if args.all else None)
		puml = args.puml or cfg.get("puml") or (defval["puml"] if args.all else None)
		mmd = args.mmd or cfg.get("mmd") or (defval["mmd"] if args.all else None)
		dot = args.dot or cfg.get("dot") or (defval["dot"] if args.all else None)
		shapes = args.shapes or cfg.get("shapes") or (defval["shapes"] if args.all else None)
		for name, val in [("ttl", ttl), ("csv", csv), ("puml", puml), ("mmd", mmd), ("dot", dot)]:
			if not val:
				parser.error(f"Missing required argument: --{name} (use --all or --config to supply defaults)")
		args.ttl, args.csv, args.puml, args.mmd, args.dot, args.shapes = ttl, csv, puml, mmd, dot, shapes
		results = {"ttl": None, "csv": None, "puml": None, "mmd": None, "dot": None, "shapes": None}
		try:
			validators.validate_ttl(args.ttl)
			results["ttl"] = "ok"
			validators.validate_csv(args.csv, args.ttl)
			results["csv"] = "ok"
			validators.validate_puml(args.puml)
			results["puml"] = "ok"
			validators.validate_mermaid(args.mmd)
			results["mmd"] = "ok"
			validators.validate_dot(args.dot)
			results["dot"] = "ok"
			if args.shapes:
				validators.validate_shapes(args.ttl, args.shapes)
				results["shapes"] = "ok"
		except Exception as exc:
			if args.json_out:
				print(json.dumps({"ok": False, "error": str(exc), "results": results}, indent=2))
			else:
				if not args.quiet:
					print("❌ validate: failed")
				raise
		else:
			if args.json_out:
				print(json.dumps({"ok": True, "results": results}, indent=2))
			else:
				if not args.quiet:
					print("✅ validate: all checks passed.")
	elif args.command == "sync":
		out_path = Path(args.dict)
		out_path.parent.mkdir(parents=True, exist_ok=True)
		validators.generate_dictionary(args.csv, args.dict, args.ontology)
		print(f"✅ sync: updated {args.dict}")
	else:
		parser.error("Unknown command")


