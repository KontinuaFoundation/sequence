"""Functions and Their Graphs, Even and Odd Functions: Computing in Python companion code.

Covers symmetry checks with h(x), h(-x), and -h(-x).
Each block matches a minted listing in student.tex. Close a plot window to
move on to the next one. Requires numpy and matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------
# Even and Odd Functions: compare h(x), h(-x), and -h(-x)
# ---------------------------------------------------------------
def h(x):
    return x**3 + 1


x = np.linspace(-2, 2, 200)

plt.plot(x, h(x), label="h(x)")
plt.plot(x, h(-x), linestyle="--", label="h(-x)")
plt.plot(x, -h(-x), linestyle=":", label="-h(-x)")
plt.grid(True)
plt.legend()
plt.show()

print(np.allclose(h(-x), h(x)))   # even test: False
print(np.allclose(-h(-x), h(x)))  # odd test: False
print(h(1), h(-1), -h(-1))        # 2 0 0
