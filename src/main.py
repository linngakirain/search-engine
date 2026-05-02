import json
import os

from src.crawler import crawl
from src.indexer import build_index, save_index, load_index
from src.search import display_find_results, find_phrase, print_word

INDEX_PATH = "data/index.json"
DOCS_PATH = "data/docs.json"


def save_docs(docs):
    with open(DOCS_PATH, "w") as f:
        json.dump(docs, f)


def load_docs():
    with open(DOCS_PATH) as f:
        return json.load(f)


def main():
    index = None
    docs = None

    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            print()
            break

        if not line:
            continue

        parts = line.split(maxsplit=1)
        cmd = parts[0].lower()
        rest = parts[1].strip() if len(parts) > 1 else ""

        if cmd == "build":
            docs = crawl()
            index = build_index(docs)
            os.makedirs("data", exist_ok=True)
            save_index(index, INDEX_PATH)
            save_docs(docs)
            print("Saved.")

        elif cmd == "load":
            try:
                index = load_index(INDEX_PATH)
                docs = load_docs()
                print("Loaded.")
            except FileNotFoundError:
                print("No saved index yet, run build first.")

        elif cmd == "print":
            if rest:
                print_word(rest.lower(), index, docs)

        elif cmd == "find":
            if rest:
                q = rest.lower()
                hits = find_phrase(q, index)
                display_find_results(q, hits, docs)

        elif cmd in ("exit", "quit"):
            break

        else:
            print("Commands: build, load, print <word>, find <phrase>, exit")


if __name__ == "__main__":
    main()
