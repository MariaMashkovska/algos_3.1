import unittest

from src.boyer_moore import shift_table_building, boyer_moore


class MyTestCase(unittest.TestCase):
    def test_boyer_moore(self):
        string = "Hello Victoria Secret Hello Victoria Secret"
        pattern = "Victoria"
        bad_char_map = shift_table_building(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, [6, 28])

    def test_if_no_result(self):
        string = "vybujdsnmivkrvn"
        pattern = "fje"
        bad_char_map = shift_table_building(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, [])

    def test_if_empty(self):
        string = ""
        pattern = ""
        bad_char_map = shift_table_building(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, "Put some letters")

    def test_if_pattern_empty(self):
        string = "tvybhjkm"
        pattern = ""
        bad_char_map = shift_table_building(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, "Put some letters")

    def test_if_string_empty(self):
        string = ""
        pattern = "gvhb"
        bad_char_map = shift_table_building(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, "Put some letters")

    def test_is_one(self):
        pattern = "krokodyl"
        res = shift_table_building(pattern)
        self.assertEqual(res, {100: 5, 107: 3, 108: 7, 111: 4, 114: 1, 121: 6})


if __name__ == "__main__":
    unittest.main()
