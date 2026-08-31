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
