from tornado import httpclient
from tornado.curl_httpclient import CurlAsyncHTTPClient


def configure(proxyPort=8500, proxyHost="localhost"):
  defaults = dict(proxy_host=proxyHost, proxy_port=proxyPort)
  httpclient.AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient', defaults=defaults)


