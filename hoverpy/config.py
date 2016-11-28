import sys
import platform
import os
import shutil
import urllib
import zipfile
import stat

def getArch():
  arch = platform.machine()
  if arch == "x86_64":
    return "amd64"
  return arch

def getOS():
  o = platform.system().lower()
  if o == "darwin":
    return "OSX"
  return o

dist = getOS()+"_"+getArch()

dirName = os.path.dirname(os.path.abspath(__file__))

version = '0.1.3'
dist_version = '0.9.0'
hoverflyDirectory = os.path.join(os.path.expanduser("~"), ".hoverfly", "bin", "dist_v"+dist_version, getOS()+"_"+getArch(),)
hoverflyPath = os.path.join(hoverflyDirectory, "hoverfly")

def getHoverFlyBinaryPath():
  if os.path.isfile(hoverflyPath):
    return hoverflyPath
  return ""

def downloadHoverFly():
  bundlePath = "/tmp/hoverfly_bundle_%s.zip"%dist
  print("DOWNLOADING HOVERFLY")

  url = "https://github.com/SpectoLabs/hoverfly/releases/download/v%s/hoverfly_bundle_%s.zip"%(dist_version, dist)

  if sys.version_info.major == 2:
    import urllib
    urllib.urlretrieve(url, bundlePath)
  elif sys.version_info.major == 3:
    import shutil
    import urllib.request
    with urllib.request.urlopen(url) as response, open(bundlePath, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

  print("UNZIPPING")
  zip_ref = zipfile.ZipFile(bundlePath, 'r')
  zip_ref.extractall("/tmp/")
  zip_ref.close()
  st = os.stat('/tmp/hoverfly')
  os.chmod('/tmp/hoverfly', st.st_mode | stat.S_IEXEC)
  print("Deleting downloaded zip file")
  os.unlink(bundlePath)
  return installHoverFly()

def installHoverFly():
  if not os.path.isdir(hoverflyDirectory):
    os.makedirs(hoverflyDirectory)
  shutil.copy("/tmp/hoverfly", hoverflyPath)
  if os.path.isfile(hoverflyPath):
    print("Hoverfly installed successfully: %s" % hoverflyPath)
  else:
    raise ValueError('HoverFly binary not installed successfully')
  return hoverflyPath
