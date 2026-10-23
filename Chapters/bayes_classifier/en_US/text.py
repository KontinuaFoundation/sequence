"""Tools for turning text into lists of word stems."""
import re

STOP_WORDS = {"a", "an", "and", "are", "at", "be", "by", "can", "do", "for",
              "from", "have", "i", "in", "is", "it", "me", "my", "of", "on",
              "or", "so", "the", "this", "to", "we", "you", "your"}

SUFFIXES = [("sses", "ss"), ("ies", "i"), ("ing", ""), ("ed", ""),
            ("ly", ""), ("s", "")]

def tokenize(text):
    """Split text into lowercase words, dropping punctuation."""
    return re.findall(r"[a-z0-9$]+", text.lower())

def stem(word):
    """Chop one common suffix off a word, as long as 3 letters remain."""
    for suffix, replacement in SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            word = word[:len(word) - len(suffix)] + replacement
            # running -> runn -> run
            if suffix in ("ing", "ed") and word[-1] == word[-2] and word[-1] not in "lsz":
                word = word[:-1]
            return word
    return word

def prepare(text):
    """Tokenize, drop stop words, and stem."""
    return [stem(w) for w in tokenize(text) if w not in STOP_WORDS]
