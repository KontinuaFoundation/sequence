# Images in Python — Notes

## Summary
Represents an image as a NumPy array of 8-bit integers (480 × 640 × 3 for RGB), then builds three scripts with imageio: a black 640 × 480 image, a red-to-black gradient with blue and green stripes added pixel by pixel, and a script that splits an existing image into red, green, and blue channel files.

## Strengths
- The code grows in small steps, and each step has a described visual result (black → red → blue/magenta → stripes).
- The RGB-to-magenta and cyan/yellow explanations match the channel math.

## Weaknesses
- **Broken import:** all three listings use `import NumPy as np`. Python is case-sensitive, so this raises ImportError. It should be `numpy`.
- **Missing import:** separate_image.py calls `np.zeros` but never imports numpy, so it raises NameError.
- **Typo:** "Let's create a simply python program".
- **Possibly deprecated API:** `imageio.imread` and `imwrite` are older calls, and recent imageio versions have changed them. Check against the version the book targets.
- **Overly terse usage line:** "Usage {argv[0]} <outfile>" does not say what the output format is.
- **Unverified figures:** red.png, rb.png, and rgb.png are referenced but not checked against the code.

## Index entries added
imageio, NumPy array, RGB, pixel, command-line argument, color (RGB), image file formats.

## Editor to-do
- Fix the import capitalization in all three listings and add the numpy import to separate_image.py.
- Confirm the imageio API and regenerate the figures from the final code.
