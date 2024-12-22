from utils import read, write
from bisect import bisect_left


def subsequence(n, sequence):
    lis = []
    parent = [-1] * n
    indexes = []

    for i in range(n):
        pos = bisect_left(lis, sequence[i])
        if pos == len(lis):
            lis.append(sequence[i])
            indexes.append(i)
        else:
            lis[pos] = sequence[i]
            indexes[pos] = i

        if pos > 0:
            parent[i] = indexes[pos - 1]

    lis_length = len(lis)
    lis_sequence = []
    current_index = indexes[-1]

    for _ in range(lis_length):
        lis_sequence.append(sequence[current_index])
        current_index = parent[current_index]

    lis_sequence.reverse()
    return [lis_length], lis_sequence


def main():
    write(end='')
    data = [line for line in read(type_convert=int)]
    n = data[0][0]
    array = data[1]
    result = subsequence(n, array)
    for line in result:
        write(*line, to_end=True)


if __name__ == '__main__':
    main()
