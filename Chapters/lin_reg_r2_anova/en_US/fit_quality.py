import numpy as np
from scipy import stats
from penguins import load_penguins

data = load_penguins()
x = data["flipper_length_mm"]
y = data["body_mass_g"]
n = len(y)

fit = stats.linregress(x, y)
y_hat = fit.intercept + fit.slope * x

ss_tot = np.sum((y - np.mean(y))**2)
ss_reg = np.sum((y_hat - np.mean(y))**2)
ss_res = np.sum((y - y_hat)**2)
print(f"SS_tot = {ss_tot:.4g}, SS_reg + SS_res = {ss_reg + ss_res:.4g}")

r_squared = 1 - ss_res / ss_tot
print(f"R^2 = {r_squared:.3f}, r^2 = {fit.rvalue**2:.3f}")
print(f"RMSE = {np.sqrt(ss_res / n):.0f} g")

# ANOVA: one predictor, n - 2 residual degrees of freedom
F = (ss_reg / 1) / (ss_res / (n - 2))
p_value = stats.f.sf(F, 1, n - 2)
print(f"F = {F:.0f}, p-value = {p_value:.1e}")

# The t statistic for the slope, from the previous chapter
t = fit.slope / fit.stderr
print(f"t = {t:.2f}, t^2 = {t**2:.0f}")
