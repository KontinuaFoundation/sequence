# Sequences in Calculus — Notes

## Summary
Defines explicit and recursive sequences, uses the coin-flip sample mean to motivate convergence, proves convergence and divergence (n/(n+1), n/√(10+n), sin(nπ/2)), evaluates limits with L'Hôpital and the Squeeze Theorem (ln n / n, n!/nⁿ), treats monotonic and bounded sequences, and applies sequences to savings, deer, and fish models.

## Changes in this pass
- Changed "series" to "sequence" when describing aₙ = n/(n+1) as convergent.
- Fixed the missing backslash in \lim in the squeeze argument.
- Removed a stray "\\" after the induction step for the bounded-above proof.
- Changed "Which is true" to "This is true" and "Out principal" to "Our principal."
- Rewrote the fish exercise to avoid assigning a pronoun to "the farmer."

## Strengths
- All seqcalc1 answers are correct, as are the seqcalc3 classifications and the n/(n²+1) decreasing proof.
- The n!/nⁿ squeeze argument (0 < aₙ < 1/n) is correct and clearly presented.
- The deer table (6520, 6542, 6565, 6590, 6617) checks out. The fish-loss total (about 137) was recomputed with the recurrence P_n = 0.95⁶P_{n−1} + 10. The 1500(1.06)¹⁰ = 2686.27 answer is correct.
- The savings table (4297.50 through 11445.62) was recomputed and is correct.

## Open items
- The population section introduces Pₙ = P₀(1+r)ⁿ, and the example uses a recurrence with harvesting. The two are related but the transition could be clearer.
- "FIXME summary section -- comparing exponents and growth rates" remains at the end of the file. The chapter needs a summary section or the FIXME should be removed.
