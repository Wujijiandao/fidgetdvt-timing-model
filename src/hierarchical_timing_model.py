"""
FidgetDVT canonical hierarchical timing model — v0.6.0

The model distinguishes two timing levels.

MICROSTRUCTURE (within a movement bout)
---------------------------------------
Individual muscular pump events are separated by delta (seconds).
Fast event-to-event refill is represented by R in [0,1]:

    R_next^- = 1 - (1 - R_prev^+) exp(-delta/tau_r)
    E_i      = epsilon R_i^-
    R_i^+    = (1-epsilon) R_i^-

The dimensionless micro-gap is:
    Pi = delta / tau_r

Keijsers et al. (2015) reported times to 95% refill of 1.54–2.45 s.
Under a first-order approximation:
    tau_r = t95 / ln(20) = 0.514–0.818 s.

MACROSTRUCTURE (between effective movement bouts)
-------------------------------------------------
Let d(a) be the fractional venous-flow deficit after uninterrupted sedentary
age a since the last effective bout. The core theorem requires only that d(a)
is nondecreasing.

For an ideal effective reset, the low-flow burden of a gap Delta is:
    B(Delta) = integral_0^Delta d(a) da

If d is nondecreasing, B is convex. Therefore, for a fixed total seated time
and a fixed number of equally effective resets, equal gap spacing minimizes
the total low-flow burden.

The project uses a transparent, data-anchored piecewise-linear example:
    d(0 min)   = 0
    d(65 min)  = 0.29   (Hitos 2007)
    d(100 min) = 0.42   (Hitos 2007)

This interpolation is an illustrative observable mapping, not a universal
physiological law.

No model output is a DVT/PE probability or a safe sitting threshold.
"""
import math
import numpy as np

LN20 = math.log(20.0)

HITOS_T_MIN = np.array([0.0, 65.0, 100.0])
HITOS_DEFICIT = np.array([0.0, 0.29, 0.42])

def tau_from_t95(t95_s):
    return float(t95_s)/LN20

def empirical_flow_deficit(age_min):
    """Piecewise-linear Hitos-anchored deficit; plateaus after 100 min."""
    x = np.asarray(age_min, dtype=float)
    y = np.interp(np.minimum(np.maximum(x, 0.0), 100.0),
                  HITOS_T_MIN, HITOS_DEFICIT)
    return y

def integrated_gap_burden(delta_min):
    """
    Exact integral of the piecewise-linear empirical deficit curve.
    Returns deficit-minutes.
    """
    delta = max(0.0, float(delta_min))
    pts = [0.0]
    for b in (65.0, 100.0):
        if b < delta:
            pts.append(b)
    pts.append(delta)
    total = 0.0
    for a,b in zip(pts[:-1], pts[1:]):
        da = float(empirical_flow_deficit(a))
        db = float(empirical_flow_deficit(b))
        total += (b-a)*(da+db)/2.0
    return total

def ideal_reset_schedule_burden(event_times_min, T_min=100.0):
    """
    Low-flow burden with equally effective ideal resets.
    """
    ts = np.sort(np.asarray(event_times_min, dtype=float))
    if np.any(ts < 0) or np.any(ts > T_min):
        raise ValueError("events must be within observation window")
    gaps = np.diff(np.concatenate(([0.0], ts, [float(T_min)])))
    total = sum(integrated_gap_burden(g) for g in gaps)
    return {
        "mean_flow_deficit": total/float(T_min),
        "deficit_minutes": total,
        "max_gap_min": float(np.max(gaps)),
        "peak_deficit": float(empirical_flow_deficit(np.max(gaps))),
        "gaps_min": gaps,
    }

def microevent_bout(n_events, frequency_per_min, tau_r_s, epsilon=0.4):
    """
    Effective pump-dose proxy for n standardized events within one bout.
    """
    if n_events <= 0:
        return {"effective_dose":0.0, "relative_to_independent":0.0}
    delta_s = 60.0/float(frequency_per_min)
    R = 1.0
    total = 0.0
    pre = []
    for i in range(int(n_events)):
        if i > 0:
            R = 1.0-(1.0-R)*math.exp(-delta_s/float(tau_r_s))
        pre.append(R)
        E = float(epsilon)*R
        total += E
        R = (1.0-float(epsilon))*R
    independent = n_events*float(epsilon)
    return {
        "effective_dose": total,
        "relative_to_independent": total/independent,
        "mean_pre_event_availability": float(np.mean(pre)),
        "min_pre_event_availability": float(np.min(pre)),
        "Pi": delta_s/float(tau_r_s),
        "delta_s": delta_s,
    }

def uniform_event_times(n_events, T_min):
    n = int(n_events)
    if n <= 0:
        return np.array([])
    return (float(T_min)/(n+1))*np.arange(1,n+1,dtype=float)
