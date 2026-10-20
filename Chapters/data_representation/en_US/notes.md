# Data Representation — Notes

## Summary
Covers text (newlines, ASCII, UTF-8, alphabets and accents), natural numbers in decimal, binary, hexadecimal, and octal (with hex colors), floating-point arithmetic (overflow and underflow, the (β, p, m, M) system, IEEE 754, and machine epsilon), and data compression with entropy.

## Changes in this pass
- Fixed the addition table row for 9 (it had 10 cells, not 11).
- Added the missing row for 8 to the multiplication table.
- Corrected the overflow exercise. 3.00 × 10⁸ is above 10⁸, so it overflows (the old answer said "neither").
- Corrected the parameters exercise: the smallest representable positive number is 10⁻⁴, not 10⁻³.
- Corrected the machine epsilon note: Python's sys.float_info.epsilon (2⁻⁵²) is twice the u defined in the text (½β^(1−p)). Removed a visible "[correct punctuation]" note.
- Removed the claim that IEEE 754 defines integer types. Integer types are a separate idea.
- Fixed the French accent example (é and è mark different vowel sounds). Replaced the broken `('e)` markup.
- Replaced the claim that memory is "4-bit sequences" with "a long list of bytes."
- Corrected the origin of "hexadecimal" (Greek hexa and Latin decem).
- Fixed the hex-binary sentence, the octal sentence, and removed a duplicated bit sentence.
- Removed a duplicate subsection heading under data compression.

## Strengths
- The binary, hex, octal, and bit-size exercises are correct (4 MB = 3.2 × 10⁷ bits; −85 = 1010 1011 in two's complement; 110101₂ = 65₈).
- The (β, p, m, M) parameter exercise has correct overflow and underflow answers.
- The entropy formula and its role in compression are stated correctly.

## Open items
- The chapter does not show how floating-point values are converted between decimal and binary. A worked conversion (for example, 0.1) would help.
