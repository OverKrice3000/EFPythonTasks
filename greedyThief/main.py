from collections import namedtuple
from typing import List, Tuple

Item = namedtuple('Item', 'weight price')
epsilon = 1e-7


def sort_items_by_rate_desc(items: List[Item]):
    items.sort(key=lambda item: item.price / (item.weight + epsilon), reverse=True)
    return items


def sort_items_by_price_asc(items: List[Item]):
    items.sort(key=lambda item: item.price)
    return items


def calculate_critical_index(sorted_items: List[Item], weight: int) -> int:
    total_weight = 0
    for i in range(0, len(sorted_items)):
        total_weight += sorted_items[i].weight
        if total_weight > weight:
            return i
    return len(sorted_items)


def calculate_best_alternative(sorted_items: List[Item], my_items: List[Item], weight: int, start_index=None,
                               end_index=None) -> Tuple[List[Item], int, int]:
    alternative_items = []
    alternative_weight = 0
    alternative_price = 0
    start_index = 0 if start_index is None else start_index
    end_index = len(sorted_items) if end_index is None else end_index
    for i in range(start_index, end_index):
        if alternative_weight + sorted_items[i].weight <= weight and sorted_items[i] not in my_items:
            alternative_items.append(sorted_items[i])
            alternative_weight += sorted_items[i].weight
            alternative_price += sorted_items[i].price
    return alternative_items, alternative_weight, alternative_price


def try_add_item(sorted_items: List[Item], my_items: List[Item], critical_item_index: int, extra_weight: int) -> Tuple[
    List[Item], int, bool]:
    critical_item = sorted_items[critical_item_index]
    sorted_by_price_items = sort_items_by_price_asc(my_items.copy())

    items_to_remove = []
    removed_weight = 0
    extra_price = critical_item.price

    for item in sorted_by_price_items:
        items_to_remove.append(item)
        removed_weight += item.weight
        extra_price -= item.price
        if removed_weight + extra_weight >= critical_item.weight:
            break
    if extra_weight + removed_weight < critical_item.weight:
        return [], 0, False
    for item in items_to_remove:
        sorted_by_price_items.remove(item)
    sorted_by_price_items.append(critical_item)
    (alternative_items, alternative_weight, alternative_price) = calculate_best_alternative(sorted_items,
                                                                                            sorted_by_price_items,
                                                                                            removed_weight + extra_weight - critical_item.weight,
                                                                                            end_index=critical_item_index)
    extra_price += alternative_price
    for item in alternative_items:
        try:
            items_to_remove.remove(item)
        except ValueError:
            pass

    return items_to_remove, extra_price, True


def greedy_thief(items: List[Item], weight: int) -> List[Item]:
    sorted_items = sort_items_by_rate_desc(items.copy())
    max_price = 0
    max_items = []
    my_weight = 0
    my_price = 0
    my_items = []
    critical_item_index = calculate_critical_index(sorted_items, weight)
    for i in range(0, critical_item_index):
        my_items.append(sorted_items[i])
        my_weight += sorted_items[i].weight
        my_price += sorted_items[i].price
    (alternative_items, alternative_weight, alternative_price) = calculate_best_alternative(sorted_items, my_items,
                                                                                            weight - my_weight)
    max_price = my_price + alternative_price
    max_items = my_items.copy()
    max_items.extend(alternative_items)

    for i in range(critical_item_index, len(sorted_items)):
        (best_to_remove, extra_price, can_add) = try_add_item(sorted_items, my_items, i, weight - my_weight)
        if not can_add:
            continue
        for item in best_to_remove:
            my_items.remove(item)
            my_weight -= item.weight
            my_price -= item.price
        my_items.append(sorted_items[i])
        my_weight += sorted_items[i].weight
        my_price += sorted_items[i].price
        (alternative_items, alternative_weight, alternative_price) = calculate_best_alternative(sorted_items, my_items,
                                                                                                weight - my_weight)
        max_price_candidate = my_price + alternative_price
        if max_price < max_price_candidate:
            max_price = max_price_candidate
            max_items = my_items.copy()
            max_items.extend(alternative_items)
    return max_items


if __name__ == '__main__':
    __items = [
        Item(weight=9, price=1),
        Item(weight=9, price=2),
        Item(weight=9, price=3),
        Item(weight=9, price=4),
        Item(weight=9, price=5),
    ]
    __weight = 8

    result = greedy_thief(__items, __weight)
    print(result)
