import unittest

from main import solve


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(solve("tft", "^&"), 2)
        self.assertEqual(solve("ttftff", "|&^&&"), 16)
        self.assertEqual(solve("ttftfftf", "|&^&&||"), 339)
        self.assertEqual(solve("ttftfftft", "|&^&&||^"), 851)
        self.assertEqual(solve("ttftfftftf", "|&^&&||^&"), 2434)