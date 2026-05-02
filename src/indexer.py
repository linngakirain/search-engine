import json
import re
from collections import defaultdict


def tokenize(text):
    return re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())


def build_index(docs):
    index = defaultdict(list)  # word -> [(doc_id, [positions])]
    for doc_id, url, text in docs:
        words = tokenize(text)
        by_word = defaultdict(list)
        for i, w in enumerate(words):
            by_word[w].append(i)
        for w, positions in by_word.items():
            index[w].append((doc_id, positions))
    return dict(index)


def save_index(index, filename):
    with open(filename, "w") as f:
        json.dump(index, f)


def load_index(filename):
    with open(filename) as f:
        return json.load(f)
