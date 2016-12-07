import unittest
import requests
from localTornado import LocalTornado


class TestServer(LocalTornado):

    def testServer(self):
        r = requests.get("http://localhost:8000/ip")
        j = r.json()
        self.assertIn('ip', j)

if __name__ == '__main__':
    unittest.main()
