import unittest

from main import find_spec_prod_part


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(find_spec_prod_part(1416, 'max'), [[708, 2], 1420])
        self.assertEqual(find_spec_prod_part(1416, 'min'), [[59, 24], 166])
        self.assertEqual(find_spec_prod_part(10007, 'max'), "It is a prime number")