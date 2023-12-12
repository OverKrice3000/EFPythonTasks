import unittest

from main import last_digit


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        test_data = [
            ([], 1),
            ([0, 0], 1),
            ([0, 0, 0], 0),
            ([1, 2], 1),
            ([3, 4, 5], 1),
            ([4, 3, 6], 4),
            ([7, 6, 21], 1),
            ([12, 30, 21], 6),
            ([2, 2, 2, 0], 4),
            ([937640, 767456, 981242], 0),
            ([123232, 694022, 140249], 6),
            ([499942, 898102, 846073], 6)
        ]
        for test_input, test_output in test_data:
            self.assertEqual(last_digit(test_input), test_output)