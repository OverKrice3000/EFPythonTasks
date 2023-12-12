import unittest

from main import draw


class TestCorrectness(unittest.TestCase):

    def test_correctness(self):
        self.assertEqual(draw(1), '\n'.join([
            " _ ",
            "|_|"]))
        self.assertEqual(draw(2), '\n'.join([
            " _ _ ",
            "|  _|",
            "|_|_|"]))
        self.assertEqual(draw(3), '\n'.join([
            " _ _ _ ",
            "|    _|",
            "|  _|_|",
            "| |  _|",
            "|_|_|_|"]))
        self.assertEqual(draw(4), '\n'.join([
            " _ _ _ _ ",
            "|      _|",
            "|    _|_|",
            "|   |  _|",
            "|  _|_|_|",
            "| |    _|",
            "| |  _|_|",
            "| | |  _|",
            "|_|_|_|_|"]))