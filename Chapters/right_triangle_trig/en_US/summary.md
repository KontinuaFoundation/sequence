# Right-Triangle Trigonometry: Summary

## What the chapter covers
Defines sine, cosine, and tangent as side ratios in a right triangle (justified by similar triangles); derives tan = sin/cos and sin² + cos² = 1; gives exact values from the 45-45-90 and 30-60-90 triangles; and solves right triangles using angles of elevation and depression and the inverse trig keys. It then extends to any triangle: the Law of Sines (derived from an altitude) with the ambiguous SSA case, the Law of Cosines (derived with coordinates), the area formula ½ab sin C, a 'which tool?' table, and Python helpers.

## Key ideas
- SOH-CAH-TOA; the ratios depend only on the angle because right triangles with the same acute angle are similar.
- sin²θ + cos²θ = 1 is the Pythagorean theorem divided by hyp².
- Law of Sines: a/sin A = b/sin B = c/sin C (AAS, ASA; SSA may give 0, 1, or 2 triangles).
- Law of Cosines: c² = a² + b² − 2ab cos C (SAS, SSS); with C = 90°, it is the Pythagorean theorem.
- Area = ½ab sin C.

## Changes in this pass
- New chapter, placed first in volume 6, right before trig_functions.
- Why there: trig_functions opens with 'You already know that … sine is opposite over hypotenuse' and trig_identities says 'Recall SOH-CAH-TOA', but no chapter taught them. This chapter fills that gap. It builds on similar triangles and the 'no SSA test' from congruence (volume 5) and the Pythagorean theorem and distance formula from triangles_angles_parallels (volume 4).
- Includes 6 figures (side names with a similar triangle, flagpole, labeled triangle with altitude, ambiguous case), a Python listing (triangle.py) with real output, and 8 exercises with answers.
- All values verified in Python (flagpole 15.5 m, ladder 66.4°, pond 156.8 m, 5-6-7 angle 78.5°, ambiguous case 66.7°/113.3°, ship 33.8 km).
