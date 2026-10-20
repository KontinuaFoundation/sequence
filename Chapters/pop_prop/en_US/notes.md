# Population Proportion Statistics — Notes

## Summary
Builds from the binomial distribution for a 12-voter sample (r = 0.62) to the likelihood of an observed 9-of-12 result, then to a posterior density under a uniform prior, identifies it as a Beta(k+1, n−k+1) distribution, and gives a scipy calculation that P(r > 0.5) ≈ 95.39%. It ends with one exercise (20 voters, 15 yes).

## Changes in this pass
- Fixed the share of the population that does not support the candidate. It is 38%, not 48%.
- Fixed "This is a called a likelihood" to "This is called a likelihood."
- Replaced the claim that the likelihood's area is "significantly less" than 1 with the actual value. The integral of 220 r⁹(1−r)³ over [0, 1] is 1/13 ≈ 0.077.
- Removed the unused numpy import from the Python block.
- Added an exercise (20 voters, 15 yes). The answer is the Beta(16, 6) probability P(r > 0.5) ≈ 98.67%.

## Checked and correct
- The binomial table for n = 12, r = 0.62 (checked each entry, including p(0) ≈ 0.000009 and p(11) ≈ 0.023729; the mode is k = 8 at 0.2254).
- The 9-of-12 likelihoods: 1.6 × 10⁻⁷ at r = 0.1 and 0.2397 at r = 0.7.
- The beta result: P(r > 0.5) = 1 − 378/8192 ≈ 95.39%, which matches the scipy output.

## Open items
- The chapter uses "Bayes' Law" in one place and "Bayes' theorem" in the index. Pick one name.
- The bar chart and likelihood figures are image files. They were not checked in this pass.
