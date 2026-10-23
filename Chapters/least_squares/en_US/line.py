import numpy as np
from penguins import load_penguins

data = load_penguins()
x = data["flipper_length_mm"]
y = data["body_mass_g"]

# The formulas from this chapter
x_bar, y_bar = np.mean(x), np.mean(y)
b1 = np.sum((x - x_bar) * (y - y_bar)) / np.sum((x - x_bar)**2)
b0 = y_bar - b1 * x_bar
print(f"mass = {b0:.1f} + {b1:.2f} * flipper")

# How good is it?
residuals = y - (b0 + b1 * x)
rmse = np.sqrt(np.mean(residuals**2))
print(f"RMSE = {rmse:.0f} g")
print(f"Sum of residuals = {round(np.sum(residuals), 6) + 0.0}")

# A 200 mm flipper
print(f"Prediction for 200 mm: {b0 + b1 * 200:.0f} g")
