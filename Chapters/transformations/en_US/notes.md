# Matrices as Transformations — Notes

## Summary
Treats matrices as functions T: ℝⁿ → ℝᵐ, explains that columns are the images of the basis vectors, then works scaling, shear, reflections across the axes and y = ±x, rotations, a guess-the-matrix exercise, and inverses for undoing transforms, ending with a note on non-invertible matrices.

## Strengths
- The reflection matrices are correct, including y = −x, which maps (x, y) to (−y, −x) with matrix [[0, −1], [−1, 0]].
- The general rotation matrices and the inverse of the 30° rotation (which is the counterclockwise rotation) are correct in their final form.
- The non-invertible examples (determinant zero) are correct.

## Weaknesses
- **Swapped rotation directions:** the text says a 90° clockwise rotation sends e₁ to e₂, and counterclockwise sends e₁ to −e₂. The reverse is true (counterclockwise sends e₁ → e₂). The basis-tracking lines are swapped relative to the labeled matrices as well.
- **Mislabeled transformation:** [[1, 0], [0, 2]] is called a "rightward shear," but it is a vertical scaling, not a shear.
- **Wrong intermediate step:** in the 30° inverse, the adjugate is written as [[cos, sin], [sin, cos]]. It should be [[cos, −sin], [sin, cos]], which is the form in the final line.
- **Stray text:** a dangling sentence "all had something similar %fixme" appears in the rotations section.

## Index entries added
matrix transformation, domain, codomain, shear, rotation matrix, inverse transformation, non-invertible transformation.

## Editor to-do
- Swap the cw and ccw basis-tracking lines (and check the matrices).
- Rename the rightward-shear example and fix the adjugate step.

