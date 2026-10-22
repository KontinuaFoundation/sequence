# Binomial and Geometric Distributions: Summary

## What the chapter covers
Covers the two AP Statistics distributions for repeated independent trials:
- Binomial (successes in a fixed number of trials): the BINS conditions, the formula C(n,k)pᵏ(1−p)ⁿ⁻ᵏ derived from counting arrangements, 'at least' and 'at most' with complements, μ = np and σ = √(np(1−p)) derived from 0/1 indicator variables, shape and the np ≥ 10 rule, and the 10% condition.
- Geometric (trials until the first success): (1−p)ᵏ⁻¹p, P(X > k) = (1−p)ᵏ, μ = 1/p by a first-step argument, σ = √(1−p)/p, and memorylessness (the gambler's fallacy).
Includes SciPy and simulation checks, and ends with a preview of the Poisson distribution as the rare-event limit of the binomial.

## Key ideas
- Binomial: BINS; P(X = k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ; μ = np, σ = √(np(1−p)).
- Geometric: P(X = k) = (1−p)ᵏ⁻¹p; P(X > k) = (1−p)ᵏ; μ = 1/p, σ = √(1−p)/p.
- Use complements for 'at least one'; read 'at least' vs. 'more than' carefully.
- Sampling without replacement is approximately binomial if the sample is at most 10% of the population.
- The geometric distribution has no memory: past failures do not make success 'due'.

## Changes in this pass
- New chapter, placed in volume 28 between random_variables (expected value, variance, linearity) and poisson_exponential, which it previews (Poisson as the rare-event limit; memorylessness as with the exponential).
- Uses the binomial coefficients from discrete_probability_counting; replaced that chapter's '%FIXME go more indepth on binomial distribution' with a pointer here.
- Includes two PMF figures (binomial_pmfs.png, geometric_pmf.png), a SciPy listing (distributions.py), a seeded simulation (simulate_free_throws.py), and 6 exercises with answers (is it binomial?, lefties, just guessing, the first miss, how many packs for 90% (18), binomial or geometric?).
- All values verified with SciPy and by simulation.
