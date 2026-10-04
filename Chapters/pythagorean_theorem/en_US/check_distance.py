# check_distance.py
# Checks your distance work one step at a time.
#
# HOW TO USE
#   1. Work out the distance by hand first.
#   2. To check a new problem, change only the numbers in the last line:
#        check_steps(x1, y1, z1, x2, y2, z2)
#   3. Run the file and compare each printed line with your own work.
#      The first line that does not match is where your mistake is.
#
# COMMON MISTAKES
#   - Python writes exponents with **, so x squared is x**2.
#     x^2 means something different in Python and gives wrong answers.
#   - -3**2 is -9 in Python. Write (-3)**2 to get 9.
#
# Runs on plain Python. Nothing to install.

import math

def check_steps(x1, y1, z1, x2, y2, z2):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    print("dx =", dx, "  dx**2 =", dx**2)
    print("dy =", dy, "  dy**2 =", dy**2)
    print("dz =", dz, "  dz**2 =", dz**2)
    total = dx**2 + dy**2 + dz**2
    print("sum =", total, "  distance =", math.sqrt(total))

check_steps(0, 0, 0, 2, 8, 4)
