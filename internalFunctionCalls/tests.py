import unittest

from main import count_calls


def add(a, b):
    return a + b


def add_ten(a):
    return add(a, 10)


def misc_fun():
    return add(add_ten(3), add_ten(9))


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(count_calls(add, 8, 12), (0, 20))
        self.assertEqual(count_calls(add_ten, 5), (1, 15))
        self.assertEqual(count_calls(misc_fun), (5, 32))
