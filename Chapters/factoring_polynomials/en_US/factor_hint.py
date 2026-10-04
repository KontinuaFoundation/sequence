# Stuck? Let SymPy help you factor.
# Try the problem by hand first. Then use this file to get a hint,
# and the full answer if you still need it.
#
# TO USE THIS FILE
#   1. Install SymPy once:  python3 -m pip install sympy
#   2. Change the polynomial line below to your polynomial.
#   3. Run the file. It shows a hint first, then the full answer
#      after you press Enter.
#
# Reminders: write x**2 for x squared (never x^2), and always put *
# between things you multiply: 5*x, not 5x.
#
# factor() usage adapted from GeeksforGeeks, "Python | sympy.factor() method":
# https://www.geeksforgeeks.org/python/python-sympy-factor-method/

# Make sure SymPy is installed. Use python -m pip install sympy . 
try:
    from sympy import symbols, factor, factor_terms
except ImportError:
    print("SymPy is not installed for this copy of Python.")
    print("Install it by running this in a terminal, then try again:")
    print("    python3 -m pip install sympy")
    raise SystemExit

x = symbols('x')

polynomial = 5*x**3 - 45*x

print("Polynomial:", polynomial)
print()

# Hint: pull out the greatest common factor of all the terms.
hint = factor_terms(polynomial)
print("Hint (common factor pulled out):", hint)
if hint == polynomial:
    print("The terms have no common factor. If the polynomial is a")
    print("quadratic that starts with x**2, look for two numbers that")
    print("multiply to the constant term and add to the middle coefficient.")
print()

try:
    input("Try to finish it yourself, then press Enter to see the answer...")
except EOFError:
    pass

# Full answer
print("Fully factored:", factor(polynomial))
print()
print("Read the roots from the factors: set each factor equal to zero.")
print("If SymPy gives back the same polynomial, it has no factors")
print("with integer coefficients.")
