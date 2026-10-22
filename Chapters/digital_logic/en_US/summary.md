# Digital Logic: From Transistors to Adders: Summary

## What the chapter covers
Answers 'how does a computer actually compute?' by building an adder from switches:
- bits as voltages and truth tables (1 and 0 instead of T and F);
- MOSFETs as switches (nMOS and pMOS) and a circuitikz CMOS inverter;
- a 4-transistor CMOS NAND gate;
- the gate family with symbols and a combined truth table;
- NAND universality (NOT, AND, OR via De Morgan's law, and XOR from 4 NANDs), with a worked trace;
- binary addition by hand (6 + 7);
- half adder, full adder, and a 4-bit ripple-carry adder, with figures;
- a Python simulation (adder.py) that builds everything from one nand function and tests all 256 4-bit additions;
- subtraction through two's complement;
- a short tour from adders to computers (ALU, memory latch, clock, control).

## Key ideas
- A transistor is a voltage-controlled switch; CMOS pairs pMOS and nMOS so one is always off.
- NAND (4 transistors) is universal: every other gate can be built from it.
- Half adder: sum = A ⊕ B, carry = A and B; a full adder chains two half adders and an OR.
- A ripple-carry adder chains full adders; subtraction is addition of the flipped number plus a carry-in of 1.

## Changes in this pass
- New chapter, placed in volume 26 after data_representation. It uses sets (logic tables, De Morgan exercise; volume 3), diodes (doped silicon; volume 14), and data_representation (binary and two's complement). Added pointers in diodes and sets.
- Includes 6 circuitikz/TikZ figures (inverter, CMOS NAND, gate family, XOR from NANDs, half adder, ripple-carry adder), adder.py, and 8 exercises with answers (NOR table, NOR universality, binary addition, tracing a full adder, transistor count, the 9-NAND full adder in Python, carry delay, and subtraction in Python).
- All outputs were verified by running the code: 0 errors in 256 pairs, 60 NANDs (15 per full adder) and 36 for the 9-NAND version, and 13 − 6 = 7.
