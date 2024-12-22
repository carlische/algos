from lab4.task13.src.stack import Stack
from utils import read, write


def addition(x, y): return x + y
def subtraction(x, y): return x - y
def multiplication(x, y): return x * y


operators = {'+': addition, '-': subtraction, '*': multiplication}


def postfix_notation(expression):
    stack = Stack()
    for operator in expression:
        if operator in operators:
            y, x = stack.pop(), stack.pop()
            stack.push(operators[operator](x, y))
        else:
            try:
                stack.push(int(operator))
            except ValueError:
                raise KeyError()
    return stack.pop()


def main():
    expression, = read(type_convert=str)
    write(postfix_notation(expression))


if __name__ == '__main__':
    main()
