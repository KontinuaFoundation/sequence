import numpy as np
import torch
from torch import nn

# Simulated data: temperature (degrees C) every 15 minutes for one day, with noise
rng = np.random.default_rng(0)
hours = np.arange(0, 24, 0.25)
temps = 12 - 6 * np.cos(2 * np.pi * (hours - 3) / 24) + rng.normal(0, 0.8, len(hours))

# Scale the input to -1..1 and standardize the target
mean, sd = temps.mean(), temps.std()
x = torch.tensor((hours - 12) / 12, dtype=torch.float32).unsqueeze(1)   # shape (96, 1)
y = torch.tensor((temps - mean) / sd, dtype=torch.float32).unsqueeze(1)

torch.manual_seed(0)
model = nn.Sequential(
    nn.Linear(1, 16),       # 1 input  -> 16 hidden neurons
    nn.ReLU(),
    nn.Linear(16, 1),       # 16 hidden neurons -> 1 output
)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

for epoch in range(1, 2001):
    optimizer.zero_grad()           # clear old gradients
    loss = loss_fn(model(x), y)     # feedforward and loss
    loss.backward()                 # backpropagation
    optimizer.step()                # update the weights
    if epoch in (1, 10, 100, 2000):
        print(f"epoch {epoch:4d}: RMSE {loss.item() ** 0.5 * sd:.2f} degrees")

with torch.no_grad():
    for h in [3, 15]:
        guess = model(torch.tensor([[(h - 12) / 12]])).item() * sd + mean
        print(f"{h:2d}:00  predicted {guess:.1f} degrees")
