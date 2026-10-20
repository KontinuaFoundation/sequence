# Stemming and Lemmatization — Notes

## Summary
Defines stemming (crude reduction to a stem, which may not be a real word) and lemmatization (reduction to a dictionary base form using morphological analysis). Compares speed and accuracy and lists uses in search and NLP.

## Strengths
- The jumping/jumped/jumps example is good for showing stemming.
- The running and runs examples show the difference between the two methods.
- Speed versus precision is a useful way to pick between them.

## Weaknesses
- **No code:** there is no example using a library such as NLTK or spaCy.
- **No exercise:** nothing for students to try.
- **Unclear wording:** "the stem of the word 'running' could be 'run' depending on the algorithm" is hard to follow, since "run" is also the lemma.
- **Vague applications:** "algorithmic searches" and "baseline programs for autofill" are unclear.
- **Internal note in source:** line 2 is a LaTeX comment about moving the chapter to book 29 and should be removed or moved to the book file.

## Index entries added
stem, inflectional forms, morphological analysis, natural language processing, text normalization.

## Editor to-do
- Add a short code example and an exercise.
- Clarify the "running" stem example and the applications sentence.
