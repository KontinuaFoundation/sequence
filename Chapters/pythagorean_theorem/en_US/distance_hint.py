# distance_hint.py
# Use this only when you are stuck on a 3D distance problem.
# It shows a hint first. Press Enter to see the full answer.
#
# To use it on a new problem, change the six numbers below.
#
# This file needs the SymPy library, which writes square roots in
# simplified form (for example, sqrt(84) becomes 2*sqrt(21)).
# Written for the Kontinua Sequence
# SymPy documentation: https://docs.sympy.org/latest/index.html

import sys

try:
    from sympy import sqrt
except ImportError:
    print("This helper needs the SymPy library.")
    print("Install it by running:  python3 -m pip install sympy")
    sys.exit(1)

# Change these six numbers for your problem
x1, y1, z1 = 0, 0, 0
x2, y2, z2 = 2, 8, 4

dx = x2 - x1
dy = y2 - y1
dz = z2 - z1

print("HINT")
print("Change in x:", dx, "  Change in y:", dy, "  Change in z:", dz)
print("Square each change, add the squares, then take the square root.")
input("Press Enter to see the full answer...")

total = dx**2 + dy**2 + dz**2
print()
print("ANSWER")
print("Squares:", dx**2, "+", dy**2, "+", dz**2, "=", total)
print("Exact distance:   ", sqrt(total))
print("Decimal distance: ", sqrt(total).evalf())
