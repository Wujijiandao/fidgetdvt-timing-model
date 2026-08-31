# FidgetDVT Timing Model

Reproducible code and literature-derived data for the manuscript:

**Temporal Patterning of Intermittent Lower-Leg Muscle-Pump Activation During Prolonged Sitting: A Hierarchical Timing Model with Held-Out Human Doppler Validation**

**Author:** Yuzhan Zhang  
**Affiliation:** Independent Researcher, Beijing, China  
**ORCID:** https://orcid.org/0009-0000-3121-7972

## Scope

This repository contains a reduced biomechanics framework for studying the temporal organization of intermittent lower-leg muscle-pump activation during prolonged sitting. The model separates minute-scale gaps between effective movement bouts from rapid within-bout pump events and includes a held-out human Doppler validation.

> **Research-use boundary:** this repository does not estimate individual DVT or pulmonary-embolism probability, does not define a clinically safe sitting interval, and is not a clinical decision tool.

## Main reproducible results

- Complete-reset timing benchmark based on convex cumulative low-flow burden.
- Held-out human popliteal Doppler schedule validation (MAE 1.31 percentage points).
- Finite-reset robustness and boundary-relaxed timing optimization.
- Evidence-constrained fast-refill analysis using the dimensionless interval `Pi = delta / tau_r`.

## Repository structure

- `src/` — canonical model code
- `tests/` — automated tests
- `data/` — source-tagged literature-derived input tables
- `results/` — manuscript-relevant processed outputs
- `figures/` — final manuscript figures
- `reproduce_all.py` — minimal reproduction entry point

## Reproduce

```bash
python -m pip install -r requirements.txt
python reproduce_all.py
python -m pytest -q
```

The frozen release passes 11/11 automated tests.

## Data provenance

The repository contains processed values extracted from published literature. No participant-level raw clinical dataset is redistributed. Source information and interpretation limits are included with the data tables.

## Citation

Use GitHub's **Cite this repository** metadata (`CITATION.cff`) and, after archival, cite the Zenodo release DOI. The article citation will be added when available.

## License

MIT License. See `LICENSE`.
