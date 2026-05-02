import unittest
from src.search import find_phrase, display_find_results
from src.indexer import build_index

class TestSearch(unittest.TestCase):
    def setUp(self):
        docs = [
            [0, "url0", "good friends are good"],
            [1, "url1", "good morning friends"],
            [2, "url2", "friends are good"]
        ]
        self.index = build_index(docs)
        self.docs = docs

    def test_find_single_word(self):
        results = find_phrase("good", self.index)
        self.assertEqual(len(results), 3)   # all three contain 'good'

    def test_find_phrase_consecutive(self):
        results = find_phrase("good friends", self.index)
        self.assertEqual(results, [0])   # only doc0 has consecutive "good friends"

    def test_find_nonexistent(self):
        results = find_phrase("xyz abc", self.index)
        self.assertEqual(results, [])

if __name__ == '__main__':
    unittest.main()