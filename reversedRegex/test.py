import unittest

from main import reverse_regex


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        regex_list = [
            r'abc',
            r'tuv?',
            r'a(b|c)',
            r'a([bc]|cd)',
            r'^a[^bc]d$',
            r'p{2}',
            r'q{7,}',
        ]
        self.assertEqual(reverse_regex("abc"), "cba")
        self.assertEqual(reverse_regex("tuv?"), "v?ut")
        self.assertEqual(reverse_regex("a(b|c)"), "(c|b)a")
        self.assertEqual(reverse_regex("a([bc]|cd)"), "(dc|[bc])a")
        self.assertEqual(reverse_regex("^a[^bc]d$"), "^d[^bc]a$")
        self.assertEqual(reverse_regex("p{2}"), "p{2}")
        self.assertEqual(reverse_regex("q{7,}"), "q{7,}")
