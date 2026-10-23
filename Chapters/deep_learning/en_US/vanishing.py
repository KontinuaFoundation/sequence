import torch
from torch import nn

def first_layer_gradient(activation, depth, seed=0):
    """Average size of the gradient reaching the first layer of a deep network."""
    torch.manual_seed(seed)
    layers = []
    for _ in range(depth):
        linear = nn.Linear(64, 64)
        if activation is nn.ReLU:      # "He" initialization, designed for ReLU
            nn.init.kaiming_normal_(linear.weight, nonlinearity="relu")
        else:                          # "Xavier" initialization, designed for sigmoid-like units
            nn.init.xavier_normal_(linear.weight)
        nn.init.zeros_(linear.bias)
        layers += [linear, activation()]
    model = nn.Sequential(*layers, nn.Linear(64, 1))
    x = torch.randn(256, 64)
    loss = model(x).pow(2).mean()
    loss.backward()
    return model[0].weight.grad.abs().mean().item()

print("depth   sigmoid      ReLU")
for depth in [2, 5, 10, 20, 40]:
    s = first_layer_gradient(nn.Sigmoid, depth)
    r = first_layer_gradient(nn.ReLU, depth)
    print(f"{depth:5d}  {s:9.2e}  {r:9.2e}")
