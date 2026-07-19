import numpy as np
import matplotlib.pyplot as plt

V_initial = 2.0 # cubic meters
V_final = 0.5 # cubic meters
step_count = 40 # steps

T_initial = 300.0 # kelvin
P_initial = 100000 # pascals

# Constants
R = 8.314462618 # ideal gas constant
C_v =  3.0 * R / 2.0 # molar heat capacity (constant volume)

# Compute the number of moles
n = P_initial * V_initial/(R * T_initial) 
print(f"The container holds {n:.2f} moles of helium")

# How much volume do we need to eliminate in each step? 
# (in cubic meters)
step_size = (V_initial - V_final) / step_count

# For recording the state for each step
data_log = np.zeros((step_count, 3))

# Variables to update in the loop
V_current = V_initial
T_current = T_initial
P_current = P_initial

for i in range(step_count):
    # Record the current state
    data_log[i,:] = [T_current, V_current, P_current/1000.0]

    # Find how much energy to make the step at the current pressure
    E_step = step_size * P_current

    # Find how big the change in temperature will be from that energy
    delta_T = E_step / (n * C_v)

    # Update the current temperature, volume, and pressure
    T_current += delta_T
    V_current -= step_size
    P_current = n * R * T_current / V_current

print(f"Iterative:{T_current:0.3f} K, {V_current:0.3f} m3, {P_current/1000.0:0.3f} kPa")

C_p =  C_v + R
gamma = C_p/C_v
s_t = T_initial * V_initial**(gamma - 1.0)
s_p = P_initial * V_initial**gamma
final_T = s_t / V_final**(gamma - 1.0)
final_P = s_p / V_final**gamma
print(f"Continuous:{final_T:0.3f} K, {V_current:0.3f} m3, {final_P/1000.0:0.3f} kPa")

fig, axs = plt.subplots(3,1,sharex=True, figsize=(8, 6))
axs[0].set_xlim((0,step_count))
axs[0].plot(data_log[:,0], 'k', lw=0.2)
axs[0].plot(data_log[:,0], 'r.')
axs[0].set_ylabel("Temperature (K)")

axs[1].plot(data_log[:,1],'k', lw=0.2)
axs[1].plot(data_log[:,1], 'r.')
axs[1].set_ylabel("Volume (cubic m)")

axs[2].plot(data_log[:,2], 'k', lw=0.2)
axs[2].plot(data_log[:,2], 'r.')
axs[2].set_ylabel("Pressure (kPa)")

axs[2].set_xlabel("Step")

fig.savefig('tvpplot.png')

