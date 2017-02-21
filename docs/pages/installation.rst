.. installation

============
Installation
============

Installing from PIP
-------------------

You can also install HoverPy from PIP:

.. code:: bash

    $ pip install hoverpy

Cloning
-------

.. code:: bash

    $ git clone https://github.com/SpectoLabs/hoverpy.git
    $ cd hoverpy
    $ virtualenv .venv
    $ source .venv/bin/activate
    $ python setup.py install

This installs hoverpy and its requirements in your .venv folder; make sure to pull often, and run the ``python setup.py install`` when you do.

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

    $ python examples/basic/basic.py

Hoverfly binary
---------------

Please note that when you install HoverPy, the Hoverfly binaries get downloaded and installed in your home directory, in

.. code:: bash

    ${home}/.hoverfly/bin/dist_vX.X.X/${OS}_${ARCH}/hoverfly

