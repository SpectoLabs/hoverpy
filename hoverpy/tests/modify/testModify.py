import unittest
from hoverpy import HoverPy
import requests
import logging
from .. import basetestcase


class TestModify(basetestcase.BaseTestCase):

    def testModify(self):
        logging.debug("testModify")
        with HoverPy(
                modify=True,
                middleware="python tests/modify/modify.py"):
            r = requests.get("http://example.com")

            self.assertIn("Hoverfly", r.text)

if __name__ == '__main__':
    unittest.main()
