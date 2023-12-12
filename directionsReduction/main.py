import unittest
from typing import List

dir_map = {
    'NORTH': 1,
    'SOUTH': -1,
    'WEST': 2,
    'EAST': -2
}


def left_nonzero_index_from(arr: List[str], reference: int) -> int:
    for i in reversed(range(0, reference + 1)):
        if arr[i] != '0':
            return i
    return -1


def right_nonzero_index_from(arr: List[str], reference: int) -> int:
    for i in range(reference, len(arr)):
        if arr[i] != '0':
            return i
    return -1


def are_opposite_to(first_dir: str, second_dir: str) -> bool:
    return dir_map[first_dir] + dir_map[second_dir] == 0


def dir_reduc(arr: List[str]):
    copied_arr = arr.copy()
    for i in range(0, len(copied_arr) - 1):
        left_index = i
        right_index = i + 1
        if copied_arr[i] == '0' or copied_arr[i + 1] == '0':
            continue
        while True:
            if not are_opposite_to(copied_arr[left_index], copied_arr[right_index]):
                break
            copied_arr[left_index] = '0'
            copied_arr[right_index] = '0'
            left_index = left_nonzero_index_from(copied_arr, left_index)
            right_index = right_nonzero_index_from(copied_arr, right_index)
            if left_index == -1 or right_index == -1:
                break
    result_arr = []
    for i in iter(copied_arr):
        if i != '0':
            result_arr.append(i)
    return result_arr


if __name__ == '__main__':
    unittest.main()