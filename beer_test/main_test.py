import unittest

from beer_algo.main import min_beer_types, read_input


class TestMinBeerTypesFunction(unittest.TestCase):
    def test_scenario_1(self):
        input_filename = "input_1.txt"
        N, B, preferences = read_input(input_filename)

        result = min_beer_types(N, B, preferences)

        self.assertEqual(result, 2)

    def test_scenario_2(self):
        input_filename = "input_2.txt"
        N, B, preferences = read_input(input_filename)

        result = min_beer_types(N, B, preferences)

        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
