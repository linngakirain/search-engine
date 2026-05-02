import unittest
import io
from contextlib import redirect_stdout
from src.search import find_phrase, display_find_results, print_word
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

    def test_find_empty_query(self):
        self.assertEqual(find_phrase("", self.index), [])
        self.assertEqual(find_phrase("   ", self.index), [])

    def test_print_nonexistent_word(self):
        out = io.StringIO()
        with redirect_stdout(out):
            print_word("nonsense", self.index, self.docs)
        self.assertIn("not found", out.getvalue().lower())

    def test_print_multiple_words(self):
        out = io.StringIO()
        with redirect_stdout(out):
            print_word("good friends", self.index, self.docs)
        self.assertIn("please enter one word only", out.getvalue().lower())

    def test_print_empty_word(self):
        out = io.StringIO()
        with redirect_stdout(out):
            print_word("   ", self.index, self.docs)
        self.assertIn("please enter a word", out.getvalue().lower())

    def test_display_find_results_empty(self):
        out = io.StringIO()
        with redirect_stdout(out):
            display_find_results("unknown", [], self.docs)
        self.assertIn("no pages contain", out.getvalue().lower())

    def test_display_find_results_empty_phrase(self):
        out = io.StringIO()
        with redirect_stdout(out):
            display_find_results("   ", [], self.docs)
        self.assertIn("please enter a phrase", out.getvalue().lower())

if __name__ == '__main__':
    unittest.main()