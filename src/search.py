from src.indexer import tokenize


def print_word(word, index, docs):
    word = word.strip().lower()
    if word == "":
        print("Please enter a word.")
        return
    if len(word.split()) != 1:
        print("Please enter one word only.")
        return
    if index is None or docs is None:
        print("Run build or load first.")
        return
    if word not in index:
        print(f"Word '{word}' not found.")
        return
    print(f"Inverted index for '{word}':")
    for doc_id, positions in index[word]:
        url = docs[doc_id][1]
        print(f"  {url} -> positions {positions}")


def find_phrase(phrase, index):
    if index is None:
        return []
    words = tokenize(phrase)
    if not words:
        return []

    first = words[0]
    if first not in index:
        return []

    results = []
    for doc_id, start_positions in index[first]:
        for start in start_positions:
            if phrase_here(doc_id, start, words, index):
                results.append(doc_id)
                break
    return results


def phrase_here(doc_id, pos, words, index):
    p = pos
    for w in words:
        plist = None
        for d, positions in index.get(w, []):
            if d == doc_id:
                plist = positions
                break
        if plist is None or p not in plist:
            return False
        p += 1
    return True


def display_find_results(phrase, doc_ids, docs):
    if docs is None:
        print("Run build or load first.")
        return
    if phrase.strip() == "":
        print("Please enter a phrase.")
        return
    if not doc_ids:
        print(f"No pages contain '{phrase}'.")
        return
    print(f"Pages containing '{phrase}':")
    for doc_id in doc_ids:
        print(f"  {docs[doc_id][1]}")
