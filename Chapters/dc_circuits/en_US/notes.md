# DC Circuit Analysis — Notes

## Summary
Builds DC circuit analysis from Ohm's law: series resistors (total resistance, voltage drops, Kirchhoff's Voltage Law), parallel resistors (the 1/R_t formula with a worked branch-current exercise), capacitors in series and parallel, and Kirchhoff's Current Law with a five-branch node exercise.

## Strengths
- Worked series and parallel examples check every step (e.g., 6 Ω ∥ 3 Ω = 2 Ω, 8 V drop, 2/3 A and 4/3 A).
- The KCL node exercise has a sign-convention twist (answer is 5 A entering) that tests understanding.
- Voltage-ladder diagram shows KVL visually.

## Weaknesses
- **Wrong physics:** "current is still divided evenly among both branches" is false; current divides inversely with resistance.
- **Wrong justification:** KCL is justified by "energy is always conserved"; KCL is charge conservation.
- **Inconsistent diagram:** the ground diagram labels the battery 6 V, but the node voltages (10 V, 4 V, 0 V) imply 10 V.
- **Broken reference:** the answer is labeled `series_resistors`, but the exercise is `series_resistor`.
- **Wrong wording:** a capacitor "stores voltage" (it stores charge); "equivalent capacitants" typo; "==" in an equation.
- **Garbled paragraph:** "lose voltage, and thus, cannot lose current" and "conservative" are misused.
- **Stray index:** `\index{index}` should be `\index{ground}` (fixed in this pass).
- **Unfinished:** ADD/FIXME markers for Ohm's law definition, KCL diagrams, and a capacitor section.

## Index entries added
series circuit, Ohm's law, node, equivalent resistance, direct current, ground (replaced "index"). (Existing entries kept.)

## Editor to-do
- Fix the "evenly divided" claim and the KCL justification.
- Fix the 6 V/10 V diagram and the answer label.
