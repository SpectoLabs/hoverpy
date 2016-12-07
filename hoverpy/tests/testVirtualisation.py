from . import basetestcase
import requests
import unittest
from hoverpy import HoverPy
import logging


class TestVirt(unittest.TestCase):

    def testCapture(self):
        with HoverPy(capture=True):
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

    def testPlayback(self):
        with HoverPy(capture=True) as hoverpy:
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

            hoverpy.simulate()

            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

    def testdbpath(self):
        import tempfile
        import os
        tmp = tempfile.mkdtemp()
        requestsFile = os.path.join(tmp, "requests.db")
        with HoverPy(capture=True, dbpath=requestsFile) as hoverpy:
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

            hoverpy.simulate()

            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

        self.assertTrue(os.path.isfile(requestsFile))


if __name__ == '__main__':
    unittest.main()
