import math
from typing import List, Optional, Tuple


def compute_special_sum(n: int, m: int):
    if m == 1:
        return n + 1
    special_sum = 0
    for i in range(0, n + 1):
        special_sum += compute_special_sum(i, m - 1)
    return special_sum


def have_common_letter(first: str, second: str) -> Tuple[bool, int, int]:
    letter_map = {}
    for i in range(0, len(first)):
        letter = first[i]
        letter_map[letter] = i
    for i in range(0, len(second)):
        letter = second[i]
        first_position = letter_map.get(letter)
        if first_position is not None:
            return True, first_position, i
    return False, 0, 0


def merge_sub_permutations(first: str, second: str, first_common_letter_index: int, second_common_letter_index: int) -> \
Optional[str]:
    min_left_len = min(first_common_letter_index, second_common_letter_index)
    if first[first_common_letter_index - min_left_len:first_common_letter_index] != second[
                                                                                    second_common_letter_index - min_left_len:second_common_letter_index]:
        return None
    min_right_len = min(len(first) - first_common_letter_index - 1, len(second) - second_common_letter_index - 1)
    if first[first_common_letter_index + 1:first_common_letter_index + 1 + min_right_len] != second[
                                                                                             second_common_letter_index + 1: second_common_letter_index + 1 + min_right_len]:
        return None
    max_left_str = first if first_common_letter_index > second_common_letter_index else second
    max_left_str_common_index = first_common_letter_index if first_common_letter_index > second_common_letter_index else second_common_letter_index
    max_right_str = first if len(first) - first_common_letter_index > len(
        second) - second_common_letter_index else second
    max_right_str_common_index = first_common_letter_index if len(first) - first_common_letter_index > len(
        second) - second_common_letter_index else second_common_letter_index

    if have_common_letter(max_left_str[:max_left_str_common_index - min_left_len],
                          max_right_str[max_right_str_common_index + min_right_len + 1:])[0]:
        return None
    return max_left_str[:max_left_str_common_index] + max_right_str[max_right_str_common_index:]


def merge_sub_permutations_list(sub_permutations: List[str]) -> List[str]:
    sub_permutations: List[Optional[str]] = sub_permutations.copy()
    i = 0
    for i in range(0, len(sub_permutations)):
        for j in range(i + 1, len(sub_permutations)):
            (do_have_common_letter, common_letter_first_index, common_letter_second_index) = have_common_letter(
                sub_permutations[i], sub_permutations[j])
            if do_have_common_letter:
                merged_sub_permutations = merge_sub_permutations(sub_permutations[i], sub_permutations[j],
                                                                 common_letter_first_index, common_letter_second_index)
                if merged_sub_permutations is None:
                    return []
                sub_permutations[j] = merged_sub_permutations
                sub_permutations[i] = None
                break
    merged_sub_permutations = []
    for i in sub_permutations:
        if i is not None:
            merged_sub_permutations.append(i)
    return merged_sub_permutations


def compute_sub_permutations_total_len(sub_permutations: List[str]) -> int:
    total_len = 0
    for i in sub_permutations:
        total_len += len(i)
    return total_len


def count_permutations_including(alphabet: str, sub_permutations: List[str]):
    merged_sub_permutations = merge_sub_permutations_list(sub_permutations)
    if len(merged_sub_permutations) == 0:
        return 0
    alphabet_len = len(alphabet)
    sub_permutations_total_len = compute_sub_permutations_total_len(merged_sub_permutations)
    sub_permutations_count = len(merged_sub_permutations)
    diff_len = alphabet_len - sub_permutations_total_len
    if diff_len < 0:
        return 0
    permutations_including = compute_special_sum(diff_len, sub_permutations_count) * math.factorial(
        diff_len) * math.factorial(sub_permutations_count)
    return permutations_including


def select_from_bads_by_binary_number(bads: List[str], number: int) -> Tuple[List[str], int]:
    bits_sum = 0
    selected_items = []
    i = 0
    while number > 0:
        bit = number % 2
        bits_sum += bit
        if bit == 1:
            selected_items.append(bads[i])
        i += 1
        number = (number - bit) / 2
    bits_parity = 1 if bits_sum % 2 == 1 else -1
    return selected_items, bits_parity


def totally_bad(alphabet: str, bads: List[str]) -> int:
    bad_permutations = 0
    bads_count = len(bads)
    bads_sets = pow(2, bads_count)
    for i in range(1, bads_sets):
        (selected_bads, bits_parity) = select_from_bads_by_binary_number(bads, i)
        curr_bad_permutations = count_permutations_including(alphabet, selected_bads)
        bad_permutations += curr_bad_permutations * bits_parity
    return bad_permutations


def totally_good(alphabet: str, bads: List[str]) -> int:
    return math.factorial(len(alphabet)) - totally_bad(alphabet, bads)


if __name__ == '__main__':
    __result = totally_good('ABC', ['AB', 'CA'])
    print(__result)
