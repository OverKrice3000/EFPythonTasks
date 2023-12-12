def get_first_n_digit_number(n: int) -> int:
    return pow(10, n - 1)


def calculate_count_of_n_digit_numbers(n: int) -> int:
    return get_first_n_digit_number(n + 1) - get_first_n_digit_number(n)


def calculate_count_of_digits_in_number(number: int) -> int:
    return 1 if number == (number % 10) else 1 + calculate_count_of_digits_in_number(
        round((number - (number % 10)) / 10))
