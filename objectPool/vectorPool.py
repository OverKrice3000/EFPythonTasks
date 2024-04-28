from objectPool import ObjectPool, T
from vector import Vector


class VectorPool(ObjectPool[Vector]):
    def __init__(self, initial_size: int, extra_allocation_allowed: bool = False):
        super().__init__(initial_size, extra_allocation_allowed)

    def _create_object(self) -> T:
        return Vector()

    def _dispose_object(self, pool_object: T):
        pass
