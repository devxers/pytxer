import unittest
import handling_test
from upxer import StringPytxer


class TestStringPytxer(unittest.TestCase):
    def test_capitalize_first_letter(self):

        string_test_first_letter = "diego"
        string_result_first_letter = "Diego"

        self.assertEqual(string_result_first_letter,
                         StringPytxer.capitalize(string_test_first_letter))


if __name__ == '__main__':
    unittest.main()
