import csv
import numpy as np
from collections import Counter
from text import prepare

with open("messages.csv", newline="") as f:
    rows = list(csv.DictReader(f))
texts = [row["text"] for row in rows]
labels = [row["label"] for row in rows]

def train(texts, labels):
    counts = {"spam": Counter(), "ham": Counter()}
    for text, label in zip(texts, labels):
        counts[label].update(prepare(text))
    vocab = set(counts["spam"]) | set(counts["ham"])
    model = {}
    for label in ("spam", "ham"):
        total = sum(counts[label].values())
        log_prior = np.log(labels.count(label) / len(labels))
        # Laplace smoothing: add 1 to every count
        log_like = {w: np.log((counts[label][w] + 1) / (total + len(vocab)))
                    for w in vocab}
        model[label] = (log_prior, log_like)
    return model

def spam_probability(model, text):
    scores = {}
    for label, (log_prior, log_like) in model.items():
        # Words the model has never seen are skipped
        words = [w for w in prepare(text) if w in log_like]
        scores[label] = log_prior + sum(log_like[w] for w in words)
    # Turn the two log scores back into probabilities that add to 1
    biggest = max(scores.values())
    spam = np.exp(scores["spam"] - biggest)
    ham = np.exp(scores["ham"] - biggest)
    return spam / (spam + ham)

# Leave-one-out: train on 59 messages, test on the one left out, 60 times
correct = 0
for i in range(len(texts)):
    model = train(texts[:i] + texts[i + 1:], labels[:i] + labels[i + 1:])
    guess = "spam" if spam_probability(model, texts[i]) >= 0.5 else "ham"
    correct += guess == labels[i]
    if guess != labels[i]:
        print("Missed:", labels[i], "|", texts[i])
print(f"Leave-one-out accuracy: {correct}/{len(texts)}")

model = train(texts, labels)
for text in ["Free pizza at the game tonight",
             "Click here to claim your prize",
             "Can you send me the notes from history class?"]:
    print(f"{spam_probability(model, text):.3f}  {text}")
