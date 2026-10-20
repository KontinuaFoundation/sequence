# Introduction to Linear Algebra — Notes

## Summary
Reviews vectors, matrices, and transformations from earlier workbooks, explains linear combinations, and walks through bitmap image operations (flip, rotate, invert, transpose, channel swaps, adding and normalizing grayscale images), applications, and a Python/PIL/NumPy script.

## Strengths
- The f + g image example is correct: the sum is [[1.5, 0.5, 0], [2, 1.5, 2], [1.5, 1, 1]], and dividing by 2 gives the normalized matrix shown.
- The inversion code is sound: np.invert on 0/1 gives −2 and −1, and adding 2 maps them to 0 and 1.

## Weaknesses
- **Likely code error:** Image.fromarray(bitmapArray*255) passes a float64 array. Pillow expects uint8, so this will likely fail. Use .astype(np.uint8).
- **Wrong claim:** rotating by an arbitrary angle is a linear transformation (a rotation matrix). The text says it "would be treading into nonlinear territory."
- **Open FIXMEs:** "this needs improvement" before the exercise, and the exercise is a single sentence.

## Index entries added
linear combinations, bitmap, false color images, Lagrange point, Halo orbit, Python Imaging Library, NumPy.

## Editor to-do
- Fix the fromarray dtype and the rotation sentence.
- Replace the placeholder exercise with a full set of tasks.

