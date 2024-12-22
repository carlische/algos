from utils import read, write
from collections import OrderedDict


def associative_array(commands):
    assoc_array = OrderedDict()
    results = []

    for parts in commands:
        command = parts[0]

        if command == "put":
            x, y = parts[1], parts[2]
            if x in assoc_array:
                assoc_array[x] = y
            else:
                assoc_array[x] = y

        elif command == "get":
            x = parts[1]
            results.append(assoc_array.get(x, "<none>"))

        elif command == "prev":
            x = parts[1]
            if x in assoc_array:
                keys = list(assoc_array.keys())
                idx = keys.index(x)
                if idx > 0:
                    results.append(assoc_array[keys[idx - 1]])
                else:
                    results.append("<none>")
            else:
                results.append("<none>")

        elif command == "next":
            x = parts[1]
            if x in assoc_array:
                keys = list(assoc_array.keys())
                idx = keys.index(x)
                if idx < len(keys) - 1:
                    results.append(assoc_array[keys[idx + 1]])
                else:
                    results.append("<none>")
            else:
                results.append("<none>")

        elif command == "delete":
            x = parts[1]
            assoc_array.pop(x, None)

    return results


def main():
    write(end='')
    array = read(type_convert=str)
    result = associative_array(array)
    for line in result:
        write(line, to_end=True)


if __name__ == '__main__':
    main()
