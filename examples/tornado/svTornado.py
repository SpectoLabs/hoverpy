from tornado import gen, web, ioloop, httpclient

class MainHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = httpclient.AsyncHTTPClient()
        time = yield http_client.fetch("http://time.ioloop.io?format=json")
        self.write(time.body)

from hoverpy import capture, lib

@lib.tornado
@capture(dbpath="tornado.db")
def start():
    app = web.Application([("/", MainHandler)])
    app.listen(8080)
    ioloop.IOLoop.current().start()

start()