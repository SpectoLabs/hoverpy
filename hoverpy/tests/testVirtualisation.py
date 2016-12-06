from . import basetestcase
import requests
import unittest
from hoverpy import HoverPy
import logging


class TestVirt(basetestcase.BaseTestCase):

    def testCapture(self):
        logging.debug("test_capture")
        with HoverPy(capture=True):
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

    def testPlayback(self):
        logging.debug("test_playback")
        with HoverPy(capture=True) as hoverpy:
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

            hoverpy.simulate()

            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

if __name__ == '__main__':
    unittest.main()
