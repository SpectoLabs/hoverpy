from twisted.python.log import err
from twisted.web.client import ProxyAgent
from twisted.internet import reactor

def display(response):
    print "Received response"
    print response

from hoverpy import capture, simulate, lib

@simulate("twisted.db")
def main():
    endpoint = lib.twisted.TCP4ClientEndpoint()
    agent = ProxyAgent(endpoint)
    d = agent.request("GET", "http://echo.ioloop.io/a/b?format=json")
    d.addCallbacks(display, err)
    d.addCallback(lambda ignored: reactor.stop())
    reactor.run()

main()