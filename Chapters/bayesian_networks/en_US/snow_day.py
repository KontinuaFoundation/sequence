import numpy as np

# Each table gives P(variable = True) for every combination of its parents.
# Axis order everywhere: S (snow), I (ice), D (school closed), C (robocall), B (brother)
p_snow = 0.1
p_ice = 0.08
p_closed = np.array([[0.01, 0.5],                # index: S, I
                     [0.7, 0.95]])
p_call = np.array([0.02, 0.98])                  # index: D
p_brother = np.array([0.3, 0.9])                 # index: D

def table(p_true):
    """Stack P(False) and P(True) along a new last axis."""
    return np.stack([1 - p_true, p_true], axis=-1)

S = table(np.array(p_snow))         # shape (2,)
I = table(np.array(p_ice))          # shape (2,)
D = table(p_closed)                 # shape (2, 2, 2):    S, I, D
C = table(p_call)                   # shape (2, 2):       D, C
B = table(p_brother)                # shape (2, 2):       D, B

# The joint distribution: P(s, i, d, c, b) = P(s) P(i) P(d|s,i) P(c|d) P(b|d)
joint = np.einsum("s,i,sid,dc,db->sidcb", S, I, D, C, B)
print("Joint table shape:", joint.shape, " total:", round(joint.sum(), 10))

AXES = "SIDCB"

def probability(query, given={}):
    """P(query variable is True | given), by adding up rows of the joint table."""
    keep = joint.copy()
    for name, value in given.items():
        index = [slice(None)] * 5
        index[AXES.index(name)] = 1 - int(value)    # zero out rows that disagree
        keep[tuple(index)] = 0
    other = tuple(k for k in range(5) if k != AXES.index(query))
    marginal = keep.sum(axis=other)
    return marginal[1] / marginal.sum()

print(f"P(closed)                     = {probability('D'):.3f}")
print(f"P(closed | brother says so)   = {probability('D', {'B': True}):.3f}")
print(f"P(closed | robocall)          = {probability('D', {'C': True}):.3f}")
print(f"P(snow | closed)              = {probability('S', {'D': True}):.3f}")
print(f"P(snow | closed, icy)         = {probability('S', {'D': True, 'I': True}):.3f}")
print(f"P(snow | closed, not icy)     = {probability('S', {'D': True, 'I': False}):.3f}")
