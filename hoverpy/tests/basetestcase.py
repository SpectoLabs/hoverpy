import unittest
import os


def wipe():
    try:
        os.remove("./requests.db")
    except OSError:
        pass


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        wipe()

    def tearDown(self):
        wipe()
