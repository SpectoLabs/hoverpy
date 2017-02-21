.. modify

======
modify
======

Modifying requests and responses via middleware is simply a matter of using the ``modify`` function decorator.

.. literalinclude:: ../../../examples/modify/modify.py

.. code:: bash
  
  $ python examples/modify/modify.py

Output:

::

  {u'date': u'2017-02-17', u'epoch': 101010, u'time': u'21:22:38'}

As you can see, the epoch has been successfully modified by the middleware script.

Middleware
----------

Middleware is required, and can be written in any language that is supported in your development environment.

.. literalinclude:: ../../../examples/modify/middleware.py

