.. modify

======
modify
======

Let's look into mutating responses using middleware. This is particularly useful for sending curved balls to your applications, and make sure they deal with them correctly. 

::

>>> from hoverpy import HoverPy
>>> import requests
>>> with HoverPy(
>>>         modify=True,
>>>         middleware="python examples/modify/modify_payload.py") as hoverpy:


Above we created our HoverPy object with modify and middleware enabled. Please note this brings in ``python examples/modify/modify_payload.py`` which will get run on every request. 

::

>>>     for i in range(30):
>>>         r = requests.get("http://time.jsontest.com")


Let's make 30 requests to http://time.jsontest.com which simply gets us the current local time 

::

>>>         if "time" in r.json().keys():
>>>             print(
>>>                 "response successfully modified, current date is " +
>>>                 r.json()["time"])


The ``time`` key is inside the response, which is what we expected. 

::

>>>         else:
>>>             print("something went wrong - deal with it gracefully")


However if the ``time`` key isn't in the response, then something clearly went wrong. Next let's take a look at the middleware.

.. include:: modify_payload.rst 