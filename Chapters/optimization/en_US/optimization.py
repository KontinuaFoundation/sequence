import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 1) Define the variable
x = sp.symbols('x')

# 2) Define the objective function (STUDENTS EDIT THIS)
f = 20*x - x**2

# 3) Derivatives
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)

# 4) Solve f'(x) = 0
critical_point = sp.solve(f_prime, x)[0]

# 5) Classify using second derivative
second_derivative_value = f_double_prime.subs(x, critical_point)

if second_derivative_value > 0:
    classification = "minimum"
elif second_derivative_value < 0:
    classification = "maximum"
else:
    classification = "inconclusive"

print("f(x) =", f)
print("f'(x) =", f_prime)
print("f''(x) =", f_double_prime)
print("Critical point:", critical_point)
print("Classification:", classification)

# 6) Plot
f_num = sp.lambdify(x, f, "numpy")

X = np.linspace(0, 20, 400)
Y = f_num(X)

xc = float(critical_point)
yc = float(f_num(xc))

plt.plot(X, Y)
plt.scatter([xc], [yc])
plt.title("Optimization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)

plt.annotate(
    classification,
    (xc, yc),
    xytext=(xc + 1, yc),
    arrowprops=dict(arrowstyle="->")
)

plt.show()
