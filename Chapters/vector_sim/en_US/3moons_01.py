import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11              # Gravitational constant (Nm^2/kg^2)
SEC_PER_DAY = 24 * 60 * 60   # How many seconds in a day?
MAX_TIME = 100 * SEC_PER_DAY # 100 days
TIME_STEP = 2 * 60 * 60      # Update every two hours
PAIR_LINE_STEP = 300  # How time steps between pair lines

# Create the inital state of Moon 1
m1 = {
    "mass": 6.0e22,  # kg
    "position": np.array([0.0, 200_000_000]),  # m
    "velocity": np.array([100.0, 25.0]),  # m/s
    "radius": 1_500_000.0,  # m
    "color": "red" # For plotting
}

# Create the inital state of Moon 2
m2 = {
    "mass": 11.0e22,  # kg
    "position": np.array([0.0, -150_000_000]),  # m
    "velocity": np.array([-45.0, 2.0]),  # m/s
    "radius": 2_000_000.0,  # m
    "color": "blue" # For plotting
}  

# Create the inital state of Moon 3
m3 = {
    "mass": 4.0e22,  # kg
    "position": np.array([50_000_000, 80_000_000]),  # m
    "velocity": np.array([-30.0, -35.0]),  # m/s
    "radius": 1_700_000.0,  # m
    "color": "green" 
}  

# Lists to hold positions and time
position1_log = []
position2_log = []
position3_log = []
time_log = []

# Start at time zero seconds
current_time = 0.0

# Loop until current time exceed Max Time
while current_time <= MAX_TIME:

    # Add time and positions to log
    time_log.append(current_time)
    position1_log.append(m1["position"])
    position2_log.append(m2["position"])
    position3_log.append(m3["position"])

    print(f"Day {current_time/SEC_PER_DAY:.2f}:")
    print(f"\tMoon 1:({m1['position'][0]:,.1f},{m1['position'][1]:,.1f})")
    print(f"\tMoon 2:({m2['position'][0]:,.1f},{m2['position'][1]:,.1f})")
    print(f"\tMoon 3:({m3['position'][0]:,.1f},{m3['position'][1]:,.1f})")

    # Update the positions based on the current velocities
    m1["position"] = m1["position"] + m1["velocity"] * TIME_STEP
    m2["position"] = m2["position"] + m2["velocity"] * TIME_STEP
    m3["position"] = m3["position"] + m3["velocity"] * TIME_STEP

    # Find the displacement vectors
    delta_1_2 = m2["position"] - m1["position"] # From 1 to 2
    delta_2_3 = m3["position"] - m2["position"] # From 2 to 3
    delta_3_1 = m1["position"] - m3["position"] # From 3 to 1

    # What is the distance between the moons?
    distance_1_2 = np.linalg.norm(delta_1_2)
    distance_2_3 = np.linalg.norm(delta_2_3)
    distance_3_1 = np.linalg.norm(delta_3_1)

    # Have the moons collided?
    if distance_1_2 < m1["radius"] + m2["radius"]:
        print(f"*** Moon 1 and 2 collided {current_time:.1f} seconds in!")
        break

    if distance_2_3 < m2["radius"] + m3["radius"]:
        print(f"*** Moon 2 and 3 collided {current_time:.1f} seconds in!")
        break

    if distance_3_1 < m3["radius"] + m1["radius"]:
        print(f"*** Moon 3 and 1 collided {current_time:.1f} seconds in!")
        break

    # What is a unit vector that points from moon1 toward moon2?
    direction_1_2 = delta_1_2 / distance_1_2
    direction_2_3 = delta_2_3 / distance_2_3
    direction_3_1 = delta_3_1 / distance_3_1

    # Calculate the magnitude of the gravitational attraction
    magnitude_1_2 = G * m1["mass"] * m2["mass"] / (distance_1_2**2)
    magnitude_2_3 = G * m2["mass"] * m3["mass"] / (distance_2_3**2)
    magnitude_3_1 = G * m3["mass"] * m1["mass"] / (distance_3_1**2)

    # Acceleration vectors (a = f/m)
    acceleration1 = (direction_1_2 * magnitude_1_2 + -1 * direction_3_1 * magnitude_3_1) / m1["mass"]
    acceleration2 = (direction_2_3 * magnitude_2_3 + -1 * direction_1_2 * magnitude_1_2) / m2["mass"]
    acceleration3 = (direction_3_1 * magnitude_3_1 + -1 * direction_2_3 * magnitude_2_3) / m3["mass"]

    # Update the velocity vectors
    m1["velocity"] = m1["velocity"] + acceleration1 * TIME_STEP
    m2["velocity"] = m2["velocity"] + acceleration2 * TIME_STEP
    m3["velocity"] = m3["velocity"] + acceleration3 * TIME_STEP

    # Update the clock
    current_time += TIME_STEP

print(f"Generated {len(position1_log)} data points.")

# Convert lists to np.arrays
positions1 = np.array(position1_log)
positions2 = np.array(position2_log)
positions3 = np.array(position3_log)

# Create a figure with a set of axes
fig, ax = plt.subplots(1, figsize=(7.2, 10))

# Label the axes
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_aspect("equal", adjustable='box')

# Draw the path of the two moons
ax.plot(positions1[:, 0], positions1[:, 1], m1["color"], lw=0.7)
ax.plot(positions2[:, 0], positions2[:, 1], m2["color"], lw=0.7)
ax.plot(positions3[:, 0], positions3[:, 1], m3["color"], lw=0.7)

# Save out the figure
fig.savefig("plot3moons.png")