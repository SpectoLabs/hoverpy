#!/usr/bin/python


def gen():
    import os
    import re

    examples = [
        "examples/delays/delays.py",
        "examples/basic/basic.py",
        "examples/modify/modify.py",
        "examples/modify/modify_payload.py",
        "examples/readthedocs/readthedocs.py",
        "examples/unittesting/unittesting.py",
        "examples/urllib2eg/urllib2eg.py",
        "examples/urllib3eg/urllib3eg.py",
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
            lineType = "comment" if re.match("^\s*# ", line) else "code"
            if lastLineType == "":
                lastLineType = lineType
            if lineType == "comment":
                line = re.match(".*# (.*)", line).group(1)
            if lineType == lastLineType:
                thisFar += line+"\n" if lineType == "code" else line+" "
            else:
                stuff.append((lastLineType, thisFar))
                thisFar = line+"\n" if lineType == "code" else line+" "
            lastLineType = lineType

        stuff.append((lastLineType, thisFar))

        p = os.path.join(os.path.splitext(example)[0]+".rst")
        f = open(p, "w")
        print("writing %s" % p)
        bn = os.path.splitext(os.path.basename(example))[0]
        f.write(
            ".. " +
            bn +
            "\n\n" +
            len(bn) *
            "=" +
            "\n" +
            bn +
            "\n" +
            len(bn) *
            "=" +
            "\n\n")
        for s in stuff:
            if s[0] == "code":
                code = s[1].replace("\n", "\n>>> ")
                code = code[:-4]
                f.write("\n\n::\n\n>>> "+code+"\n\n")
            else:
                text = s[1]
                if text[0] == " ":
                    text = text[1:]
                text = text[0].upper() + text[1:]
                text = text.replace("<br> ", "\n")
                text = text.replace("<br>", "\n")
                f.write(text)


if __name__ == "__main__":
    gen()
