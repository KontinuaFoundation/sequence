import numpy as np
import matplotlib.pyplot as plt

rate = 8000                          # samples per second
t = np.arange(0, 1, 1 / rate)        # one second of time

# A 440 Hz note with two overtones
signal = (1.0 * np.sin(2 * np.pi * 440 * t)
          + 0.5 * np.sin(2 * np.pi * 880 * t)
          + 0.25 * np.sin(2 * np.pi * 1320 * t))

spectrum = np.abs(np.fft.rfft(signal)) / (len(t) / 2)   # amplitudes
freqs = np.fft.rfftfreq(len(t), 1 / rate)               # in Hz

for f, a in zip(freqs, spectrum):
    if a > 0.1:
        print(f"{f:.0f} Hz: amplitude {a:.2f}")

fig, (top, bottom) = plt.subplots(2, 1)
top.plot(t[:160] * 1000, signal[:160])
top.set_xlabel("time (ms)")
bottom.plot(freqs, spectrum)
bottom.set_xlim(0, 2000)
bottom.set_xlabel("frequency (Hz)")
fig.tight_layout()
fig.savefig("spectrum.png")
