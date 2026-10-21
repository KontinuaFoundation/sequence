import sympy as sp

x, y, lam = sp.symbols("x y lambda", real=True)
f = x**2 + 2*y**2          # what we optimize
g = x**2 + y**2            # the constraint is g = 1

# grad f = lambda * grad g, together with the constraint
equations = [
    sp.Eq(sp.diff(f, x), lam * sp.diff(g, x)),
    sp.Eq(sp.diff(f, y), lam * sp.diff(g, y)),
    sp.Eq(g, 1),
]
for sol in sp.solve(equations, [x, y, lam], dict=True):
    print(sol, " f =", f.subs(sol))
