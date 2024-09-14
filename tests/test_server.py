# tests/test_server.py
import unittest
from app.main import app

class TestServer(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_dns_query(self):
        response = self.client.get('/dns-query', query_string={'query': 'example.com'})
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = self.client.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn('cache_size', response.json)

if __name__ == '__main__':
    unittest.main()
