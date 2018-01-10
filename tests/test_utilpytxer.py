import handling_test
from upxer import UtilPytxer
import unittest

class TestUtilPytxer(unittest.TestCase):

def test_has_some_number(self):

    string_with_number = "An0th3r 5tr1ng"

    self.assertTrue(has_some_number(string_with_number))

def another_test_has_some_number(self):

    string_without_number = "Another String"

    self.assertFalse(has_some_number(string_without_number))



if __name__ == '__main__':
    unittest.main()
