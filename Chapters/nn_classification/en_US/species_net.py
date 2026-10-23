import numpy as np
import torch
from torch import nn
from penguins import load_penguins

data = load_penguins()
names, labels = np.unique(data["species"], return_inverse=True)
X = np.column_stack([data["bill_length_mm"], data["bill_depth_mm"],
                     data["flipper_length_mm"], data["body_mass_g"]])
order = np.random.default_rng(1).permutation(len(labels))
train, test = order[:233], order[233:]

mean, sd = X[train].mean(axis=0), X[train].std(axis=0)
x_tr = torch.tensor((X[train] - mean) / sd, dtype=torch.float32)
x_te = torch.tensor((X[test] - mean) / sd, dtype=torch.float32)
y_tr = torch.tensor(labels[train])        # class numbers 0, 1, 2 (integers)
y_te = torch.tensor(labels[test])

torch.manual_seed(0)
model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 3))   # 3 scores out
loss_fn = nn.CrossEntropyLoss()             # applies softmax, then -ln p(true class)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(1, 31):
    perm = torch.randperm(len(y_tr))        # shuffle, then mini-batches of 32
    for start in range(0, len(y_tr), 32):
        batch = perm[start:start + 32]
        optimizer.zero_grad()
        loss = loss_fn(model(x_tr[batch]), y_tr[batch])
        loss.backward()
        optimizer.step()
    if epoch in (1, 5, 30):
        with torch.no_grad():
            acc = (model(x_te).argmax(dim=1) == y_te).float().mean().item()
            print(f"epoch {epoch:2d}: training loss {loss_fn(model(x_tr), y_tr).item():.3f},"
                  f" test accuracy {acc:.3f}")

with torch.no_grad():
    probs = torch.softmax(model(x_te), dim=1)
predicted = probs.argmax(dim=1)
matrix = np.zeros((3, 3), dtype=int)
for p, a in zip(predicted, y_te):
    matrix[p, a] += 1
print("Rows: predicted, columns: actual", names)
print(matrix)
print("Least confident test penguin:")
i = probs.max(dim=1).values.argmin()
print(" probabilities", np.round(probs[i].numpy(), 3), " actually", names[y_te[i]])
