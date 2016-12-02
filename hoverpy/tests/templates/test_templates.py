import unittest
from hoverpy import HoverPy
import logging
from .. import basetestcase


class TestTemplates(basetestcase.BaseTestCase):

    def testTemplate(self):
        logging.debug("testTemplates")
        with HoverPy() as hoverpy:
            data = open(
                "hoverpy/tests/templates/template.json",
                "r").read()
            hoverpy.records(data=data)
            records = hoverpy.records()
            self.assertTrue("data" in records)
            self.assertTrue(isinstance(records["data"], list))

if __name__ == '__main__':
    unittest.main()
