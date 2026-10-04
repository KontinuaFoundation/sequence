# quadratic_formula_check.py
# Checks your hand work on the quadratic formula. You do the math first;
# this script only tells you whether your answers hold up.
#
# To check a new problem:
#   1. Change the three numbers inside discriminant(...) to your a, b, and c.
#   2. Change the return line in p(x) to your quadratic.
#   3. Change the list in the for loop to the roots you found by hand.
#
# Common mistakes:
#   - Write x**2, not x^2. In Python, ^ does not mean "to the power of".
#   - Write 8*x, not 8x. Python needs the * between a number and a letter.
#   - Keep every minus sign: a = -4.9 goes in as -4.9*x**2.
#   - Rounded roots give values close to 0, not exactly 0. That is fine.


def discriminant(a, b, c):
    return b**2 - 4*a*c


print(discriminant(1, -2, 3))   # first graph
print(discriminant(1, -4, 4))   # second graph
print(discriminant(1, -3, 1))   # third graph


def p(x):
    return 6*x**2 + 8*x - 12


for x in [0.897, -2.230]:
    print(x, p(x))
