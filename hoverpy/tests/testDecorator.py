import requests
import unittest
import logging
import hoverpy


class TestDecorators(unittest.TestCase):

    def testDecorators(self):
        @hoverpy.capture
        def testCapture():
            logging.debug("test_capture")
            r = requests.get("http://ip.jsontest.com/myip")
            self.assertIn('ip', r.json())

        @hoverpy.simulate
        def testSimulate():
            logging.debug("test_simulate")
            r = requests.get("http://ip.jsontest.com/myip")
            self.assertIn('ip', r.json())

        testCapture()
        testSimulate()

if __name__ == '__main__':
    unittest.main()
