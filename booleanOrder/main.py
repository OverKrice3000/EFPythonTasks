from typing import List, Dict, Tuple, Optional

OpResultMapT = Dict[str, Dict[bool, List[Tuple[bool, bool]]]]

op_result_map: OpResultMapT = {
    '&': {
        False: [(False, False), (True, False), (False, True)],
        True: [(True, True)]
    },
    '|': {
        False: [(False, False)],
        True: [(True, False), (False, True), (True, True)]
    },
    '^': {
        False: [(True, True), (False, False)],
        True: [(False, True), (True, False)]
    }
}

evaluations_cache = {}


def solve(s: str, ops: str) -> int:
    s_list = list(s)
    ops_list = list(ops)
    return count_evaluations_to_result(s_list, ops_list, True)


def count_evaluations(s_len: int) -> int:
    pass


def char_to_bool(char: str) -> bool:
    return True if char == 't' else False


def get_from_cache(s: str, ops: str, result: bool) -> Optional[int]:
    cached_s = evaluations_cache.get(s)
    if cached_s is None:
        return None
    cached_ops = cached_s.get(ops)
    if cached_ops is None:
        return None
    return cached_ops.get(result)


def set_to_cache(s: str, ops: str, result: bool, value: int):
    cached_s = evaluations_cache.get(s)
    if cached_s is None:
        evaluations_cache[s] = {ops: {result: value}}
        return
    cached_ops = cached_s.get(ops)
    if cached_ops is None:
        cached_s[ops] = {result: value}
        return
    cached = cached_ops.get(result)
    if cached is None:
        cached_ops[result] = value
        return

def count_evaluations_to_result(s_list: List[str], ops_list: List[str], result: bool) -> int:
    if len(ops_list) == 0:
        return 1 if char_to_bool(s_list[0]) == result else 0
    s = ''.join(s_list)
    ops = ''.join(ops_list)
    cached = get_from_cache(s, ops, result)
    if cached is not None:
        return cached

    result_evaluations_count = 0
    for i in range(0, len(ops_list)):
        op = ops_list[i]
        possible_evaluations = op_result_map[op][result]
        for evaluation_tuple in possible_evaluations:
            left_evaluations = count_evaluations_to_result(s_list[:i + 1], ops_list[:i], evaluation_tuple[0])
            right_evaluations = count_evaluations_to_result(s_list[i + 1:], ops_list[i + 1:], evaluation_tuple[1])
            result_evaluations_count += left_evaluations * right_evaluations

    set_to_cache(s, ops, result, result_evaluations_count)
    return result_evaluations_count


if __name__ == '__main__':
    __result = solve("tft", "^&")
    print(__result)
