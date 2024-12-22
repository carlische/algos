from lab2.task7.utils import read, write

def find_max_subarray(n, array):
    max_sum = 0
    left = 0
    right = 0
    current_sum = 0
    for i in range(n):
        if current_sum == 0:
            left = i
        current_sum += array[i]
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
            right = i
    return [max_sum, [left, right]]


def main():
    write(end='')
    (n,), array = read(type_convert=int)
    write(*find_max_subarray(n, array), to_end=True)


if __name__ == '__main__':
    main()