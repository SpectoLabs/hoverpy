import unittest
import requests
from hoverpy import capture

class TestTime(unittest.TestCase):

    @capture("test_time.db", recordMode="once")
    def test_time(self):
        time = requests.get("http://time.jsontest.com")
        self.assertTrue("time", time.json())

if __name__ == '__main__':
    unittest.main()
