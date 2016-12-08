#!/usr/bin/env python

import sys
import json
import logging
import random
from lxml import objectify
from lxml import etree

logging.basicConfig(filename='middleware.log', level=logging.DEBUG)
logging.debug('Middleware "modify_request" called')


def main():
    data = sys.stdin.readlines()
    payload = data[0]
    payload_dict = json.loads(payload)

    if "response" in payload_dict and "body" in payload_dict["response"]:
        body = payload_dict["response"]["body"]
        try:
            root = objectify.fromstring(str(body))
            ns = "{http://ws.cdyne.com/}"
            logging.debug("transforming")

            ipe = ns + "ResolveIPResponse"
            ipt = ns + "ResolveIPResult"

            root.Body[ipe][ipt].City = "New York"

            objectify.deannotate(root.Body[ipe][ipt].City)
            etree.cleanup_namespaces(root.Body[ipe][ipt].City)

            payload_dict["response"]["body"] = etree.tostring(root)

            logging.debug(etree.tostring(root))

        except Exception:
            pass

    print(json.dumps(payload_dict))

if __name__ == "__main__":
    main()
