import sys
import platform
import os
import shutil
import urllib
import zipfile
import stat
import tempfile
from os.path import join
from os.path import dirname
from os.path import abspath
from os.path import expanduser
from os.path import isfile


def getArch():
    arch = platform.machine()
    if arch == "x86_64":
        return "amd64"
    return arch.lower()


def getOS():
    o = platform.system().lower()
    if o == "darwin":
        return "OSX"
    return o.lower()

dist = getOS()+"_"+getArch()

dirName = dirname(abspath(__file__))

version = '0.1.17'
dist_version = '0.9.2'

hoverflyDirectory = join(
    expanduser("~"),
    ".hoverfly",
    "bin",
    "dist_v" +
    dist_version,
    getOS() +
    "_" +
    getArch())
hoverflyBinFile = "hoverfly.exe" if getOS() == "windows" else "hoverfly"
hoverflyPath = join(hoverflyDirectory, hoverflyBinFile)


def getHoverFlyBinaryPath():
    if isfile(hoverflyPath):
        return hoverflyPath
    return ""


def downloadHoverFly():
    tmp = tempfile.mkdtemp()
    bundlePath = join(tmp, "hoverfly_bundle_%s.zip" % dist)
    hoverflyBinTempFile = join(tmp, hoverflyBinFile)

    url = "https://github.com/SpectoLabs/hoverfly/"\
        "releases/download/v%s/hoverfly_bundle_%s.zip" % (
            dist_version, dist)

    print("DOWNLOADING HOVERFLY FROM %s TO %s" % (url, tmp))

    if sys.version_info.major == 2:
        import urllib
        urllib.urlretrieve(url, bundlePath)
    elif sys.version_info.major == 3:
        import shutil
        import urllib.request
        with urllib.request.urlopen(url) as response:
            with open(bundlePath, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)

    print("UNZIPPING")
    zip_ref = zipfile.ZipFile(bundlePath, 'r')
    zip_ref.extractall(tmp)
    zip_ref.close()
    st = os.stat(hoverflyBinTempFile)
    os.chmod(hoverflyBinTempFile, st.st_mode | stat.S_IEXEC)
    return installHoverFly(hoverflyBinTempFile)


def installHoverFly(hoverflyBinTempFile):
    if not os.path.isdir(hoverflyDirectory):
        os.makedirs(hoverflyDirectory)
    shutil.copy(hoverflyBinTempFile, hoverflyPath)
    if os.path.isfile(hoverflyPath):
        print("Hoverfly installed successfully: %s" % hoverflyPath)
    else:
        raise ValueError('HoverFly binary not installed successfully')
    return hoverflyPath
