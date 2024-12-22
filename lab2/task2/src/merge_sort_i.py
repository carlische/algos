def merge_with_indices(array, p, q, r):
    left_array = array[p:q + 1] + [float('inf')]
    right_array = array[q + 1:r + 1] + [float('inf')]
    i, j = 0, 0
    print(f"Индексы {p + 1}-{r + 1}, значения: {array[p]}-{array[r]}")
    for k in range(p, r + 1):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1


def merge_sort_with_indices(array, p, r):
    if p >= r:
        return

    middle = (p + r) // 2
    merge_sort_with_indices(array, p, middle)
    merge_sort_with_indices(array, middle + 1, r)
    merge_with_indices(array, p, middle, r)


if __name__ == '__main__':
    with open('input.txt') as f:
        n, array1 = f.readlines()
    array = list(map(int, array1.split()))
    merge_sort_with_indices(array, 0, len(array) - 1)
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)