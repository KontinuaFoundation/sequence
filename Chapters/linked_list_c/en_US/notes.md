# Linked Lists and C++ Transition — Notes

## Summary
Moves from C to C++ (new replaces malloc plus sizeof; classes), defines linked lists with head, tail, and successor nodes, walks through building a three-node list, introduces doubly linked lists, and runs a four-node program that prints addresses and sizes. Closes by contrasting linked lists with Python lists.

## Changes in this pass
- Fixed the language claim: C++ extends C. Fixed "stand C" and "strong" typos.
- Added #include <iostream> to the DoublyNode program.
- Fixed "is the a difference" and the linked-list overhead wording (extra pointers, not temporary variables).

## Strengths
- Diagrams show each step of building and linking the list.
- The address-difference arithmetic (0x20 = 32 bytes) is correct.
- The DoublyNode program is complete and clearly commented.

## Open items
- Reworded the struct keyword sentence in this pass.
- The "Advanced Python chapter" cross-reference has not been checked against the book list.
- Done: the 32-byte allocation is now described as "in this run".
