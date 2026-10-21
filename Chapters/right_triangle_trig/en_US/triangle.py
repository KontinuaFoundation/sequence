from math import sin, cos, acos, sqrt, radians, degrees

def third_side(a, b, angle_C):
    """Law of Cosines: the side opposite angle C (in degrees)."""
    C = radians(angle_C)          # math.cos expects radians
    return sqrt(a**2 + b**2 - 2*a*b*cos(C))

def angle_opposite(a, b, c):
    """Law of Cosines, solved for the angle opposite side c."""
    return degrees(acos((a**2 + b**2 - c**2) / (2*a*b)))

print(round(third_side(120, 150, 70), 1))   # the pond
print(round(angle_opposite(5, 6, 7), 1))    # the 5-6-7 triangle
print(round(third_side(3, 4, 90), 1))       # a right angle gives Pythagoras
