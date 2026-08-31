import math
import sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve()
CURRENT=HERE.parents[1]/"current"
sys.path.insert(0,str(CURRENT))

from hierarchical_timing_model import (
    tau_from_t95, empirical_flow_deficit, ideal_reset_schedule_burden,
    microevent_bout, uniform_event_times
)

def test_t95_conversion():
    assert abs(tau_from_t95(1.54)-1.54/math.log(20)) < 1e-12

def test_empirical_deficit_monotone():
    x=np.linspace(0,120,500)
    y=empirical_flow_deficit(x)
    assert np.all(np.diff(y) >= -1e-12)
    assert y.min() >= 0
    assert y.max() <= 1

def test_uniform_minimizes_random_ideal_reset():
    T=100.0
    u=ideal_reset_schedule_burden(uniform_event_times(5,T),T)["mean_flow_deficit"]
    rng=np.random.default_rng(1234)
    for _ in range(2000):
        ev=np.sort(rng.uniform(0,T,5))
        b=ideal_reset_schedule_burden(ev,T)["mean_flow_deficit"]
        assert b >= u-1e-10

def test_max_gap_sets_peak_deficit():
    ev=np.array([10.,20.,30.,40.,50.])
    r=ideal_reset_schedule_burden(ev,100)
    assert abs(r["peak_deficit"]-float(empirical_flow_deficit(r["max_gap_min"]))) < 1e-12

def test_microevent_more_refill_with_slower_frequency():
    tau=tau_from_t95(2.45)
    fast=microevent_bout(60,248,tau,epsilon=0.4)["relative_to_independent"]
    slow=microevent_bout(60,30,tau,epsilon=0.4)["relative_to_independent"]
    assert slow > fast

def test_microevent_independent_limit():
    tau=tau_from_t95(1.54)
    r=microevent_bout(10,1,tau,epsilon=0.4)["relative_to_independent"]
    assert r > 0.999
