#!/usr/bin/env python3
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/"src"))

from macro_human_validation_v0_7 import heldout_airline_predictions

obs = {45.0:0.22, 85.0:0.10, 100.0:0.17}
pred = heldout_airline_predictions()
rows=[]
for t in (45.0,85.0,100.0):
    rows.append({
        "time_min": t,
        "observed_fractional_deficit": obs[t],
        "predicted_fractional_deficit": pred[t],
        "absolute_error_percentage_points": abs(pred[t]-obs[t])*100,
    })

out = pd.DataFrame(rows)
(ROOT/"results").mkdir(exist_ok=True)
out.to_csv(ROOT/"results"/"heldout_validation_reproduced.csv", index=False)
print(out.to_string(index=False))
print("MAE percentage points:", out["absolute_error_percentage_points"].mean())
