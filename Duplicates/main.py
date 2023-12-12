from typing import List, Dict


def process_array(obj: Dict[str, List[str]], key: str, char_dict: Dict[str, bool]):
    new_arr = []
    for i in obj[key]:
        cached_char = char_dict.get(i)
        if cached_char is None:
            new_arr.append(i)
            char_dict[i] = True
    obj[key] = new_arr


def remove_duplicate_ids(obj: Dict[str, List[str]]):
    char_dict: Dict[str, bool] = {}
    for i in sorted(obj.keys(), key=lambda x: int(x), reverse=True):
        process_array(obj, i, char_dict)
    return obj


if __name__ == '__main__':
    pass
