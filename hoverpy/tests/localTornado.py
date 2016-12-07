import unittest
import server


class LocalTornado(unittest.TestCase):

    def setUp(self):
        server.start()

    def tearDown(self):
        server.stop()
