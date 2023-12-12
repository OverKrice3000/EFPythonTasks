from typing import Any, Set, Tuple

NULL_SET = set()
A = {1}
B = {1, 2}
C = {1, 2, 3}
X = {'a'}
Y = {'a', 'b'}
Z = {'a', 'b', 'c'}

def cart_prod(*sets: Set[Any]) -> Set[Tuple[Any, ...]]:
    if len(sets) == 0:
        empty_set = set()
        empty_set.add(())
        return empty_set
    sets_head = sets[0]
    sets_tail = sets[1:]
    if len(sets_tail) == 0:
        basic_set = set()
        for i in sets_head:
            basic_set.add((i,))
        return basic_set
    little_cart_prod = cart_prod(*sets_tail)
    cartesian_product = set()
    for i in sets_head:
        for j in little_cart_prod:
            cartesian_product.add((i,) + j)
    return cartesian_product


if __name__ == '__main__':
    prod = cart_prod(X, A)
    print(prod)