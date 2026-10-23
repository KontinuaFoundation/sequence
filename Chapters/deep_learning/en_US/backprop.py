import torch

# A tiny network: h = relu(w1*x + b1), y_hat = w2*h + b2, loss = (y_hat - t)^2
x, t = 2.0, 1.0
w1, b1, w2, b2 = 0.5, 0.5, -1.5, 0.25

# Forward pass by hand
z = w1 * x + b1             # 1.5
h = max(0.0, z)             # 1.5
y_hat = w2 * h + b2         # -2.0
loss = (y_hat - t)**2       # 9.0

# Backward pass by hand: the chain rule, from the loss back toward the input
dL_dyhat = 2 * (y_hat - t)              # -6
dL_dw2 = dL_dyhat * h                   # -9
dL_db2 = dL_dyhat * 1                   # -6
dL_dh = dL_dyhat * w2                   # 9
dL_dz = dL_dh * (1.0 if z > 0 else 0.0) # ReLU passes the gradient only if z > 0
dL_dw1 = dL_dz * x                      # 18
dL_db1 = dL_dz * 1                      # 9
print("by hand:  ", loss, [dL_dw1, dL_db1, dL_dw2, dL_db2])

# The same thing with PyTorch's automatic differentiation
params = [torch.tensor(v, requires_grad=True) for v in (w1, b1, w2, b2)]
W1, B1, W2, B2 = params
loss_t = (W2 * torch.relu(W1 * x + B1) + B2 - t)**2
loss_t.backward()
print("autograd: ", loss_t.item(), [p.grad.item() for p in params])
