import sys


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return x

    def peek(self):
        return self.queue[self.head] if self.queue[self.head] else None


if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    for _ in range(n):
        commands = sys.stdin.readline().split()
        command = commands[0]

        if command == 'peek':
            print(queue.peek())
        elif command == 'push':
            queue.push(int(commands[1]))
        elif command == 'pop':
            print(queue.pop())
        elif command == 'size':
            print(queue.size)
