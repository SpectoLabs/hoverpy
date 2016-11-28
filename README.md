# hoverpy

Hoverpy is a Python library that enables you to transparently use [HoverFly](https://github.com/SpectoLabs/hoverfly) in your python applications.

Hoverfly is a lightweight, open source service virtualization tool. Using Hoverfly, you can virtualize your application dependencies to create a self-contained development or test environment.

[Read the HoverFly docs](http://hoverfly.io/) else continue to jump straight into HoverPy.

## Installation

If you plan on trying out the examples:

```bash
git clone https://github.com/SpectoLabs/hoverpy.git
cd hoverpy
python setup.py test

# please note, this is not required for running the examples!
sudo python setup.py install
```

Or whether you just want to install it:

```bash
pip install --user -i https://testpypi.python.org/pypi hoverpy
```

## Examples

### [basic](examples/basic)

```bash
python examples/basic/basic.py
```

This is the most basic example possible. Captures one request, and replays it.

### [readthedocs](examples/readthedocs)

```bash
python examples/readthedocs/readthedocs.py
```

Slightly more advanced example, where we query readthedocs.io for articles, get these articles. The program can be run in capture or simulate mode, and the functionality is timed.

### [delays](examples/delays)

```bash
python examples/delays/delays.py
```

Demonstrates how to add latency to calls, based on host, and method type.

### [modify](examples/modify)

```bash
python examples/modify/modify.py
```

Demonstrations how to modify requests. This is particularly useful for sending curved balls to your applications, and make sure they deal with them correctly.

-------------------------------

![logo](https://github.com/SpectoLabs/hoverfly/raw/master/core/static/img/hoverfly_logo.png)
=======
