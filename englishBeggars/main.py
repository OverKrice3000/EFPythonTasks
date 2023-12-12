def beggars(values, n):
    if n == 0:
        return []
    earn = []
    for i in range(0, n):
        earn.append(0)
    for i in range(0, len(values)):
        earn[i % n] += values[i]
    return earn

if __name__ == '__main__':
    solution = beggars([1, 2, 3, 4, 5], 2)
    print(solution)