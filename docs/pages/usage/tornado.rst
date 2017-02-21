.. _tornado:

=======
Tornado
=======

HoverPy can be used to make virtualise asynchronous requests made from Tornado's AsyncHTTPClient.

Capturing traffic
-----------------

.. literalinclude:: ../../../examples/tornado/svTornado.py

Making a request to our server now captures the requests.

``curl http://localhost:8080``

In fact you may notice your directory now contains a ``tornado.db``.


Simulating traffic
------------------

We can how switch our server to simulate mode:

.. literalinclude:: ../../../examples/tornado/simTornado.py

Which means we are no longer hitting the real downstream dependency.

Modifying traffic
-----------------

HoverPy can also be used to modify your requests, to introduce failures, or build tolerant readers

.. literalinclude:: ../../../examples/tornado/modTornado.py

This is our middleware:

.. literalinclude:: ../../../examples/tornado/middleware.py
