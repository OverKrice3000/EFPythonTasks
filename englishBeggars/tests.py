import unittest

from main import beggars


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(beggars([1, 2, 3, 4, 5], 1), [15])
        self.assertEqual(beggars([1, 2, 3, 4, 5], 2), [9, 6])
        self.assertEqual(beggars([1, 2, 3, 4, 5], 3), [5, 7, 3])
        self.assertEqual(beggars([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5, 0])
        self.assertEqual(beggars([1, 2, 3, 4, 5], 0), [])