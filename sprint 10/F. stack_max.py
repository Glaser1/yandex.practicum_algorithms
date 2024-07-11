import sys


class Stack:
    def __init__(self, ):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        if not self.items:
            print('error')
        else:
            self.items.pop()

    def get_max(self):
        if not self.items:
            print('None')
        else:
            print(max(self.items))


if __name__ == '__main__':
    stack = Stack()
    n = int(input())
    for _ in range(n):
        command = sys.stdin.readline().rstrip().split()

        if command[0] == 'get_max':
            stack.get_max()
        elif command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            stack.pop()
