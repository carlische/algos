from utils import read, write


def operations(data):
    result = []
    current_set = set()
    for line in data:
        operation, x = line
        if operation == 'A':
            current_set.add(x)
        elif operation == 'D':
            current_set.discard(x)
        elif operation == '?':
            if x in current_set:
                result.append('Y')
            else:
                result.append('N')
    return result


def main():
    write(end='')
    array = read(type_convert=str)
    result = operations(array)
    for line in result:
        write(line, to_end=True)


if __name__ == '__main__':
    main()
