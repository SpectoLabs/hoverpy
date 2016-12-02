.. _modify

======
modify
======

Demonstrates how to modify requests. This is particularly useful for sending curved balls to your applications, and make sure they deal with them correctly. import hoverpy's main class: HoverPy 

::

>>> from hoverpy import HoverPy


Import requests for http 

::

>>> import requests


Create our HoverPy object with modify and middleware enabled. please note this brings in ```python examples/modify/modify_payload.py``` which will get run on every request 

::

>>> with HoverPy(
>>>     flags=[
>>>         "-modify",
>>>         "-middleware",
>>>         "python examples/modify/modify_payload.py"]) as hoverpy:


Our middleware is designed to random return an empty body instead of what it's supposed to return (the curren time). This is a good example of how to alter your dependencies, and adequately test and react based on their content 

::

>>>     for i in range(30):
>>>         r = requests.get("http://time.jsontest.com")
>>>         if "time" in r.json().keys():
>>>             print(
>>>                 "response successfully modified, current date is " +
>>>                 r.json()["time"])
>>>         else:
>>>             print("something went wrong - deal with it gracefully")


