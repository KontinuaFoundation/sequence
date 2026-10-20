# Matrices and Systems — Notes

## Summary
Shows how a linear system becomes a matrix equation Ax = b, then solves systems with row operations to REF and RREF. Covers free variables, zero rows, inconsistent systems, rank, dimension, and basis. Ends with applications (linear combinations in matrix form, a trail-mix budget, and a weighted-grades exercise) and numpy examples for creating and transposing matrices.

## Merge history
- Sources: `systems_matrices` (4270 words), `matrices_applications` (930 words).
- `matrices_creation.py` lives in this directory.

## Changes in this pass
- Fixed the constant vector in the opening example (b = (-1, 4)).
- Fixed Kai's trail-mix cost ($393.00, not $615.50), and stated that Kai costs the most.
- Rewrote the answer to "Augmented Matrices 2". The old answer showed the RREF of a different matrix. The new answer solves the given system: (-5, 11, 8).
- Corrected the rule for an inconsistent system. A row of zeros does not signal inconsistency. A zero row with a nonzero constant does.
- Fixed the numpy output for the vector-matrix product ([32 -9 -11]) and a syntax error (`np.diag(Q)`).
- Removed a visible "FIXME exercises" line and stray tab characters.
- Replaced "ie." with plain examples and corrected a few typos.

## Open items
- The printed outputs in the numpy listings were checked by hand, not by running the code.
