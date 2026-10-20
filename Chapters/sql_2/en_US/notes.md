# Relational Databases and Normalization — Notes

## Summary
Covers keys, normalization (1NF, 2NF, 3NF, with functional dependencies), entity-relationship diagrams (drawn with mermaid), relational algebra basics, relating two tables with foreign keys, and advanced queries (translating a question into relational algebra and then into SQL). It has exercises with answers.

## Changes in this pass
- Defined relational algebra before it is used (the symbols pi and subset), and removed the FIXME.
- Replaced the placeholder 3NF exercise with a real exercise and answer (split Orders into Orders and Customers).
- Replaced the "fill in the blanks" placeholder with an exercise (equipment in Lab A, answer: Oscilloscope).

## Not compiled
- This chapter uses mermaid diagrams, which do not compile in the current toolchain. Compile checks were skipped by request.

## Open items
- Check the mermaid diagram syntax when the toolchain is fixed.
- The advanced-queries section has one translation example. Add one more, for a join.
