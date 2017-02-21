.. latency

=======
latency
=======


Simulating service latency during the development phase of a service is good practice, as it forces developers to write code that acts gracefully and resiliently in the event of unexpected latency during network io.

To add latency to services, simply add the FQDN, delay in milliseconds, and optional HTTP method in an array of tuples for the ``delays`` parameter.

.. literalinclude:: ../../../examples/latency/latency.py

.. code:: python

  $ python examples/latency/latency.py

The latency is added when querying these services. If the HTTP method is omitted in the tupes, then the delay applies to all methods.