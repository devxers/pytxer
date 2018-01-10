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

def test_has_some_letter(self):

    string_with_letters = "5884899A88B"

    self.assertTrue(has_some_letter(string_with_letters))

def another_test_has_some_letter(self):

    string_without_letters = "854494187"

    self.assertFalse(has_some_letter(string_without_letters))

def test_has_some_letter_whit_expected_true(self):

    string_with_letters = "4A 6A A3 E8 A5S"

    self.assertTrue(has_some_letter(string_with_letters))


if __name__ == '__main__':
    unittest.main()
