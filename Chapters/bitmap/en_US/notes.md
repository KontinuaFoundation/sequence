# Bitmaps — Notes

## Summary
Explains 24-bit BMP pixels (BGR byte order), the BITMAPFILEHEADER and BITMAPINFOHEADER structs, 4-byte row padding and the rowSize formula, and pixel indexing. Walks through a C++ reader that swaps red and blue, an exercise that removes green, a program that writes a 3×3 bitmap from scratch, a 4×2 exercise, and a horizontal flip.

## Changes in this pass
- Fixed the file header label: 14 bytes (it was "(?)" in one diagram).
- Changed the 3×3 row calculation from "9 pixels" to "9 bytes".
- Added the missing output step to the red/blue swap: write the pixel data, close the file, and free the buffers.
- Added fclose(f) to the 3×3 example, and declared the row buffer with padding bytes set to 0.
- Made the row labels in the memory-order diagram match the code (Row 3 bottom, Row 1 top).
- Corrected the cow figure caption (it said "on a gradient").
- Fixed the flip explanation: the matrix [[−1, 0], [0, 1]] sends x to −x. The flip needs the shift x' = w − 1 − x, and a shift cannot be done by a matrix alone.
- Fixed typos ("species", "th ebitmap", "stays the same of", "can represented", "a more representation").

## Strengths
- The padding math is correct: 9 bytes rounds up to 12, and a 4×2 image is 78 bytes in the file.
- The red/blue swap writes the right bytes, and the green-removal answer is correct.
- The 4×2 and 3×3 BGR byte values are correct.
- The indexing formula y × rowSize + x × bytesPerPixel is clearly derived.

## Open items
- The reader snippets use std::string and argv without showing the includes. Add the includes to the reader code.
- The chapter has no worked example in the usual sense. The 3×3 build is the closest. Consider labeling it as one.
