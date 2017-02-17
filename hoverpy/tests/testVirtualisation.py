import requests
import unittest
from hoverpy import HoverPy, capture, simulate
import time
import json
import logging
import os

class TestVirt(unittest.TestCase):
    endpoint = 'http://localhost:8000/'

    def testCapture(self):
        with HoverPy(capture=True) as hp:
            r = requests.get("http://time.ioloop.io?format=json")
            j = r.json()
            self.assertIn("time", j)
            sim = hp.simulation()
            self.assertEquals("time.ioloop.io", sim["data"]["pairs"][0]["request"]["destination"])

    def testPlayback(self):
        with HoverPy(capture=True) as hp:
            r1 = requests.get("http://time.ioloop.io?format=json")
            hp.simulate()
            time.sleep(0.01)
            r2 = requests.get("http://time.ioloop.io?format=json")
            self.assertEquals(r1.json()["epoch"], r2.json()["epoch"])

    # in memory doesn't seem to be working
    # def testInMemory(self):
    #     with HoverPy(showCmd=True, db="memory") as hp:
    #         r1 = requests.get("http://time.ioloop.io?format=json")
    #         hp.simulate()
    #         time.sleep(0.01)
    #         r2 = requests.get("http://time.ioloop.io?format=json")
    #         self.assertEquals(r1.json()["epoch"], r2.json()["epoch"])

    def testDecorators(self):
        @capture(dbpath="decorators.db")
        def testCapture():
            logging.debug("test_capture")
            r = requests.get("http://time.ioloop.io?format=json")
            j = r.json()
            self.assertIn('epoch', j)
            time.sleep(0.01)
            return j["epoch"]

        @simulate(dbpath="decorators.db")
        def testSimulate(epoch):
            logging.debug("test_simulate")
            r = requests.get("http://time.ioloop.io?format=json")
            j = r.json()
            self.assertIn('epoch', j)
            self.assertEquals(j["epoch"], epoch)

        epoch = testCapture()
        testSimulate(epoch)
        os.unlink("decorators.db")

if __name__ == '__main__':
    unittest.main()
