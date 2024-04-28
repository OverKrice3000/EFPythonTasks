import unittest

from main import differentiate


class TestCorrectness(unittest.TestCase):
    def test_constant(self):
        self.assertEqual(differentiate("2", 1), 0)
        self.assertEqual(differentiate("-6", 30), 0)
        self.assertEqual(differentiate("1", 43), 0)

    def test_linear(self):
        self.assertEqual(differentiate("12x+2", 3), 12)
        self.assertEqual(differentiate("-3x-6", 3), -3)
        self.assertEqual(differentiate("10x", 3), 10)

    def test_complex(self):
        self.assertEqual(differentiate("-5x^2+10x+4", 3), -20)
        self.assertEqual(differentiate("-x^4+x^3-x^2+x-1", 3), -86)
