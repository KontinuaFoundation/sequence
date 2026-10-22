# Euler's Formula and the Complex Exponential: Summary

## What the chapter covers
Defines e^z for complex z by its Taylor series and derives Euler's formula e^{iθ} = cos θ + i sin θ, with a Python check of the partial sums spiraling to e^{iπ} = −1. Then interprets e^{iθ} as the point on the unit circle at angle θ (Euler's identity), introduces polar form re^{iθ}, explains multiplication as 'multiply lengths, add angles', De Moivre's formula, and roots of unity, derives the angle-sum identities, and applies the complex exponential to circular motion, springs, damped oscillations, and AC phasors.

## Key ideas
- e^{iθ} = cos θ + i sin θ; e^{iπ} + 1 = 0.
- z = re^{iθ}, with r = |z| and θ = the argument; multiply by multiplying lengths and adding angles.
- (re^{iθ})ⁿ = rⁿe^{inθ}; the nth roots of unity are e^{2πik/n}.
- cos θ = (e^{iθ} + e^{−iθ})/2 and sin θ = (e^{iθ} − e^{−iθ})/(2i).
- d/dt e^{iωt} = iω e^{iωt}: the velocity is the position rotated 90°.

## Changes in this pass
- New chapter, placed in volume 34 right after taylor_series, whose series for eˣ, sin, and cos it builds on.
- Explains three things earlier chapters stated without proof: 'multiplying rotates and stretches' (complex_numbers, volume 9), the geometric sum formulas (trig_identities, volume 6), and the e^{αt}(cos βt + sin βt) row for complex roots (diff_eqs, volume 32).
- Includes a partial-sums figure (partial_sums.png, generated from partial_sums.py), a unit-circle figure, a cube-roots figure, two Python listings with real output, and 6 exercises with answers (values on the circle, polar form, De Moivre, cube roots of 8, double angles, i^i ≈ 0.2079, conjugates, and a Python check).
- All values verified in Python (for example, (1 + i)^10 = 32i, (1 − √3i)^6 = 64, and the 75° product).
