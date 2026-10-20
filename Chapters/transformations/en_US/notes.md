# Matrices as Transformations — Notes

## Summary
Treats matrices as functions T: ℝⁿ → ℝᵐ, explains that columns are the images of the basis vectors, then works scaling, shear, reflections across the axes and y = ±x, rotations, a guess-the-matrix exercise, and inverses for undoing transforms, ending with a note on non-invertible matrices.

## Changes in this pass
- Swapped the basis-vector tracking for the clockwise and counterclockwise 90° rotations so each matches its matrix.
- Fixed the adjugate step in the 30° inverse: [[cos, −sin], [sin, cos]].
- Renamed the matrix [[1, 0], [0, 2]] from "rightward shear" to "vertical scaling". Added a real shear, [[1, 2], [0, 1]], with a short explanation before the house figure.
- Removed the dangling "%fixme" sentence in the rotations section.
- Stated the domain and codomain in ordinary words, and fixed "every vector in the subspace of ℝⁿ."
- Rewrote the garbled "reflected across the rotated 30° clockwise" sentence and the "plethora transformations" sentence.
- Added a clock-hands picture to the rotation section, and a worked example applying the counterclockwise matrix to (2, 1), giving (−1, 2).
- Fixed a stray space in the cw rotation matrix in LaTeX.
- Removed the reference to "previous" inverse functions in the y = −x section, which the chapter did not cover.

## Strengths
- The reflection matrices are correct, including y = −x, which maps (x, y) to (−y, −x) with matrix [[0, −1], [−1, 0]].
- The general rotation matrices and the inverse of the 30° rotation are correct in their final form.
- The non-invertible examples (determinant zero) are correct.
- The shear inverse exercise is correct: [[1, −k], [0, 1]].
- All figure files and transforms.py referenced by the chapter exist in this directory.

## Open items
- The guess-the-matrix answer (A = [[1.5, 0], [−2, −1]]) was not checked against the image.
- The chapter describes transforms.py, but the chapter does not explain how to run it. A short note would help.
