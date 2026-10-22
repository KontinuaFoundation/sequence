# Nuclear Physics and Radioactivity: Summary

## What the chapter covers
Covers the nucleus and nuclear energy:
- nucleus notation, and why the strong force must beat a 230 N proton–proton repulsion;
- alpha, beta, and gamma decay, with nuclear equations balanced by A and Z, and how smoke detectors work;
- half-life and N = N₀(1/2)^{t/T} (linked to exponentials and logs), with a seeded simulation of 1,000 atoms, a table of half-lives, and carbon dating Ötzi;
- mass defect and binding energy (u, MeV, 931.5 MeV/u), with a binding-energy-per-nucleon figure;
- fission (173 MeV, chain reactions, control rods, waste) and D–T fusion (17.6 MeV, why it is hard, the 2022 ignition result);
- background radiation and doses.

## Key ideas
- ^A_Z X: Z protons, A − Z neutrons; nuclear reactions conserve A and Z.
- Alpha: A − 4, Z − 2; beta: Z + 1; gamma: a photon, no change in A or Z.
- N(t) = N₀(1/2)^{t/T}; solve for t with logarithms (dating).
- Mass defect × 931.5 MeV/u = binding energy; the curve peaks near iron.
- Fission of heavy nuclei and fusion of light nuclei both move toward iron and release energy.

## Changes in this pass
- New chapter, placed at the end of volume 13 after special_relativity, completing photons → relativity → the nucleus. It builds on isotopes and half-life (atomic_mass_reactions), E = mc² and the H→He example (matter_energy), Coulomb's law (charge), exponentials and logs (volume 10), and the randomness ideas from monte_carlo.
- Added a pointer from atomic_mass_reactions' half-life definition to this chapter.
- Includes a seeded decay simulation (decay_simulation.py) with real output, two figures (decay.png and binding_energy.png, the latter with arrows showing that fission and fusion both move toward iron), and 6 exercises with answers.
- Every energy was computed from standard atomic masses (He-4 7.07 MeV/nucleon, D 2.22 MeV, fission 173 MeV, D–T 17.6 MeV, about 3 million times coal per kg).
- The E = mc² back-reference now names the Work and Energy chapter, where that section moved.
