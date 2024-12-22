def s_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, array_1 = f.readlines()
    array_2 = s_sort(list(map(int, array_1.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array_2))), file=f)