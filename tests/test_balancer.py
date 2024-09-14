# tests/test_balancer.py
import unittest
from app.balancer import get_dns_server, handle_query

class TestBalancer(unittest.TestCase):
    
    def test_get_dns_server(self):
        servers = ['8.8.8.8', '8.8.4.4', '1.1.1.1']
        self.assertIn(get_dns_server(), servers)

    def test_handle_query(self):
        query = "example.com"
        response = handle_query(query)
        self.assertIn("A", response)  # Assuming the response contains an "A" record

if __name__ == '__main__':
    unittest.main()
