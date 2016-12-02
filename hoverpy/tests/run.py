# RUNME as 'python -m hoverpy.tests.run'
import unittest
import hoverpy.tests
import doctest


def runTests():
    "Run all of the tests when run as a module with -m."
    suite = hoverpy.tests.get_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


def runDocTests():
    finder = doctest.DocTestFinder(exclude_empty=False)
    suite = doctest.DocTestSuite(test_finder=finder)


def main():
    runTests()

if __name__ == '__main__':
    main()
