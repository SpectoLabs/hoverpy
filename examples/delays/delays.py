# Demonstrates how to add latency to calls, based on host, and method type.
# import hoverpy's main class: HoverPy
from hoverpy import HoverPy

# import requests and random for http and testing
import requests
import random

# create our HoverPy object in capture mode
with HoverPy(capture=True) as hp:

    # this function either generates a echo server url, or a md5 url
    # it is seeded so that we get the exact same requests on capture as we do
    # on simulate

    def getServiceData():
        for i in range(10):
            random.seed(i)
            print(
                requests.get(
                    random.choice(
                        [
                            "http://echo.jsontest.com/i/%i" %
                            i,
                            "http://md5.jsontest.com/?text=%i" %
                            i])).json())

    # make the requests to the desired host dependencies
    print("capturing responses from echo server\n")
    getServiceData()

    # There are two ways to add delays. One is to call the delays method
    # with the desired delay rules passed in as a json document
    print(hp.delays({"data": [
        {
            "urlPattern": "md5.jsontest.com",
            "delay": 1000
        }
    ]
    }
    ))

    # the other more pythonic way is to call addDelay(...)
    print(hp.addDelay(urlPattern="echo.jsontest.com", delay=3000))

    # now let's switch over to simulate mode
    print(hp.simulate())

    # make the requests. This time HoverFly adds the simulated delays.
    # these requests would normally be run asynchronously, and we could deal
    # gracefully with the dependency taking too long to respond
    print("\nreplaying delayed responses from echo server\n")
    getServiceData()
