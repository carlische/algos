from utils import read, write


def is_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n


def is_fibonacci(n):
    if is_perfect_square(5 * n**2 + 4) or is_perfect_square(5 * n**2 - 4):
        return 'Yes'
    return 'No'


def main():
    write(end='')
    data = [line[0] for line in read(type_convert=int)][1:]
    for line in data:
        write(is_fibonacci(line), to_end=True)


if __name__ == '__main__':
    main()
