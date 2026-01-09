import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Parameter values (like "time")
t = np.linspace(0, 3, 50) 

# 2. Parametric equations for the curve. Change the equations for x(t) and y(t) based on question
x = 4 - 2*t  # x(t)
y = 3 + 6*t - 4*t**2  # y(t)

# 3. Set up the figure and axes
fig, ax = plt.subplots()
ax.set_aspect("equal", "box")

# Draw x- and y-axis lines for reference
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)

ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_title("Parametric Equation of Curve")

# Fix the view 
ax.set_xlim([x.min() - 1, x.max() + 1])
ax.set_ylim([y.min() - 1, y.max()+ 1])

# 4. Create:
(line,) = ax.plot([], [], "b--")  # path being drawn
(point,) = ax.plot([], [], "ro")  # moving point

# 5. Animation 
def update(frame):
    # Showing the path
    line.set_data(x[:frame + 1], y[:frame + 1])

    # Moving the red dot to the current point
    x_pos = x[frame]
    y_pos = y[frame]
    point.set_data([x_pos], [y_pos]) 

    return line, point

# 6. Create the animation
ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=50,
    blit=True
)

ani.save("parametric_animation.mp4") # Save the animation as a .gif or .mp4 file using whatever name you want. 

plt.show()

