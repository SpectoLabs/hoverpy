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
    self.assertTrue(re.match('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', j['ip']))

  def test_playback(self):
    hoverpy = HoverPy(capture=True)
    r = requests.get("http://ip.jsontest.com/asdf")
    j = r.json()
    self.assertIn('ip', j)
    self.assertTrue(re.match('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', j['ip']))

    hoverpy.simulate()
    r = requests.get("http://ip.jsontest.com/asdf")
    j = r.json()
    self.assertIn('ip', j)
    self.assertTrue(re.match('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', j['ip']))