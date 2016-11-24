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

version = '0.0.2'
dist_version = '0.9.0'

def getHoverFlyBinaryPath():
  """
  get hoverpy from where setup.py would have installed it
  """
  hoverfly = os.path.join(dirName, "..", "bin", "hoverfly")
  if os.path.isfile(hoverfly):
    return hoverfly

  for path in sys.path:
    newPath = os.path.join(path, "..", "..", "..", "hoverpy", "bin", version, "dist_v"+dist_version, getOS()+"_"+getArch(), "hoverfly")
    if os.path.isfile(newPath):
      return newPath

  return ""

def downloadHoverFly():
  bundlePath = "/tmp/hoverfly_bundle_%s.zip"%dist
  print("DOWNLOADING HOVERFLY")
  urllib.urlretrieve("https://github.com/SpectoLabs/hoverfly/releases/download/v%s/hoverfly_bundle_%s.zip"%(dist_version, dist), bundlePath)
  print("UNZIPPING")
  zip_ref = zipfile.ZipFile(bundlePath, 'r')
  zip_ref.extractall("/tmp/")
  zip_ref.close()
  st = os.stat('/tmp/hoverfly')
  os.chmod('/tmp/hoverfly', st.st_mode | stat.S_IEXEC)
  print("Deleting downloaded zip file")
  print("hoverfly binary at", '/tmp/hoverfly')
  os.unlink(bundlePath)
  installHoverFly()

def installHoverFly():
  # figure out where we are. Are we a dev?
  # or are we a library that's been installed?

  devMode = os.path.isfile(os.path.join(dirName, "..", "README.md"))

  if devMode:
    print("We are in dev mode! Copying binary to ourselves!")
    targetDir = os.path.join(dirName, "..", "bin")
    target = os.path.join(targetDir, "hoverfly")
    if not os.path.isdir(targetDir):
      os.mkdir(targetDir)
    shutil.copy("/tmp/hoverfly", target)
  else:
    print("We don't seem to be in dev mode")

