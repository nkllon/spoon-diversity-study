from __future__ import annotations

from pathlib import Path
from typing import Tuple, Set


def require_file(path: str | Path) -> None:
	path = Path(path)
	if not path.is_file():
		raise FileNotFoundError(f"File not found: {path}")


def _load_rdf_graph(ttl_path: str | Path):
	"""
	Load a TTL file into an rdflib Graph. Raises ValueError with readable context on failure.
	"""
	try:
		from rdflib import Graph  # type: ignore
		graph = Graph()
	except Exception as exc:  # pragma: no cover
		raise RuntimeError("rdflib is required for TTL validation. Please install rdflib.") from exc
	path = Path(ttl_path)
	require_file(path)
	try:
		graph.parse(path.as_posix(), format="turtle")
	except Exception as exc:
		raise ValueError(f"TTL validation failed: RDF parse error in {path}: {exc}") from exc
	return graph


def validate_ttl(ttl_path: str | Path) -> None:
	# Parse to ensure syntactic validity
	_load_rdf_graph(ttl_path)


def validate_csv_header(csv_path: str | Path) -> None:
	require_file(csv_path)
	expected = (
		"ParticipantID,HandSize_cm,TaskID,ToolSet,Time_s,NumOperations,ErrorRate_pct,"
		"SwitchCount,SwitchTime_s,PerceivedCognitiveCost,PerceivedDiscomfort"
	)
	first = Path(csv_path).read_text(encoding="utf-8", errors="ignore").splitlines()[0].strip()
	if first != expected:
		raise ValueError(f"CSV validation failed: header mismatch.\nExpected: {expected}\nActual:   {first}")


def validate_puml(puml_path: str | Path) -> None:
	require_file(puml_path)
	content = Path(puml_path).read_text(encoding="utf-8", errors="ignore")
	if "@startuml" not in content or "@enduml" not in content:
		raise ValueError("PUML validation failed: missing @startuml/@enduml")
	if ("->" not in content) and ("-->" not in content):
		raise ValueError("PUML validation failed: no transitions found (expected '->' or '-->')")


def validate_mermaid(mmd_path: str | Path) -> None:
	require_file(mmd_path)
	first = Path(mmd_path).read_text(encoding="utf-8", errors="ignore").splitlines()[0]
	if not (first.startswith("flowchart") or first.startswith("graph")):
		raise ValueError("Mermaid validation failed: expected 'flowchart' or 'graph' on first line")
	content = Path(mmd_path).read_text(encoding="utf-8", errors="ignore")
	if "-->" not in content:
		raise ValueError("Mermaid validation failed: no edges found ('-->')")


def validate_dot(dot_path: str | Path) -> None:
	require_file(dot_path)
	first = Path(dot_path).read_text(encoding="utf-8", errors="ignore")
	if "digraph" not in first:
		raise ValueError("DOT validation failed: missing 'digraph' keyword")
	if ":" not in first:
		raise ValueError("DOT validation failed: expected at least one namespaced label (e.g., 'sp:Class')")


def validate_shapes(ttl_path: str | Path, shapes_path: str | Path | None) -> None:
	if not shapes_path:
		return
	data_graph = _load_rdf_graph(ttl_path)
	shapes_graph = _load_rdf_graph(shapes_path)
	try:
		from pyshacl import validate as shacl_validate  # type: ignore
	except Exception as exc:  # pragma: no cover
		raise RuntimeError("pyshacl is required for SHACL validation. Please install pyshacl.") from exc
	conforms, _, report_text = shacl_validate(
		data_graph=data_graph,
		shacl_graph=shapes_graph,
		inference="rdfs",
		advanced=True,
		abort_on_first=False,
		meta_shacl=False,
		debug=False,
	)
	if not conforms:
		raise ValueError(f"SHACL validation failed:\n{report_text}")


def _get_vocab_from_ttl(ttl_path: str | Path) -> Tuple[Set[str], Set[str]]:
	from rdflib import Namespace, RDF, Literal  # type: ignore
	g = _load_rdf_graph(ttl_path)
	SP = Namespace("http://example.org/spore/Spore001#")
	SCHEMA = Namespace("http://schema.org/")
	def collect(catalog_local: str) -> Set[str]:
		items: Set[str] = set()
		catalog_class = SP[catalog_local]
		for s in g.subjects(RDF.type, catalog_class):
			for _, _, ident in g.triples((s, SCHEMA["identifier"], None)):
				if isinstance(ident, Literal) and str(ident).strip():
					items.add(str(ident).strip())
		return items
	return collect("ToolSetCatalog"), collect("TaskCatalog")


