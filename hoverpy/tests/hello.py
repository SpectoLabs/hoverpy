import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("hoverpy unit test server")


class IPHandler(tornado.web.RequestHandler):

    def get(self):
        import socket
        ip = socket.gethostbyname(socket.gethostname())
        self.write({"ip": ip})


class EchoURIHandler(tornado.web.RequestHandler):

    def get(self, args):
        self.write(self.request.uri)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ip", IPHandler),
        (r"/echouri(.*)", EchoURIHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
