# Bitmaps — Notes

## Summary
Explains 24-bit BMP pixels (BGR byte order), the BITMAPFILEHEADER and BITMAPINFOHEADER structs, 4-byte row padding and the rowSize formula, and pixel indexing. Walks through a C++ reader that swaps red and blue, an exercise that removes green, a program that writes a 3×3 bitmap from scratch, a 4×2 exercise, and a horizontal flip.

## Strengths
- The padding math is correct (9 bytes → 12; 12 × 3 = 36; 4×2 image = 78 bytes file).
- The red/blue swap logic writes the right bytes, and the green-removal answer is correct.
- The 4×2 and 3×3 BGR byte values are correct.
- The indexing formula y × rowSize + x × bytesPerPixel is clearly derived.

## Weaknesses
- **Header size:** the file header is labeled "(?)" in one diagram and "14-bit" in the text. It is 14 bytes.
- **Caption error:** the cow figure caption says "on a gradient."
- **Row labels:** the memory-order diagram uses Row 0–2, but the code uses ROW 1–3.
- **Flip matrix:** T = [[−1,0],[0,1]] flips about the origin, so it gives −x, not w−1−x. The text needs a translation step.
- **Undefined macro:** \vecb is not standard LaTeX and may not compile.
- **Typos:** "species" (twice), "th ebitmap," and "a more representation" in the selfie passage.
- **Missing code:** the 3×3 example never closes the file, and the snippets use std:: and the `row` buffer without declaring them.

## Index entries added
BMP file format, BITMAPINFOHEADER, row-major order, little endian, pragma pack, horizontal flip, BGR order. The chapter already had bitmaps, hexadecimal, padding, and segmentation fault.

## Editor to-do
- Fix the header size, cow caption, row labels, and flip matrix.
- Replace \vecb and fix the typos.
