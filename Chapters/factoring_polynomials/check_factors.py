# Computing in Python: Factoring Polynomials
# Check a factorization by comparing the original polynomial and your
# factored form at several values of x.
#
# TO USE THIS FOR YOUR OWN PROBLEM
#   1. Factor the polynomial by hand.
#   2. Change the return line in p(x) to your original polynomial.
#   3. Change the return line in f(x) to your factored answer.
#   4. Put the roots you read off your factors in the first list.
#   5. Run the file.
#
# Reminders: write x**2 for x squared (never x^2), and always put *
# between things you multiply: 5*x and (x + 3)*(x - 3).


def p(x):
    return 5*x**3 - 45*x


def f(x):
    return (5*x)*(x + 3)*(x - 3)


# Check the roots: each one should print 0.
for x in [0, -3, 3]:
    print(x, p(x))

print()

# Compare the two forms. If every line says True, your factorization
# is correct. Check at least (degree + 1) values of x; this polynomial
# has degree 3, so four values are enough.
for x in [0, 1, 2, 3]:
    print(x, p(x), f(x), p(x) == f(x))
