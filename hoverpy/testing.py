from hoverpy import HoverPy
import unittest
import os


class TestCase(unittest.TestCase):

    """
    TestCase, which can be used like unittest.TestCase
    """

    def setUp(self):
        """
        Set up each test case by initializing HoverPy
        """

        enabled = os.environ.get(
            "HOVERPY_ENABLED",
            "true").lower() in [
            "true",
            "1",
            "on"]
        if enabled:
            capture = os.environ.get(
                "HOVERPY_CAPTURE",
                "").lower() in [
                "true",
                "1",
                "on"]
            self.hp = HoverPy(capture=capture)

    def tearDown(self):
        del self.hp
