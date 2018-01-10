import handling_test
from upxer import UtilPytxer
import unittest


class TestUtilPytxer(unittest.TestCase):


def test_has_some_number(self):

    string_with_number = "An0th3r 5tr1ng"

    self.assertTrue(UtilPytxer.has_some_number(string_with_number))


def another_test_has_some_number(self):

    string_without_number = "Another String"

    self.assertFalse(UtilPytxer.has_some_number(string_without_number))


def test_has_some_letter(self):

    string_with_letters = "5884899A88B"

    self.assertTrue(UtilPytxer.has_some_letter(string_with_letters))


def another_test_has_some_letter(self):

    string_without_letters = "854494187"

    self.assertFalse(UtilPytxer.has_some_letter(string_without_letters))


def test_has_some_letter_whit_expected_true(self):

    string_with_letters = "4A 6A A3 E8 A5S"

    self.assertTrue(UtilPytxer.has_some_letter(string_with_letters))


def test_is_valid_email(self):

    valid_email = "somename125_8!@somedomain.com"

    self.assertTrue(UtilPytxer.is_valid_email(valid_email))


def test_is_valid_email_expected_false(self):

    unvalid_email = "someelse@domain"

    self.assertFalse(UtilPytxer.is_valid_email(unvalid_email))


if __name__ == '__main__':
    unittest.main()
