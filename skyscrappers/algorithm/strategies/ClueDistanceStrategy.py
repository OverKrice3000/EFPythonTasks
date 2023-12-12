from model.fieldModel import Field, RowView, NonDeterminedSquare
from utils.typings import CluesT


class ClueDistanceStrategy:
    __field: Field
    __clues: CluesT
    __field_size: int

    def __init__(self, field: Field, clues: CluesT):
        self.__field = field
        self.__clues = clues
        self.__field_size = field.get_size()

    def execute(self):
        for i in range(0, self.__field_size):
            self.execute_row(self.__field.get_row_view(i, False))
            self.execute_row(self.__field.get_row_view(i, True))
            self.execute_row(self.__field.get_column_view(i, False))
            self.execute_row(self.__field.get_column_view(i, True))

    def execute_row(self, row: RowView):
        row_clue = row.get_clue()
        for i in range(0, self.__field_size):
            square = row.get_square_at(i)
            if not isinstance(square, NonDeterminedSquare):
                continue
            maximum_height = self.__field_size - row_clue + 1 + i
            if maximum_height >= self.__field_size:
                break
            for j in range(maximum_height + 1, self.__field_size + 1):
                square.remove_height_possible(j)
