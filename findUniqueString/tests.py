import unittest

from main import find_uniq


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']), 'BbBb')
        self.assertEqual(find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']), 'foo')
        self.assertEqual(find_uniq(['    ', 'a', '  ']), 'a')