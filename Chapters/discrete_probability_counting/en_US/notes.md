# Discrete Probability and Counting — Notes

## Summary
Introduces discrete probability (complements, independence, correlation and causation), dice sums and simulation in Python, counting with the multiplication principle, permutations, combinations, the generalized binomial theorem and series, binomial probability, and permutations and sorting (composition, inverses, cycles).

## Changes in this pass
- Corrected the table entry for a sum of 10: probability 1/12 (3/36), not 1/22.
- Fixed the random-number examples (random.randrange, the range(30) output, which had 29 twice).
- Fixed three broken print statements (Counts, the per-sum loop) and the math.comb call.
- Corrected the general binomial coefficient: the product ends at (n − k + 1).
- Fixed "In the previous chapter" (it refers to this chapter's earlier section) and "are not you glad."
- Added a hint for the permutation challenge (swap first two, swap last two of a three-item list; the two swaps do not commute).

## Strengths
- The fractional binomial exercise answers are correct: 1 − x + x² − x³ for (1 + x)⁻¹ (valid for |x| < 1), and 1 − x − ½x² for √(1 − 2x).
- The binomial probability (10/32 = 5/16 for 3 heads in 5 flips) and free-throw answer (0.31104) are correct.
- The inverse and cycle examples are correct.

## Open items
- The permutation challenge has no written answer. Add one, or keep the hint as the only guidance.
- The sample printed outputs are random. They are illustrative.
