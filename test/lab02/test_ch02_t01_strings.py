import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content = execfile("lab02/ch02_t01_strings.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['brian'], str)


if __name__ == '__main__':
    unittest.main()
