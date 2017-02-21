HoverPy
=======

HoverPy speeds up and simplifies Python development and testing that involves downstream HTTP / HTTPS services. It does so by using a high-performance Go caching proxy to capture, simulate, modify and synthesize network traffic.

.. code:: python

  from hoverpy import capture, simulate
  import requests

  @capture("requests.db")
  def captured_get():
      print(requests.get("http://time.jsontest.com").json())

  @simulate("requests.db")
  def simulated_get():
      print(requests.get("http://time.jsontest.com").json())

  captured_get()
  simulated_get()

This grants several benefits:

-  Increased development speed
-  Increased test speed
-  Ability to work offline
-  A deterministic test environment
-  Ability to modify traffic
-  Ability to sythesize traffic
-  Ability to simulate network latency

.. code:: python

  from hoverpy import capture, modify
  import requests

  @simulate("requests.db", delays=[("time.json.com", 1000)])
  def simulated_latency():
      print(requests.get("http://time.jsontest.com").json())

  @modify(middleware="python middleware.py")
  def modified_request():
      print(requests.get("http://time.jsontest.com").json())

  simulated_latency()
  modified_request()

If/when the downstream service you are testing against changes, then you can simply delete your db file, and capture the test results again. Or you could have versioned db files for services that use versioning.

HoverPy uses `Hoverfly <http://hoverfly.io>`__ a Service Virtualisation server written in GoLang. For this reason it is rock solid in terms of speed and reliability.

Library Support
~~~~~~~~~~~~~~~

HoverPy works great with the following HTTP clients out of the box:

-  tornado
-  twisted
-  requests
-  urllib2
-  urllib3
-  pysimplesoap
-  etc.

Since HoverPy can act as a proxy or a reverse proxy, it can easily be made to work with any networking library or framework.

Source
~~~~~~

https://github.com/SpectoLabs/hoverpy/

.. image:: hoverpy_logo.png

License
~~~~~~~

HoverPy uses Apache License V2. See LICENSE.txt for more details.

.. |PyPI version| image:: https://badge.fury.io/py/hoverpy.svg
   :target: https://pypi.python.org/pypi/hoverpy
.. |RTD badget| image:: https://readthedocs.org/projects/hoverpy/badge/?version=latest
   :target: http://hoverpy.readthedocs.io/en/latest/
.. |Build Status| image:: https://travis-ci.org/SpectoLabs/hoverpy.svg?branch=master
   :target: https://travis-ci.org/SpectoLabs/hoverpy

Contents
========

.. toctree::
   :maxdepth: 3

   pages/installation
   pages/introduction
   pages/usage/usage

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


|

|PyPI version| |RTD badget|  |Build Status|

|