# Linked Lists and C++ Transition — Notes

## Summary
Moves from C to C++ (new replaces malloc plus sizeof; classes), defines linked lists with head, tail, and successor nodes, walks through building a three-node list, introduces doubly linked lists, and runs a four-node program that prints addresses and sizes. Closes by contrasting linked lists with Python lists.

## Strengths
- Diagrams show each step of building and linking the list.
- The address-difference arithmetic (0x20 = 32 bytes) is correct.
- The DoublyNode program is complete and clearly commented.

## Weaknesses
- **Language claims:** "a more modern version of C++" should read "of C". "In C++, classes are defined using the struct keyword" is imprecise, since struct and class both define classes.
- **Overhead:** linked-list overhead is the extra pointers, not "temporary variables."
- **Cross-reference:** "Advanced Python chapter" is not checked against the book list.
- **Missing include:** the DoublyNode program uses std::cout without showing `#include <iostream>`.
- **Typos:** "stand C" and "strong."

## Index entries added
classes!C++, new operator, linked list, node, successor node, head node, tail node, doubly linked list, predecessor node, memory!padding.

## Editor to-do
- Add the iostream include and fix the typos.
