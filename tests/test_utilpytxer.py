import handling_test
from upxer import UtilPytxer
import unittest


class TestUtilPytxer(unittest.TestCase):

    def test_has_some_number(self):

        self.assertTrue(UtilPytxer.has_some_number("An0th3r 5tr1ng"))

    def another_test_has_some_number(self):

        self.assertFalse(UtilPytxer.has_some_number("Another String"))

    def test_has_some_letter(self):

        self.assertTrue(UtilPytxer.has_some_letter("5884899A88B"))

    def another_test_has_some_letter(self):

        self.assertFalse(UtilPytxer.has_some_letter("854494187"))

    def test_has_some_letter_whit_expected_true(self):

        self.assertTrue(UtilPytxer.has_some_letter("4A 6A A3 E8 A5S"))

    def test_is_valid_email(self):

        self.assertTrue(UtilPytxer.is_valid_email(
            "somename125_8!@somedomain.com"))

    def test_is_valid_email_expected_false(self):

        self.assertFalse(UtilPytxer.is_valid_email("someelse@domain"))


if __name__ == '__main__':
    unittest.main()
