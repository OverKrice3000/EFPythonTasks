import unittest

from main import max_sequence


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
            self.assertEqual(max_sequence([]), 0)
            self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
            self.assertEqual(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
            self.assertEqual(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)