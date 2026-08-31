# GitHub and Zenodo Release Metadata — v1.0.0

## GitHub repository

**Repository name**  
`fidgetdvt-timing-model`

**About / Description**  
Reproducible code and literature-derived data for a hierarchical timing model of intermittent lower-leg muscle-pump activation during prolonged sitting, with held-out human Doppler validation. Research software; not a clinical DVT risk calculator.

**Visibility**  
Public at archival release.

**Default branch**  
`main`

**License**  
MIT License

**Topics**  
`venous-hemodynamics`, `calf-muscle-pump`, `prolonged-sitting`, `biomechanics`, `biofluid-mechanics`, `doppler-ultrasound`, `venous-stasis`, `temporal-patterning`, `deep-vein-thrombosis`, `reproducible-research`, `scientific-python`, `computational-modeling`

**Suggested homepage after Zenodo archival**  
`https://doi.org/<ZENODO_DOI>`

## GitHub release

**Git tag**  
`v1.0.0`

**Target**  
`main`

**Release title**  
`v1.0.0 — Submission Release`

**Release notes**

## FidgetDVT Timing Model v1.0.0

This is the first frozen, reproducible release corresponding to the Journal of Biomechanics submission candidate:

**Temporal Patterning of Intermittent Lower-Leg Muscle-Pump Activation During Prolonged Sitting: A Hierarchical Timing Model with Held-Out Human Doppler Validation**

### Included in this release

- Canonical hierarchical timing model separating minute-scale movement-bout gaps from fast within-bout pump events.
- Human-anchored macro low-flow model derived from published popliteal Doppler data.
- Zero-refit held-out human Doppler schedule validation.
- Finite-reset robustness analysis and boundary-relaxed timing optimization.
- Evidence-constrained fast venous-refill model and the dimensionless micro-gap parameter `Pi = delta / tau_r`.
- Source-tagged literature-derived input tables.
- Manuscript-relevant numerical outputs and figures.
- Automated tests and a minimal reproduction entry point.

### Reproducibility status

- Test suite: **11/11 passed**.
- Held-out human Doppler validation: **MAE 1.31 percentage points**.
- No participant-level raw clinical data are redistributed.

### Interpretation boundary

This repository contains research software for venous-hemodynamic modeling. It does **not** estimate individual DVT or pulmonary-embolism probability, does not define a clinically safe sitting interval, and should not be used as a clinical decision tool.

### Citation and archival DOI

A Zenodo DOI will be added to the repository and citation metadata after the GitHub release is archived.


## Zenodo

Zenodo does not use a Git-style release tag. Use the GitHub tag `v1.0.0` and set the Zenodo **Version** field to `1.0.0`.

**Record title**  
`FidgetDVT Timing Model v1.0.0`

**Resource type**  
Software

**Version**  
`1.0.0`

**Creator**  
Zhang, Yuzhan — ORCID 0009-0000-3121-7972 — Independent Researcher, Beijing, China

**Access**  
Open

**License**  
MIT

**Language**  
English (`eng`)

**Keywords**  
venous hemodynamics; calf muscle pump; prolonged sitting; biomechanics; biofluid mechanics; Doppler ultrasound; venous stasis; temporal patterning; deep vein thrombosis; reproducible research; scientific Python; computational modeling

**Description**

Reproducible research software and literature-derived input data supporting the manuscript “Temporal Patterning of Intermittent Lower-Leg Muscle-Pump Activation During Prolonged Sitting: A Hierarchical Timing Model with Held-Out Human Doppler Validation.” The release contains the canonical hierarchical timing model, held-out human Doppler validation, finite-reset robustness analysis, evidence-constrained fast-refill calculations, source-tagged processed data tables, manuscript figures, automated tests, and a minimal reproduction entry point. The model distinguishes minute-scale spacing between effective lower-leg muscle-pump bouts from rapid within-bout pump events. It is a hemodynamic research model and does not estimate clinical DVT or pulmonary-embolism probability or define a safe sitting interval.

**Related identifier after article publication**  
Add the article DOI with relation `isSupplementTo` and resource type `publication-article`.

## Recommended release sequence

1. Create the public GitHub repository and push the frozen `repository_release_candidate/` contents to `main`.
2. Connect/enable that repository in Zenodo before creating the release.
3. Create GitHub tag `v1.0.0` and GitHub Release `v1.0.0 — Submission Release`.
4. Let Zenodo ingest the release and mint the version DOI and concept DOI.
5. Add the Zenodo DOI badge/link to README and update Data/Code Availability in the manuscript if publication timing permits.
