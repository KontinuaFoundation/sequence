import torch

x = torch.tensor(3.0, requires_grad=True)
y = x**2 + 2 * x            # PyTorch records how y was computed
y.backward()                # ...so it can work out dy/dx
print(y.item(), x.grad.item())
