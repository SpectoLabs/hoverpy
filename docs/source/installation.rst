.. installation

============
Installation
============

Cloning
-------

We're currently in development mode, so you're better off cloning the repository. Make sure to pull often!

.. code:: bash

    $ git clone https://github.com/SpectoLabs/hoverpy.git
    $ cd hoverpy

Or using virtualenv
-------------------

If you prefer using virtualenv to keep your environment clean:

.. code:: bash

    $ virtualenv hoverpyenv
    $ cd hoverpyenv
    $ source bin/activate
    $ git clone https://github.com/SpectoLabs/hoverpy.git
    $ cd hoverpy

Testing
-------

Make sure everything is working:

.. code:: bash

    $ python setup.py test

Running the examples
--------------------

.. code:: bash

    $ ls examples/*
    $ basic       delays      modify      readthedocs tornado     unittesting urllib2eg   urllib3eg
    $ python examples/basic/basic.py

Please note we'll cover the examples in `usage`_ page.

.. _usage: usage.html

Installing from repo
--------------------

Please note there isn't yet much point installing HoverPy since we're currently still in development mode. This means the code will change often. But if you really want to, then here's the command:

.. code:: bash

    sudo python setup.py install

Installing from PIP
-------------------

You can also install HoverPy from PIP, however once again you're better off playing with your repo clone for now. But if you really wish so, then here's how you can do so:

.. code:: bash

    pip install --user -i https://testpypi.python.org/pypi hoverpy
