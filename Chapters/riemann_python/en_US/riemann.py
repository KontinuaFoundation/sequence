import matplotlib.pyplot as plt
import sys
import math

from matplotlib.table import Rectangle

# Did the user supply two arguments?
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <stop> <divisions>")
    print(f"Numerically integrates 1/x from 1 to <stop>.")
    print(f"Calculates the value of 1/x at <divisions> spots in the range.")
    exit(1)

# Check to make sure the number of divisions is greater than zero?
divisions = int(sys.argv[2])
if divisions <= 0:
    print("ERROR: Divisions must be at least 1.")
    exit(1)

# Is the stopping point after 1.0?
stop = float(sys.argv[1])
if stop <= 1.0:
    print("ERROR: Stopping point must be greater than 1.0")
    exit(1)

start = 1.0
step_size = (stop - start)/divisions

print(f"Step size is {step_size:.5f}.")
x_values = []
y_values = []
sum = 0.0
for i in range(divisions):
    current_x = start + i * step_size
    current_y = 1.0/current_x
    area = current_y * step_size
    print(f"{i}: 1 / {current_x:.3f} = {current_y:4f}, area of rect = {area:8f} ")

    x_values.append(current_x)
    y_values.append(current_y)
    sum += area
    print(f"\tCumulative={sum:.3f}, ln({current_x:.3f})={math.log(current_x):.3f}")

print(f"Numerical integration of 1/x from 1.0 to {stop:.4f} is {sum:.4f}")
print(f"The natural log of {stop:.4f} is {math.log(stop):.4f}")

# Create data for the smooth 1/x line
SMOOTH_DIVISIONS = 200
smooth_start = start - 0.15
smooth_stop = stop + 1.0
smooth_step = (smooth_stop - smooth_start)/SMOOTH_DIVISIONS
smooth_x_values = []
smooth_y_values = []
for i in range(SMOOTH_DIVISIONS):
    current_x = smooth_start + i * smooth_step
    current_y = 1.0/current_x
    smooth_x_values.append(current_x)
    smooth_y_values.append(current_y)

# Put it on a plot
fig, ax = plt.subplots()
ax.set_xlim((smooth_x_values[0], smooth_x_values[-1]))
ax.set_ylim((0, smooth_y_values[0]))
ax.set_title("Riemann Sums for 1/x")

# Make the Riemann rects
for i in range(divisions):
    current_x = x_values[i]
    next_x = current_x + step_size
    current_y = y_values[i]
    rect = Rectangle((current_x, 0), step_size, current_y, edgecolor="green", facecolor="lightgreen")
    ax.add_patch(rect)

# Make the true 1/x curve
ax.plot(smooth_x_values, smooth_y_values, c="k", label="1/x")

# Show the user
plt.show()

