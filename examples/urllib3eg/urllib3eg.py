from hoverpy import capture, simulate, lib

@capture("urllib3.db")
def captured_get():
    http = lib.urllib3.ProxyManager()
    print(http.request('GET', 'http://time.ioloop.io').data)

@simulate("urllib3.db")
def simulated_get():
    http = lib.urllib3.ProxyManager()
    print(http.request('GET', 'http://time.ioloop.io').data)

captured_get()
simulated_get()