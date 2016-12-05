#!/usr/bin/env python

# This is the payload modification script. It truly allows us to do all
# types of weird, wild and wonderful mutations to the data that gets sent
# back to our application. Let's begin by imporing what we'll need.

import sys
import json
import logging
import random

logging.basicConfig(filename='middleware.log', level=logging.DEBUG)
logging.debug('Middleware "modify_request" called')

# Above we've also configured our logging. This is essential, as it's
# difficult to figure out what went wrong otherwise.


def main():
    data = sys.stdin.readlines()
    payload = data[0]
    logging.debug(payload)
    payload_dict = json.loads(payload)

    # The response to our request gets sent to middleware via stdin.
    # Therefore, we are really only interested in the first line.

    payload_dict['response']['status'] = random.choice([200, 201])

    # Let's randomly switch the status for the responses between 200, and 201.
    # This helps us build a resilient client, that can deal with curved balls.

    if random.choice([True, False]):
        payload_dict['response']['body'] = "{}"

    # Let's also randomly return an empty response body. This is tricky
    # middleware indeed.
    print(json.dumps(payload_dict))

if __name__ == "__main__":
    main()
# If is good practice for your client to be able to deal with unexpected
# data. This is a great example building middleware that'll thoroughly
# test your apps.<br><br>
# We are now ready to run our payload modification script:
# ``python examples/modify/modify.py``<br><br>
# Output:<br><br>
# >>> something went wrong - deal with it gracefully<br>
# >>> something went wrong - deal with it gracefully<br>
# >>> something went wrong - deal with it gracefully<br>
# >>> something went wrong - deal with it gracefully<br>
# >>> something went wrong - deal with it gracefully<br>
# >>> response successfully modified, current date is 01:45:15 PM<br>
# >>> something went wrong - deal with it gracefully<br>
# >>> something went wrong - deal with it gracefully<br>
# >>> response successfully modified, current date is 01:45:16 PM<br>
# >>> [...]<br><br>
# Excellent, above we can see how our application now deals with dire
# responses adequately. This is how resilient software is built!
