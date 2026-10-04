import math


def solve_quadratic(a, b, c):
    """Return a list of the real roots of ax^2 + bx + c = 0."""
    if a == 0:
        raise ValueError("a cannot be zero in a quadratic")
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return []
    if discriminant == 0:
        return [-b / (2 * a)]
    root = math.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
    return [x1, x2]


# Check the factoring examples from this section
examples = [
    (1, 5, 6),     # (x + 2)(x + 3)
    (6, 11, 4),    # AC method
    (1, 6, 9),     # perfect square
    (1, 0, -16),   # difference of squares
    (1, 1, 1),     # no real roots
]

for a, b, c in examples:
    roots = solve_quadratic(a, b, c)
    print(f"{a}x^2 + {b}x + {c} = 0  ->  {roots}")
