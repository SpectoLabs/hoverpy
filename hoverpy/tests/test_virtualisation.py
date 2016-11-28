import unittest
import requests
import re
from hoverpy import HoverPy

class TestVirt(unittest.TestCase):
  
  def test_capture(self):
    hoverpy = HoverPy(capture=True)
    r = requests.get("http://ip.jsontest.com/")
    j = r.json()
    self.assertIn('ip', j)

  def test_playback(self):
    hoverpy = HoverPy(capture=True)
    r = requests.get("http://ip.jsontest.com/foobar")
    j = r.json()
    self.assertIn('ip', j)

    hoverpy.simulate()
    r = requests.get("http://ip.jsontest.com/foobar")
    j = r.json()
    self.assertIn('ip', j)
