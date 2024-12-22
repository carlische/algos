def l_search(arr, v):
    result = list()
    for i, num in enumerate(arr):
        if num == v:
            result.append(str(i))
    return result if result else '-1'


if __name__ == '__main__':
    with open('input.txt') as f:
        array, v = f.readlines()
    result = l_search(array.split(), v)
    result = ', '.join(result) if isinstance(result, list) else '-1'
    with open('output.txt', 'w') as f:
        print(result, file=f)