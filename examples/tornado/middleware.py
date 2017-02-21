# middleware.py

import sys
import logging
import json

logging.basicConfig(filename='middleware.log', level=logging.DEBUG)

data = sys.stdin.readlines()
payload = data[0]
doc = json.loads(payload)

logging.debug(json.dumps(doc, indent=4, separators=(',', ': ')))

if "request" in doc:
  doc["request"]["headers"]["Accept-Encoding"] = ["identity"]

if "response" in doc and doc["response"]["status"] == 200:
  if doc["request"]["destination"] == "time.ioloop.io":
    body = json.loads(doc["response"]["body"])
    body["epoch"] = 101010
    doc["response"]["body"] = json.dumps(body)
    doc["response"]["headers"]["Content-Length"] = [str(len(json.dumps(body)))]

print(json.dumps(doc))