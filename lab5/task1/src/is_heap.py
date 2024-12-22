from utils import read, write


def is_heap(array_len, array):
    for index in range(array_len // 2):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if array[index] > array[left_index]:
            return 'NO'
        if right_index < len(array) and array[index] > array[right_index]:
            return 'NO'
    return 'YES'


def main():
    write(end='')
    (n, ), array = read(type_convert=int)
    write(is_heap(n, array), to_end=True)


if __name__ == '__main__':
    main()
