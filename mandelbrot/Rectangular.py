class Point:
    __x: float
    __y: float

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def x(self):
        return self.__x

    def y(self):
        return self.__y


class Rectangular:
    __upper_left: Point
    __lower_right: Point

    def __init__(self, first: Point, second: Point):
        self.__upper_left = first
        self.__lower_right = second

    def upper_left(self):
        return self.__upper_left

    def lower_right(self):
        return self.__lower_right
