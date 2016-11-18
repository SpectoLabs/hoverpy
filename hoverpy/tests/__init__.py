import unittest

def get_suite():
    "Return a unittest.TestSuite."
    import hoverpy.tests.test_virtualisation
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(hoverpy.tests.test_virtualisation)
    return loader.discover("./")
