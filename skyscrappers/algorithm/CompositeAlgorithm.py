from algorithm.strategies.ClueDistanceStrategy import ClueDistanceStrategy
from model.fieldModel import Field
from utils.typings import CluesT, FieldRawArrayT


class CompositeAlgorithm:
    __field_size: int
    __clues: CluesT
    __field: Field

    def __init__(self, field_size: int, clues: CluesT):
        self.__field_size = field_size
        self.__clues = clues
        self.__field = Field(field_size, clues)

    def execute(self):
        ClueDistanceStrategy(self.__field, self.__clues).execute()
        self.__field.print_field()

    def get_solution(self) -> FieldRawArrayT:
        return []
