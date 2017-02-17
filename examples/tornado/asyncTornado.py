from tornado import gen, web, ioloop, httpclient
import json

class MainHandler(web.RequestHandler):

    @gen.coroutine
    def get(self):
        http_client = httpclient.AsyncHTTPClient()
        time, ip, headers = yield [http_client.fetch("http://time.ioloop.io?format=json"),
                                   http_client.fetch("http://ip.ioloop.io?format=json"),
                                   http_client.fetch("http://headers.ioloop.io?format=json")]
        self.write({
            "time": json.loads(time.body),
            "ip": json.loads(ip.body),
            "headers": json.loads(headers.body)
        })


from hoverpy import HoverPy, ext
with HoverPy(capture=True):
    ext.tor.configure()
    app = web.Application([("/", MainHandler)])
    app.listen(8080)
    ioloop.IOLoop.current().start()