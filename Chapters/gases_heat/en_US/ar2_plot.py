import matplotlib.pyplot as plt
from scipy.stats import maxwell
import numpy as np

n = 300

speeds = np.linspace(0, 1500, num=n)
pdf = np.zeros((n))

m = 39.948 * .000167  # Mass of 1 atom of Ar * 10^23
k = 1.380  # Boltzman constant  * 10^23
T1 = 298.15  # 25C in Kelvin
T2 = T1 - 125.0

a1 = np.sqrt(k * T1 / m)
a2 = np.sqrt(k * T2 / m)

v_rms1 = np.sqrt(3 * k * T1/m)
v_rms2 = np.sqrt(3 * k * T2/m)

pdf = maxwell.pdf(speeds, 0, a1)
plt.plot(speeds, pdf, color="b")
pdf = maxwell.pdf(speeds, 0, a2)
plt.plot(speeds, pdf, color="r", linestyle="dashed")
plt.xlabel("Speed of molecule (m/s)")
plt.ylabel("Probability Density")
plt.text(310, 0.003, "-100 degrees C", color="r")
plt.text(620, 0.001, "25 degrees C", color="b")

# plt.axvline(v_rms1, color="b", linestyle="dashed", lw=0.7)
# plt.axvline(v_rms2, color="r", linestyle="dashed", lw=0.7)
plt.axhline(0, color="k", linestyle="dashed", lw=0.7)
plt.axvline(0, color="k", linestyle="dashed", lw=0.7)
plt.show()