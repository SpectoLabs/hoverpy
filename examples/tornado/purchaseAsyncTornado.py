from tornado import gen, web, ioloop, httpclient
from tornado.escape import json_decode, json_encode
import json

class MainHandler(web.RequestHandler):

    def initialize(self):
        self.http_client = httpclient.AsyncHTTPClient()

    @gen.coroutine
    def finditem(self, obj, key):
        if key in obj: raise gen.Return(obj[key])
        for k, v in obj.items():
            if isinstance(v,dict):
                raise gen.Return(_finditem(v, key))

    @gen.coroutine
    def custProd(self):
        product_id = self.get_query_argument("product_id")
        customer_id = self.get_query_argument("customer_id")
        customer, product = yield [
            self.http_client.fetch("http://customers.ioloop.io/?id=%s"%customer_id),
            self.http_client.fetch("http://products.ioloop.io/get/%s"%product_id)
        ]
        raise gen.Return((json_decode(customer.body), json_decode(product.body)))

    @gen.coroutine
    def get(self):
        (customer, product) = yield self.custProd()

        customer_id = yield self.finditem(customer, "id")
        product_id = yield self.finditem(product, "id")

        purchase_data = json_encode({"product_id": product_id, "customer_id": customer_id})
        purchase = yield self.http_client.fetch("http://purchase.ioloop.io", method="POST", body=purchase_data)

        self.write(purchase.body)

from hoverpy import HoverPy
from hoverpy import ext
from tornado.options import define, options, parse_command_line

define("virtualise", default=False, help="Proxy through our Service Virtualisation Server")
define("capture", default=False, help="Capture the requests if True, else simulate them. Requires the virtualise flag.")
define("middleware", default="", help="middleware to use to mutate dependencies.")

def run_server():
    app = web.Application([("/", MainHandler)], debug=True)
    app.listen(8080)
    ioloop.IOLoop.current().start()

parse_command_line()

if options.virtualise:
    ext.tor.configure()
    if options.middleware:
        with HoverPy(modify=True, middleware="python %s" % options.middleware, capture=options.capture) as hp:
            print("starting virtual tornado server with middleware: " + str(options.middleware))
            run_server()
    else:
        with HoverPy(capture=options.capture) as hp:
            # hp.addDelay(urlPattern="customers.ioloop.io", delay=500)
            # hp.addDelay(urlPattern="products.ioloop.io", delay=1000)
            print("starting virtual tornado server, capture: " + str(options.capture))
            run_server()
else:
    print("starting regular tornado server")
    run_server()


