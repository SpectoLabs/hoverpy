try:
  from . import tor
except:
  pass

class tornado(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        tor.configure()
        return self.f(*args)

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
