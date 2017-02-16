.. modify_soap

===========
modify soap
===========

In this example we'll take a look at using hoverpy in conjunction with middleware to modify SOAP data. This example builds upon the previous SOAP example, so I strongly suggest you do that one first.

examples/soap/soapModify.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../../../examples/soap/soapModify.py
   :language: python
   :lines: 7

Above, the only real difference with ``examples/soap/soap.py`` is that we're loading up HoverPy with middleware enabled.

.. literalinclude:: ../../../examples/soap/soapModify.py
   :language: python
   :lines: 15

When running this script with ``python examples/soap/soapModify.py`` you should notice your city is 'New York'. That's the middleware modifying the result of our SOAP operation.

The XML from ip2geo
~~~~~~~~~~~~~~~~~~~

Before jumping into the middleware, let's see what we'll be modifying.

.. code:: xml

  <?xml version="1.0" encoding="UTF-8"?>
  <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <soap:Body>
        <ResolveIPResponse xmlns="http://ws.cdyne.com/">
           <ResolveIPResult>
              <City>New York</City>
              <StateProvince>H9</StateProvince>
              <Country>United Kingdom</Country>
              <Organization />
              <Latitude>51.5092</Latitude>
              <Longitude>-0.09550476</Longitude>
              <AreaCode>0</AreaCode>
              <TimeZone />
              <HasDaylightSavings>false</HasDaylightSavings>
              <Certainty>90</Certainty>
              <RegionName />
              <CountryCode>GB</CountryCode>
           </ResolveIPResult>
        </ResolveIPResponse>
     </soap:Body>
  </soap:Envelope>

This is the XML that gets sent back to us after calling the ``ResolveIP`` method, as defined in http://ws.cdyne.com/ip2geo/ip2geo.asmx?WSDL. We are interested in modifying the ``City`` node.

examples/soap/modify_payload.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

And here are the important parts of our payload modification script.

.. literalinclude:: ../../../examples/soap/modify_payload.py
   :language: python
   :lines: 7-8

Above we make sure we are importing the lxml classes that will help us modify the data.


.. literalinclude:: ../../../examples/soap/modify_payload.py
   :language: python
   :lines: 19-21

Let's make sure we only operate when we have a response, and it has a body. 


.. literalinclude:: ../../../examples/soap/modify_payload.py
   :language: python
   :lines: 22-29

We parse our xml and turn it into an object. Remember that our program gets our IP address, then tries to geo-locate us based on our IP. The intent of our middleware is to override the city no matter what.

.. literalinclude:: ../../../examples/soap/modify_payload.py
   :language: python
   :lines: 31-34

We finally remove annotations and namespaces that got added to the City element by the objectify library, and serialise the modified body back into the response. And we are done.