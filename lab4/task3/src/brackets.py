from utils import read, write
from lab4.task13.src.stack import Stack


def brackets_check(brackets):
    stack = Stack()
    for item in brackets:
        if item in '])':
            if stack.is_empty():
                return False
            last_item = stack.pop()
            if (item + last_item == '](') or (item + last_item == ')['):
                return False
        else:
            stack.push(item)
    return stack.is_empty()


def main():
    brackets_list = read(type_convert=str)
    write(end='')
    for brackets, in brackets_list:
        write('YES' if brackets_check(brackets) else 'NO', to_end=True)


if __name__ == '__main__':
    main()
