def merge(array, p, q, r):
    left_array = array[p:q + 1] + [float('inf')]
    right_array = array[q + 1:r + 1] + [float('inf')]
    i, j = 0, 0
    for k in range(p, r + 1):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1


def merge_sort(array, p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(array, p, q)
    merge_sort(array, q + 1, r)
    merge(array, p, q, r)



if __name__ == '__main__':
    with open('input.txt') as f:
        n, array1 = f.readlines()
    array = list(map(int, array1.split()))
    merge_sort(array, 0, len(array) - 1)
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)