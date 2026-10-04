"""Functions and Their Graphs, Piecewise Functions: Computing in Python companion code.

Covers piecewise plotting, if/elif evaluation, and floor/ceiling.
Each block matches a minted listing in student.tex. Close a plot window to
move on to the next one. Requires numpy and matplotlib.
"""
import math

import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------
# Piecewise Functions: plotting g(x) with open and closed circles
# ---------------------------------------------------------------
x_left = np.linspace(-2, 0, 100)
x_right = np.linspace(0, 2, 100)

plt.plot(x_left, x_left**2 + 1, color="C0")
plt.plot(x_right, x_right**2, color="C0")
plt.plot(0, 0, "o", color="C0")                           # closed circle
plt.plot(0, 1, "o", color="C0", markerfacecolor="white")  # open circle
plt.grid(True)
plt.title("piecewise g(x)")
plt.show()


# ---------------------------------------------------------------
# Piecewise Functions: evaluating a three-case function
# ---------------------------------------------------------------
def p(x):
    if -5 <= x < -1:
        return x + 2
    elif -1 <= x <= 2:
        return x**2
    elif 2 < x <= 5:
        return 3 - x
    return None


for x in range(-5, 6):
    print(x, p(x))


# ---------------------------------------------------------------
# Piecewise Functions: case order matters
# ---------------------------------------------------------------
def q(x):
    if x == 4:
        return 10.2
    elif x >= 0:
        return x**2
    return None


print(q(4), q(3))  # 10.2 9


# ---------------------------------------------------------------
# Floor and Ceiling
# ---------------------------------------------------------------
print(math.floor(-2.5), math.ceil(-2.5), math.ceil(8.00001), math.floor(7))  # -3 -2 9 7
