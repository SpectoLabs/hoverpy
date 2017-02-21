from tornado import httpclient, ioloop

config = {
    'proxy_host': 'localhost',
    'proxy_port': 8500
}

httpclient.AsyncHTTPClient.configure(
    "tornado.curl_httpclient.CurlAsyncHTTPClient")

def handle_request(response):
    if response.error:
        print("Error:", response.error)
    else:
        print(response.body)
    ioloop.IOLoop.instance().stop()

http_client = httpclient.AsyncHTTPClient()
http_client.fetch("http://twitter.com/",
    handle_request, **config)
ioloop.IOLoop.instance().start()