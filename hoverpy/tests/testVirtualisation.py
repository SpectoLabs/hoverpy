import requests
import unittest
from hoverpy import HoverPy
import hoverpy
import logging


class TestVirt(unittest.TestCase):

    def testCapture(self):
        with HoverPy(capture=True):
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

    def testPlayback(self):
        with HoverPy(capture=True) as hp:
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

            hp.simulate()

            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

    def testSimulation(self):
        hoverpy.wipe()
        simulation = None
        with HoverPy(capture=True) as hp:
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())
            import json
            simulation = json.dumps(hp.simulation())
        hoverpy.wipe()
        with HoverPy() as hp:
            hp.simulation(simulation)
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())
        hoverpy.wipe()

    def testdbpath(self):
        import tempfile
        import os
        tmp = tempfile.mkdtemp()
        requestsFile = os.path.join(tmp, "requests.db")
        with HoverPy(capture=True, dbpath=requestsFile) as hp:
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

            hp.simulate()

            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())

        self.assertTrue(os.path.isfile(requestsFile))


if __name__ == '__main__':
    unittest.main()
