Examples
========

.. toctree::
   :maxdepth: 1

   basic.rst
   readthedocs.rst
   modify.rst
   delays.rst
   unittesting.rst

basic
-----

.. code:: bash

    python examples/basic/basic.py

This is the most basic example possible. Captures one request, and
replays it.

`readthedocs <readthedocs.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    python examples/readthedocs/readthedocs.py

Slightly more advanced example, where we query readthedocs.io for
articles, get these articles. The program can be run in capture or
simulate mode, and the functionality is timed.

`delays <delays.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    python examples/delays/delays.py

Demonstrates how to add latency to calls, based on host, and method
type.

`modify <modify.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    python examples/modify/modify.py

Demonstrations how to modify requests. This is particularly useful for
sending curved balls to your applications, and make sure they deal with
them correctly.

`unittesting <unittesting.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    env HOVERPY_CAPTURE=true python examples/unittesting/unittesting.py
    python examples/unittesting/unittesting.py

Demonstrates how to use the ``hoverpy.TestCase`` class for unit testing
purposes.

