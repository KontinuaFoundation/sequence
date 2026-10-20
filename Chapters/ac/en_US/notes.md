# Alternating Current — Notes

## Summary
Contrasts DC batteries with household AC (a 60 Hz, ±170 V sine wave that is 120 V RMS), derives the power of a resistor (V²/2R average, I_rms and V_rms = V_p/√2), explains why high-voltage transmission reduces line losses, and covers transformers, phase, three-phase power, and the 120/240 V split-phase supply in homes.

## Strengths
- Derives the average power by integrating the constant and cosine parts, showing why RMS is needed.
- The transmission-loss argument (I²R at high voltage) is the core engineering reason for transformers.
- Explains the home 120 V / 240 V supply, which students meet every day.

## Weaknesses
- **Wrong power-line numbers:** 12 kW at 120 V is 100 A, not 10 A. With 100 A, the loss in 20 Ω is I²R = 200 kW, which is more than the load. The chapter's 2 kW loss figure needs recomputing.
- **Wrong current:** at 120,000 V, 12 kW gives 0.1 A, not 0.01 A. The loss is then 0.2 W, not 0.002 W.
- **Wrong argument:** the power wave is written as cos(2πt/120). Its frequency is twice 60 Hz, so the argument should be cos(2π·120·t).
- **Unfinished:** a FIXME asks for a center-tap transformer diagram.

## Index entries added
direct current, RMS voltage, power line losses, phase, three-phase power, center-tap transformer, transformer. (Existing: 4 entries kept.)

## Editor to-do
- Recompute the transmission example (100 A, 200 kW) and the 120 kV current.
- Fix the power-wave argument.
