# import hoverpy's main class: HoverPy
from hoverpy import HoverPy

# create our HoverPy object in capture mode
with HoverPy(capture=True) as hp:

    # import urllib3 for http, and build a proxy manager
    import urllib3
    http = urllib3.proxy_from_url("http://localhost:8500/")

    # print the json from our get request. Hoverpy acted as a proxy: it made
    # the request on our behalf, captured it, and returned it to us.
    print(http.request('GET', 'http://ip.jsontest.com/myip').data)

    # switch HoverPy to simulate mode. HoverPy no longer acts as a proxy; all
    # it does from now on is replay the captured data.
    hp.simulate()

    # print the json from our get request. This time the data comes from the
    # store.
    print(http.request('GET', 'http://ip.jsontest.com/myip').data)
