import tornado
import tornado.ioloop
import tornado.gen
import tornado.httpclient
import pycurl
from tornado.testing import AsyncTestCase
from tornado.testing import AsyncHTTPTestCase
import unittest
from hoverpy import HoverPy


def prepare_curl_socks5(curl):
    curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)

hp = HoverPy(capture=False)


@tornado.gen.coroutine
def main():
    tornado.httpclient.AsyncHTTPClient.configure(
        "tornado.curl_httpclient.CurlAsyncHTTPClient")

    http_client = tornado.httpclient.AsyncHTTPClient()
    http_request = tornado.httpclient.HTTPRequest(
        "http://jsonip.com",
        prepare_curl_callback=prepare_curl_socks5,
        proxy_host="localhost",
        proxy_port=8500
    )
    response = yield http_client.fetch(http_request)

    print response.body

import hello


class TestHelloApp(AsyncHTTPTestCase):

    def get_app(self):
        return hello.make_app()

    @tornado.testing.gen_test
    def test_homepage(self):
        # set CurlAsyncHTTPClient the default AsyncHTTPClient
        tornado.httpclient.AsyncHTTPClient.configure(
            "tornado.curl_httpclient.CurlAsyncHTTPClient")

        port = self.get_http_port()

        url = "http://jsonip.com"
        # url = "http://localhost:%i/echouri/0" % (port)

        http_client = tornado.httpclient.AsyncHTTPClient()
        http_request = tornado.httpclient.HTTPRequest(
            url,
            prepare_curl_callback=prepare_curl_socks5,
            proxy_host="localhost",
            proxy_port=8500
        )
        response = yield http_client.fetch(http_request)

        print response.body


if __name__ == '__main__':
    tornado.ioloop.IOLoop.instance().run_sync(main)
    unittest.main()
