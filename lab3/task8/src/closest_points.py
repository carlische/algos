from utils import read, write


def partition(A, l, r):
    x = A[l][0]
    j = l
    for i in range(l+1, r+1):
        if A[i][0] < x:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[l], A[j] = A[j], A[l]
    return j


def quick_sort(A, l, r):
    if l < r:
        j = partition(A, l, r)
        quick_sort(A, l, j-1)
        quick_sort(A, j+1, r)


def closest_points(array, k):
    points = []
    for cord in array:
        x, y = cord
        distance = int((x**2 + y**2)**0.5)
        points.append([distance, [x, y]])
    quick_sort(points, 0, len(points)-1)
    return [elem[1] for elem in points[:k]]


def main():
    write(end='')
    data = [list(line) for line in read(type_convert=int)]
    n, k = data[0]
    array = data[1:]
    write(*closest_points(array, k), to_end=True)


if __name__ == '__main__':
    main()
