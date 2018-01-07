import unittest
import handling_test
from upxer import StringPytxer


class TestStringPytxer(unittest.TestCase):
    def test_capitalize_first_letter(self):

        string_test_first_letter = "diego"
        string_result_first_letter = "Diego"

        self.assertEqual(string_result_first_letter,
                         StringPytxer.capitalize(string_test_first_letter))

    def test_capitalize_name(self):

        string_test_capitalize_name = "lady richy june"
        result_capitalize_name = "Lady Richy June"

        self.assertEqual(result_capitalize_name,
                         StringPytxer.capitalize_name(string_test_capitalize_name))

    def test_capitalize_name_with_upper_lower_mix():

        string_test_capitalize_name = "laDy riChy JunE"
        result_capitalize_name = "Lady Richy June"

        self.assertEqual(result_capitalize_name,
                         StringPytxer.capitalize_name(string_test_capitalize_name))


if __name__ == '__main__':
    unittest.main()
