#!/usr/bin/python

import tornado.ioloop
import tornado.web
import requests
import tornado.web
import tornado.gen
p = None
import random
import string


def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def session():
    session = requests.Session()
    session.trust_env = False
    return session


def start():
    import subprocess
    from subprocess import Popen, PIPE
    import os
    import time
    global p
    FNULL = open(os.devnull, 'w')
    p = Popen(
        ["python", __file__],
        stdout=FNULL,
        stderr=subprocess.STDOUT)

    start = time.time()

    while time.time() - start < 1:
        try:
            r = session().get("http://localhost:8000/")
            if r.text == "hoverpy unit test server":
                return
            else:
                time.sleep(1/100.0)
        except:
            # wait 10 ms before trying again
            time.sleep(1/100.0)
            pass

    raise ValueError('Could not start hoverpy unit test server')


def stop():
    p.kill()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("hoverpy unit test server")


class IPHandler(tornado.web.RequestHandler):

    def get(self):
        import socket
        ip = socket.gethostbyname(socket.gethostname())
        self.write({"ip": ip})


class EchoURIHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, args):
        self.write(self.request.uri)
        self.finish()


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/ip", IPHandler),
        (r"/echouri(.*)", EchoURIHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
