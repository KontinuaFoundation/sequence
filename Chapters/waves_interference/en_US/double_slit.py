import numpy as np
import matplotlib.pyplot as plt

wavelength = 650e-9    # red laser, meters
d = 0.25e-3            # distance between the slits, meters
a = 0.04e-3            # width of each slit, meters
L = 2.0                # distance to the screen, meters

y = np.linspace(-0.04, 0.04, 4000)          # position on the screen, meters
theta = y / L                               # small-angle approximation

two_slit = np.cos(np.pi * d * theta / wavelength) ** 2
# np.sinc(x) means sin(pi x) / (pi x)
one_slit = np.sinc(a * theta / wavelength) ** 2
intensity = two_slit * one_slit

print(f"fringe spacing: {wavelength * L / d * 1000:.1f} mm")
print(f"central bright band: {2 * wavelength * L / a * 1000:.0f} mm wide")

plt.figure(figsize=(7, 3), dpi=200)
plt.plot(y * 1000, intensity)
plt.plot(y * 1000, one_slit, "--", color="orange")
plt.xlabel("position on screen (mm)")
plt.ylabel("brightness")
plt.tight_layout()
plt.savefig("double_slit.png")
