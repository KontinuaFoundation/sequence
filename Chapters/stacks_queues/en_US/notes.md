# Stacks and Queues — Notes

## Summary
Covers stacks (LIFO) with an array-based and a linked-list implementation, then queues (FIFO) with a circular array and a linked list. Ends with a comparison of array and linked versions.

## Changes in this pass
- Finished the queue section, which was unfinished. It had a TODO, a placeholder, an empty linked-list subsection, and an array queue that used undefined names (Queue, MAX, isFull).
- The enqueue operation now adds at the back. The old text said "front."
- Rewrote the array queue with front and count, with % for wrap-around, and added isEmpty and isFull.
- Added the linked-list queue with front and back pointers, and explained why the back pointer makes enqueue constant time.
- Added an unworked exercise that traces a circular queue (CAPACITY 4). The answer is front = 2, count = 3, and the queue holds 3, 4, 5.
- Removed a stray asterisk in the array-versus-linked advice.

## Strengths
- The stack code is correct: push, pop, and the linked-stack version all handle full and empty cases.
- The stack-of-books picture and the call-stack connection to the C chapter are clear.

## Open items
- The stack section says "In this version, we added memory address output." The code shown does not print addresses. Either show the change or drop the sentence.
- The text says both stack operations take constant time "(we will cover this in a future chapter)." Consider explaining O(1) briefly.
