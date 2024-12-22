from utils import write, read


class QueueWithMin:
    def __init__(self):
        self.queue = []
        self.minimum = float('+inf')

    def push(self, value):
        self.queue.append(int(value))
        if int(value) < self.minimum:
            self.minimum = int(value)

    def pop(self):
        if not self.queue:
            raise IndexError()
        del_value = self.queue.pop(0)
        if del_value == self.minimum:
            self.minimum = float('+inf')
            for value in self.queue:
                if int(value) < self.minimum:
                    self.minimum = int(value)

    def get_min(self):
        if not self.queue:
            raise IndexError()
        return self.minimum


def main():
    queue = QueueWithMin()
    write(end='')
    for line in read(type_convert=str):
        if line[0] == '+':
            value = line[1]
            queue.push(value)
        elif line[0] == '-':
            queue.pop()
        else:
            write(queue.get_min(), sep='\n', to_end=True)


if __name__ == '__main__':
    main()
