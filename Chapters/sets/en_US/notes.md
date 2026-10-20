# Sets and Logic — Notes

## Summary
Introduces sets (notation, membership, subsets, union, intersection, complement, difference, power sets, cardinality) with Venn diagrams, then logical connectives (and, or, not, implies, if and only if, XOR), truth tables, DeMorgan's rules, and the contrapositive. It ends with Python code that prints truth tables with itertools.

## Strengths
- Venn diagrams with concrete numbers make set operations concrete.
- Truth tables are built one step at a time, and an exercise checks DeMorgan's rule.
- Python code connects logic to programming, which the course needs later.

## Weaknesses
- **Wrong example in code:** the text says "what is 'a and not b'," but the code computes "a or not b."
- **Broken LaTeX:** "index{XOR}" is missing its backslash, so the word "index{XOR}" prints in the text.
- **Wrong variable:** the "even" iff statement uses p in the first clause and n in the second.
- **Misspelling:** "George Bool" should be George Boole.
- **Dangling sentence:** "Outside of logic, the concept of a set" ends the complement section with no continuation.
- **Unfinished:** FIXME "expand this logic section," and an ADD for a chapter summary.
- **Weak claim:** "a few strange results" from the axiom of choice is not specified; the ZFC axiom count (10) depends on how axioms are counted.
- **Unclear:** "there is even notation for 'there exists'" should be "there is also."

## Index entries added
axiom, ZFC, empty set, DeMorgan's laws, complement, distributive property, exclusive or, XOR (fixed), cardinality ! infinite sets. (Existing entries kept.)

## Editor to-do
- Fix the "a or not b" example and the XOR index markup.
- Correct the "p/n" variable and "George Boole."
- Finish the logic section and the complement paragraph.
