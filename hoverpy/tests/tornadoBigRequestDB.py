import unittest
import requests
import hoverpy
import server
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado.testing import AsyncTestCase
from tornado.testing import AsyncHTTPTestCase
import tornado
import pycurl
import time


def prepare_curl_socks5(curl):
    curl.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)


hoverpy.wipe()

n = 100


class TestBigRequestsDBTornado(AsyncTestCase):

    def setUp(self):
        server.start()
        AsyncTestCase.setUp(self)

    @tornado.testing.gen_test(timeout=1000)
    def test_http_fetch(self):

        tornado.httpclient.AsyncHTTPClient.configure(
            "tornado.curl_httpclient.CurlAsyncHTTPClient")

        http_client = tornado.httpclient.AsyncHTTPClient()

        with hoverpy.HoverPy(capture=True) as hp:

            start = time.time()
            for i in range(n):
                p = "/echouri/" + str(i)
                http_request = tornado.httpclient.HTTPRequest(
                    "http://localhost:8000" + p,
                    prepare_curl_callback=prepare_curl_socks5,
                    proxy_host="localhost",
                    proxy_port=8500
                )
                response = yield http_client.fetch(http_request)
                self.assertIn(p, response.body)

            print("generating data took %f" % (time.time() - start))

            start = time.time()

            server.stop()

        start = time.time()
        with hoverpy.HoverPy() as hp:

            for i in range(n):
                p = "/echouri/" + str(i)
                http_request = tornado.httpclient.HTTPRequest(
                    "http://localhost:8000" + p,
                    prepare_curl_callback=prepare_curl_socks5,
                    proxy_host="localhost",
                    proxy_port=8500
                )
                response = yield http_client.fetch(http_request)
                self.assertIn(p, response.body)

            print("re-reading data took %f" % (time.time() - start))

            simulation = hp.simulation()

            with open("simulation.json", "w") as f:
                import json
                # f.write(json.dumps(simulation, sort_keys=True,
                #                    indent=4, separators=(',', ': ')))
                f.write(json.dumps(simulation))

        hoverpy.wipe()

        # start = time.time()
        # with hoverpy.HoverPy(simulation="./simulation.json") as hp:

        #     for i in range(n):
        #         p = "/echouri/" + str(i)
        #         http_request = tornado.httpclient.HTTPRequest(
        #             "http://localhost:8000" + p,
        #             prepare_curl_callback=prepare_curl_socks5,
        #             proxy_host="localhost",
        #             proxy_port=8500
        #         )
        #         response = yield http_client.fetch(http_request)
        #         # self.assertIn(p, response.body)

        #     print("re-reading data in json took %f" % (time.time() - start))

        # hoverpy.wipe()


if __name__ == '__main__':
    unittest.main()
unittest.main()
