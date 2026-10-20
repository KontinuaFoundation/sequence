# Matrices — Notes

## Summary
Covers matrices and their dimensions, matrix addition and scalar multiplication, the dot product, matrix multiplication (with a check that the inner dimensions match), and types of matrices such as transposes. It has eight exercises with answers and three worked examples.

## Changes in this pass
- Checked the dot-product answers (-7, -8, and 9). Correct.
- Checked the matrix product A B for the 2 x 2 example ([[23, -18], [1, -1]]). Correct.
- Repaired two garbled answers in the "Multiplying Matrices 2" exercise. The first product's fourth row is [8, -6, 10, 4], and the B A entry that was a dash is 0. The full set of six products was recomputed with numpy, and the answers now match it.

## Open items
- The chapter's section headings are "Matrices," "Operations of Matrices," and "Types of Matrices," but the dimension exercises depend on matrices defined in the text. Check that the dimension answers match the matrices shown.
