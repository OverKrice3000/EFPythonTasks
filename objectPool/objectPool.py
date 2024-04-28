from abc import abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar("T", bound=object)


class PoolObjectWithAllocatedId(Generic[T]):
    object_pool_allocation_id: int
    pool_object: T

    def __init__(self, pool_object: T, object_id: int):
        self.pool_object = pool_object
        self.object_pool_allocation_id = object_id


class ObjectPool(Generic[T]):
    _objects_pool: List[PoolObjectWithAllocatedId[T]]
    _objects_allocated: List[bool]

    _initial_size: int
    _size: int
    _allocated_objects_count: int

    _extra_allocation_allowed: bool

    def __init__(self, initial_size: int, extra_allocation_allowed: bool = False):
        self._objects_pool = []
        self._objects_allocated = []
        self._initial_size = initial_size
        self._size = 0
        self._allocated_objects_count = 0
        self._extra_allocation_allowed = extra_allocation_allowed
        self._create_and_add_objects(initial_size)

    def _create_and_add_objects(self, amount: int):
        for i in range(amount):
            self._create_and_add_object()

    def _create_and_add_object(self):
        pool_object = self.__create_object_with_allocated_id()
        self._objects_pool.append(pool_object)
        self._objects_allocated.append(False)
        self._size += 1
        if self._size > self._initial_size and not self._extra_allocation_allowed:
            raise OverflowError("Extra object allocation detected!")

    def __create_object_with_allocated_id(self) -> PoolObjectWithAllocatedId[T]:
        pool_object = self._create_object()

        return self.__ensure_id_allocated(pool_object)

    @abstractmethod
    def _create_object(self) -> T:
        pass

    def __ensure_id_allocated(self, pool_object: T) -> PoolObjectWithAllocatedId[T]:
        return pool_object if isinstance(pool_object, PoolObjectWithAllocatedId) else PoolObjectWithAllocatedId(pool_object, self._size)

    def allocate(self, size: int) -> List[PoolObjectWithAllocatedId[T]]:
        self.__ensure_can_allocate_object(size)
        non_allocated_indices = self.__find_non_allocated_indices(size)
        objects: List[PoolObjectWithAllocatedId[T]] = []
        for index in non_allocated_indices:
            objects.append(self._objects_pool[index])
            self._objects_allocated[index] = True
        self._allocated_objects_count += size

        return objects

    def __find_non_allocated_indices(self, size: int):
        indices: List[int] = []
        for i in range(self._size):
            if not self._objects_allocated[i]:
                indices.append(i)
            if len(indices) == size:
                return indices
        return indices

    def __ensure_can_allocate_object(self, size: int):
        if self._allocated_objects_count + size > self._size:
            self._create_and_add_objects(self._allocated_objects_count + size - self._size)

    def deallocate(self, pool_objects: List[PoolObjectWithAllocatedId[T]]):
        for pool_object in pool_objects:
            if not isinstance(pool_object, PoolObjectWithAllocatedId):
                raise ValueError("Trying to deallocate unexpected object!")
            object_allocated_id = pool_object.object_pool_allocation_id
            self._objects_allocated[object_allocated_id] = False
            self._allocated_objects_count -= 1

    def dispose(self):
        for pool_object in self._objects_pool:
            self._dispose_object(pool_object)
        self._objects_pool.length = 0
        self._objects_allocated.length = 0

    @abstractmethod
    def _dispose_object(self, pool_object: T):
        pass

    def get_size(self):
        return self._size

    def get_allocated_objects_count(self):
        return self._allocated_objects_count
