import matplotlib.pyplot as plt
from scipy.stats import maxwell
import numpy as np

n = 300

speeds = np.linspace(0, 1500, num=n)
pdf = np.zeros((n))

m = 39.948 * .000167  # Mass of 1 atom of Ar * 10^23
k = 1.380  # Boltzman constant  * 10^23
T = 298.15  # 25C in Kelvin

a = np.sqrt(k * T / m)
print(a)

v_rms = np.sqrt(3 * k * T/m)

pdf = maxwell.pdf(speeds, 0, a)
plt.plot(speeds, pdf, color="b")
plt.xlabel("Speed of molecule (m/s)")
plt.ylabel("Probability Density")
plt.axvline(v_rms, color="b", linestyle="dashed", lw=1.1)
plt.axhline(0, color="k", linestyle="dashed", lw=0.7)
plt.axvline(0, color="k", linestyle="dashed", lw=0.7)
plt.show()