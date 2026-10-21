import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 1000)

def partial_sum(x, terms):
    """The first `terms` nonzero terms of the square wave's Fourier series."""
    total = np.zeros_like(x)
    for k in range(terms):
        n = 2 * k + 1                    # only odd n appear
        total += 4 / (n * np.pi) * np.sin(n * x)
    return total

plt.plot(x, np.sign(x), "k", linewidth=2, label="square wave")
for terms in [1, 3, 15]:
    plt.plot(x, partial_sum(x, terms), label=f"{terms} term" + ("s" if terms > 1 else ""))
plt.xlabel("x")
plt.legend()
plt.savefig("square_wave.png")
