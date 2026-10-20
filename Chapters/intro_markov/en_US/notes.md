# Introduction to Markov Chains — Notes

## Summary
Introduces the Markov property with a weather example, state diagrams and transition matrices, a hot dog stand exercise (state diagram and a 3-visit path sum of 0.3705), multi-step transitions with matrix powers (a chemical example with P³), steady-state distributions, and applications: PageRank, hidden Markov models, and part-of-speech tagging.

## Changes in this pass
- Made the eigen-exercise matrix row-stochastic (each row sums to 1), matching the chapter's convention. The steady-state equation is now written as π P = π. The answer π = (1 − q, 1 − p) and the value 4/11 ≈ 0.364 are unchanged.
- Fixed the HMM text: it said T but showed S.
- Replaced a garbled dynamic-programming sentence.
- Replaced "Adverb" with "Adjective" in the NLP example (the tag set has no adverb).
- Replaced a Unicode ∣ inside math mode with \mid.
- Fixed "was curious," "only square matrices are possible," and a repeated Law of Large Numbers reference.

## Strengths
- The hot dog answers are correct: P(R | I, R, N) = 0.30, the two-step I → R probability is 0.24, and the three-step N → I probability is 0.3705.
- The chemical example's P² and P³ are correct, and P(Green | Blue) after three steps is 0.111.
- The NLP exercise answer 0.10 is correct.

## Open items
- The PageRank section describes the modified matrix without a worked numerical example.
- The text uses P(Verb | Noun) = 0.6 as an example, and the NLP exercise uses 0.5 from its own training data. This is fine, but the two numbers may confuse readers.
