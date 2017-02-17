from hoverpy import capture, simulate, lib
import urllib2

@capture("urllib2.db")
def captured_get():
    print(urllib2.urlopen("http://time.ioloop.io").read())

@simulate("urllib2.db")
def simulated_get():
    print(urllib2.urlopen("http://time.ioloop.io").read())

captured_get()
simulated_get()