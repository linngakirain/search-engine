import json
import os

from src.crawler import crawl
from src.indexer import build_index
from src.search import display_find_results, find_phrase, print_word

INDEX_PATH = "data/index.json"


def save_data(index, docs):
    with open(INDEX_PATH, "w") as f:
        json.dump({"index": index, "docs": docs}, f)


def load_data():
    with open(INDEX_PATH) as f:
        data = json.load(f)
    return data["index"], data["docs"]


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
            print("Building index... Please wait.")
            docs = crawl()
            index = build_index(docs)
            os.makedirs("data", exist_ok=True)
            save_data(index, docs)
            print("Build complete.")

        elif cmd == "load":
            try:
                index, docs = load_data()
                print("Load complete.")
            except FileNotFoundError:
                print("No index created, run 'build' first.")

        elif cmd == "print":
            if rest:
                print_word(rest.lower(), index, docs)

        elif cmd == "find":
            if rest:
                q = rest.lower()
                hits = find_phrase(q, index)
                display_find_results(q, hits, docs)

        elif cmd == "exit":
            break

        else:
            print("Commands: build, load, print <word>, find <phrase>, exit")


if __name__ == "__main__":
    main()
