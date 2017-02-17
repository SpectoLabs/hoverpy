from tornado import httpclient
from tornado.curl_httpclient import CurlAsyncHTTPClient

class VirtualAsyncHTTPClient(CurlAsyncHTTPClient):
    
    def _curl_setup_request(self, curl, request, buffer, headers):
        request.proxy_host = "http://127.0.0.1"
        request.proxy_port = 8500
        super(VirtualAsyncHTTPClient, self)._curl_setup_request(curl, request, buffer, headers)


def configure():
  httpclient.AsyncHTTPClient.configure(VirtualAsyncHTTPClient)
