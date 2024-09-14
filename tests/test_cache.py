# tests/test_cache.py
import unittest
from app.cache import cache_response, get_cached_response

class TestCache(unittest.TestCase):
    
    def test_cache_response(self):
        query = "example.com"
        response = "response_data"
        cache_response(query, response, ttl=300)
        self.assertEqual(get_cached_response(query), response)

    def test_cache_expiration(self):
        query = "example.com"
        response = "response_data"
        cache_response(query, response, ttl=1)  # TTL of 1 second
        time.sleep(2)
        self.assertIsNone(get_cached_response(query))

if __name__ == '__main__':
    unittest.main()
