import unittest
import json
from hoverpy import HoverPy
import os
import time

def wipe():
  try:
      os.remove("./requests.db")
  except OSError:
      pass

class TestTemplates(unittest.TestCase):

  def testTemplate(self):
    wipe()
    hoverpy = HoverPy()
    data = open("hoverpy/tests/templates/template.json", "r").read()
    hoverpy.records(data=data)
    dump = json.dumps(hoverpy.records())
    self.assertEqual(dump, '{"data": [{"request": {"body": null, "requestType": "template", "destination": null, "headers": null, "query": null, "path": "/template", "scheme": null, "method": null}, "response": {"status": 200, "body": "<h1>Matched on template</h1>", "headers": {"Content-Type": ["text/html; charset=utf-8"]}, "encodedBody": false}}]}')
