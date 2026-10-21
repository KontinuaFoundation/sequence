import numpy as np
import matplotlib.pyplot as plt

fc = 2500                                  # crossover frequency, Hz
f = np.logspace(1, np.log10(20000), 500)   # 10 Hz to 20 kHz

woofer = 1 / np.sqrt(1 + (f / fc) ** 2)               # low-pass
tweeter = (f / fc) / np.sqrt(1 + (f / fc) ** 2)       # high-pass

for test in [100, 2500, 10000]:
    w = 1 / np.sqrt(1 + (test / fc) ** 2)
    tw = (test / fc) / np.sqrt(1 + (test / fc) ** 2)
    print(f"{test} Hz: woofer {w:.2f}, tweeter {tw:.2f}")

plt.semilogx(f, woofer, label="woofer (low-pass)")
plt.semilogx(f, tweeter, label="tweeter (high-pass)")
plt.axvline(fc, color="gray", linestyle="--")
plt.xlabel("frequency (Hz)")
plt.ylabel("fraction of the signal passed")
plt.legend()
plt.savefig("crossover.png")
