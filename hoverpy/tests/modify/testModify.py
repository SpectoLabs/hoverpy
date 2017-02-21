import unittest
from hoverpy import HoverPy
import requests
import logging


class TestModify(unittest.TestCase):

    def testModify(self):
        logging.debug("testModify")
        with HoverPy(
                modify=True,
                middleware="python hoverpy/tests/modify/modify.py"):
            r = requests.get("http://localhost:8888")

            self.assertIn("modified!", r.text)

if __name__ == '__main__':
    unittest.main()
