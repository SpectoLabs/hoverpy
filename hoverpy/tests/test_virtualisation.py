import unittest
import requests
from hoverpy import HoverPy


class TestVirt(unittest.TestCase):

    def test_capture(self):
        hoverpy = HoverPy(capture=True, inMemory=True)
        r = requests.get("http://localhost:8888/api/v2/hoverfly")
        self.assertIn('destination', r.json())

    def test_playback(self):
        hoverpy = HoverPy(capture=True, inMemory=True)
        r = requests.get("http://localhost:8888/api/v2/hoverfly")
        self.assertIn('destination', r.json())

        hoverpy.simulate()

        r = requests.get("http://localhost:8888/api/v2/hoverfly")
        self.assertIn('destination', r.json())

if __name__ == '__main__':
    unittest.main()
