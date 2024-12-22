def binary_search(array, target):
    p = 0
    r = len(array) - 1

    while p <= r:
        q = (p + r) // 2
        if array[q] == target:
            return q
        elif array[q] < target:
            p = q + 1
        else:
            r = q - 1
    return -1


if __name__ == '__main__':
    with open('input.txt') as f:
        n, array1, target = f.readlines()
    array = list(map(int, array1.split()))
    result = binary_search(array, int(target.strip()))
    with open('output.txt', 'w') as f:
        print(result, file=f)