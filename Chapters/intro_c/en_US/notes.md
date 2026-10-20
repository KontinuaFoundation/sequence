# Introduction to C — Notes

## Summary
Introduces C for Python programmers: compile-then-run with gcc, hello world, static types, printf, conditionals and loops, functions and forward declarations, the stack and frames, pointers, pass-by-reference (modf and meters-to-feet), structs, heap allocation with malloc/free, and how Python objects are built, ending with exercises.

## Changes in this pass
- Removed the repeated sentence about the -o flag.
- Fixed the epoch wording: time(NULL) counts seconds since the Unix epoch (midnight UTC, January 1, 1970).
- Relabeled the boolean item as "Boolean" (it was labeled int).

## Strengths
- Strong Python-to-C bridge with a clear stack "blackboard" metaphor and stack diagrams.
- Memory concepts build in order: stack, pointers, pass-by-reference, heap.
- Worked examples are correct: cookingMinutes(9) = 150, BMI values, and the modf output.
- Exercises build up and include a memory-leak hunt.

## Open items
- The exercise on struct tm uses localtime_r and time_t, which are POSIX functions and may not work on Windows. Say so, or give a portable variant.
- The Python object model description (a pointer to a method table inside a struct) is simplified. Label it as a simplified picture of CPython.
