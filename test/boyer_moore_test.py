import unittest

from src.boyer_moore import bad_characters, boyer_moore


class MyTestCase(unittest.TestCase):
    def test_boyer_moore(self):
        string = "Hello Victoria Secret Hello Victoria Secret"
        pattern = "Victoria"
        bad_char_map = bad_characters(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, [6, 28])

    def test_if_no_result(self):
        string = "vybujdsnmivkrvn"
        pattern = "fje"
        bad_char_map = bad_characters(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, [])

    def test_if_empty(self):
        string = ""
        pattern = ""
        bad_char_map = bad_characters(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, "Put some letters")

    def test_if_pattern_empty(self):
        string = "tvybhjkm"
        pattern = ""
        bad_char_map = bad_characters(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, "Put some letters")

    def test_if_string_empty(self):
        string = ""
        pattern = "gvhb"
        bad_char_map = bad_characters(pattern)
        result = boyer_moore(string, pattern, bad_char_map)
        self.assertEqual(result, "Put some letters")


if __name__ == '__main__':
    unittest.main()
