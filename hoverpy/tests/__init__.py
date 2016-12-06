import unittest


def get_suite():
    "Return a unittest.TestSuite."
    loader = unittest.TestLoader()
    return loader.discover("./")
