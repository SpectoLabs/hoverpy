.. _basic:

=====
basic
=====

This is by far the simplest example on how to get started with HoverPy.

.. literalinclude:: ../../../examples/basic/basic.py

``$ python examples/basic/basic.py``

You should see time printed twice. Notice the time is the same on each request, that is because the ``simulated_get`` was served from data that was captured while calling ``captured_get``.

You may have noticed this created a ``requests.db`` inside your current directory. This is a boltdb database, holding our requests, and their responses. 