.. basic

Basic Example
********


Import hoverpy's main class: HoverPy

.. code:: python

    from hoverpy import HoverPy

Import requests and random for http

.. code:: python

    import requests

Create our HoverPy object in capture mode

.. code:: python

    hp = HoverPy(capture=True)

Print the json from our get request. Hoverpy acted as a proxy: it made
the request on our behalf, captured it, and returned it to us.

.. code:: python

    print(requests.get("http://ip.jsontest.com/myip").json())

Switch HoverPy to simulate mode. HoverPy no longer acts as a proxy; all
it does from now on is replay the captured data.

.. code:: python

    hp.simulate()

Print the json from our get request. This time the data comes from the
store.

.. code:: python

    print(requests.get("http://ip.jsontest.com/myip").json())

