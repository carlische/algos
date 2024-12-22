from lab4.task13.src.singly_linked_list import SinglyLinkedList
from typing import TypeVar
T = TypeVar('T')


class Stack:
    def __init__(self):
        self.stack = SinglyLinkedList()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item: T):
        self.stack.push(item)

    def pop(self):
        return self.stack.pop()
