import unittest
import json
from hoverpy import HoverPy
import os
import time


class TestTemplates(unittest.TestCase):

    def testTemplate(self):
        hoverpy = HoverPy()
        data = open("hoverpy/tests/templates/template.json", "r").read()
        hoverpy.records(data=data)
        records = hoverpy.records()
        self.assertTrue("data" in records)
        self.assertTrue(isinstance(records["data"], list))

if __name__ == '__main__':
    unittest.main()
