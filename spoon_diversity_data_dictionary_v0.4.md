# Spoon Diversity Data Dictionary (v0.4)

This file is generated from the CSV header via scripts/kiro spec:sync.

## Columns
### ParticipantID
- Type: string
- Unit: 
- Mapping: schema:identifier (sp:Participant)

### HandSize_cm
- Type: decimal >= 0
- Unit: cm
- Mapping: sp:handSizeCm

### TaskID
- Type: string
- Unit: 
- Mapping: sp:Task (identifier)

### ToolSet
- Type: string
- Unit: 
- Mapping: sp:ToolSet (identifier)

### Time_s
- Type: decimal >= 0
- Unit: s
- Mapping: sp:timeSeconds

### NumOperations
- Type: integer >= 0
- Unit: count
- Mapping: sp:numOperations

### ErrorRate_pct
- Type: decimal 0–100
- Unit: %
- Mapping: sp:errorRatePercent

### SwitchCount
- Type: integer >= 0
- Unit: count
- Mapping: sp:switchCount

### SwitchTime_s
- Type: decimal >= 0
- Unit: s
- Mapping: sp:switchTimeSeconds

### PerceivedCognitiveCost
- Type: integer 1–7
- Unit: Likert
- Mapping: sp:perceivedCognitiveCost

### PerceivedDiscomfort
- Type: integer 1–7
- Unit: Likert
- Mapping: sp:perceivedDiscomfort

## Missing-Value Policy
- Use empty cells for missing numeric values; do not use NaN.
- Use 'NA' for categorical unknowns where applicable.

