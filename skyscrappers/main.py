from __future__ import annotations
from typing import List

from algorithm.CompositeAlgorithm import CompositeAlgorithm
from utils.typings import FieldRawArrayT


def solve_puzzle(clues: List[int]) -> FieldRawArrayT:
    field_size = int(len(clues) / 4)
    algorithm = CompositeAlgorithm(field_size, clues)
    algorithm.execute()
    return algorithm.get_solution()


if __name__ == '__main__':
    __clues = [7, 0, 0, 0, 2, 2, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 4]
    solution = solve_puzzle(__clues)
    print(solution)
