# roots_hint.py
# Use this only when you are stuck, after you have tried the problem by hand.
# It shows a hint first, waits for you to press Enter, then shows the roots.
#
# To use it for a new problem, change the numbers on the a, b, c lines below.
#
# This script needs the SymPy library. If it is missing, run:
#     python3 -m pip install sympy
#
# The solve() pattern is adapted from the SymPy tutorial "Solvers":
# https://docs.sympy.org/latest/tutorials/intro-tutorial/solvers.html
# (SymPy is BSD-licensed.)

import sys

a = 6
b = 8
c = -12

try:
    from sympy import symbols, solve
except ImportError:
    print("This helper needs the SymPy library, which is not installed.")
    print("Install it by running this command in a terminal:")
    print("    python3 -m pip install sympy")
    sys.exit(1)

if a == 0:
    print("a cannot be 0. With a = 0 the equation is linear, not quadratic.")
    sys.exit(1)

x = symbols("x", real=True)
d = b**2 - 4*a*c

print(f"Equation: ({a})x^2 + ({b})x + ({c}) = 0")
print()
print("HINT")
print(f"  a = {a}, b = {b}, c = {c}")
print(f"  Discriminant: b^2 - 4ac = ({b})^2 - 4({a})({c}) = {d}")
if d < 0:
    print("  The discriminant is negative, so there are no real roots.")
elif d == 0:
    print("  The discriminant is 0, so there is exactly one real root.")
else:
    print("  The discriminant is positive, so there are two real roots.")
    print(f"  Next step: x = ({-b} +/- sqrt({d})) / {2*a}")

input("\nPress Enter to see the full answer...")

roots = solve(a*x**2 + b*x + c, x)
print("ANSWER")
if len(roots) == 0:
    print("  No real roots.")
for r in roots:
    print(f"  x = {r}   (about {r.evalf(4)})")
