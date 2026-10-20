# Introduction to Markov Chains — Notes

## Summary
Introduces the Markov property with a weather chain (Sunny/Rainy), state diagrams, transition matrices and P^k, steady-state distributions via eigenvalue 1, PageRank with damping, and hidden Markov models for illness and part-of-speech tagging. Includes exercises with answers.

## Strengths
- The weather and hot-dog examples are clear, and the state diagrams match their matrices.
- The hot-dog returns exercise is correct: P(I→R in two steps) = 0.24 and P(N→I in three steps) = 0.3705, both checked by enumeration.
- The chemical exercise is correct (P³ entries 0.112, 0.888, 0.111, 0.889).
- The steady-state exercise is correct: the eigenvector (1−q, 1−p), giving 4/11 ≈ 0.364 at p = 0.3, q = 0.6. The NLP answer (0.5 × 0.2 = 0.10) is also right.

## Weaknesses
- **Wrong statement:** "Probability Distribution after k steps = P^k" is wrong. A distribution is π₀Pᵏ, and Pᵏ is the transition matrix.
- **Misattributed theorem:** convergence of Pᵏ is attributed to the Law of Large Numbers, which is the wrong result.
- **Name mismatch:** the text says "transition matrix T" and "emission matrix E," but the HMM display names the transition matrix S.
- **Adjective vs adverb:** the state set has Adjective, but the example path uses Adverb.
- **Garbled sentence:** the Viterbi/Forward paragraph says dynamic programming is "a method that programming similar to excel processing."
- **Typos:** "curious about," "an regular customer," and "only possible square matrices."

## Index entries added
Markov property, Markov chain, state space, transition matrix, steady-state distribution, PageRank, hidden Markov model, emission matrix.

## Editor to-do
- Correct the Pᵏ distribution statement and the LLN attribution.
- Fix the S/T naming, the Adverb/Adjective mismatch, and the garbled sentence.
