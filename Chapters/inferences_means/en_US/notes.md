# Statistical Inferences for Means — Notes

## Summary
Covers the t-distribution, conditions, matched pairs, one-mean and two-mean intervals and tests (Welch approximation), Excel's CONFIDENCE.T, error types, and a procedure-selection flowchart.

## Strengths
- Most numbers check out: t* values (2.064, 2.069, 2.602, 1.796, 1.699, 1.740), the watch-time interval, and the battery interval (0.23, 2.57).
- I recomputed the one-sided and two-sided p-values with numerical integration; they match (0.0465, 0.0158, 0.0043, 0.0383, 0.0020, 0.278).
- The interpretation section correctly explains the confidence level as a property of the method, not a probability for μ.

## Weaknesses
- **Wrong t* value:** "At df = 100, t* = 1.984" is the 95% value. The 90% value is 1.660.
- **Overgeneralized claim:** "A confidence interval and a significance test on the same data will always agree" holds only for a two-sided test against a matching two-sided interval. The paired example compares a one-sided test to a 90% two-sided interval.
- **Broken cross-reference:** the battery-justification answer uses ref={ex:justify}, but the exercise label is ex:means-justify.
- **Unverified claim:** the pooled-variance answer says the current AP Statistics CED omits pooled procedures. I did not check this.
- **Typo:** "TTesting."

## Index entries added
conditions for inference, standard error, Type I error, Type II error, power, Welch-Satterthwaite approximation, two-sample t-interval, hypothesis test (two-sample), confidence interval interpretation.

## Editor to-do
- Fix the paired-data direction in the answer and the test narrative.
- Correct the df = 100 value and the cross-reference, and narrow the "always agree" claim.
