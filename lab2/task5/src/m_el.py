def majority_element(array):
    tmp = None
    counter = 0
    for i in array:
        if counter == 0:
            tmp = i
        counter += 1 if i == tmp else -1
    if array.count(tmp) > len(array) // 2:
        return 1
    return None


if __name__ == '__main__':
    with open('input.txt') as f:
        n, array1 = f.readlines()
    array = list(map(int, array1.split()))
    result = majority_element(array)
    with open('output.txt', 'w') as f:
        print(result if result else "Нет элемента большинства", file=f)