# Requirements: Spoon Dataset v0.3

## 1. Schema
THE dataset SHALL follow the fixed header in `spoon_diversity_dataset_template_v0.3.csv`.

## 2. Units and Constraints
THE dataset SHALL use units and ranges defined in the data dictionary and ontology.

## 3. Sync
WHEN the CSV header changes THE system SHALL regenerate the data dictionary.

## 4. Encoding & Format
THE CSV SHALL be UTF-8 and RFC4180 compliant with the exact header line.

## 5. Constraints & Vocabularies
WHERE numeric columns exist THE values SHALL respect documented bounds; TaskID and ToolSet SHALL match ontology lists.

## 6. ParticipantID Pattern
THE ParticipantID SHALL match `^P\\d{3,}$`.

## 7. Missing Values
WHEN missing values occur THE representation SHALL follow the data dictionary.


