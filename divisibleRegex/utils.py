def find_greatest_pow_of_two(n: int) -> int:
    current_pow = 0
    while True:
        if pow(2, current_pow) > n:
            return current_pow - 1
        elif pow(2, current_pow) == n:
            return current_pow
        current_pow += 1


def to_binary(n: int, padding=0) -> str:
    binary_str_list = []
    while n > 0:
        remainder = n % 2
        binary_str_list.append(str(remainder))
        n = int((n - remainder) / 2)
    binary_str_list.reverse()
    binary_str = ''.join(binary_str_list)
    if len(binary_str) < padding:
        binary_str = ('0' * (padding - len(binary_str))) + binary_str
    return binary_str