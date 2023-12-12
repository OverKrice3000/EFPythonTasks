import math
from typing import Literal, Union, Tuple, List, Any

OperationType = Union[Literal['max'], Literal['min']]
PowTuple = Tuple[int, int]


def is_prime(n: int) -> bool:
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True


def next_prime(n: int) -> int:
    while True:
        n += 1
        if is_prime(n):
            return n


def find_primes_partition(n: int) -> List[PowTuple]:
    if is_prime(n):
        return [(n, 1)]
    partition = []
    sqrt = math.sqrt(n)
    div = 2
    current_pow = 0
    while n != 1 and div <= sqrt:
        if n % div == 0:
            current_pow += 1
            n = int(n / div)
            if n == 1:
                partition.append((div, current_pow))
            continue
        if current_pow != 0:
            partition.append((div, current_pow))
        div = next_prime(div)
        current_pow = 0
    if n != 1:
        partition.append((n, 1))
    return partition


def compute_starting_maximum(n: int, partition: List[PowTuple]) -> Tuple[List[PowTuple], int]:
    least_base_partition = partition[0]
    least_base = least_base_partition[0]
    return [(least_base, 1), (int(n / least_base), 1)], (int(n / least_base) + least_base) * 2


def compute_partition_product(partition: List[PowTuple]) -> int:
    parts_sum = 0
    pow_sum = 0
    for i in partition:
        parts_sum += pow(i[0], i[1])
        pow_sum += i[1]
    return parts_sum * pow_sum


def compute_grouped_by_pow_partition(partition: List[PowTuple], group_pow: int) -> Tuple[
    List[PowTuple], List[PowTuple]]:
    greater_pow = []
    equal_pow = []
    less_pow = []
    for i in partition:
        if i[1] > group_pow:
            greater_pow.append(i)
        elif i[1] == group_pow:
            equal_pow.append(i)
        else:
            less_pow.append(i)

    pending_partition = []
    determined_partition = []

    pending_partition.extend(less_pow)
    determined_partition_base = 1
    for i in equal_pow:
        determined_partition_base *= i[0]
    for i in greater_pow:
        pow_remainder = i[1] % group_pow
        pow_quotient = int((i[1] - pow_remainder) / group_pow)
        determined_partition_base *= pow(i[0], pow_quotient)
        if pow_remainder != 0:
            pending_partition.append((i[0], pow_remainder))
    determined_partition.append((determined_partition_base, group_pow))
    return determined_partition, pending_partition


def compute_grouped_by_pow_maximum_partition_product(partition: List[PowTuple],
                                                     determined_partition: List[PowTuple] = []) -> Tuple[
    List[PowTuple], int]:
    if len(partition) == 0:
        return determined_partition, compute_partition_product(determined_partition)
    sorted_by_pow_desc_partition = partition.copy()
    sorted_by_pow_desc_partition.sort(key=lambda pow_tuple: pow_tuple[1], reverse=True)
    current_pow = 0
    maximum_product = 0
    maximum_partition = []
    for i in sorted_by_pow_desc_partition:
        if i[1] != current_pow:
            current_pow = i[1]
            (new_determined_partition, pending_partition) = compute_grouped_by_pow_partition(
                sorted_by_pow_desc_partition, current_pow)

            next_determined_partition = determined_partition.copy()
            next_determined_partition.extend(new_determined_partition)
            best_partition, best_product = compute_grouped_by_pow_maximum_partition_product(pending_partition,
                                                                                            next_determined_partition)
            if best_product > maximum_product and best_partition[0][1] != 1:
                maximum_product = best_product
                maximum_partition = best_partition

    return maximum_partition, maximum_product


def find_maximum_product(n: int, partition: List[PowTuple]) -> Tuple[List[PowTuple], int]:
    starting_maximum = compute_starting_maximum(n, partition)
    maximum_grouped_by_pow = compute_grouped_by_pow_maximum_partition_product(partition)
    return starting_maximum if starting_maximum[1] > maximum_grouped_by_pow[1] else maximum_grouped_by_pow


def compute_divisors(partition: List[PowTuple]):
    divisors = []
    for i in partition:
        divisors.append(i[0])
    return divisors


def find_left_divisor(n: int, start: int, determined_partition: List[PowTuple]) -> int:
    divisors = compute_divisors(determined_partition)
    for i in reversed(range(2, start)):
        if n % i == 0 and i not in divisors:
            return i
    return -1


def find_right_divisor(n: int, start: int, determined_partition: List[PowTuple]) -> int:
    divisors = compute_divisors(determined_partition)
    for i in range(start + 1, n):
        if n % i == 0 and i not in divisors:
            return i
    return -1


def find_minimum_partition_for_partition_length(n: int, partition_len: int,
                                                determined_partition: List[PowTuple] = []) -> List[PowTuple]:
    if partition_len == 1:
        divisors = compute_divisors(determined_partition)
        if n in divisors:
            return []
        min_partition = [(n, 1)]
        min_partition.extend(determined_partition)
        return min_partition
    sqrt = int(pow(n, 1 / partition_len))
    if sqrt <= 1:
        return []
    left_divisor = find_left_divisor(n, sqrt, determined_partition)
    left_determined_partition = determined_partition.copy()
    left_determined_partition.append((left_divisor, 1))
    left_partition = find_minimum_partition_for_partition_length(int(n / left_divisor), partition_len - 1,
                                                                 left_determined_partition) if left_divisor != -1 else []
    left_product = compute_partition_product(left_partition)
    right_divisor = find_right_divisor(n, sqrt, determined_partition)
    right_determined_partition = determined_partition.copy()
    right_determined_partition.append((right_divisor, 1))
    right_partition = find_minimum_partition_for_partition_length(int(n / right_divisor), partition_len - 1,
                                                                  right_determined_partition) if right_divisor != -1 else []
    right_product = compute_partition_product(right_partition)
    min_product = min(left_product, right_product)
    min_partition = left_partition if min_product == left_product and len(left_partition) != 0 else right_partition
    return min_partition


def find_minimum_product(n: int, partition: List[PowTuple]) -> Tuple[List[PowTuple], int]:
    minimum_product = compute_partition_product(partition)
    minimum_partition = partition
    partition_length = 2
    while True:
        new_partition = find_minimum_partition_for_partition_length(n, partition_length)
        if len(new_partition) == 0:
            break
        new_partition_product = compute_partition_product(new_partition)
        if new_partition_product < minimum_product:
            minimum_product = new_partition_product
            minimum_partition = new_partition
        if n <= pow((partition_length + 1) / partition_length, partition_length * (partition_length + 1)):
            break
        partition_length += 1

    return minimum_partition, minimum_product


def parse_pow_tuple_list(pow_tuple_list: List[PowTuple]) -> List[int]:
    parsed_list = []
    for i in pow_tuple_list:
        for j in range(0, i[1]):
            parsed_list.append(i[0])
    parsed_list.sort(reverse=True)
    return parsed_list


def find_spec_prod_part(n: int, com: OperationType) -> Union[List[Any], Literal["It is a prime number"]]:
    partition = find_primes_partition(n)
    if partition[0][0] == n:
        return "It is a prime number"
    if com == "max":
        (maximum_partition, maximum_product) = find_maximum_product(n, partition)
        return [parse_pow_tuple_list(maximum_partition), maximum_product]
    if com == "min":
        (minimum_partition, minimum_product) = find_minimum_product(n, partition)
        return [parse_pow_tuple_list(minimum_partition), minimum_product]


if __name__ == '__main__':
    __result = find_spec_prod_part(8232, 'min')
