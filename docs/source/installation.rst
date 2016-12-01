.. installation

Installation
============

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