def generate_json_schema_from_shacl(shapes_path: str | Path, out_path: str | Path) -> None:
	"""
	Generate a minimal JSON Schema representation from SHACL shapes to assist CSV validation tooling.
	This focuses on the known properties used by the study schema.
	"""
	from rdflib import Namespace, RDF, Literal  # type: ignore

	require_file(shapes_path)
	g = _load_rdf_graph(shapes_path)
	SH = Namespace("http://www.w3.org/ns/shacl#")
	SP = Namespace("http://example.org/spore/Spore001#")

	property_specs = []
	for node_shape in g.subjects(RDF.type, SH.NodeShape):
		for _, _, prop_bnode in g.triples((node_shape, SH.property, None)):
			spec: dict[str, object] = {}
			for _, _, path in g.triples((prop_bnode, SH.path, None)):
				spec["path"] = str(path)
			for _, _, dtype in g.triples((prop_bnode, SH.datatype, None)):
				spec["datatype"] = str(dtype)
			for _, _, min_inc in g.triples((prop_bnode, SH.minInclusive, None)):
				if isinstance(min_inc, Literal):
					spec["minInclusive"] = float(min_inc) if "." in str(min_inc) else int(min_inc)
			for _, _, max_inc in g.triples((prop_bnode, SH.maxInclusive, None)):
				if isinstance(max_inc, Literal):
					spec["maxInclusive"] = float(max_inc) if "." in str(max_inc) else int(max_inc)
			property_specs.append(spec)

	# Map to JSON Schema-ish constraints
	def map_datatype(dt: str) -> str:
		if dt.endswith("#integer"):
			return "integer"
		if dt.endswith("#decimal") or dt.endswith("#float") or dt.endswith("#double"):
			return "number"
		return "string"

	properties: dict[str, dict] = {}
	required: list[str] = []
	column_for_path = {
		str(SP["handSizeCm"]): "HandSize_cm",
		str(SP["timeSeconds"]): "Time_s",
		str(SP["numOperations"]): "NumOperations",
		str(SP["errorRatePercent"]): "ErrorRate_pct",
		str(SP["switchCount"]): "SwitchCount",
		str(SP["switchTimeSeconds"]): "SwitchTime_s",
		str(SP["perceivedCognitiveCost"]): "PerceivedCognitiveCost",
		str(SP["perceivedDiscomfort"]): "PerceivedDiscomfort",
	}
	for spec in property_specs:
		path = spec.get("path")
		col = column_for_path.get(path) if isinstance(path, str) else None
		if not col:
			continue
		entry: dict[str, object] = {"type": map_datatype(str(spec.get("datatype", "")))}
		if "minInclusive" in spec:
			entry["minimum"] = spec["minInclusive"]
		if "maxInclusive" in spec:
			entry["maximum"] = spec["maxInclusive"]
		properties[col] = entry

	schema = {
		"$schema": "https://json-schema.org/draft/2020-12/schema",
		"title": "Spoon Diversity CSV Row Schema",
		"type": "object",
		"properties": properties,
		"required": required,
		"additionalProperties": True,
	}
	Path(out_path).write_text(__import__("json").dumps(schema, indent=2), encoding="utf-8")

