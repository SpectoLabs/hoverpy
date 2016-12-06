.. installation

============
Installation
============

Cloning
-------

We're currently in development mode, so you're better off cloning the repository. Make sure to pull often!

.. code:: bash

    $ virtualenv hoverpyenv
    $ cd hoverpyenv
    $ source bin/activate
    $ git clone https://github.com/SpectoLabs/hoverpy.git
    $ cd hoverpy

Testing
-------

Please make sure everything is working before proceeding to the next steps.

.. code:: bash

    $ python setup.py test

You should get a series of ``OKs``.

`Output:`

.. code:: bash

    ...
    testModify (hoverpy.tests.modify.testModify.TestModify) ... ok
    testTemplate (hoverpy.tests.templates.testTemplates.TestTemplates) ... ok
    testCapture (hoverpy.tests.testVirtualisation.TestVirt) ... ok
    testPlayback (hoverpy.tests.testVirtualisation.TestVirt) ... ok

Running the examples
--------------------

.. code:: bash

    $ ls examples/*
    $ basic       delays      modify      readthedocs tornado     unittesting urllib2eg   urllib3eg

Please note we'll cover the examples in the `usage`_ page. But for the truly impatient, you can try running the most basic example, just to make sure everything's working at this point.

.. _usage: usage.html 

.. code:: bash

    $ env PYTHONPATH=.:${PYTHONPATH} python examples/basic/basic.py

Installing from repo
--------------------

Please note there isn't yet much point installing HoverPy since we're currently still in development mode. This means the code will change often. But if you really want to, then here's the command:

.. code:: bash

    $ sudo python setup.py install

Installing from PIP
-------------------

You can also install HoverPy from PIP, however once again you're better off playing with your repo clone for now. But if you really wish so, then here's how you can do so:

.. code:: bash

    $ pip install --user -i https://testpypi.python.org/pypi hoverpy
