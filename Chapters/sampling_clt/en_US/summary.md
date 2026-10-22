# Sampling Distributions and the Central Limit Theorem: Summary

## What the chapter covers
Explains why a poll of 1,000 people can describe a whole country:
- parameters vs. statistics and sampling variability;
- a simulation of 10,000 sample means from a skewed population (n = 1, 5, 30) showing the center, spread, and shape of the sampling distribution;
- μ_x̄ = μ and σ_x̄ = σ/√n derived from the random-variable rules (unbiasedness and the square-root law);
- the Central Limit Theorem and the n ≥ 30 rule of thumb;
- an elevator weight-limit example, and individuals vs. averages;
- the sampling distribution of p̂ (mean p, sd √(p(1−p)/n), large counts), the origin of '±3 points', and a poll simulation.

## Key ideas
- A sampling distribution is the distribution of a statistic over all possible samples.
- μ_x̄ = μ and σ_x̄ = σ/√n; four times the data halves the spread.
- CLT: for large n, x̄ is approximately normal whatever the population's shape (rule of thumb n ≥ 30).
- p̂ has mean p and sd √(p(1−p)/n); it is approximately normal when np ≥ 10 and n(1−p) ≥ 10.
- The CLT is about the distribution of sample means, not about the data becoming normal.

## Changes in this pass
- New chapter, placed in volume 30 between continuous_distributions (the normal distribution) and inferences_proportion. It explains the large-counts and n ≥ 30 conditions those inference chapters use without justification. Added a pointer from continuous_distributions' one-bullet CLT mention.
- Builds on random_variables (linearity, adding variances), binomial_geometric (p̂ = X/n), poisson_exponential (the skewed exponential population), and monte_carlo (the 1/√n error).
- Includes two seeded simulations with real output (clt_simulation.py with its figure, poll_simulation.py) and 4 exercises with answers (center and spread, watch times, a common misconception, dice averages).
- Verified with SciPy, including an honest note that the normal approximation for the n = 100 poll (0.157) differs from the exact binomial answer (0.135) because p̂ moves in steps of 0.01.
