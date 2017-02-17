.. readthedocs

===========
readthedocs
===========

This is a slightly more advanced example, where we query readthedocs.io for articles.

.. literalinclude:: ../../../examples/readthedocs/readthedocs.py

.. code:: python

  python examples/readthedocs/readthedocs.py

The first time this command is invoked it takes ``Time taken: 7.658194``. The second time we run it, ``Time taken: 0.093647``. Please note this uses the ``recordMode="once"`` which is legacy from Ruby's `VCR <https://github.com/vcr/vcr>`_ and Python's `VCR.py <http://vcrpy.readthedocs.io>`_.
