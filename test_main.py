import unittest

from main import Node, sum_of_depths


class TestSumOfDepth(unittest.TestCase):

    def test_sum_of_depths(self):
        root = Node(3)
        root.left = Node(9)
        root.right = Node(20)
        result = sum_of_depths(root)
        self.assertEqual(result, 2)

    def test_if_single_root(self):
        root = Node(3)
        result = sum_of_depths(root)
        self.assertEqual(result, 0)

    def test_if_empty(self):
        root = None
        result = sum_of_depths(root)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
