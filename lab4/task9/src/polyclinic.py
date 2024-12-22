from utils import write, read


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class Queue:
    def __init__(self):
        self.head = None
        self.middle = None
        self.end = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def push_to_end(self, item):
        node = Node(item)
        node.previous = self.end
        if node.previous is not None:
            node.previous.next = node
            if self.__length % 2 == 0:
                self.middle = self.middle.next
        else:
            self.head = self.middle = node
        self.end = node
        self.__length += 1

    def push_to_middle(self, item):
        node = Node(item)
        node.previous = self.middle
        if self.middle is not None:
            node.next = self.middle.next
            self.middle.next = node
            if node.next is not None:
                node.next.previous = node
            else:
                self.end = node
            if self.__length % 2 == 0:
                self.middle = self.middle.next
        else:
            self.head = self.middle = self.end = node
        self.__length += 1

    def pop_from_head(self):
        if self.__length == 0:
            raise IndexError
        if self.__length % 2 == 0:
            self.middle = self.middle.next
        pop_node = self.head
        self.head = self.head.next
        self.__length -= 1
        if self.__length == 0:
            self.middle = self.end = None
        return pop_node.value

    def print(self):
        node = self.head
        while node is not None:
            print(node, end=' ')
            node = node.next
        print()


def main():
    queue = Queue()
    write(end='')
    for line in read(type_convert=str):
        if line[0] == '+':
            queue.push_to_end(line[1])
        elif line[0] == '*':
            queue.push_to_middle(line[1])
        else:
            write(queue.pop_from_head(), sep='\n', to_end=True)


if __name__ == '__main__':
    main()
