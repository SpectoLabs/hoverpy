# RUNME as 'python -m hoverpy.tests.run'
import unittest
import hoverpy.tests

def main():
    "Run all of the tests when run as a module with -m."
    suite = hoverpy.tests.get_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()