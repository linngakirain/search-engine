import unittest
import tempfile
import os
from src.indexer import tokenize, build_index, save_index, load_index

class TestIndexer(unittest.TestCase):
    def test_tokenize(self):
        text = "Don't stop believing!"
        tokens = tokenize(text)
        self.assertEqual(tokens, ["don't", "stop", "believing"])

    def test_build_index(self):
        docs = [[0, "url1", "hello world"], [1, "url2", "hello again"]]
        idx = build_index(docs)
        self.assertIn("hello", idx)
        self.assertEqual(len(idx["hello"]), 2)
        self.assertIn("world", idx)
        self.assertEqual(idx["world"][0][1], [1])

    def test_save_load(self):
        docs = [[0, "url", "test word"]]
        idx = build_index(docs)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "idx.json")
            save_index(idx, path)
            loaded = load_index(path)
            self.assertEqual(loaded["test"][0][0], 0)

if __name__ == '__main__':
    unittest.main()