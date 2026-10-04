"""Functions and Their Graphs, Graphing Calculators: Computing in Python companion code.

Covers the Desmos example, y = 1/x, and a function with its inverse.
Each block matches a minted listing in student.tex. Close a plot window to
move on to the next one. Requires numpy and matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------
# Graphing Calculators: the Desmos example, y = x^2 - x - 6
# ---------------------------------------------------------------
def f(x):
    return x**2 - x - 6


x = np.linspace(-5, 6, 200)
y = f(x)

plt.plot(x, y)
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^2 - x - 6")
plt.show()

print(f(0), f(3), f(-2))  # -6 0 0


# ---------------------------------------------------------------
# Graphing Calculators: y = 1/x, plotted in two pieces
# ---------------------------------------------------------------
x_left = np.linspace(-6, -0.15, 100)
x_right = np.linspace(0.15, 6, 100)

plt.plot(x_left, 1 / x_left, color="C0")
plt.plot(x_right, 1 / x_right, color="C0")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.ylim(-7, 7)
plt.grid(True)
plt.title("y = 1/x")
plt.show()


# ---------------------------------------------------------------
# Graphing Calculators: a function, its inverse, and the line y = x
# ---------------------------------------------------------------
def g(x):
    return x**3


def g_inv(x):
    return np.cbrt(x)


x = np.linspace(-3, 3, 200)

plt.plot(x, g(x), label="g(x) = x^3")
plt.plot(x, g_inv(x), linestyle="--", label="inverse")
plt.plot(x, x, color="gray", linewidth=0.8, label="y = x")
plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)
plt.gca().set_aspect("equal")
plt.grid(True)
plt.legend()
plt.show()
