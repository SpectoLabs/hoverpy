import sys
import os

if sys.argv[1] == "generateDocs":

  examples = [
    "examples/delays/delays.py",
    "examples/basic/basic.py",
    "examples/modify/modify.py",
    "examples/readthedocs/readthedocs.py"
  ]

  for example in examples:
    lineType = ""
    lastLineType = ""
    stuff = []
    thisFar = ""

    for line in open(example, "r").readlines():
      line = line[0:-1]
      if line == "":
        continue
      assert(line)
      lineType = "comment" if line[0] == "#" else "code"
      if lastLineType == "":
        lastLineType = lineType
      if lineType == "comment":
        line = line[2:]
      if lineType == lastLineType:
        thisFar += line+"\n" if lineType == "code" else line+" "
      else:
        stuff.append((lastLineType, thisFar))
        thisFar = line+"\n" if lineType == "code" else line+" "
      lastLineType = lineType

    stuff.append((lastLineType, thisFar))

    f = open(os.path.join(os.path.dirname(example), "README.md"), "w")  

    for s in stuff:
      if s[0] == "code":
        f.write("\n\n```python\n"+s[1]+"\n```\n\n")
      else:
        f.write(s[1][0].upper() + s[1][1:])

  exit()

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

import platform
import urllib
import zipfile
import stat
import hoverpy.config as config

version = '0.0.2'
dist_version = '0.9.0'

hoverfly = config.getHoverFlyBinaryPath()

if sys.argv[1] != "egg_info" and not os.path.isfile(hoverfly):
  config.downloadHoverFly()

hoverfly_target_dir = os.path.join('hoverpy', 'bin', version, 'dist_v%s'%dist_version, config.dist)
hoverfly_bin = os.path.join('hoverpy', 'bin', 'v%s'%dist_version, config.dist, "hoverfly")

setup(
  name = 'hoverpy',
  packages = ['hoverpy'],
  version = version,
  description = 'A python library for HoverFly',
  author = 'SpectoLabs',
  author_email = 'shyal@shyal.com',
  url = 'https://github.com/shyal/hoverpy',
  download_url = 'https://github.com/shyal/hoverpy/tarball/%s'%version,
  keywords = ['testing', 'rest', 'caching', 'ci'],
  test_suite = 'hoverpy.tests.get_suite',
  classifiers = [],
  data_files=[(hoverfly_target_dir,["/tmp/hoverfly"])],
)
