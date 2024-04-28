from typing import List, Dict, TypeVar, Generic

from abc import ABC, abstractmethod

T = TypeVar('T')


class Composite(Generic[T]):
    _primitives_array: List[T]

    def __init__(self):
        self._primitives_array = []

    def add_primitive(self, primitive: T):
        self._primitives_array.append(primitive)
        return self

    def clear_primitives(self):
        self._primitives_array = []


class Validator(ABC):
    @abstractmethod
    def validate(self) -> bool:
        pass


class BattleshipValidator(Validator):
    _field: List[List[int]]
    _field_size: int

    def __init__(self, field: List[List[int]]):
        super().__init__()
        self._field = field
        self._field_size = len(field)

    @abstractmethod
    def validate(self) -> bool:
        pass


class ShipFieldValidator(BattleshipValidator):
    def __init__(self, field: List[List[int]]):
        super().__init__(field)

    def validate(self) -> bool:
        is_valid = True
        for row in self._field:
            is_valid = self._field_size == len(row)
            if not is_valid:
                return is_valid
        return is_valid


class ShipFormValidator(BattleshipValidator):
    def __init__(self, field: List[List[int]]):
        super().__init__(field)

    def validate(self) -> bool:
        is_valid = True
        for i in range(0, self._field_size):
            for j in range(0, self._field_size):
                ship_present = self._field[i][j] == 1
                x_shift_present = (j > 0 and self._field[i][j - 1] == 1) or (
                        j < self._field_size - 1 and self._field[i][j + 1] == 1)
                y_shift_present = (i > 0 and self._field[i - 1][j] == 1) or (
                        i < self._field_size - 1 and self._field[i + 1][j] == 1)
                is_valid = not (ship_present and x_shift_present and y_shift_present)
                if not is_valid:
                    return is_valid
        return is_valid


class ShipsNumberValidator(BattleshipValidator):
    def __init__(self, field: List[List[int]]):
        super().__init__(field)

    def validate(self) -> bool:
        ships_number_map = dict()
        field_dirty = [[0] * self._field_size for _ in range(self._field_size)]
        for i in range(0, self._field_size):
            for j in range(0, self._field_size):
                if self._field[i][j] == 1 and field_dirty[i][j] != 1:
                    self.__mark_ship_cells(i, j, ships_number_map, field_dirty)
        if ships_number_map.get(1) != 4 or ships_number_map.get(2) != 3 or ships_number_map.get(
                3) != 2 or ships_number_map.get(4) != 1:
            return False
        return True

    def __mark_ship_cells(self, x: int, y: int, ships_number_map: Dict[int, int], field_dirty: List[List[int]]):
        ship_size = self.__get_ship_size(x, y, field_dirty)
        ships_number_map[ship_size] = 1 if ships_number_map.get(ship_size) is None else ships_number_map[ship_size] + 1

    def __get_ship_size(self, x: int, y: int, field_dirty: List[List[int]]) -> int:
        if x < 0 or y < 0 or x >= self._field_size or y >= self._field_size or field_dirty[x][y] == 1 or self._field[x][
            y] == 0:
            return 0
        field_dirty[x][y] = 1
        return 1 + self.__get_ship_size(x + 1, y, field_dirty) + self.__get_ship_size(x - 1, y,
                                                                                      field_dirty) + self.__get_ship_size(
            x, y + 1, field_dirty) + self.__get_ship_size(x, y - 1, field_dirty)


class ShipsIntersectionsValidator(BattleshipValidator):
    def __init__(self, field: List[List[int]]):
        super().__init__(field)

    def validate(self) -> bool:
        is_valid = True
        for i in range(0, self._field_size):
            for j in range(0, self._field_size):
                is_valid = self._field[i][j] == 0 or (
                        self.__check_diagonal_cell(i, j, -1, -1) and self.__check_diagonal_cell(i, j, -1,
                                                                                                1) and self.__check_diagonal_cell(
                    i, j, 1, -1) and self.__check_diagonal_cell(i, j, 1, 1))
                if not is_valid:
                    return is_valid
        return is_valid

    def __check_diagonal_cell(self, cell_x: int, cell_y: int, cell_shift_x: int, cell_shift_y: int) -> bool:
        shifted_cell_x = cell_x + cell_shift_x
        shifted_cell_y = cell_y + cell_shift_y
        if shifted_cell_x < 0 or shifted_cell_y < 0 or shifted_cell_x >= self._field_size or shifted_cell_y >= self._field_size:
            return True
        return not (self._field[shifted_cell_x][shifted_cell_y] == 1 and self._field[shifted_cell_x][cell_y] == 0 and
                    self._field[cell_x][shifted_cell_y] == 0)


class CompositeValidator(Validator, Composite[BattleshipValidator]):
    def __init__(self):
        super().__init__()

    def validate(self) -> bool:
        is_valid = True
        for validator in self._primitives_array:
            is_valid = validator.validate()
            if not is_valid:
                return is_valid
        return is_valid
