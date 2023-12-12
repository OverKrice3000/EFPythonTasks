from typing import List, Dict, Optional

from utils.typings import RowTypeT

# TODO additional typings
FieldSquaresArrayT = List[List['Square']]


def get_row_of_size(n: int, row_number: int, field: 'Field') -> List['Square']:
    row = []
    for i in range(0, n):
        square = NonDeterminedSquare(row_number, i, field)
        square.init(n)
        row.append(square)
    return row


def get_field_of_size(n: int, field: 'Field') -> FieldSquaresArrayT:
    field_squares = []
    for i in range(0, n):
        field_squares.append(get_row_of_size(n, i, field))
    return field_squares


def get_possible_height_for_size(n: int) -> Dict[int, bool]:
    height_dict = {}
    for i in range(1, n + 1):
        height_dict[i] = True
    return height_dict


class Square:
    __is_determined: bool
    __row_number: int
    __column_number: int
    __field: 'Field'

    def __init__(self, row_number: int, column_number: int, field: 'Field'):
        self.__field = field
        self.__row_number = row_number
        self.__column_number = column_number
        self.__is_determined = False
        pass

    def is_determined(self) -> bool:
        return self.__is_determined


class DeterminedSquare(Square):
    __height: int
    __row_number: int
    __column_number: int
    __field: 'Field'

    def __init__(self, field: 'Field', row_number: int, column_number: int, height: int):
        super().__init__(row_number, column_number, field)
        self.__field = field
        self.__row_number = row_number
        self.__column_number = column_number
        self.__is_determined = True

        self.__height = height

    def clone(self):
        clone = DeterminedSquare(self.__field, self.__row_number, self.__column_number, self.__height)
        return clone

    def get_height(self) -> int:
        return self.__height


class NonDeterminedSquare(Square):
    __possible_heights: Optional[Dict[int, bool]]
    __row_number: int
    __column_number: int
    __field: 'Field'

    def __init__(self, row_number: int, column_number: int, field: 'Field'):
        super().__init__(row_number, column_number, field)
        self.__field = field
        self.__row_number = row_number
        self.__column_number = column_number
        self.__possible_heights = None
        self.__is_determined = False

    def init(self, field_size: int):
        self.__possible_heights = get_possible_height_for_size(field_size)

    def clone(self):
        clone = NonDeterminedSquare(self.__row_number, self.__column_number, self.__field)
        clone.__set_possible_heights(self.__possible_heights.copy())
        return clone

    def is_height_possible(self, height) -> bool:
        return self.__possible_heights[height]

    def get_possible_heights(self) -> List[int]:
        if self.__possible_heights is None:
            raise Exception("Square is not initialized!")
        possible_heights_list = []
        for i in iter(self.__possible_heights):
            if self.__possible_heights[i]:
                possible_heights_list.append(i)
        return possible_heights_list

    def remove_height_possible(self, height):
        self.__possible_heights[height] = False
        possible_heights = self.get_possible_heights()
        if len(possible_heights) == 1:
            self.__field.determine(self.__row_number, self.__column_number, possible_heights[0])

    def determine(self, height: int):
        self.__field.determine(self.__row_number, self.__column_number, height)

    def __set_possible_heights(self, possible_heights: Optional[Dict[int, bool]]):
        self.__possible_heights = possible_heights


class RowView:
    __squares: List['Square']
    __field: 'Field'
    __row_number: int
    __row_type: RowTypeT
    __clue: int
    __reverse_clue: int
    __size: int

    def __init__(self, field: 'Field', row_type: RowTypeT, row_number: int, squares: List['Square'], clues: List[int]):
        self.__squares = squares
        self.__field = field
        self.__row_type = row_type
        self.__row_number = row_number
        self.__clue = clues[0]
        self.__reverse_clue = clues[1]
        self.__size = len(squares)

    def get_square_at(self, square_number: int):
        return self.__squares[square_number]

    def get_clue(self):
        return self.__clue

    def get_reverse_clue(self):
        return self.__reverse_clue

    def determine(self, square_number: int, height: int):
        if self.__row_type == 'row':
            self.__determine(self.__row_number, square_number, height)
        elif self.__row_type == 'column':
            self.__determine(square_number, self.__row_number, height)

    def __determine(self, row_number: int, column_number: int, height: int):
        self.__field.determine(row_number, column_number, height)


class Field:
    __field: FieldSquaresArrayT
    __clues: List[int]
    __size: int

    def __init__(self, size: int, clues: List[int]):
        self.__size = size
        self.__field = get_field_of_size(size, self)
        self.__clues = clues

    def get_size(self):
        return self.__size

    def get_row_view(self, row_number: int, reverse: bool) -> 'RowView':
        row_squares = self.__field[row_number].copy()
        row_clues = self.__get_row_clues(row_number)
        if reverse:
            row_squares.reverse()
            row_clues.reverse()
        return RowView(self, 'row', row_number, row_squares, row_clues)

    def get_column_view(self, column_number: int, reverse: bool) -> 'RowView':
        column_squares = self.__get_column_squares(column_number)
        column_clues = self.__get_column_clues(column_number)
        if reverse:
            column_squares.reverse()
            column_clues.reverse()
        return RowView(self, 'column', column_number, column_squares, column_clues)

    def get_square_at(self, row_number: int, column_number: int):
        return self.__field[row_number][column_number]

    def determine(self, row_number: int, column_number: int, height: int):
        self.__field[row_number][column_number] = DeterminedSquare(self, row_number, column_number, height)
        self.__remove_height_from_adjacent(row_number, column_number, height)

    def is_determined(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if not self.__field[i][j].is_determined():
                    return False
        return True

    def remove_square_height_possible(self, row_number: int, column_number: int, height: int):
        square = self.__field[row_number][column_number]
        if isinstance(square, NonDeterminedSquare):
            square.remove_height_possible(height)

    def __remove_height_from_adjacent(self, row_number: int, column_number: int, height: int):
        for i in range(0, self.__size):
            column_square = self.__field[row_number][i]
            row_square = self.__field[i][column_number]
            if isinstance(column_square, NonDeterminedSquare):
                column_square.remove_height_possible(height)
            if isinstance(row_square, NonDeterminedSquare):
                row_square.remove_height_possible(height)

    def __get_column_squares(self, column_number: int) -> List[Square]:
        column_squares_arr = []
        for i in range(0, self.__size):
            column_squares_arr.append(self.__field[i][column_number])
        return column_squares_arr

    def __get_column_clues(self, column_number: int) -> List[int]:
        return [self.__clues[column_number], self.__clues[self.__size * 3 - column_number - 1]]

    def __get_row_clues(self, row_number: int) -> List[int]:
        return [self.__clues[self.__size * 4 - row_number - 1], self.__clues[self.__size + row_number]]

    def print_field(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                square = self.__field[i][j]
                if isinstance(square, DeterminedSquare):
                    print(square.get_height())
                elif isinstance(square, NonDeterminedSquare):
                    print(square.get_possible_heights())
