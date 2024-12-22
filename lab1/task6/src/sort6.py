def b_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(0, l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, array_1 = f.readlines()
    array_2 = b_sort(list(map(int, array_1.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array_2))), file=f)