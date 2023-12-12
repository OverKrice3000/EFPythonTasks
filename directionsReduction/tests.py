import unittest

from main import dir_reduc


class TestCorrectness(unittest.TestCase):
    def test_pass_tests(self):
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        self.assertEqual(dir_reduc(a), ['WEST'])
        a = ["NORTH", "WEST", "SOUTH", "EAST"]
        self.assertEqual(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]  # ['WEST']
        self.assertEqual(dir_reduc(a), ['WEST'])
        a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH", "WEST",
             "EAST"]  # ['NORTH', 'NORTH']
        self.assertEqual(dir_reduc(a), ['NORTH', 'NORTH'])
        a = []  # []
        self.assertEqual(dir_reduc(a), [])
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]  # []
        self.assertEqual(dir_reduc(a), [])
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"]  # ["NORTH"]
        self.assertEqual(dir_reduc(a), ["NORTH"])
        a = ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"]  # ["EAST", "NORTH"]
        self.assertEqual(dir_reduc(a), ["EAST", "NORTH"])
        a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST",
             "SOUTH"]  # ["NORTH", "EAST"])
        self.assertEqual(dir_reduc(a), ["NORTH", "EAST"])
        a = ["NORTH", "WEST", "SOUTH", "EAST"]  # ["NORTH", "WEST", "SOUTH", "EAST"])
        self.assertEqual(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
        a = ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
        self.assertEqual(dir_reduc(a), ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])
