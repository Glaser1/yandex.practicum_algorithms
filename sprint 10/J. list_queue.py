import sys


class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self):
        if self.size:
            node_to_delete = self.head
            self.head = self.head.next_item
            self.size -= 1
            return node_to_delete.value
        return 'error'

    def put(self, node):
        if not self.size:
            self.head = self.tail = node
        else:
            self.tail.next_item = node
            self.tail = self.tail.next_item
        self.size += 1


if __name__ == '__main__':
    queue = Queue()
    n = int(input())

    for _ in range(n):
        commands = sys.stdin.readline().rstrip().split()
        command = commands[0]
        if command == 'get':
            print(queue.get())
        elif command == 'put':
            node = Node(int(commands[1]))
            queue.put(node)
        elif command == 'size':
            print(queue.size)
