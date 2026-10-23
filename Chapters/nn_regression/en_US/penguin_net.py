import copy
import numpy as np
import torch
from torch import nn
from penguins import load_penguins

data = load_penguins()
columns = [data["flipper_length_mm"], data["bill_length_mm"], data["bill_depth_mm"],
           data["sex"] == "male", data["species"] == "Gentoo", data["species"] == "Chinstrap"]
X = np.column_stack(columns).astype(float)
y = data["body_mass_g"]
order = np.random.default_rng(1).permutation(len(y))
train, val, test = order[:183], order[183:233], order[233:]

# Standardize with training statistics only
x_mean, x_sd = X[train].mean(axis=0), X[train].std(axis=0)
y_mean, y_sd = y[train].mean(), y[train].std()
def tensors(rows):
    xs = torch.tensor((X[rows] - x_mean) / x_sd, dtype=torch.float32)
    ys = torch.tensor((y[rows] - y_mean) / y_sd, dtype=torch.float32).unsqueeze(1)
    return xs, ys
(x_tr, y_tr), (x_va, y_va), (x_te, y_te) = tensors(train), tensors(val), tensors(test)

torch.manual_seed(0)
model = nn.Sequential(nn.Linear(6, 32), nn.ReLU(), nn.Linear(32, 32), nn.ReLU(),
                      nn.Linear(32, 1))
optimizer = torch.optim.Adam(model.parameters(), lr=0.003)
loss_fn = nn.MSELoss()

def rmse_grams(x, y):
    with torch.no_grad():
        return loss_fn(model(x), y).item() ** 0.5 * y_sd

best_val, best_state, best_epoch = np.inf, None, 0
for epoch in range(1, 1001):
    optimizer.zero_grad()
    loss = loss_fn(model(x_tr), y_tr)
    loss.backward()
    optimizer.step()
    val_rmse = rmse_grams(x_va, y_va)
    if val_rmse < best_val:                   # remember the best weights so far
        best_val, best_epoch = val_rmse, epoch
        best_state = copy.deepcopy(model.state_dict())
    if epoch in (10, 100, 300, 1000):
        print(f"epoch {epoch:4d}: training {rmse_grams(x_tr, y_tr):4.0f} g,"
              f" validation {val_rmse:4.0f} g")

model.load_state_dict(best_state)             # early stopping
print(f"best validation RMSE {best_val:.0f} g at epoch {best_epoch}")
print(f"test RMSE {rmse_grams(x_te, y_te):.0f} g")
print("parameters:", sum(p.numel() for p in model.parameters()))
