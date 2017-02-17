import unittest
from hoverpy import HoverPy
import logging


class TestTemplates(unittest.TestCase):

    def testTemplate(self):
        logging.debug("testTemplates")
        with HoverPy() as hoverpy:
            with open(
                    "hoverpy/tests/templates/template.json",
                    "r") as f:
                data = f.read()
                hoverpy.records(data=data)
                records = hoverpy.records()
                self.assertTrue("data" in records)
                self.assertTrue(isinstance(records["data"], list))

if __name__ == '__main__':
    unittest.main()
