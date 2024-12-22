from utils import read, write

def scarecrow_sort(n, k, array):
    for i in range(0, n-k):
        if array[i] > array[i+k]:
            array[i], array[i+k] = array[i+k], array[i]
    return "YES" if array == sorted(array) else "NO"


def main():
    write(end='')
    data = [list(line) for line in read(type_convert=int)]
    n, k = data[0]
    array = data[1]
    write(scarecrow_sort(n, k, array), to_end=True)


if __name__ == '__main__':
    main()
