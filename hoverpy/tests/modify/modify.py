#!/usr/bin/env python

import sys
import json
import logging

logging.basicConfig(filename='middleware.log', level=logging.DEBUG)
logging.debug('Middleware "modify_request" called')

payload = sys.stdin.readlines()[0]
logging.debug(payload)

payload_dict = json.loads(payload)

payload_dict['response']['body'] = "modified!"
print(json.dumps(payload_dict))
