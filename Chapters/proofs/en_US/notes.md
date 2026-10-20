# Proofs — Notes

## Summary
A survey of proof techniques: direct proof (even and odd sums), trivial proof, proof by cases, disproof by counterexample, contraposition and contradiction (both applied to "3n+2 even ⇒ n even"), and induction (2ⁿ < n! for n ≥ 4). Closes with a summary and forward links.

## Strengths
- Each technique has a worked theorem with a complete proof.
- The same theorem is proved two ways (contraposition and contradiction), which shows how the methods differ.
- The induction example is correct and includes all steps.

## Weaknesses
- **Wrong definitions:** an implication is called "a theorem that relies on one proposition being equivalent to another," but it is a conditional statement. A proof is "valid" when its logic holds, not when its conclusion is true.
- **Induction error:** the inductive step says "we want to show 2^{k+1} < (k+1)" (should be (k+1)!), and "since k ≥ 4, k+1 < 2" is reversed.
- **Inconsistent hypothesis:** the inductive hypothesis says k ≥ 0, but the theorem starts at 4.
- **Duplicated sentence:** "a proof shows that a new statement aligns with all true statements" appears twice.
- **Typos:** "1true," "no affect," "counterexample,more," "us a base case," "the each case."
- **Stray items:** an empty \item in the definitions list.
- **Unfinished:** ADD markers for exercises in three places.

## Index entries added
direct proof, trivial proof, proof by contraposition, proof by contradiction, proof by induction, base case, inductive hypothesis.

## Editor to-do
- Correct the implication and validity definitions and the induction steps.
- Add the promised exercises.
