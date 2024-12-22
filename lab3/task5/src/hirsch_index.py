from utils import read, write
from lab3.task1.src.quick_sort import quick_sort


def hirsch_index(citations):
    n = len(citations)
    quick_sort(citations, 0, n-1)
    for h in range(n):
        if (n - h) <= citations[h]:
            return n - h
    return 0


def main():
    write(end='')
    array,  = read(type_convert=int)
    write(hirsch_index(array), to_end=True)


if __name__ == '__main__':
    main()
