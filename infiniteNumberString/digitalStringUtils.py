from mathUtils import calculate_count_of_digits_in_number, get_first_n_digit_number, calculate_count_of_n_digit_numbers


def calculate_number_position_in_infinite_digital_string(number: int) -> int:
    digits_in_number = calculate_count_of_digits_in_number(number)
    first_n_digit_number = get_first_n_digit_number(digits_in_number)
    number_position = 0
    for i in range(1, digits_in_number):
        number_position += calculate_count_of_n_digit_numbers(i) * i
    n_digit_numbers_before_target = number - first_n_digit_number
    number_position += digits_in_number * n_digit_numbers_before_target
    return number_position


def increment_digital_string(digital_string: str) -> str:
    parsed_number = int(digital_string) + 1
    incremented_string = str(parsed_number)
    if len(digital_string) < len(incremented_string):
        return incremented_string[1:]
    elif len(incremented_string) < len(digital_string):
        incremented_string = prepend_placeholders(incremented_string, len(digital_string), "0")
    return incremented_string


def prepend_placeholders(digital_string: str, n: int, placeholder: str) -> str:
    placeholders_str = placeholder * (n - len(digital_string))
    return placeholders_str + digital_string


def append_placeholders(digital_string: str, n: int) -> str:
    placeholders_str = '?' * (n - len(digital_string))
    return digital_string + placeholders_str


def test_for_reverse_digit_step(first: str, second: str, n: int) -> bool:
    if n < 2:
        return False
    first_sliced = first[1:] if len(first) == n else first
    for i in first_sliced:
        if i != '9':
            return False
    if second[0] != '1':
        return False
    for i in second[1:]:
        if i != '0':
            return False
    return True


def left_shift_by_right_shift(digital_string_len: int, n: int, right_shift: int) -> int:
    nums_left = (digital_string_len - (n - right_shift)) % n
    return 0 if nums_left == 0 else n - nums_left
