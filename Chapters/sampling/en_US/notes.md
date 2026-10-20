# Sampling Data — Notes

## Summary
Covers the planning of a study: population, frame, sample, census, and the reasons a census is often impractical. It then describes biased methods (judgmental, convenience, voluntary response), simple random sampling, systematic, stratified, and cluster sampling (with the strata-versus-clusters distinction), and sources of survey bias (sampling error, response, nonresponse, undercoverage, and wording). Ends with Python exercises that use a web dataset and a simulated dataset.

## Strengths
- The population/frame/sample/census vocabulary is clear, with examples.
- The exercises are varied and their answers are correct (for example, the identifying-sampling-methods table).
- The seed-42 simulation's true mean (79.7) matches a recomputation.

## Weaknesses
- **Broken list:** the three reasons a census is hard are written with dashes, not \texttt{itemize}, so they will run together in one paragraph.
- **Imprecise definition:** "a census is what happens when the sample and the population are the same thing or equal in number" is unclear.
- **Unverified claim:** the web dataset is said to hold 265 countries and territories. This is not checked, and the exercise depends on a live URL.
- **Deprecated pattern:** `groupby(...).apply(lambda x: x.sample(n=3))` may warn in pandas 2.2+.
- **Commented-out answer:** the answer to the Python comparison is commented out with `%`, so it does not appear in the book.
- **Missing images:** eight "FIXME image/illustration needed" comments remain.
- **Typo:** "ie:" should be "i.e.".

## Index entries added
sampling frame, population parameter, random number table, quota sampling, non-probability sampling, TI-84!randInt.

## Editor to-do
- Convert the dash list to \texttt{itemize} and rewrite the census definition.
- Verify the dataset count and add a fallback if the URL fails.
- Decide whether to restore the commented-out answer and add the eight illustrations.
