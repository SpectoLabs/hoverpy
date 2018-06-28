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
            r = requests.get("http://jsonplaceholder.typicode.com/posts/1")
            j = r.json()
            self.assertIn("body", j)
            sim = hp.simulation()
            self.assertEqual("jsonplaceholder.typicode.com", sim["data"]["pairs"][0]["request"]["destination"])

    def testPlayback(self):
        with HoverPy(capture=True) as hp:
            r1 = requests.get("http://jsonplaceholder.typicode.com/posts/1")
            hp.simulate()
            time.sleep(0.01)
            r2 = requests.get("http://jsonplaceholder.typicode.com/posts/1")
            self.assertEqual(r1.json(), r2.json())

    # in memory doesn't seem to be working
    # def testInMemory(self):
    #     with HoverPy(showCmd=True, db="memory") as hp:
    #         r1 = requests.get("http://jsonplaceholder.typicode.com/posts/1")
    #         hp.simulate()
    #         time.sleep(0.01)
    #         r2 = requests.get("http://jsonplaceholder.typicode.com/posts/1")
    #         self.assertEqual(r1.json()["epoch"], r2.json()["epoch"])

    def testDecorators(self):
        @capture(dbpath="decorators.db")
        def testCapture():
            logging.debug("test_capture")
            r = requests.get("http://jsonplaceholder.typicode.com/posts/1")
            j = r.json()
            self.assertIn('body', j)
            time.sleep(0.01)
            return j["body"]

        @simulate(dbpath="decorators.db")
        def testSimulate(body):
            logging.debug("test_simulate")
            r = requests.get("http://jsonplaceholder.typicode.com/posts/1")
            j = r.json()
            self.assertIn('body', j)
            self.assertEqual(j["body"], body)

        body = testCapture()
        testSimulate(body)
        os.unlink("decorators.db")

if __name__ == '__main__':
    unittest.main()
