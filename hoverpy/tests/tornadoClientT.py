import unittest
import requests
from hoverpy import HoverPy
import server
import tornado
from tornado.testing import AsyncTestCase
from tornado.httpclient import AsyncHTTPClient


class MyTestCase(AsyncTestCase):

    @tornado.testing.gen_test
    def test_http_fetch(self):
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch("http://www.tornadoweb.org")
        # Test contents of response
        self.assertIn("FriendFeed", response.body)


class TestTornadoClient(unittest.TestCase):

    def testPlayback(self):
        with HoverPy(capture=True) as hoverpy:
            server.start()
            r = requests.get("http://localhost:8000/ip")
            self.assertIn('ip', r.json())
            server.stop()

        with HoverPy(capture=False) as hoverpy:
            r = requests.get("http://localhost:8000/ip")
            self.assertIn('ip', r.json())


if __name__ == '__main__':
    unittest.main()
