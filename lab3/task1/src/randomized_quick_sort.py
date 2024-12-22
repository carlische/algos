import random
from utils import read, write


def partition(A, l, r):
    x = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] < x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j


def randomized_quick_sort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m = partition(A, l, r)
        randomized_quick_sort(A, l, m-1)
        randomized_quick_sort(A, m+1, r)
    return A


def main():
    write(end='')
    (n,), array = read(type_convert=int)
    write(*randomized_quick_sort(array, 0, n - 1), to_end=True)


if __name__ == '__main__':
    main()
