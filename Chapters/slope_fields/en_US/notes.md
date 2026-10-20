# Slope Fields — Notes

## Summary
Introduces slope fields for y′ = x + y, sketches a solution through (1, 0), and applies a linear RL-type circuit (V = L dI/dt + RI) to get dI/dt = 15 − 3I with equilibrium I = 5 and I(t) = 5 − 5e^(−3t). Ends with a practice exercise for y′ = x + y².

## Strengths
- The construction of the slope field step by step (isoclines at y = −x) is clear and correct.
- The circuit derivation is correct: 4 dI/dt + 12I = 60 gives dI/dt = 15 − 3I, and the solution fits I(0) = 0.
- The autonomous-equation idea is explained well.

## Weaknesses
- **Typo:** "Kirchoff" should be "Kirchhoff" (used correctly elsewhere).
- **Typo:** "\addplot[red, thick,, domain" has a double comma.
- **Duplicate figures:** three or four slope-field figures repeat the same long block of draw commands, which makes the source hard to maintain.
- **Unverified answer:** the practice-problem answer curve through (0, 0) is hand-drawn and not checked against the field.

## Index entries added
direction field, inductor, Ohm's law, Kirchhoff's law, slope field (sketching solutions). The chapter already had slope field.

## Editor to-do
- Fix the typos.
- Factor the repeated slope-field code into one reusable definition.
