import unittest

from main import Potion

potions = [
    Potion((153, 210, 199), 32),
    Potion((135, 34, 0), 17),
    Potion((18, 19, 20), 25),
    Potion((174, 211, 13), 4),
    Potion((255, 23, 148), 19),
    Potion((51, 102, 51), 6)
]
a = potions[0].mix(potions[1])
b = potions[0].mix(potions[2]).mix(potions[4])
c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])
d = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[4]).mix(potions[5])
e = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[3]).mix(potions[4]).mix(potions[5])


class TestCorrectness(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(a.color, (147, 149, 130))
        self.assertEqual(a.volume, 49)
        self.assertEqual(b.color, (135, 101, 128))
        self.assertEqual(b.volume, 76)
        self.assertEqual(c.color, (74, 50, 18))
        self.assertEqual(c.volume, 52)
        self.assertEqual(d.color, (130, 91, 102))
        self.assertEqual(d.volume, 99)
        self.assertEqual(e.color, (132, 96, 99))
        self.assertEqual(e.volume, 103)
