import unittest
import json
from hoverpy import HoverPy
import os
import time
import requests

class TestModify(unittest.TestCase):

  def testModify(self):
    hoverpy = HoverPy(flags=["-modify", "-middleware", "python tests/modify/modify.py"])
    r = requests.get("http://example.com")
    self.assertIn("Hoverfly", r.text)
