from math import sqrt

C = 299_792_458            # speed of light, m/s

def gamma(v):
    """The time-dilation factor for speed v in m/s."""
    return 1 / sqrt(1 - (v / C) ** 2)

for fraction in [0.1, 0.5, 0.9, 0.99, 0.999]:
    print(f"{fraction:>5} c: gamma = {gamma(fraction * C):.3f}")

# Muons made 15 km up, moving at 0.995 c, with a half-life of 1.52 microseconds
v = 0.995 * C
earth_time = 15_000 / v                  # seconds, on Earth's clocks
muon_time = earth_time / gamma(v)        # seconds, on the muons' own clocks
half_life = 1.52e-6
print(f"surviving with relativity:    {0.5 ** (muon_time / half_life):.3f}")
print(f"surviving without relativity: {0.5 ** (earth_time / half_life):.1e}")
