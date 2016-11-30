# In this example, we'll take a look at writing unit tests that use HoverPy.
# Please note that doing so means that you, as a developer, can be entirely sure
# that you are testing your code against known data. This makes you hermetic to
# to issues with third party APIs. Let's begin by importing hoverpy.

import hoverpy

# Instead of inheriting off `unittest.TestCase` let's inherit off
# `hoverpy.TestCase`
class TestRTD(hoverpy.TestCase):

# if our test, we'll once again download a load of readthedocs pages
    def test_rtd_links(self):
        import requests
        limit = 50
        sites = requests.get("http://readthedocs.org/api/v1/project/?limit=%d&offset=0&format=json" % limit)
        objects = sites.json()['objects']
        links = ["http://readthedocs.org" + x['resource_uri'] for x in objects]
        self.assertTrue(len(links) == limit)
        for link in links:
            response = requests.get(link)
            print(link, response)
            self.assertTrue(response.status_code == 200)

# let's run our hoverpy testcase if the script is invoked directly
if __name__ == '__main__':
    import unittest
    unittest.main()


# <hr> Now the correct way of launching this script the first time is: <br><br>
# `$ env HOVERPY_CAPTURE=true python examples/unittesting/unittesting.py`<br><br>
# which sets HoverPy in capture mode, and creates our all important `requests.db`.
# This process may take around 10 seconds depending on your internet speed.
# Now when we're rerun our unit tests, we'll always be running them against the
# data we captured.<br><br>
# `$ python examples/unittesting/unittesting.py`<br><br>
# This time we are done in around 100ms.