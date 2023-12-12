from typing import Dict, List


def build_map_for_str(string: str) -> Dict[str, bool]:
    list_str = list(string)
    char_map = {}
    for i in list_str:
        char_map[i.lower()] = True
    return char_map


def compare_maps(first: Dict[str, bool], second: Dict[str, bool]) -> bool:
    for i in first.keys():
        if second.get(i) is None:
            return False
    return True


def test_against_map(string: str, map: Dict[str, bool]) -> bool:
    list_str = list(string)
    for i in list_str:
        if i.lower() not in map.keys():
            return False
    return True


def find_uniq(arr):
    first = build_map_for_str(arr[0])
    second = build_map_for_str(arr[1])
    third = build_map_for_str(arr[2])
    base_map = {}
    if compare_maps(first, second):
        base_map = first
    elif compare_maps(first, third):
        base_map = first
    else:
        base_map = second
    for i in arr:
        if not test_against_map(i, base_map):
            return i


if __name__ == '__main__':
    unique = find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a'])
    print(unique)
