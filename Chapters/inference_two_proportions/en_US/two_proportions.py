from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep

# Confidence interval: juniors vs. seniors who sleep 8+ hours
low, high = confint_proportions_2indep(84, 240, 54, 200, method="wald")
print(f"95% CI for p1 - p2: ({low:.3f}, {high:.3f})")

# Significance test: text reminder vs. no reminder
z, p_value = proportions_ztest([102, 84], [150, 150], alternative="larger")
print(f"z = {z:.2f}, p-value = {p_value:.4f}")
