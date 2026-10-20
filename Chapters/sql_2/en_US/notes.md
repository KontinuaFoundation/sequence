# Advanced SQL and Database Management — Notes

## Summary
Covers keys (primary, super, candidate, composite, alternate, natural, surrogate), normalization to 1NF, 2NF, and 3NF using a lab-equipment checkout table, then ER diagrams in Mermaid, relational algebra with its SQL equivalents, foreign keys with referential integrity, and an EXCEPT query.

## Strengths
- The 1NF → 2NF → 3NF progression is correct and each step shows the decomposed tables.
- The functional-dependency definitions and the transitive-dependency chain (EquipmentID → EquipmentLocation → LocationManager) are accurate.
- The ER diagram section ties the one-to-one, zero-to-many, and many-to-many cases to the tables.

## Weaknesses
- **Incomplete candidate keys:** Email could also be a candidate key (it is unique in the sample rows), but the text lists only StudentID and SSN.
- **Unsupported claim:** "Hex Codes that do not have the opportunity to change" is not a property of hex codes.
- **Duplicate caption:** the expanded relational-algebra table reuses "Equipment Table [3NF]".
- **Possibly stale FIXME:** "relational algebra not defined before here" — the Relational Algebra Basics section comes earlier, so check whether it is still needed.
- **Placeholder exercises:** "FIXME exercise transform a full table up to 3NF" and "Multiple translation fill in the blanks" are not real exercises.
- **Leftover comments:** "Formally address..." and an outline comment remain in the source.

## Index entries added
primary key, super key, candidate key, surrogate key, normalization, functional dependency, partial dependency, transitive dependency, relational algebra, foreign key, Mermaid.

## Editor to-do
- Add Email as a candidate key and correct the caption.
- Write the two exercises (3NF transformation and SQL/algebra translation).
- Remove the stale FIXME and leftover comments; fix the hex-code claim.
