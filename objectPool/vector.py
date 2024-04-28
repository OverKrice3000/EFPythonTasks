from __future__ import annotations


class Vector:
    __x: float
    __y: float
    __z: float

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.__x = x
        self.__y = y
        self.__z = z

    def set(self, x: float, y: float, z: float) -> Vector:
        self.__x = x
        self.__y = y
        self.__z = z
        return self

    def copy(self, vector: Vector) -> Vector:
        self.__x = vector.__x
        self.__y = vector.__y
        self.__z = vector.__z
        return self

    def add(self, vector: Vector) -> Vector:
        self.__x += vector.__x
        self.__y += vector.__y
        self.__z += vector.__z
        return self
