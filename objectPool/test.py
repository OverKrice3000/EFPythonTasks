import unittest

from vectorPool import VectorPool


class TestCorrectness(unittest.TestCase):
    def test_correct_size_after_allocation(self):
        pool = VectorPool(10)
        vectors = pool.allocate(5)
        self.assertTrue(pool.get_allocated_objects_count() == 5)
        vectors[0].pool_object.set(1, 1, 1)
        pool.deallocate(vectors)
        self.assertTrue(pool.get_allocated_objects_count() == 0)

    def test_raises_when_extra_allocation_disallowed(self):
        pool = VectorPool(1)
        self.assertRaises(OverflowError, lambda *args: pool.allocate(2))

    def test_does_not_raise_when_extra_allocation_allowed(self):
        pool = VectorPool(1, True)
        pool.allocate(2)
