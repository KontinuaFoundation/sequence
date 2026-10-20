# Bayesian Networks — Notes

## Summary
Introduces Bayesian networks as DAGs with conditional probability tables. The rain-and-wet-grass example gives P(W) = 0.26 and P(R | W) ≈ 0.692 by Bayes' rule. It names three reasoning patterns (prediction, diagnosis, and explaining away), and it distinguishes parameter learning from structure learning. It has two exercises (P(W) = 0.5 when P(R) = 0.5, and the number of CPT rows for a node with two binary parents).

## Changes in this pass
- Fixed the count of numbers for R. The network needs one number, P(R) = 0.2, because P(¬R) = 0.8 follows. The old text said "two numbers."
- Retitled exercise bn1 from "Compute a posterior" to "Compute a total probability," since it computes P(W).
- Added a high school link for explaining away: a wet lawn from rain or a sprinkler.

## Checked and correct
- P(W) = 0.9(0.2) + 0.1(0.8) = 0.26.
- P(R | W) = 0.18/0.26 ≈ 0.692.
- Exercise bn1: with P(R) = 0.5, P(W) = 0.5.
- Exercise bn2: two binary parents give 4 rows.

## Open items
- The chapter has no figure of the rain-and-grass network. A small DAG figure would make the arrow convention concrete.
- The worked example could also show the explaining-away calculation with a second cause (for example, a sprinkler) using numbers.
