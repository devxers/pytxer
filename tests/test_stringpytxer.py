import unittest
import handling_test
from upxer import StringPytxer


class TestStringPytxer(unittest.TestCase):
    def test_capitalize_first_letter(self):
        self.assertEqual("Diego", StringPytxer.capitalize("diego"))

    def test_list_to_string(self):
        test_list_of_strings = ["Garcias",
                                "Kevin",
                                "Days"]

        self.assertEqual("Garcias Kevin Days",
                         StringPytxer.list_to_string(test_list_of_strings))

    def test_capitalize_name(self):

        self.assertEqual("Lady Richy June",
                         StringPytxer.capitalize_name("lady richy june"))

    def test_capitalize_name_with_upper_lower_mix(self):

        self.assertEqual("Lady Richy June",
                         StringPytxer.capitalize_name("laDy riChy JunE"))

    def test_abbreviate_name(self):

        self.assertEqual("Kevin S. G.",
                         StringPytxer.abbreviate_name("Kevin smith garcias"))

    def test_abbreviate_name_with_all_lowercase(self):

        self.assertEqual("Lilian D. S.",
                         StringPytxer.abbreviate_name("lilian days sia"))


if __name__ == '__main__':
    unittest.main()
