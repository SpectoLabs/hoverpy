import requests
import unittest
from hoverpy import HoverPy
import hoverpy
import logging
from pipetestserver import ThreadedServerControl
from pipetestserver import application
from pipetestserver import proxiedClient
import time
import json
import os
import tempfile


class TestVirt(unittest.TestCase):
    endpoint = 'http://localhost:8000/'

    def testCapture(self):
        server = ThreadedServerControl(application)
        server.start()

        with HoverPy(capture=True):
            result = proxiedClient(2, endpoint=self.endpoint)
            self.assertEqual(result, 4)

        server.stop()

    def testPlayback(self):
        server = ThreadedServerControl(application)
        server.start()

        with HoverPy(capture=True) as hp:
            result = proxiedClient(2, endpoint=self.endpoint)
            self.assertEqual(result, 4)
            server.stop()
            hp.simulate()
            result = proxiedClient(2, endpoint=self.endpoint)
            self.assertEqual(result, 4)

    def testStressTest(self):
        server = ThreadedServerControl(application)
        server.start()

        n = 10

        def runChecks():
            for i in range(n):
                st = str(i)*2**20
                result = proxiedClient(st, endpoint=self.endpoint)
                self.assertEqual(result, st*2)

        hoverpy.wipe()
        start = time.time()
        with HoverPy(capture=True):
            runChecks()
            print("generating data took %f" % (time.time() - start))

        server.stop()
        simulation = None
        start = time.time()

        with HoverPy() as hp:
            open("simulation.json", "wa").write(json.dumps(hp.simulation()))

        print(
            "re-reading data, getting simulation, and writing it to disk took %f" %
            (time.time() - start))

        # for some reason, hoverfly falls over when trying to re-read the json
        # data from disk
        # start = time.time()
        # with HoverPy(simulation="./simulation.json") as hp:
        #     simulation = hp.simulation()
        #     print(
        #         "re-loading hoverfly, with json file, and reading it again took %f" %
        #         (time.time() - start))

        hoverpy.wipe()
        os.unlink("simulation.json")

    def testSimulation(self):
        hoverpy.wipe()
        simulation = None
        with HoverPy(capture=True) as hp:
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())
            simulation = json.dumps(hp.simulation())
        hoverpy.wipe()
        with HoverPy() as hp:
            hp.simulation(simulation)
            r = requests.get("http://localhost:8888/api/v2/hoverfly")
            self.assertIn('destination', r.json())
        hoverpy.wipe()

    def testdbpath(self):
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
