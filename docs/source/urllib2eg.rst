.. urllib2

urllib2
********


Import hoverpy's main class: HoverPy

.. code:: python

    from hoverpy import HoverPy

Create our HoverPy object in capture mode

.. code:: python

    hp = HoverPy(capture=True)

Import urllib2 for http

.. code:: python

    import urllib2

Build our proxy handler for urllib2. This is currently a rather crude
method of initialising urllib2, and this code will be incorporated into
the main library shortly.

.. code:: python

    proxy = urllib2.ProxyHandler({'http': 'localhost:8500'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

Print the json from our get request. Hoverpy acted as a proxy: it made
the request on our behalf, captured it, and returned it to us.

.. code:: python

    print(urllib2.urlopen("http://ip.jsontest.com/myip").read())

Switch HoverPy to simulate mode. HoverPy no longer acts as a proxy; all
it does from now on is replay the captured data.

.. code:: python

    hp.simulate()

Print the json from our get request. This time the data comes from the
store.

.. code:: python

    print(urllib2.urlopen("http://ip.jsontest.com/myip").read())

