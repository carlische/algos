import random
from utils import read, write


def partition3(A, l, r):
    x = A[l]
    m1 = l
    m2 = r
    i = l
    while i <= m2:
        if A[i] < x:
            A[m1], A[i] = A[i], A[m1]
            m1 += 1
            i += 1
        elif A[i] > x:
            A[i], A[m2] = A[m2], A[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2


def randomized_quick_sort_p3(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r)
        randomized_quick_sort_p3(A, l, m1-1)
        randomized_quick_sort_p3(A, m2+1, r)
    return A


def main():
    write(end='')
    (n,), array = read(type_convert=int)
    write(*randomized_quick_sort_p3(array, 0, n - 1), to_end=True)


if __name__ == '__main__':
    main()
