# Interference, Diffraction, and the Doppler Effect: Summary

## What the chapter covers
Covers what happens when waves meet each other, meet obstacles, or come from moving sources:
- superposition, constructive and destructive interference, noise-cancelling headphones, and beats (derived with the sum formulas; f_beat = |f₁ − f₂|);
- two-source interference and Young's double slit (a TikZ geometry figure, d sin θ = mλ, Δy = λL/d, and a Python intensity pattern with its single-slit envelope), plus the photon-at-a-time puzzle;
- diffraction (hearing around corners, single slits, resolution limits, Blu-ray, gratings, CDs);
- the Doppler effect (a TikZ wavefront figure, f·v/(v ∓ v_s), sirens, radar, ultrasound, sonic booms, redshift, and Hubble's expanding universe).

## Key ideas
- Superposition: overlapping waves add; in step they reinforce, out of step they cancel.
- Beats: f_beat = |f₁ − f₂|.
- Double slit: bright fringes at d sin θ = mλ; spacing Δy = λL/d.
- Diffraction is strong when the opening is about the size of the wavelength.
- Doppler: f_heard = f·v/(v − v_s) approaching and f·v/(v + v_s) receding; for light, Δλ/λ ≈ v/c.

## Changes in this pass
- New chapter, placed in volume 13 right after emwaves and before optics and photons, so the double slit shows light is a wave just before the Photons chapter shows it is also a particle. It builds on intro_waves and sound (volume 11) and the sum formulas from trig_identities; the paradoxes chapter's double-slit teaser now has a full treatment.
- Titled 'Interference, Diffraction, and the Doppler Effect' (not 'Waves, Part Two'), because the longer title overflowed the page header.
- Includes two TikZ figures (double-slit geometry with the path difference d sin θ highlighted, and Doppler wavefronts), three matplotlib figures (superposition, beats, the double-slit pattern), a Python listing (double_slit.py) with real output, and 8 exercises with answers.
- All values verified in Python (ambulance 767/644 Hz, a drop of about 3 half steps; fringe spacing 5.2 mm; grating 23°, highest order 2; galaxy recession speeds 3,000 and 6,000 km/s).
