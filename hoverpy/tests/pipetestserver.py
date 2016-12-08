# -*- coding: utf-8 -*-
"""\
==============
pipetestserver
==============

This recipe describes how you can create / activate and kill a temporary HTTP
server with a WSGI app to provide unittest resources to a client software,
that's the target of your application.

For our demo, we create a stupid wsgi app that returns the double of the value
provided in a simple JSON structure.

{"value": 5} -> {"value": 10}
{"value": "ta"} -> {"value": "tata"}
{"value": {}} -> {"error": "TypeError", "traceback": "..."}

Run this module with either::

  $ python testserver.py
  $ python -m unittest discover -v

Note that this will work only on an Unix box (use of select.select on a pipe).
This code works on Python 2.6 or 2.7 and needs some changes for Python 3.x
"""

import httplib
import json
import os
import select
import StringIO
import threading
import traceback
import unittest
import urllib2
import wsgiref.simple_server

# APPLICATION
# ===========
# This part is a portion of your application sw that includes an HTTP client

ENDPOINT = "http://somehost.mydomain.com"


def proxiedClient(value, endpoint=ENDPOINT):
    proxy = urllib2.ProxyHandler({'http': 'localhost:8500'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    payload = json.dumps({'value': value})
    headers = {'Content-Type': 'application/json'}
    request = urllib2.Request(endpoint, payload, headers)
    payload = urllib2.urlopen(request).read()
    result = json.loads(payload)
    if 'value' in result:
        return result['value']
    else:
        return result  # dict with 'error' and 'traceback' keys


def client(value, endpoint=ENDPOINT):
    payload = json.dumps({'value': value})
    headers = {'Content-Type': 'application/json'}
    request = urllib2.Request(endpoint, payload, headers)
    payload = urllib2.urlopen(request).read()
    result = json.loads(payload)
    if 'value' in result:
        return result['value']
    else:
        return result  # dict with 'error' and 'traceback' keys


# RESSOURCES
# ==========
# This part sits tipycally in a tests/resources.py module
# Make an "application" that suits your client and mocks a real web service

def application(environ, start_response):
    """The WSGI application that mocks a real server
    """
    def make_status(value):
        """HTTP status (int) -> WSGI response suitable status
        """
        return "{0} {1}".format(value, httplib.responses[value])

    headers = [('Content-Type', 'application/json')]
    try:
        if environ.get('REQUEST_METHOD') != 'POST':
            start_response(make_status(httplib.METHOD_NOT_ALLOWED, headers))
            return ["Seul le mode POST est admis"]
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        request_body = environ['wsgi.input'].read(request_body_size)
        request_dict = json.loads(request_body)
        value = request_dict[u'value']
        result = 2 * value
        response_body = json.dumps({'value': result})
        status = httplib.OK

    except Exception as exc:
        tb_stream = StringIO.StringIO()
        traceback.print_exc(file=tb_stream)
        response = {
            'exception': exc.__class__.__name__,
            'traceback': tb_stream.getvalue()
        }
        response_body = json.dumps(response)
        status = httplib.OK

    headers.append(('Content-Length', str(len(response_body))))
    start_response(make_status(status), headers)
    return [response_body]

# But you can copy this class as-is in your tests/resources.py module.


class ThreadedServerControl(object):

    """Will provide a temporary test server in another thread for your
    application.

    :param app: A wsgi application
    :param host: Listening hostname or IP
    :param port: Listening port preferably >= 1024 unless you're root
    """
    __stop_marker = 'stop'

    def __init__(self, app, host='localhost', port=8000):
        self.app = app
        self.host = host
        self.port = port

        # Communication pipe with the thread
        self.stop_read, self.stop_write = os.pipe()
        self.started = False
        return

    def __run(self):
        httpd = wsgiref.simple_server.make_server(self.host, self.port,
                                                  self.app)

        # We don't want logs in the console
        log_request = httpd.RequestHandlerClass.log_request
        no_logging = lambda *args, **kwargs: None
        httpd.RequestHandlerClass.log_request = no_logging

        # Notify / unlock self.start()
        self.ready.set()
        while True:
            ready, dummy, dummy = select.select(
                [httpd, self.stop_read], [self.stop_write], []
            )
            # HTTP client request detected ?
            if httpd in ready:
                httpd.handle_request()

            # self.stop() synch called ?
            if self.stop_read in ready:
                os.read(self.stop_read, len(self.__stop_marker))
                # Re-enable console logging and exit
                httpd.RequestHandlerClass.log_request = log_request
                break

    def start(self):
        """Launches the server in a thread
        """
        # Bounce protection
        if self.started:
            return

        # Threaded server and synch setup
        self.ready = threading.Event()
        self.server_thread = threading.Thread(target=self.__run)
        self.server_thread.start()

        # Wait server readyness (if a client runs before -> raise URLError)
        self.ready.wait()
        self.started = True
        return

    def stop(self):
        """Stops and kills the server and thread
        """
        # Bounce protection
        if not self.started:
            return

        # Notify thread's suicide
        os.write(self.stop_write, self.__stop_marker)

        # Cleanup after thread's suicide
        self.server_thread.join()
        os.close(self.stop_write)
        os.close(self.stop_read)
        self.started = False
        import time
        time.sleep(0.01)
        return


# TESTS
# =====
# The usual tests suite in a tests/test_somemodule.py module. Look how we
# start and stop the server respectively in setUpClass and tearDownClass


class ClientTest(object):

    """Common mixin test case
    """
    endpoint = 'http://localhost:8000/'  # Our tests server

    def test_int(self):
        """Integer * 2 -> OK
        """
        result = client(2, endpoint=self.endpoint)
        self.assertEqual(result, 4)
        return

    def test_str(self):
        """String * 2 -> OK
        """
        result = client("co", endpoint=self.endpoint)
        self.assertEqual(result, "coco")
        return

    def test_err(self):
        """Dict * 2 -> TypeError (server)
        """
        result = client({}, endpoint=self.endpoint)
        self.assertTrue('exception' in result)
        self.assertEqual(result['exception'], 'TypeError')
        self.assertTrue('traceback' in result)
        return


class SetUpClassTest(unittest.TestCase, ClientTest):

    """Server settings through setUpClass / tearDownClass
    """
    @classmethod
    def setUpClass(cls):
        # Create and starts the server
        cls.server = ThreadedServerControl(application)
        cls.server.start()
        return

    @classmethod
    def tearDownClass(cls):
        # Stop and delete the server
        cls.server.stop()
        return


class SetUpTest(unittest.TestCase, ClientTest):

    """Server settings through setUp / tearDown
    """

    def setUp(self):
        # Create and starts the server
        self.server = ThreadedServerControl(application)
        self.server.start()
        return

    def tearDown(self):
        # Stop and delete the server
        self.server.stop()
        return


class SetUpTest(unittest.TestCase, ClientTest):

    """Server settings through setUp / tearDown
    """

    def setUp(self):
        # Create and starts the server
        self.server = ThreadedServerControl(application)
        self.server.start()
        return

    def tearDown(self):
        # Stop and delete the server
        self.server.stop()
        return


def test_suite():
    suite = unittest.TestSuite()
    tests = [unittest.makeSuite(SetUpTest)]
    if hasattr(unittest, 'skipIf'):
        # New style unittest oy unittest2
        tests += [unittest.makeSuite(SetUpClassTest)]
    suite.addTests(tests)
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
