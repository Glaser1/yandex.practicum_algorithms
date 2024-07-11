import sys


class Deque:
    def __init__(self, m):
        self.queue = [None] * m
        self.size = 0
        self.head = 0
        self.tail = 0
        self.max_m = m

    def push_back(self, item):
        if self.size != self.max_m:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_m
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.size:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head+1) % self.max_m
            self.size -= 1
            return x
        return 'error'

    def pop_back(self):
        if self.size:
            x = self.queue[self.tail-1]
            self.queue[self.tail-1] = None
            self.tail -= 1
            self.size -= 1
            return x
        return 'error'

    def push_front(self, item):
        if self.size != self.max_m:
            if self.head == self.tail:
                self.tail = (self.tail+1) % self.max_m
            else:
                self.head -= 1
            self.queue[self.head] = item
            self.size += 1
        else:
            print('error')


if __name__ == "__main__":
    n, m = int(input()), int(input())
    deque = Deque(m)

    for _ in range(n):
        line = sys.stdin.readline().split()
        command = line[0]
        if command == "push_back":
            deque.push_back(int(line[1]))
        elif command == "push_front":
            deque.push_front(int(line[1]))
        elif command == "pop_back":
            print(deque.pop_back())
        elif command == "pop_front":
            print(deque.pop_front())
