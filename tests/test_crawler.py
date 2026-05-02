import unittest
from unittest.mock import patch, Mock
from src.crawler import crawl, WEBSITE_URL

class TestCrawler(unittest.TestCase):
    @patch('src.crawler.requests.get')
    def test_crawl_one_page(self, mock_get):
        html = '''
        <div class="quote">
            <span class="text">Hello world</span>
            <small class="author">Tester</small>
            <div class="tags"><a class="tag">test</a></div>
        </div>
        '''
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.text = html
        mock_get.return_value = mock_resp

        mock_resp2 = Mock()
        mock_resp2.status_code = 200
        mock_resp2.text = '<html><body></body></html>'
        mock_get.side_effect = [mock_resp, mock_resp2]

        docs = crawl()
        self.assertEqual(len(docs), 1)
        self.assertIn("Hello world", docs[0][2])
        self.assertIn("Tester", docs[0][2])

if __name__ == '__main__':
    unittest.main()