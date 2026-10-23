import csv
import numpy as np
from text import tokenize, stem, prepare, STOP_WORDS

with open("messages.csv", newline="") as f:
    rows = list(csv.DictReader(f))
texts = [row["text"] for row in rows]
print("Messages:", len(texts))

# How big is the vocabulary after each step?
raw = {w for t in texts for w in t.split()}
lower = {w for t in texts for w in tokenize(t)}
no_stop = {w for w in lower if w not in STOP_WORDS}
stems = {stem(w) for w in no_stop}
for name, words in [("split on spaces", raw), ("lowercase, no punctuation", lower),
                    ("without stop words", no_stop), ("stemmed", stems)]:
    print(f"{name:26s} {len(words):4d} distinct words")

# Bag of words: one row per message, one column per stem
vocab = sorted(stems)
column = {word: j for j, word in enumerate(vocab)}
counts = np.zeros((len(texts), len(vocab)), dtype=int)
for i, t in enumerate(texts):
    for word in prepare(t):
        counts[i, column[word]] += 1
print("Count matrix:", counts.shape)

# The first message as counts
print({vocab[j]: int(counts[0, j]) for j in np.nonzero(counts[0])[0]})

# The most common stems overall
totals = counts.sum(axis=0)
top = np.argsort(-totals)[:8]
print("Most common:", [(vocab[j], int(totals[j])) for j in top])
