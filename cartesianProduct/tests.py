import unittest

from main import cart_prod

NULLSET = set()
A = {1}
B = {1, 2}
C = {1, 2, 3}
X = {'a'}
Y = {'a', 'b'}
Z = {'a', 'b', 'c'}
O = {1, 1}

class TestCorrectness(unittest.TestCase):
    def test_no_set(self):
        self.assertEqual(cart_prod(), {()})

    def test_one_set(self):
        self.assertEqual(cart_prod(A), {(1,)})

    def test_two_sets(self):
        self.assertEqual(cart_prod(A, A), {(1, 1)})
        self.assertEqual(cart_prod(A, X), {(1, 'a')})
        self.assertEqual(cart_prod(X, A), {('a', 1)})
        self.assertEqual(cart_prod(C, X), {(1, 'a'), (2, 'a'), (3, 'a')})
        self.assertEqual(cart_prod(B, Y), {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')})

    def test_three_sets(self):
        self.assertEqual(cart_prod(A, A, A), {(1, 1, 1)})
        self.assertEqual(cart_prod(A, X, A), {(1, 'a', 1)})
        self.assertEqual(cart_prod(A, A, X), {(1, 1, 'a')})
        self.assertEqual(cart_prod(A, B, C), {(1, 1, 1), (1, 2, 1), (1, 1, 2), (1, 2, 2), (1, 1, 3), (1, 2, 3)})
        self.assertEqual(cart_prod(B, B, B), {(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2),
                                                (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)})
    def test_null_set(self):
        self.assertEqual(cart_prod(NULLSET), NULLSET)
        self.assertEqual(cart_prod(set(NULLSET)), set())
        self.assertEqual(cart_prod(A, NULLSET), NULLSET)
        self.assertEqual(cart_prod(A, B, NULLSET), NULLSET)
        self.assertEqual(cart_prod(A, NULLSET, B), NULLSET)

    def test_overlap(self):
        self.assertEqual(cart_prod(O, O), {(1, 1)})
