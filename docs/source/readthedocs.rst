.. readthedocs

===========
readthedocs
===========

This is a slightly more advanced example, where we query readthedocs.io for articles. In the first phase, we run the program in capture mode. This is done using the capture flag:

``env PYTHONPATH=.:${PYTHONPATH} python examples/readthedocs/readthedocs.py --capture``

the program can then be run again in simulate mode, in a fraction of the time:

``env PYTHONPATH=.:${PYTHONPATH} python examples/readthedocs/readthedocs.py``

We'll now run through the code to see what it's doing. 

::

>>> from hoverpy import HoverPy
>>> import requests
>>> import time


We obviously start our program by doing the usual imports. We're using the ``time`` module to time our code. 

::

>>> from argparse import ArgumentParser
>>> parser = ArgumentParser(description="Perform proxy testing/URL list creation")
>>> parser.add_argument("--capture", help="capture the data", action="store_true")
>>> parser.add_argument(
>>>     "--limit", default=50, help="number of links to capture / simulate")
>>> args = parser.parse_args()


As you can see, we're setting up our program with the ``--capture`` flag, which either sets us up in capture mode if used, or simulate mode if not. The ``--limit`` flag can be used to increase the number of articles we fetch, however 50 is a good default value. 

::

>>> def getLinks(hp, limit):
>>>     print("\nGetting links in %s mode!\n" % hp.mode())
>>>     start = time.time()
>>>     sites = requests.get(
>>>         "http://readthedocs.org/api/v1/project/?limit="
>>>         "%d&offset=0&format=json" % int(limit))
>>>     objects = sites.json()['objects']
>>>     links = ["http://readthedocs.org" + x['resource_uri'] for x in objects]
>>>     for link in links:
>>>         response = requests.get(link)
>>>         print("url: %s, status code: %s" % (link, response.status_code))
>>>     print("Time taken: %f" % (time.time() - start))


The function above gets the 50 articles from readthedocs, and prints how long it took once we're done. 

::

>>> if __name__ == "__main__":
>>>     with HoverPy(capture=args.capture) as hp:
>>>         getLinks(hp, args.limit)


Finally our program is run. Results will vary based on your internet speed, but running in simulate mode should run around ``50x`` to ``100x`` faster. 