
"""
Human-validated macro timing model — v0.7.0
"""
import numpy as np

T_ANCHOR = np.array([0.0, 65.0, 100.0])
D_ANCHOR = np.array([0.0, 0.29, 0.42])

def flow_deficit(age_min):
    x = np.asarray(age_min, dtype=float)
    return np.interp(np.clip(x, 0.0, 100.0), T_ANCHOR, D_ANCHOR)

def integrate_deficit(a0_min, duration_min):
    a0=float(a0_min); dur=max(0.0,float(duration_min))
    a1=a0+dur
    points=[a0]
    for b in (65.0,100.0):
        if a0 < b < a1:
            points.append(b)
    points.append(a1)
    total=0.0
    for x0,x1 in zip(points[:-1],points[1:]):
        y0=float(flow_deficit(x0))
        y1=float(flow_deficit(x1))
        total += 0.5*(y0+y1)*(x1-x0)
    return total

def simulate_age_reset_schedule(event_times_min, T_min=100.0, rho=1.0):
    ts=np.sort(np.asarray(event_times_min,dtype=float))
    age=0.0
    prev=0.0
    burden=0.0
    for t in ts:
        dt=t-prev
        burden += integrate_deficit(age,dt)
        age += dt
        age *= (1.0-float(rho))
        prev=t
    dt=float(T_min)-prev
    burden += integrate_deficit(age,dt)
    age += dt
    gaps=np.diff(np.concatenate(([0.0],ts,[float(T_min)])))
    return {
        "mean_flow_deficit": burden/float(T_min),
        "deficit_minutes": burden,
        "final_effective_age_min": age,
        "final_flow_deficit": float(flow_deficit(age)),
        "max_gap_min": float(np.max(gaps)),
        "gaps_min": gaps,
    }

def heldout_airline_predictions():
    return {
        45.0: float(flow_deficit(45.0)),
        85.0: float(flow_deficit(25.0)),
        100.0: float(flow_deficit(40.0)),
    }
