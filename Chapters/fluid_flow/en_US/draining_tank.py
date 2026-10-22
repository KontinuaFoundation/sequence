import math
import matplotlib.pyplot as plt

g = 9.8
tank_area = 0.5        # m^2, the tank's cross-section
hole_area = 2e-4       # m^2, a 2 cm^2 hole at the bottom
h = 1.8                # m, starting water depth
dt = 0.1               # s, one small time step

t = 0
times, depths = [0], [h]
while h > 0:
    v = math.sqrt(2 * g * h)          # Torricelli: speed of the jet
    flow = hole_area * v              # m^3 leaving each second
    h -= flow / tank_area * dt        # the surface drops (continuity)
    t += dt
    times.append(t / 60)
    depths.append(max(h, 0))

print(f"drains in {t / 60:.1f} minutes")
exact = tank_area / hole_area * math.sqrt(2 * 1.8 / g)
print(f"exact answer: {exact / 60:.1f} minutes")

plt.figure(figsize=(6, 3), dpi=200)
plt.plot(times, depths)
plt.xlabel("time (minutes)")
plt.ylabel("water depth (m)")
plt.tight_layout()
plt.savefig("draining_tank.png")
