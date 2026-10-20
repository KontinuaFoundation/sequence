# Introduction to C — Notes

## Summary
Introduces C for Python programmers: compile-then-run with gcc, hello world, static types, printf, conditionals and loops, functions and forward declarations, the stack and frames, pointers, pass-by-reference (modf and meters-to-feet), structs, heap allocation with malloc/free, and how Python objects are built, ending with exercises.

## Strengths
- Strong Python-to-C bridge with a clear stack "blackboard" metaphor and stack diagrams.
- Memory concepts build in order: stack, pointers, pass-by-reference, heap.
- Worked examples are correct: cookingMinutes(9) = 150, BMI values, and the modf output.
- Exercises build up and include a memory-leak hunt.

## Weaknesses
- **Duplicate type entry:** the boolean item is labeled \texttt{int}; it should be a separate bool entry or describe the convention.
- **Redundant text:** the -o flag is explained twice in consecutive paragraphs.
- **Epoch wording:** time(NULL) is seconds since the Unix epoch (midnight UTC, Jan 1 1970), not "since midnight."
- **Portability:** localtime_r and the exercise's long vs. time_t mismatch are POSIX-only and may warn on Windows.
- **Cross-reference:** the closing says the next chapter introduces C++ classes; check it matches the next chapter (linked_list_c).
- **Python simplification:** the object model description (pointer to a method table in a struct) is a simplified picture of CPython and should be labeled as such.

## Index entries added
hello world program, gcc, variable!declaration in C, printf, forward declaration, Python!objects under the hood. The chapter already had about 20 entries (compiler, stack, pointer, heap, malloc, free, etc.).

## Editor to-do
- Fix the boolean type entry and the epoch wording.
- Check the C++ cross-reference and the POSIX-only exercise.
