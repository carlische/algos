def insertion_sort(arr):
    for i in range(1, len(arr)):
        arg = arr[i]
        j = i - 1
        while j >= 0 and arg > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arg
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, array_1 = f.readlines()
    array_2 = insertion_sort(list(map(int, array_1.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array_2))), file=f)