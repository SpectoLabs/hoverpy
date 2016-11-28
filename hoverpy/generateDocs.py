#!/usr/bin/python

import os

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

  p = os.path.join(os.path.dirname(example), "README.md")
  f = open(p, "w")
  print("writing %s" % p)

  for s in stuff:
    if s[0] == "code":
      f.write("\n\n```python\n"+s[1]+"\n```\n\n")
    else:
      f.write(s[1][0].upper() + s[1][1:])