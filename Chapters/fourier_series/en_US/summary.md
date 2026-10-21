# Fourier Series and Signals: Summary

## What the chapter covers
Shows that repeating signals are sums of sines and cosines:
- builds a square wave from odd harmonics;
- proves orthogonality with the product-to-sum identity and derives the Fourier coefficient formulas;
- works the square wave (with a bonus derivation of π/4 = 1 − 1/3 + 1/5 − …) and the Gibbs overshoot;
- connects harmonics and timbre to the Sound chapter, and gives the complex form using Euler's formula;
- introduces sampled signals, the FFT, spectra, and the Nyquist frequency;
- covers filters and speaker crossovers (capacitor to the tweeter, inductor to the woofer, f_c = 1/(2πRC) = R/(2πL)).

## Key ideas
- f(x) = a₀/2 + Σ(aₙ cos nx + bₙ sin nx), with aₙ = (1/π)∫ f cos nx dx and bₙ = (1/π)∫ f sin nx dx.
- Sines and cosines of different frequencies are orthogonal on [−π, π].
- Square wave: (4/π)Σ sin(nx)/n over odd n; the Gibbs overshoot stays near 9% of the jump.
- Harmonics are whole-number multiples of the fundamental; timbre is the pattern of coefficients.
- Sampling at rate r captures frequencies below r/2 (the Nyquist frequency).
- First-order crossover: woofer gets 1/√(1 + (f/f_c)²), tweeter gets (f/f_c)/√(1 + (f/f_c)²); their squares sum to 1.

## Changes in this pass
- New chapter, placed in volume 34 right after euler_formula, which supplies the complex form. It builds on the Sound chapter's overtones, the trig integrals and sum formulas, and the reactances X_C and X_L from Pendulums and Alternating Current.
- As requested, it says nothing about Fourier analysis of images, and it includes a full section on speaker crossovers with a worked 8 Ω, 2500 Hz design (8 μF, 0.51 mH).
- Includes three Python listings (square_wave.py, spectrum.py, crossover.py) with real output, their three generated figures, and 9 exercises with answers.
- All values verified with SciPy and NumPy: the coefficients by numerical integration, the Gibbs peak 1.179, the three-term sum 1.1035, the filter fractions 0.92/0.60/0.41/0.31, and the crossover parts 13.3 μF and 0.212 mH.
