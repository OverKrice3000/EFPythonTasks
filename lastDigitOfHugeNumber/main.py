from typing import List

digit_power_cycles_len_map = {
    0: 1,
    1: 1,
    2: 4,
    3: 4,
    4: 2,
    5: 1,
    6: 1,
    7: 4,
    8: 4,
    9: 2
}


def find_multiplicative_group_cycle(base: int, mod: int) -> int:
    start_base = base
    prev_base = base
    cycle = 0
    while True:
        cycle += 1
        next_base = (prev_base * start_base) % mod
        prev_base = next_base
        if next_base == start_base:
            return cycle


def find_reduced_exp(lst: List[int], cycle_len: int) -> int:
    if len(lst) == 1:
        cycled_pow = lst[0] % cycle_len
        return cycle_len if cycled_pow == 0 else cycled_pow

    lst_head = lst[0]
    lst_tail = lst[1:]
    head_cycled = lst_head % cycle_len
    # Only option when base and mod are not coprime
    if head_cycled == 2 and cycle_len == 4:
        return cycle_len
    mult_cycle = find_multiplicative_group_cycle(head_cycled, cycle_len)
    reduced_exp = find_reduced_exp(lst_tail, mult_cycle)
    reduced_pow = pow(head_cycled, reduced_exp) % cycle_len

    return cycle_len if reduced_pow == 0 else reduced_pow


def reduce_init_array(lst: List[int]) -> List[int]:
    array_0 = lst
    for i in reversed(range(0, len(lst))):
        if len(array_0) <= i:
            continue
        if lst[i] != 0:
            continue
        if i == 0:
            return [0]
        elif i == 1:
            return [1]
        array_0 = array_0[:i-1]
    try:
        index_1 = array_0.index(1)
        if index_1 == 0:
            return [1]
        else:
            return lst[:index_1]
    except ValueError:
        return array_0


def last_digit(lst: List[int]):
    reduced_lst = reduce_init_array(lst)
    if len(reduced_lst) == 0:
        return 1
    elif len(reduced_lst) == 1:
        return reduced_lst[0] % 10

    first_last_digit = reduced_lst[0] % 10
    first_cycle_len = digit_power_cycles_len_map[first_last_digit]
    reduced_exp = find_reduced_exp(reduced_lst[1:], first_cycle_len)
    reduced_pow = pow(first_last_digit, reduced_exp)
    return reduced_pow % 10


if __name__ == '__main__':
    __result = last_digit([937640, 767456, 981242])
    print(__result)
