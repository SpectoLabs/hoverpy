import time
import os
import logging
import json
import subprocess
from subprocess import Popen

from . import config

try:
    import requests
except:
    pass

logging.basicConfig(filename='hoverfly.log', level=logging.DEBUG)

hoverfly = config.getHoverFlyBinaryPath()

if not hoverfly:
    hoverfly = config.downloadHoverFly()


class HoverPy:

    def __init__(self,
                 host="localhost",
                 capture=False,
                 proxyPort=8500,
                 adminPort=8888,
                 modify=False,
                 middleware="",
                 dbpath="",
                 db="",
                 simulation="",
                 synthesize=False,
                 metrics=False,
                 dev=False,
                 auth=False,
                 delays=[],
                 cert="",
                 certName="",
                 certOrg="",
                 dest=[],
                 verbose=False,
                 generateCACert=False,
                 destination="",
                 key="",
                 tlsVerification=True,
                 httpsToHttp=False,
                 recordMode=None,
                 showCmd=False
                 ):
        self._proxyPort = proxyPort
        self._adminPort = adminPort
        self._host = host
        self._modify = modify
        self._middleware = middleware
        self._flags = []
        self._capture = capture
        self._dbpath = dbpath
        self._db = db
        self._simulation = simulation
        self._synthesize = synthesize
        self._verbose = verbose
        self._session = requests.Session()
        self._session.trust_env = False
        self._metrics = metrics
        self._dev = dev
        self._auth = auth
        self._delays = delays
        self._cert = cert
        self._certName = certName
        self._certOrg = certOrg
        self._dest = dest
        self._generateCACert = generateCACert
        self._destination = destination
        self._key = key
        self._tlsVerification = tlsVerification
        self._httpsToHttp = httpsToHttp
        self._recordMode = recordMode
        self._showCmd = showCmd
        self.__enableProxy()

        if self._recordMode == "once":
            self._capture = not os.path.isfile(self._dbpath)

        self.__start()
        self.__addDelaysFromParam()


    def wipe(self):
        """
        Wipe the bolt database.

        Calling this after HoverPy has been instantiated is
        potentially dangerous. This function is mostly used
        internally for unit tests.
        """
        try:
            if os.isfile(self._dbpath):
                os.remove(self._dbpath)
        except OSError:
            pass

    def capture(self):
        """
        Switches hoverfly to capture mode.
        """
        return self.mode("capture")

    def simulate(self):
        """
        Switches hoverfly to simulate mode.

        Please note simulate is the default mode.
        """
        return self.mode("simulate")

    def config(self):
        """
        Returns the hoverfly configuration json.
        """
        return self._session.get(self.__v2() + "/hoverfly").json()

    def simulation(self, data=None):
        """
        Gets / Sets the simulation data.

        If no data is passed in, then this method acts as a getter.
        if data is passed in, then this method acts as a setter.

        Keyword arguments:
        data -- the simulation data you wish to set (default None)
        """
        if data:
            return self._session.put(self.__v2() + "/simulation", data=data)
        else:
            return self._session.get(self.__v2() + "/simulation").json()

    def destination(self, name=""):
        """
        Gets / Sets the destination data.
        """
        if name:
            return self._session.put(
                self.__v2() + "/hoverfly/destination",
                data={"destination": name}).json()
        else:
            return self._session.get(
                self.__v2() + "/hoverfly/destination").json()

    def middleware(self):
        """
        Gets the middleware data.
        """
        return self._session.get(self.__v2() + "/hoverfly/middleware").json()

    def mode(self, mode=None):
        """
        Gets / Sets the mode.

        If no mode is provided, then this method acts as a getter.

        Keyword arguments:
        mode -- this should either be 'capture' or 'simulate' (default None)
        """
        if mode:
            logging.debug("SWITCHING TO %s" % mode)
            url = self.__v2() + "/hoverfly/mode"
            logging.debug(url)
            return self._session.put(
                url, data=json.dumps({"mode": mode})).json()["mode"]
        else:
            return self._session.get(
                self.__v2() + "/hoverfly/mode").json()["mode"]

    def usage(self):
        """
        Gets the usage data.
        """
        return self._session.get(self.__v2() + "/hoverfly/usage").json()

    def metadata(self, delete=False):
        """
        Gets the metadata.
        """
        if delete:
            return self._session.delete(self.__v1() + "/metadata").json()
        else:
            return self._session.get(self.__v1() + "/metadata").json()

    def records(self, data=None):
        """
        Gets / Sets records.
        """
        if data:
            return self._session.post(
                self.__v1() + "/records", data=data).json()
        else:
            return self._session.get(self.__v1() + "/records").json()

    def delays(self, delays=[]):
        """
        Gets / Sets the delays. 
        """
        if delays:
            return self._session.put(
                self.__v1() + "/delays", data=json.dumps(delays)).json()
        else:
            return self._session.get(self.__v1() + "/delays").json()

    def addDelay(self, urlPattern="", delay=0, httpMethod=None):
        """
        Adds delays. 
        """
        print("addDelay is deprecated please use delays instead")
        delay = {"urlPattern": urlPattern, "delay": delay}
        if httpMethod:
            delay["httpMethod"] = httpMethod
        return self.delays(delays={"data": [delay]})

    def httpProxy(self):
        return "http://%s:%i" % (self._host, self._proxyPort)

    def httpsProxy(self):
        if self._httpsToHttp:
            return self.httpProxy()
        else:
            return "https://%s:%i" % (self._host, self._proxyPort)

    def __del__(self):
        if self._process:
            self.__stop()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._process:
            self.__stop()

    def __enter__(self):
        return self

    def __host(self):
        """
        Returns the URL to the admin interface / APIs.
        """
        return "http://%s:%i" % (self._host, self._adminPort)

    def __v1(self):
        """
        Return the URL to the v1 API
        """
        return self.__host() + "/api"

    def __v2(self):
        """
        Return the URL to the v2 API
        """
        return self.__host() + "/api/v2"

    def __enableProxy(self):
        """
        Set the required environment variables to enable the use of hoverfly as a proxy.
        """
        os.environ[
            "HTTP_PROXY"] = self.httpProxy()
        os.environ[
            "HTTPS_PROXY"] = self.httpsProxy()

        os.environ["REQUESTS_CA_BUNDLE"] = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)),
            "cert.pem")

    def __disableProxy(self):
        """
        Clear the environment variables required to enable the use of hoverfly as a proxy.
        """
        del os.environ['HTTP_PROXY']
        del os.environ['HTTPS_PROXY']
        del os.environ['REQUESTS_CA_BUNDLE']

    def __writepid(self, pid):
        """
        HoverFly fails to launch if it's already running on
        the same ports. So we have to keep track of them using
        temp files with the proxy port and admin port, containing
        the processe's PID. 
        """
        import tempfile
        d = tempfile.gettempdir()
        name = os.path.join(d, "hoverpy.%i.%i"%(self._proxyPort, self._adminPort))
        with open(name, 'w') as f:
            f.write(str(pid))
            logging.debug("writing to %s"%name)

    def __rmpid(self):
        """
        Remove the PID file on shutdown, unfortunately
        this may not get called if not given the time to
        shut down.
        """
        import tempfile
        d = tempfile.gettempdir()
        name = os.path.join(d, "hoverpy.%i.%i"%(self._proxyPort, self._adminPort))
        if os.path.exists(name):
            os.unlink(name)
            logging.debug("deleting %s"%name)

    def __kill_if_not_shut_properly(self):
        """
        If the HoverFly process on these given ports
        did not shut down correctly, then kill the pid
        before launching a new instance.
        todo: this will kill existing HoverFly processes
        on those ports indiscriminately
        """
        import tempfile
        d = tempfile.gettempdir()
        name = os.path.join(d, "hoverpy.%i.%i"%(self._proxyPort, self._adminPort))
        if os.path.exists(name):
            logging.debug("pid file exists.. killing it")
            f = open(name, "r")
            pid = int(f.read())
            try:
                import signal
                os.kill(pid, signal.SIGTERM)
                logging.debug("killing %i"%pid)
            except:
                logging.debug("nothing to clean up")
                pass
            finally:
                os.unlink(name)

    def __start(self):
        """
        Start the hoverfly process.

        This function waits until it can make contact
        with the hoverfly API before returning.
        """
        logging.debug("starting %i" % id(self))
        self.__kill_if_not_shut_properly()
        self.FNULL = open(os.devnull, 'w')
        flags = self.__flags()
        cmd = [hoverfly] + flags
        if self._showCmd:
            print(cmd)
        self._process = Popen(
            [hoverfly] +
            flags,
            stdin=self.FNULL,
            stdout=self.FNULL,
            stderr=subprocess.STDOUT)
        start = time.time()
        while time.time() - start < 1:
            try:
                url = "http://%s:%i/api/health" % (self._host, self._adminPort)
                r = self._session.get(url)
                j = r.json()
                up = "message" in j and "healthy" in j["message"]
                if up:
                    logging.debug("has pid %i" % self._process.pid)
                    self.__writepid(self._process.pid)
                    return self._process
                else:
                    time.sleep(1/100.0)
            except:
                # import traceback
                # traceback.print_exc()
                # wait 10 ms before trying again
                time.sleep(1/100.0)
                pass

        logging.error("Could not start hoverfly!")
        raise ValueError("Could not start hoverfly!")

    def __stop(self):
        """
        Stop the hoverfly process.
        """
        if logging:
            logging.debug("stopping")
        self._process.terminate()
        # communicate means we wait until the process
        # was actually terminated, this removes some
        # warnings in python3
        self._process.communicate()
        self._process = None
        self.FNULL.close()
        self.FNULL = None
        self.__disableProxy()
        # del self._session
        # self._session = None
        self.__rmpid()

    def __flags(self):
        """
        Internal method. Turns arguments into flags.
        """
        flags = []
        if self._capture:
            flags.append("-capture")
        if self._dbpath:
            flags += ["-db-path", self._dbpath]
            flags += ["-db", "boltdb"]
        else:
            flags += ["-db", "memory"]
        if self._synthesize:
            assert(self._middleware)
            flags += ["-synthesize"]
        if self._simulation:
            flags += ["-import", self._simulation]
        if self._proxyPort:
            flags += ["-pp", str(self._proxyPort)]
        if self._adminPort:
            flags += ["-ap", str(self._adminPort)]
        if self._modify:
            flags += ["-modify"]
        if self._verbose:
            flags += ["-v"]
        if self._dev:
            flags += ["-dev"]
        if self._metrics:
            flags += ["-metrics"]
        if self._auth:
            flags += ["-auth"]
        if self._middleware:
            flags += ["-middleware", self._middleware]
        if self._cert:
            flags += ["-cert", self._cert]
        if self._certName:
            flags += ["-cert-name", self._certName]
        if self._certOrg:
            flags += ["-cert-org", self._certOrg]
        if self._destination:
            flags += ["-destination", self._destination]
        if self._key:
            flags += ["-key", self._key]
        if self._dest:
            for i in range(len(self._dest)):
                flags += ["-dest", self._dest[i]]
        if self._generateCACert:
            flags += ["-generate-ca-cert"]
        if not self._tlsVerification:
            flags += ["-tls-verification", "false"]

        logging.debug("flags:" + str(flags))
        return flags

    def __addDelaysFromParam(self):
        delaysDoc = []
        for delays in self._delays:
            delay = {"urlPattern": delays[0], "delay": delays[1]}
            if len(delays) == 3:
                delay["httpMethod"] = delays[2]
            delaysDoc.append(delay)
        return self.delays(delays={"data": delaysDoc})

def quick_test():
    hp = HoverPy()
    hp.capture()
    requests.get("http://ip.jsontest.com/ip")
    if "data" in hp.delays().keys():
        print("HOVERPY AND HOVERFLY QUICK TEST SUCCESS!!")

if __name__ == "__main__":
    quick_test()
