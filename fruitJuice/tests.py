import unittest

from main import Jar


class TestCorrectness(unittest.TestCase):
    def setUp(self):
        self.jar = Jar()

    def test_initialization_test_case(self):
        self.assertEqual(self.jar.get_total_amount(), 0, "Initial total amount must be 0")
        self.assertEqual(self.jar.get_concentration("apple"), 0,
                         "Nothing was added yet, concentration must be 0 for each component")

    def test_add_test_case(self):
        self.jar.add(100, "apple")
        self.assertEqual(self.jar.get_total_amount(), 100, "Wrong total amount after adding juice")
        self.assertEqual(self.jar.get_concentration("apple"), 1, "Wrong concentration after adding juice")

        self.jar.add(100, "apple")
        self.assertEqual(self.jar.get_total_amount(), 200, "Wrong total amount after adding more juice")
        self.assertEqual(self.jar.get_concentration("apple"), 1, "Wrong concentration after adding same juice")

        self.jar.add(200, "banana")
        self.assertEqual(self.jar.get_total_amount(), 400, "Wrong total amount after adding more juice")
        self.assertEqual(self.jar.get_concentration("apple"), 0.5,
                         "Wrong concentration after adding some other juice")
        self.assertEqual(self.jar.get_concentration("banana"), 0.5,
                         "Wrong concentration after adding some other juice")

    def test_pour_test_case(self):
        self.jar.add(200, "apple")
        self.jar.add(200, "banana")
        self.jar.pour_out(200)
        self.assertEqual(self.jar.get_total_amount(), 200, "Wrong total amount after pouring out some juice")
        self.assertEqual(self.jar.get_concentration("apple"), 0.5,
                         "Pouring out juice must not change the concentrations")
        self.assertEqual(self.jar.get_concentration("banana"), 0.5,
                         "Pouring out juice must not change the concentrations")

    def test_add_more_test_case(self):
        self.jar.add(100, "apple")
        self.jar.add(100, "banana")
        self.jar.add(200, "apple")
        self.assertEqual(self.jar.get_total_amount(), 400, "Wrong total amount after adding some juice again")
        self.assertEqual(self.jar.get_concentration("apple"), 0.75, "Wrong concentration after adding juice again")
        self.assertEqual(self.jar.get_concentration("banana"), 0.25,
                         "Wrong concentration after adding juice again")
