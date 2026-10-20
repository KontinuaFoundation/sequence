# Python Classes — Notes

## Summary
Motivates classes with repeated dog variables, then defines a Dog class, explains methods, instances, and operators (str's upper and +), shows inheritance with Animal and Dog, and builds a Polynomial class (repr, call, add, mul, sub, derivative) with a test file.

## Strengths
- The Polynomial class outputs are correct: I recomputed the sum, product, scalar product, difference, and derivative (for example, a·b = 4.83x⁵ + 29.25x³ − 4.60x² + 40.50x − 18.00), and the printed lines match.
- The progression from parallel variables to a class is easy to follow.
- The inheritance example uses super().__init__ and overrides speak() clearly.

## Weaknesses
- **Open FIXME:** "integrate this better with polynomials" is at the top of the chapter.
- **Stray text:** a lone "-" line appears before the str.upper() listing.
- **Vague wording:** "Here, we have made a parent class for 'dog' called 'animal'" does not explain the relationship.
- **Rough parent-class example:** the Animal section says "(ie `Animal')", which should be "e.g."

## Index entries added
object-oriented programming, method, operator overloading, type(), inheritance, Polynomial class, magic methods.

## Editor to-do
- Resolve the FIXME and remove the stray "-".
- Fix "ie" and clarify the parent-class sentence.

