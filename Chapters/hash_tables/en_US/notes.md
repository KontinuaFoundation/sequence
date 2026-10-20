# Hash Tables — Notes

## Summary
Introduces hash tables as a way to map keys to values with a hash function, explains buckets, chaining and open addressing with linear probing, and gives the O(1) average and O(n) worst-case time bounds. Uses a school-locker picture and the hash function h(k) = k mod 5.

## Changes in this pass
- Expanded the chapter from a short description to a worked-through topic.
- Added the locker-room picture and noted that Python's dict is a hash table.
- Added three exercises with answers: chaining with keys 12, 7, 17, 3 (bucket 2 holds three keys); linear probing with the same keys (final slots 3, _, 12, 7, 17); and the worst case where every key hashes to bucket 0.
- Corrected the label "Open Addressing (or Linear Probing)". Linear probing is one kind of open addressing.

## Strengths
- The complexity bounds are correct.
- The worked traces match the rules, including wrap-around in linear probing.

## Open items
- The chapter does not include Python code for a hash table. A short example would help, since the rest of the book uses Python.
