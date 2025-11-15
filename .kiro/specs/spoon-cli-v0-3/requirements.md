# Requirements: Spoon CLI (spoon-diversity-tools) v0.3

## 1. Commands
THE CLI SHALL provide `validate` and `sync` commands.

## 2. Validate Arguments
THE CLI validate SHALL accept `--ttl --csv --puml --mmd --dot [--shapes]` and fail on violations.

## 3. Sync Arguments
THE CLI sync SHALL accept `--ontology --csv --dict` and regenerate the data dictionary from the CSV header.

## 4. Compatibility
THE package SHALL support Python 3.10–3.12 and install via `pip`.

## 5. Testing
THE package SHALL include tests with coverage ≥ 80% on src; produce coverage.xml.


