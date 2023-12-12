import re

regex_symbols_reverse_map = {'^': '$', '$': '^', '(': ')', ')': '('}


def get_reversed_regex_symbol(symbol: str):
    reverse_symbol = regex_symbols_reverse_map.get(symbol)
    return symbol if reverse_symbol is None else reverse_symbol


def reverse_regex(regex: str):
    reverse_regex_list = []
    for symbol in re.findall(r'(?:\\.|\[(?:\\?.)+?\]|.)(?:[?+*]|\{.+?\})?', regex)[::-1]:
        reverse_regex_list.append(get_reversed_regex_symbol(symbol))
    return "".join(reverse_regex_list)


if __name__ == '__main__':
    reversed_regex = reverse_regex("abc")
    print(reversed_regex)
