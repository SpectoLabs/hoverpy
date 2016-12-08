.. soap

====
soap
====

In this example we'll take a look at using hoverpy when working with SOAP. To run this example, simply execute:

``examples/soap/soap.py --capture``

which runs the program in capture mode, then:

``examples/soap/soap.py``

Which simply runs our program in simulate mode.

This program gets our IP address from ``http://jsontest.com``, then uses it to do some geolocation using a WDSL SOAP web service. In my case, I'm getting this:

.. code-block:: json

    {
       'ResolveIPResult':{
          'City':u'London',
          'HasDaylightSavings':False,
          'CountryCode':u'GB',
          'AreaCode':u'0',
          'Country':u'United Kingdom',
          'StateProvince':u'H9',
          'Longitude':-0.09550476,
          'TimeZone':None,
          'Latitude':51.5092,
          'Organization':None,
          'Certainty':90,
          'RegionName':None
       }
    }

Which is what the ``ip2geo`` service thinks is the location of the SpectoLabs office!

.. literalinclude:: ../../examples/soap/soap.py
   :language: python
   :lines: 3-5

Above, we bring in our usual suspect libraries. Namely the ``HoverPy`` class, ``pysimplesoap`` which is a straight forward SOAP client, and the ``requests`` library.

.. literalinclude:: ../../examples/soap/soap.py
   :language: python
   :lines: 7-11

We use argparse so we can run our app in ``--capture`` mode first.


.. literalinclude:: ../../examples/soap/soap.py
   :language: python
   :lines: 14

We then construct HoverPy either in capture, or simulate mode, depending on the flag provided.


.. literalinclude:: ../../examples/soap/soap.py
   :language: python
   :lines: 15

We then make a get HTTP request to ``http://ip.jsontest.com`` for our IP address. This is very similar to our basic example.

.. literalinclude:: ../../examples/soap/soap.py
   :language: python
   :lines: 16

We now tell ``pysimplesoap`` to use ``urllib2``, this is because urllib2 happens to play well with proxies.

.. literalinclude:: ../../examples/soap/soap.py
   :language: python
   :lines: 18-20

We then build our SOAP client, pointing to the ip2go WSDL schema description URL.

.. literalinclude:: ../../examples/soap/soap.py
   :language: python
   :lines: 22

We finally invoke the ``ResolveIP`` method on our SOAP client. So to resume, in this example we built a program that gets our IP address from one external service, and then builds a SOAP client using a WSDL schema description, and finally queries the SOAP service for our location using said IP address.

If you really want to prove to yourself that hoverfly is indeed playing back the requests, then you can run the script in simulate mode without an internet connection. Timing our script also shows us we're now running approximately 10x faster.

