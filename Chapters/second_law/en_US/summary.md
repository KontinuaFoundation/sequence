# Entropy and the Second Law of Thermodynamics: Summary

## What the chapter covers
Explains why heat flows only from hot to cold and why no engine can be 100% efficient:
- a hook about messy rooms, cooling cocoa, and broken eggs;
- a brief statement of the first law;
- the heat version of the second law;
- microstates and macrostates with coin counting (4 coins in a table, 100 coins);
- a Python simulation of molecules spreading through a box (two_rooms.py) with its plot;
- Boltzmann's S = k ln W and why a logarithm;
- ΔS = Q/T with cocoa and melting-ice examples;
- the Carnot limit derived from entropy bookkeeping, with a TikZ engine and heat pump diagram and a power plant example;
- refrigerators and heat pumps with the COP limit;
- how order arises locally, and the arrow of time.

## Key ideas
- Systems drift toward the macrostates with the most microstates.
- Entropy: S = k ln W; for heat Q added at temperature T, ΔS = Q/T.
- Second law: the total entropy of an isolated system never decreases; heat flows on its own only from hot to cold.
- Carnot limit: e ≤ 1 − T_C/T_H; heat pump COP ≤ T_H/(T_H − T_C), with temperatures in kelvins.

## Changes in this pass
- New chapter, placed in volume 31 after engine. It uses gases_heat (kelvins, latent heat, the air conditioner), counting and binomial coefficients from discrete_probability_counting (volume 28), and natural logarithms. Added a pointer in engine's Compression Ratio section.
- Includes two_rooms.py and its figure, a TikZ engine and heat pump diagram, and 8 exercises with answers (six coins, ice in a drink, an inventor's claim, geothermal power, a cold snap, an open fridge, proving the COP limit, and a 1,000-molecule simulation).
- All values verified in Python (C(100,50) ≈ 1.01×10²⁹; 2⁻¹⁰⁰ ≈ 7.9×10⁻³¹; cocoa +0.48 J/K; ice 12.2 J/K; Carnot 62.5%; COP 14.7 and 9.8; fluctuations of about 5 for 100 molecules and 16 for 1,000).
