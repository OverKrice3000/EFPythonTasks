from typing import List

from digitalStringUtils import calculate_number_position_in_infinite_digital_string, test_for_reverse_digit_step, \
    prepend_placeholders, append_placeholders, increment_digital_string, left_shift_by_right_shift
import unittest


# First string is an end of n digit number
# Second string is a start of n digit number
# Returns first number or -1 if strings are incompatible
def test_digital_substrings(first: str, second: str, n: int) -> int:
    if second[0] == '0':
        return -1
    if len(first) == n and first[0] == '0':
        return -1
    if test_for_reverse_digit_step(first, second, n):
        return int('9' * (n - 1))
    prepended_first = prepend_placeholders(increment_digital_string(first), n, '?')
    appended_second = append_placeholders(second, n)
    result_string = ''
    for i in range(0, len(prepended_first)):
        if prepended_first[i] == '?':
            result_string += appended_second[i]
        elif appended_second[i] == '?':
            result_string += prepended_first[i]
        elif prepended_first[i] == appended_second[i]:
            result_string += prepended_first[i]
        else:
            return -1
    return int(result_string) - 1


def split_digital_string(digital_string: str, n: int, shift: int) -> List[str]:
    if len(digital_string) <= n - shift:
        return [digital_string]
    left_split_digital_string = split_digital_string(digital_string[0: len(digital_string) - (n - shift)], n, 0)
    left_split_digital_string.append(digital_string[len(digital_string) - (n - shift): len(digital_string)])
    return left_split_digital_string


# Tests whether digital string starts with n digital number with some shift to the left
# Returns the number if True, -1 if False
def test_digital_string_for_digit_and_shift(digital_string: str, n: int, shift: int) -> int:
    split_string: List[str] = split_digital_string(digital_string, n, shift)
    left_number = -1 if split_string[0][0] == '0' else int(split_string[0])
    for i in reversed(range(1, len(split_string))):
        left_number = test_digital_substrings(split_string[i - 1], split_string[i], n)
        if left_number == -1:
            return -1
        elif len(str(left_number)) == n - 1:
            left_string = ''.join(split_string[0: i])
            return left_number if i == 1 else test_digital_string_for_digit_and_shift(left_string, n - 1, 0)
    return left_number


# Tests whether digital string starts with n digital number
# Returns the number if True, -1 if False
def test_digital_string_for_digit(digital_string: str, n: int) -> int:
    found_positions = []
    for i in range(0, n):
        found_number = test_digital_string_for_digit_and_shift(digital_string, n, i)
        if found_number != -1:
            left_shift = left_shift_by_right_shift(len(digital_string), n, i)
            found_position = calculate_number_position_in_infinite_digital_string(found_number) + left_shift
            if len(str(found_number)) != n:
                found_position -= 1
            found_positions.append(found_position)
    return -1 if len(found_positions) == 0 else min(found_positions)


def find_digital_string_position_in_infinite_digital_string(digital_string: str) -> int:
    digital_string_length = len(digital_string)
    for i in range(1, digital_string_length + 1):
        found_position = test_digital_string_for_digit(digital_string, i)
        if found_position != -1:
            return found_position
    return calculate_number_position_in_infinite_digital_string(int('1' + digital_string)) + 1


if __name__ == '__main__':
    unittest.main()
