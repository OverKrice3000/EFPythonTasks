import sys;
from typing import Any, Tuple


def add(x, y):
    return x + y


def count_calls(func, *args, **kwargs) -> Tuple[int, Any]:
    calls_count = -1

    def tracer(frame, event, arg):
        nonlocal calls_count
        if event == 'call':
            calls_count += 1
        return tracer

    sys.settrace(tracer)
    result = func(*args, **kwargs)
    return calls_count, result


if __name__ == '__main__':
    res = count_calls(add, 1, 2)
    print(res)
