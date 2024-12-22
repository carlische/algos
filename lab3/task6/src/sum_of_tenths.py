from utils import read, write


def quick_sort(A, l, r):
    if l < r:
        m = partition(A, l, r)
        quick_sort(A, l, m-1)
        quick_sort(A, m+1, r)


def partition(A, l, r):
    x = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] <= x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j


def sum_of_tenths(A, B):
    C = []
    for b in B:
        for a in A:
            C.append(a * b)
    quick_sort(C, 0, len(C)-1)
    sum_of_tenths = sum(C[i] for i in range(0, len(C), 10))
    return sum_of_tenths


def main():
    write(end='')
    data = [list(line) for line in read(type_convert=int)]
    n, m = data[0]
    A, B = data[1], data[2]
    write(sum_of_tenths(A, B), to_end=True)


if __name__ == '__main__':
    main()
