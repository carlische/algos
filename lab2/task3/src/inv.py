def merge_and_count(array, temp_array, p, q, right):
    i = p
    j = q + 1
    k = p
    counter = 0
    while i <= q and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            counter += (q - i + 1)
            j += 1
        k += 1
    while i <= q:
        temp_array[k] = array[i]
        i += 1
        k += 1
    while j <= right:
        temp_array[k] = array[j]
        j += 1
        k += 1
    for i in range(p, right + 1):
        array[i] = temp_array[i]
    return counter


def merge_sort_and_count(array, temp_array, p, right):
    counter = 0
    if p < right:
        middle = (p + right) // 2
        counter += merge_sort_and_count(array, temp_array, p, middle)
        counter += merge_sort_and_count(array, temp_array, middle + 1, right)
        counter += merge_and_count(array, temp_array, p, middle, right)
    return counter


if __name__ == '__main__':
    with open('input.txt') as f:
        n, array1 = f.readlines()
    array = list(map(int, array1.split()))
    temp_array = [0] * len(array)
    inv_count = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
    with open('output.txt', 'w') as f:
        print(inv_count, file=f)