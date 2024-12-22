from utils import write, read


def tree_height(n, parents):
    children = [[] for _ in range(n)]
    root = -1
    for child, parent in enumerate(parents):
        if parent != -1:
            children[parent].append(child)
        else:
            root = child

    def calc_height(node):
        if not children[node]:
            return 1
        max_height = 0
        for child in children[node]:
            max_height = max(max_height, calc_height(child))
        return max_height + 1

    return calc_height(root)


def main():
    write(end='')
    (n,), array = read(type_convert=int)
    write(tree_height(n, array), to_end=True)


if __name__ == '__main__':
    main()
