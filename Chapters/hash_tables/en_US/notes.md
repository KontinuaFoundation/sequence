# Hash Tables — Notes

## Summary
Defines a hash table as an associative array built on a hash function and an array of buckets. Covers structure, insert and retrieve, two collision strategies (chaining and open addressing), and time complexity: O(1) average, O(n) worst case.

## Strengths
- Clear, short definitions of each part (table, bucket, hash function).
- Both collision methods are described with their lookup steps.
- The O(1) versus O(n) distinction is stated correctly.

## Weaknesses
- **Conflated terms:** "Open Addressing (or Linear Probing)" treats linear probing as a synonym. Linear probing is one probing scheme within open addressing.
- **No example:** there is no worked insert, lookup, or collision example with numbers.
- **Missing topics:** load factor and resizing are not mentioned, and resizing is what keeps the average case O(1).
- **Vague wording:** "several items if collisions occur, as will be discussed later" points forward without a reference.

## Index entries added
hash map, associative array, chaining, open addressing, linear probing, hash tables!time complexity, key-value pair. The chapter already had hash table, hash function, and collisions in hash tables.

## Editor to-do
- Separate linear probing from open addressing and add a numeric example.
- Add load factor and resizing.
