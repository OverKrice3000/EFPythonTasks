import unittest

from main import HighScoreTable


class TestCorrectness(unittest.TestCase):

    def setUp(self):
        self.highScoreTable = HighScoreTable(3)

    def test_empty_after_initialization(self):
        self.assertEqual(self.highScoreTable.scores, [])

    def test_single(self):
        self.highScoreTable.update(10)
        self.assertEqual(self.highScoreTable.scores, [10])

    def test_ordered(self):
        self.highScoreTable.update(10)
        self.highScoreTable.update(8)
        self.highScoreTable.update(12)
        self.assertEqual(self.highScoreTable.scores, [12, 10, 8])

    def test_small(self):
        self.highScoreTable.update(10)
        self.highScoreTable.update(8)
        self.highScoreTable.update(12)
        self.highScoreTable.update(5)
        self.assertEqual(self.highScoreTable.scores, [12, 10, 8])

    def test_reset(self):
        self.highScoreTable.reset()
        self.assertEqual(self.highScoreTable.scores, [])