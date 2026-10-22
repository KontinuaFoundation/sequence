# Fluids in Motion: Bernoulli's Principle: Summary

## What the chapter covers
Moves from still fluids to moving ones:
- continuity (A₁v₁ = A₂v₂; a thumb over a hose);
- Bernoulli's equation derived from the work-energy idea, showing that buoyancy's ρgh and sailing's ½ρv² are terms of one law, with a TikZ Venturi tube figure;
- a pipe pressure-drop example (Venturi meters, sprayers);
- Torricelli's law and a Python simulation of a draining tank;
- explanations of the shower curtain, passing ships, and hurricane roofs;
- an honest account of lift that debunks 'equal transit time' and shows Bernoulli and Newton describe the same flow.

## Key ideas
- Continuity: A₁v₁ = A₂v₂ for an incompressible fluid.
- Bernoulli: P + ½ρv² + ρgh is constant along the flow; faster flow at the same height means lower pressure.
- Torricelli: water leaves a tank at v = √(2gh).
- Lift: the wing turns air downward; Bernoulli and Newton's third law are two descriptions of the same flow.

## Changes in this pass
- New chapter, placed in volume 8 between boats_sailing and flight. It unifies buoyancy's hydrostatic pressure (volume 2), sailing's wind pressure ½ρv², and the work-energy idea (volume 2), and sets up flight's lift equation. Added a pointer in flight back to this chapter.
- Switches density notation from d (used by buoyancy and boats_sailing) to ρ, the notation flight uses, and says so.
- Includes a TikZ Venturi figure, a Python draining-tank simulation (draining_tank.py; 25.2 minutes vs. the exact 25.3) with its figure, and 5 exercises with answers (river gorge, water tower, Venturi meter, blowing between sheets of paper, the open-window myth).
- All values verified in Python (hose 9.4 m/s, Venturi 30,000 Pa, hurricane roof 225,000 N, a wing pressure difference of 610 Pa, about 0.6% of atmospheric).
