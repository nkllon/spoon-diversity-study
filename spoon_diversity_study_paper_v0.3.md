# Minimal Tool‑Set Diversity: A Spoon‑Size Case Study

## Methods

### Participants
We will recruit adult participants (N determined by power analysis), record basic demographics as permitted, and measure dominant-hand size in centimeters (palm breadth).

### Apparatus and Tool Sets
Tool sets consist of one or more spoon variants differing in morphology (e.g., bowl size, handle geometry). Each `ToolSet` is identified and described in study documentation.

### Tasks
Participants perform a standardized scooping task on granular material with controlled quantity and receptacle dimensions. Tasks are counterbalanced across tool sets and participants.

### Procedure
Participants are recruited and consented, then hand size is measured. The experiment proceeds through a sequence of trials per participant:
1) Brief task and switching rules
2) For each counterbalanced ToolSet × Task combination:
   - Run the trial
   - Record Time_s, NumOperations, ErrorRate_pct
   - Permit and record tool switches (SwitchCount, SwitchTime_s)
3) Post-survey for perceived cognitive cost and discomfort (Likert 1–7).

### Measures
The dataset schema is defined in `spoon_diversity_dataset_template_v0.3.csv`:
- ParticipantID, HandSize_cm, TaskID, ToolSet, Time_s, NumOperations, ErrorRate_pct, SwitchCount, SwitchTime_s, PerceivedCognitiveCost, PerceivedDiscomfort.
Ontology mappings: participants (`schema:identifier`, `sp:handSizeCm`), trials (`prov:Activity`), observations (`sosa:Observation` with `sp:*` properties).

### Analysis Plan
Data ingestion and validation; compute derived metrics (operations/sec, errors/op, switch rate, switch overhead fraction). Primary analyses via repeated-measures ANOVA or linear mixed models with hand size as covariate. Report effect sizes and adjusted p-values. Visualize distributions (boxplots, ECDF) and switching dynamics.

### Ethics
Obtain informed consent, anonymize data (ParticipantID pseudonyms), and store records per institutional policy.

### Reproducibility
Ontology (`spore_SpoonDiversityOntology_v0.3.ttl`) and diagrams are versioned with this repository. Analysis steps are documented in `spoon_analysis_pipeline_v0.3.mmd`. The data dictionary is provided in `spoon_diversity_data_dictionary_v0.3.md`.