def generate_dictionary(csv_path: str | Path, out_path: str | Path, ontology_ttl: str | Path | None = None) -> None:
	require_file(csv_path)
	header = Path(csv_path).read_text(encoding="utf-8", errors="ignore").splitlines()[0].strip()
	columns = header.split(",")
	lines = ["# Spoon Diversity Data Dictionary (auto)", "", "Generated by spoon-diversity CLI.", "", "## Columns"]
	mappings = {
		"ParticipantID": ("string", "", "schema:identifier (sp:Participant)"),
		"HandSize_cm": ("decimal >= 0", "cm", "sp:handSizeCm"),
		"TaskID": ("string", "", "sp:Task (identifier)"),
		"ToolSet": ("string", "", "sp:ToolSet (identifier)"),
		"Time_s": ("decimal >= 0", "s", "sp:timeSeconds"),
		"NumOperations": ("integer >= 0", "count", "sp:numOperations"),
		"ErrorRate_pct": ("decimal 0–100", "%", "sp:errorRatePercent"),
		"SwitchCount": ("integer >= 0", "count", "sp:switchCount"),
		"SwitchTime_s": ("decimal >= 0", "s", "sp:switchTimeSeconds"),
		"PerceivedCognitiveCost": ("integer 1–7", "Likert", "sp:perceivedCognitiveCost"),
		"PerceivedDiscomfort": ("integer 1–7", "Likert", "sp:perceivedDiscomfort"),
	}
	labels: dict[str, str] = {}
	comments: dict[str, str] = {}
	if ontology_ttl:
		try:
			from rdflib import Namespace, RDFS  # type: ignore
			g = _load_rdf_graph(ontology_ttl)
			SP = Namespace("http://example.org/spore/Spore001#")
			prop_map = {
				"HandSize_cm": SP["handSizeCm"],
				"Time_s": SP["timeSeconds"],
				"NumOperations": SP["numOperations"],
				"ErrorRate_pct": SP["errorRatePercent"],
				"SwitchCount": SP["switchCount"],
				"SwitchTime_s": SP["switchTimeSeconds"],
				"PerceivedCognitiveCost": SP["perceivedCognitiveCost"],
				"PerceivedDiscomfort": SP["perceivedDiscomfort"],
			}
			for col, prop in prop_map.items():
				for _, _, lab in g.triples((prop, RDFS.label, None)):
					labels[col] = str(lab)
				for _, _, com in g.triples((prop, RDFS.comment, None)):
					comments[col] = str(com)
		except Exception:
			# If ontology parsing fails, proceed without enrichment
			pass
	for col in columns:
		type_str, unit, mapping = mappings.get(col, ("string", "", ""))
		label = labels.get(col, "")
		comment = comments.get(col, "")
		extra = []
		if label:
			extra.append(f"- Label: {label}")
		if comment:
			extra.append(f"- Description: {comment}")
		lines.append(f"### {col}\n- Type: {type_str}\n- Unit: {unit}\n- Mapping: {mapping}\n" + ("\n".join(extra) + ("\n" if extra else "")))
	lines.append("## Missing-Value Policy")
	lines.append("- Use empty cells for missing numeric values; do not use NaN.")
	lines.append("- Use 'NA' for categorical unknowns where applicable.")
	Path(out_path).write_text("\n".join(lines), encoding="utf-8")


def validate_csv(csv_path: str | Path, ttl_path: str | Path) -> None:
	import csv
	validate_csv_header(csv_path)
	toolsets, tasks = _get_vocab_from_ttl(ttl_path)
	with Path(csv_path).open("r", encoding="utf-8", errors="ignore", newline="") as f:
		reader = csv.DictReader(f)
		for idx, row in enumerate(reader, start=2):
			def fail(col: str, msg: str) -> None:
				raise ValueError(f"CSV validation failed at row {idx} column '{col}': {msg}")
			if not row["ParticipantID"]:
				fail("ParticipantID", "missing")
			try:
				if row["HandSize_cm"] != "":
					val = float(row["HandSize_cm"])
					if val < 0:
						fail("HandSize_cm", "must be >= 0")
			except Exception:
				fail("HandSize_cm", "must be a decimal number")
			if tasks and row["TaskID"] not in tasks:
				fail("TaskID", f"not in controlled list {sorted(tasks)}")
			if toolsets and row["ToolSet"] not in toolsets:
				fail("ToolSet", f"not in controlled list {sorted(toolsets)}")
			try:
				if row["Time_s"] != "":
					val = float(row["Time_s"])
					if val < 0:
						fail("Time_s", "must be >= 0")
			except Exception:
				fail("Time_s", "must be a decimal number")
			try:
				if row["NumOperations"] != "":
					val = int(row["NumOperations"])
					if val < 0:
						fail("NumOperations", "must be >= 0")
			except Exception:
				fail("NumOperations", "must be an integer")
			try:
				if row["ErrorRate_pct"] != "":
					val = float(row["ErrorRate_pct"])
					if val < 0 or val > 100:
						fail("ErrorRate_pct", "must be between 0 and 100")
			except Exception:
				fail("ErrorRate_pct", "must be a decimal number")
			try:
				if row["SwitchCount"] != "":
					val = int(row["SwitchCount"])
					if val < 0:
						fail("SwitchCount", "must be >= 0")
			except Exception:
				fail("SwitchCount", "must be an integer")
			try:
				if row["SwitchTime_s"] != "":
					val = float(row["SwitchTime_s"])
					if val < 0:
						fail("SwitchTime_s", "must be >= 0")
			except Exception:
				fail("SwitchTime_s", "must be a decimal number")
			try:
				if row["PerceivedCognitiveCost"] != "":
					val = int(row["PerceivedCognitiveCost"])
					if val < 1 or val > 7:
						fail("PerceivedCognitiveCost", "must be 1–7")
			except Exception:
				fail("PerceivedCognitiveCost", "must be an integer")
			try:
				if row["PerceivedDiscomfort"] != "":
					val = int(row["PerceivedDiscomfort"])
					if val < 1 or val > 7:
						fail("PerceivedDiscomfort", "must be 1–7")
			except Exception:
				fail("PerceivedDiscomfort", "must be an integer")


