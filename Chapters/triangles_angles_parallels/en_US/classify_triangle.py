def classify_triangle(a, b, c):
    """Classify a triangle by its three side lengths.

    Checks the triangle inequality first, then reports whether the
    triangle is equilateral, isosceles, or scalene.
    """
    short1, short2, longest = sorted([a, b, c])
    if short1 + short2 <= longest:
        return "not a triangle"
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"


if __name__ == "__main__":
    triangles = [(5, 5, 5), (5, 5, 8), (5, 12, 13), (2, 2, 5)]
    for sides in triangles:
        print(sides, classify_triangle(*sides))
