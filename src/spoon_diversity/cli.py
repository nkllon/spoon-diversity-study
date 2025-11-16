from __future__ import annotations

import argparse
from pathlib import Path
from . import validators


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="spoon-diversity", description="Spoon Diversity Study CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_validate = subparsers.add_parser("validate", help="Validate core study artifacts")
    p_validate.add_argument("--ttl", required=True)
    p_validate.add_argument("--csv", required=True)
    p_validate.add_argument("--puml", required=True)
    p_validate.add_argument("--mmd", required=True)
    p_validate.add_argument("--dot", required=True)
    p_validate.add_argument("--shapes", required=False, default=None)

    p_sync = subparsers.add_parser("sync", help="Generate/update data dictionary from CSV header")
    p_sync.add_argument("--ontology", required=True)  # kept for parity; unused
    p_sync.add_argument("--csv", required=True)
    p_sync.add_argument("--dict", required=True)

    args = parser.parse_args()

    if args.command == "validate":
        validators.validate_ttl(args.ttl)
        validators.validate_csv_header(args.csv)
        validators.validate_puml(args.puml)
        validators.validate_mermaid(args.mmd)
        validators.validate_dot(args.dot)
        if args.shapes:
            validators.validate_shapes(args.shapes)
        print("✅ validate: all checks passed.")
    elif args.command == "sync":
        out_path = Path(args.dict)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        validators.generate_dictionary(args.csv, args.dict)
        print(f"✅ sync: updated {args.dict}")
    else:
        parser.error("Unknown command")


if __name__ == "__main__":
    main()
