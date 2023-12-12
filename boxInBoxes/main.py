from typing import List, TypeVar

box_height_cache = {}
box_str_cache = {}


def get_box_height(size: int) -> int:
    if size == 1:
        return 2
    if box_height_cache.get(size) is not None:
        return box_height_cache.get(size)
    heights_sum = 1 - (size - 2)
    for i in range(1, size):
        heights_sum += get_box_height(i)
    box_height_cache[size] = heights_sum
    return heights_sum


def get_box_width(size: int) -> int:
    return 3 if size == 1 else 2 + get_box_width(size - 1)


def get_roof_list(size: int) -> List[str]:
    str_len = get_box_width(size)
    roof_list = []
    for i in range(0, str_len):
        if i % 2 == 0:
            roof_list.append(" ")
        else:
            roof_list.append("_")
    return roof_list


def get_boundary_list(size: int) -> List[str]:
    str_len = get_box_width(size)
    boundary_list = ["|"]
    for i in range(0, str_len - 2):
        boundary_list.append(" ")
    boundary_list.append("|")
    return boundary_list


def get_foundation_list(size: int) -> List[str]:
    str_len = get_box_width(size)
    roof_list = []
    for i in range(0, str_len):
        if i % 2 == 0:
            roof_list.append("|")
        else:
            roof_list.append("_")
    return roof_list


T = TypeVar('T')


def last(elem_list: List[T]) -> T:
    return elem_list[len(elem_list) - 1]


def get_box_list(size: int) -> List[List[str]]:
    if size == 1:
        return [
            [" ", "_", " "],
            ["|", "_", "|"]
        ]
    if box_str_cache.get(size) is not None:
        return box_str_cache.get(size)
    box_list = []
    box_width = get_box_width(size)
    box_list.append(get_roof_list(size))
    for i in range(1, size):
        little_box = get_box_list(i)
        little_box_height = get_box_height(i)
        for j in range(0, little_box_height):
            little_box_layer = little_box[j]
            little_box_width = get_box_width(i)
            take_previous_list = j == 0 and i > 1
            last_layer = i == size - 1 and j == little_box_height - 1
            next_boundary_list = last(box_list) if take_previous_list else (get_foundation_list(
                size) if last_layer else get_boundary_list(size))
            for k in range(0, little_box_width):
                if little_box_layer[little_box_width - 1 - k] != " ":
                    next_boundary_list[box_width - 1 - k] = little_box_layer[little_box_width - 1 - k]
            if not take_previous_list:
                box_list.append(next_boundary_list)
    box_str_cache[size] = box_list
    return box_list


def draw_box_list(box_list: List[List[str]]):
    str_list = []
    for i in box_list:
        str_list.append("".join(i))
    return "\n".join(str_list)


def draw(size: int) -> str:
    box_list = get_box_list(size)
    return draw_box_list(box_list)


if __name__ == '__main__':
    box_size = 10
    box_str = draw(box_size)
    print(box_str)
