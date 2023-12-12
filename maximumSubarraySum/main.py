def max_sequence(arr):
    maximum_sum = 0
    cur_sum = 0
    for i in arr:
        cur_sum += i
        if maximum_sum < cur_sum:
            maximum_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0
    return maximum_sum

if __name__ == '__main__':
    maximum = max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(maximum)

