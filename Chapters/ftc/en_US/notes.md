# The Fundamental Theorem of Calculus — Notes

## Summary
States both parts of the FTC, gives the proof that d/dx ∫ₐˣ f = f, works derivatives of integrals with the chain rule, evaluates definite integrals with antiderivatives (power consumption ≈ 26.5 kWh), and covers average value of a function. Includes practice problems and answers.

## Strengths
- The proof of the first part follows the squeeze-theorem argument clearly.
- The energy integral is correct: ∫₀²⁴ (1/10)t²(t−24)² dt = 26,542.1 Wh.
- Several answers are correct: the FTC1 derivatives (including h′(x) = x eˣ and y′ = −½ tan√x), the FTC3 ranking, the defint6 value 2π − 2, the defint7 velocity 11.71, and the average value 4 on [−2, 1].

## Weaknesses
- **Wrong argument in the AP answer:** the L'Hôpital step writes g(6)/g′(6) where it should write g(1)/g′(1). The result 2 is still correct.
- **Wrong variable:** S′(x) is written as sin(πt²/2) instead of sin(πx²/2).
- **Inconsistent limit:** f(x) = ∫₁^(x⁴) sec t dt is then differentiated as if the lower limit were 0. The derivative is unchanged, but the example is inconsistent.
- **Unit mismatch:** the power-consumption figure is labeled in kW, but P is given in watts (P(12) ≈ 2074 W).
- **FIXME notes:** the chain-rule FTC and area between curves are still open.

## Index entries added
average value of a function, squeeze theorem, Fresnel function, definite integral (antiderivatives), chain rule (with integrals). The chapter already had the FTC and both parts.

## Editor to-do
- Fix g(1)/g′(1), the sin(πx²/2) variable, and the lower limit in the chain-rule example.
- Reconcile the kW label with the watt values.

- Merged in from `physics_appl_ftc`: the physics applications (position and velocity, work and kinetic energy, force and impulse) are the last section group. The exercise there is labelled `velocity`.
