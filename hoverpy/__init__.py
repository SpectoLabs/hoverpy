import time
import os
import requests
import logging
import json
import subprocess
from subprocess import Popen, PIPE
import platform
import config

logging.basicConfig(filename='hoverfly.log',level=logging.DEBUG)

hoverfly = config.getHoverFlyBinaryPath()

def session():
  session = requests.Session()
  session.trust_env = False
  return session

class HoverPy:

  _proxyPort = None
  _adminPort = None
  _host = ""
  _process = None
  _flags = []

  def __init__(self, host="localhost", capture=False, proxyPort=8500, adminPort=8888, flags=[]):
    self._proxyPort = proxyPort
    self._adminPort = adminPort
    self._host = host
    self._flags = flags
    if capture:
      self._flags.append("--capture")
    self.enableProxy()
    self.start()

  def __del__(self):
    if  self._process:
      self.stop()

  def wipe(self):
    try:
        os.remove("./requests.db")
    except OSError:
        pass

  def host(self):
    return "http://%s:%i" % (self._host, self._adminPort)

  def v1(self):
    return self.host()+"/api"

  def v2(self):
    return self.host()+"/api/v2"

  def enableProxy(self):
    logging.debug("enabling proxy")
    os.environ["HTTP_PROXY"] = "http://%s:%i" % (self._host, self._proxyPort)
    os.environ["HTTPS_PROXY"] = "https://%s:%i" % (self._host, self._proxyPort)
    os.environ["REQUESTS_CA_BUNDLE"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cert.pem")

  def disableProxy(self):
    del os.environ['HTTP_PROXY']

  def start(self):
    logging.debug("starting")
    FNULL = open(os.devnull, 'w')
    self._process = Popen([hoverfly]+self._flags, stdout=FNULL, stderr=subprocess.STDOUT)
    logging.debug("has pid %i" % self._process.pid)
    time.sleep(0.3)
    return self._process

  def stop(self):
    if logging:
      logging.debug("stopping")
    self._process.kill()
    self._process = None

  def capture(self):
    return self.mode("capture")

  def simulate(self):
    return self.mode("simulate")

  def config(self):
    return session().get(self.v2()+"/hoverfly").json()

  def simulation(self):
    return session().get(self.v2()+"/simulation").json()

  def destination(self, name=""):
    if name:
      return session().put(self.v2()+"/hoverfly/destination", data={"destination": name}).json()
    else:
      return session().get(self.v2()+"/hoverfly/destination").json()

  def middleware(self):
    return session().get(self.v2()+"/hoverfly/middleware").json()

  def mode(self, mode=None):
    if mode:
      logging.debug("SWITCHING TO %s" % mode)
      url = self.v2()+"/hoverfly/mode"
      logging.debug(url)
      return session().put(url, data=json.dumps({"mode":mode})).json()["mode"]
    else:
      return session().get(self.v2()+"/hoverfly/mode").json()["mode"]

  def usage(self):
    return session().get(self.v2()+"/hoverfly/usage").json()

  def metadata(self, delete=False):
    if delete:
      return session().delete(self.v1()+"/metadata").json()
    else:
      return session().get(self.v1()+"/metadata").json()

  def records(self, data=None):
    if data:
      return session().post(self.v1()+"/records", data=data).json()
    else:
      return session().get(self.v1()+"/records").json()

  def delays(self, delays=[]):
    if delays:
      return session().put(self.v1()+"/delays", data=json.dumps(delays)).json()
    else:
      return session().get(self.v1()+"/delays").json()

  def addDelay(self, urlPattern="", delay=0, httpMethod=None):
    delay = {"urlPattern":urlPattern, "delay": delay}
    if httpMethod:
      delay["httpMethod"] = httpMethod
    return self.delays(delays={"data":[delay]})

def quick_test():
  import pprint
  pp = pprint.PrettyPrinter(indent=4)
  hp = HoverPy()
  hp.capture()
  requests.get("http://ip.jsontest.com/ip")
  if "data" in hp.delays().keys():
    print("HOVERPY AND HOVERFLY QUICK TEST SUCCESS!!")

if __name__ == "__main__":
  quick_test()

