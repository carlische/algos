from typing import TypeVar
T = TypeVar('T')


class SinglyLinkedNode:
    def __init__(self, value):
        self.value: T = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def push(self, value: T):
        node = SinglyLinkedNode(value)
        node.next = self.head
        self.head = node
        self.__length += 1

    def pop(self):
        if self.__length == 0:
            raise IndexError()
        pop_node = self.head
        self.head = self.head.next
        self.__length -= 1
        return pop_node.value

    def find(self, value: T):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        raise ValueError()

    def remove_after(self, key: T):
        current_node = self.find(key)
        if current_node.next is None:
            raise IndexError()
        removed_node = current_node.next
        current_node.next = current_node.next.next
        self.__length -= 1
        return removed_node.value

    def print_stack(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next
        print()
