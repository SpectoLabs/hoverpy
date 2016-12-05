# This is by far the simplest example on how to get started with HoverPy.
# Let's import our most important class HoverPy, along with whatever else
# we may need
from hoverpy import HoverPy
import requests

# Now let's create our HoverPy object in capture mode. We do so with a
# `with` statement as this is the pythonic way, although this is not a necessity.
with HoverPy(capture=True) as hoverpy:

    # print the json from our get request. Hoverpy acted as a proxy: it made
    # the request on our behalf, captured it, and returned it to us.
    print(requests.get("http://ip.jsontest.com/myip").json())

    # switch HoverPy to simulate mode. HoverPy no longer acts as a proxy; all
    # it does from now on is replay the captured data.
    hoverpy.simulate()

    # print the json from our get request. This time the data comes from the
    # store.
    print(requests.get("http://ip.jsontest.com/myip").json())


# requests.db<br>
# -----------<br>
# <br>
# You may have noticed this created a ``requests.db`` inside your current
# directory. This is a boltdb database, holding our requests, and their
# responses.
