HoverPy
=======

|PyPI version| |RTD badget|\ |Build Status|

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Hoverpy is a Python library that enables you to transparently use
`HoverFly <https://github.com/SpectoLabs/hoverfly>`__ in your python
applications.

Hoverfly is a lightweight, open source service virtualization tool.
Using Hoverfly, you can virtualize your application dependencies to
create a self-contained development or test environment.

Installation
------------

If you plan on trying out the examples:

.. code:: bash

    git clone https://github.com/SpectoLabs/hoverpy.git
    cd hoverpy
    python setup.py test

    # please note, this is not required for running the examples, only for installing your local copy:
    # sudo python setup.py install

Or whether you just want to install it using pip (not yet recommended):

.. code:: bash

    pip install --user -i https://testpypi.python.org/pypi hoverpy

Test
----

.. code:: bash

    make test
    # or
    python setup.py test

Examples
--------

.. toctree::
   :maxdepth: 1

   basic.rst
   readthedocs.rst
   modify.rst
   delays.rst
   unittesting.rst

`basic <basic.html>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~

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

--------------

|logo|
======

.. |PyPI version| image:: https://badge.fury.io/py/hoverpy.svg
   :target: https://testpypi.python.org/pypi/hoverpy
.. |RTD badget| image:: https://readthedocs.org/projects/pip/badge/?version=latest
   :target: http://hoverpy.readthedocs.io/en/latest/
.. |Build Status| image:: https://travis-ci.org/SpectoLabs/hoverpy.svg?branch=master
   :target: https://travis-ci.org/SpectoLabs/hoverpy
.. |logo| image:: https://github.com/SpectoLabs/hoverfly/raw/master/core/static/img/hoverfly_logo.png
