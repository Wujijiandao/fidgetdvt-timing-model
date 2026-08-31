
import sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve()
CURRENT=HERE.parents[1]/"current"
sys.path.insert(0,str(CURRENT))

from macro_human_validation_v0_7 import flow_deficit, simulate_age_reset_schedule, heldout_airline_predictions

def test_baseline_anchors():
    assert abs(float(flow_deficit(65))-0.29)<1e-12
    assert abs(float(flow_deficit(100))-0.42)<1e-12

def test_heldout_predictions():
    p=heldout_airline_predictions()
    assert abs(p[85]-float(flow_deficit(25)))<1e-12
    assert abs(p[100]-float(flow_deficit(40)))<1e-12

def test_complete_reset_uniform_benchmark():
    T=100.
    uniform=(T/6)*np.arange(1,6)
    clustered=np.array([48.,49.,50.,51.,52.])
    bu=simulate_age_reset_schedule(uniform,T,1.0)["mean_flow_deficit"]
    bc=simulate_age_reset_schedule(clustered,T,1.0)["mean_flow_deficit"]
    assert bu < bc

def test_partial_reset_less_effective():
    events=np.array([20.,40.,60.,80.])
    full=simulate_age_reset_schedule(events,100,1.0)["final_flow_deficit"]
    partial=simulate_age_reset_schedule(events,100,0.5)["final_flow_deficit"]
    assert partial > full

def test_deficit_monotone():
    x=np.linspace(0,120,500)
    y=flow_deficit(x)
    assert np.all(np.diff(y)>=-1e-12)
