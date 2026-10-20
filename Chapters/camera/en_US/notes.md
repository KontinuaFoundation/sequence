# How Cameras Work — Notes

## Summary
Follows light from the sun to a cow and into a camera: sunlight emission, absorption versus reflection (why cows look colored), the pinhole camera and its inverted image, the similar-triangles exercise, lenses and focal length, sensor pixels and the photoelectric threshold, RGB, aspect ratio, and print sizes.

## Strengths
- The pinhole similar-triangles exercise is correct (image height = 2 m × 3 cm ÷ 3 m = 2 cm).
- The photon-energy exercise is correct (1240/1200 = 1.03 eV < 1.1 eV, so the pixels stay dark).
- Pixel arithmetic (6000 × 4000 = 24 million; 72 million numbers) and the 1920 × 1080 = 16:9 example are correct.

## Weaknesses
- **Swapped print sizes:** 4 × 6 is 3:2, and 8 × 6 is 4:3. The text says "4:3 … 4×6 … 3:2 … 8×6, respectively", which is backwards.
- **Inaccurate sensor model:** "each pixel has three types of cavities" describes a per-pixel RGB sensor. Most sensors use one color filter per photosite and interpolate the rest.
- **Unsolved exercise answer:** the answer says "the other is x cm" and then gives 2 cm without the proportion.
- **Ambiguous composition:** "About 70% of the gas is hydrogen" does not say by mass.
- **Duplicate label:** `fig:example` is used for two figures.
- **Leftover comments:** a FIXME about micro and macro lenses with a very long Amazon URL.

## Index entries added
pixel, image sensor, resolution, printing photos, work function, telephoto lens, wide-angle lens.

## Editor to-do
- Correct the print-size pairs and the sensor-model paragraph.
- Solve the proportion explicitly and rename the duplicate label; remove the Amazon URL.

