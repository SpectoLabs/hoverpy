try:
  from . import tor
except:
  pass

class tornado(object):

    def __init__(self, proxyPort=8500, proxyHost="localhost", **kwargs):
        self.port = proxyPort
        self.host = proxyHost

    def __call__(self, f):
        def wrapped_f(*args):
            tor.configure(proxyPort=self.port, proxyHost=self.host)
            return f(*args)
        return wrapped_f

class twisted(object):

    @staticmethod
    def TCP4ClientEndpoint():
        from twisted.internet.endpoints import TCP4ClientEndpoint
        from twisted.internet import reactor
        return TCP4ClientEndpoint(reactor, "localhost", 8500)

class urllib3(object):

    @staticmethod
    def ProxyManager():
        import urllib3
        proxy = urllib3.ProxyManager('http://localhost:8500/')
        return proxy
