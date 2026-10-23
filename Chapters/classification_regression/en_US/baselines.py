import numpy as np
from penguins import load_penguins

data = load_penguins()
mass = data["body_mass_g"]
species = data["species"]
print("Penguins:", len(mass))

# Regression baseline: always predict the average mass
guess = np.mean(mass)
errors = mass - guess
rmse = np.sqrt(np.mean(errors**2))
print(f"Always guess {guess:.0f} g: RMSE = {rmse:.0f} g")

# Classification baseline: always predict the most common species
names, counts = np.unique(species, return_counts=True)
most_common = names[np.argmax(counts)]
accuracy = np.mean(species == most_common)
print(f"Always guess {most_common}: accuracy = {accuracy:.1%}")
