s = {}
a = {}

def l(size):
    if size == 1:
        return 2
    if s.get(size) is not None:
        return s.get(size)
    n = 1 - (size - 2)
    for i in range(1, size):
        n += l(i)
    s[size] = n
    return n


def x(size):
    return 3 if size == 1 else 2 + x(size - 1)


def e(size):
    str_len = x(size)
    roof_list = []
    for i in range(0, str_len):
        if i % 2 == 0:
            roof_list.append(" ")
        else:
            roof_list.append("_")
    return roof_list


def i(size):
    str_len = x(size)
    v = ["|"]
    for i in range(0, str_len - 2):
        v.append(" ")
    v.append("|")
    return v


def u(size):
    str_len = x(size)
    roof_list = []
    for i in range(0, str_len):
        if i % 2 == 0:
            roof_list.append("|")
        else:
            roof_list.append("_")
    return roof_list

def last(elem_list):
    return elem_list[len(elem_list) - 1]


def g(b):
    if b == 1:
        return [
            [" ", "_", " "],
            ["|", "_", "|"]
        ]
    if a.get(b) is not None:
        return a.get(b)
    c = []
    d = x(b)
    c.append(e(b))
    for i in range(1, b):
        f = g(i)
        h = l(i)
        for j in range(0, h):
            q = f[j]
            w = x(i)
            r = j == 0 and i > 1
            t = i == b - 1 and j == h - 1
            y = last(c) if r else (u(
                b) if t else i(b))
            for k in range(0, w):
                if q[w - 1 - k] != " ":
                    y[d - 1 - k] = q[w - 1 - k]
            if not r:
                c.append(y)
    a[b] = c
    return c


def draw_box_list(box_list):
    str_list = []
    for i in box_list:
        str_list.append("".join(i))
    return "\n".join(str_list)


def draw(size):
    box_list = g(size)
    return draw_box_list(box_list)
