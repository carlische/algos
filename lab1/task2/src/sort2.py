def insertion_sort(arr):
    index = [0]
    counter = 0
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = j, i
        counter += 1
        index.append(counter)
    return index, arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, array_1 = f.readlines()
    indexes, array_2 = insertion_sort(list(map(int, array_1.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, indexes))), file=f)
        print(' '.join(list(map(str, array_2))), file=f)