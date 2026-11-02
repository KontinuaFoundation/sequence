# Illustration Guide

General guidelines for drawn Kontinua illustrations (the ones made in Adobe
Illustrator, as opposed to diagrams drawn in LaTeX with TikZ). The
[Illustration Notes](illustration.md) describe each existing illustration, and
the [Style Guide](style.md#images-and-plots) explains why we keep printing costs
down.

## Colors

| Color | Hex |
| --- | --- |
| Kontinua Blue | `#005992` |
| Dark Gray | `#c2c1c0` |
| Light Gray | `#d8d8d8` |
| Red | `#dd5041` |
| Blue | `#53a7dc` |
| Yellow | `#f0b358` |
| Green | `#4b9751` |
| Brown | `#90582f` |

When necessary, adjust the brightness of these colors.

The printed workbooks use only black and Kontinua Blue (`sdkblue` in LaTeX), and
some copies are printed in black and white. Make sure an illustration still reads
in grayscale, and avoid large areas of heavy ink.

## Type

| Use | Font |
| --- | --- |
| Body text | Open Sans Regular, 24 pt |
| Labels | Open Sans SemiBold, 24 pt |
| Titles, a rare important label | Open Sans Bold, 24 pt |
| Math and forces | Open Sans Regular, 24 pt |
| Math that the text refers to | Marcellus Regular, 24 pt |

These sizes are for the standard 10 in × 8 in artboard (see "Dimensions" below),
which LaTeX scales down to fit the page.

Exceptions:

* `cgcm.png` uses Open Sans Regular for its labels. It has an unusual key/legend,
  and a heavier weight looked bad there.
* `cow3.png` uses 12 pt text, which looks better for the photon labels.
* `hammerTime.png` uses 36 pt for the times, to show the hierarchy.

## Arrows

* **"Fancy" arrows**: forces, and any motion that the text treats as math.
* **Normal arrows**: movement, and anything that is not math or a force.

## Call-outs

* **Text call-out**: a dashed line `- - - - -`.
* **Explosion or zoom call-out**: a solid line ending in a solid circle `-----O`.

## Shading

When it helps, add shading to give depth to an illustration (for example, the
rocket illustrations).

Do not shade cross sections (for example, lenses and the jet engine).

## Isometric views

Some illustrations use an isometric view to give more context, for example the
3D printer, CNC machine and laser cutter in the manufacturing chapter.

These Illustrator actions turn a flat drawing into one face of an isometric view:

| Face | Steps |
| --- | --- |
| Top | Scale vertically 86.06%, shear 30°, rotate −30° |
| Left | Scale vertically 86.06%, shear −30°, rotate −30° |
| Right | Scale vertically 86.06%, shear 30°, rotate 30° |

## Files and organization

* **Illustrator file**: one `.ai` file per chapter, with each illustration on its
  own artboard. Keep it in the chapter's `en_US` directory, next to
  `student.tex`.
* **PNGs**: each artboard exported as a PNG into the same directory. To export
  many illustrations at once, use **Export As** and select the range of
  artboards.
* **`student.tex`**: put each PNG in a `figure` environment (see
  [Figures and diagrams](writer.md#figures-and-diagrams) in the writer's guide).

## Dimensions

* **10 in × 8 in**: the standard artboard.
* **15 in × 8 in**: for double-width or very wide graphics. Multiply font sizes by
  1.5, because LaTeX scales the image down more.

When the illustration is done, trim the artboard vertically to fit it.
