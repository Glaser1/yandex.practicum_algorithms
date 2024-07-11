import sys


class Stack:
    def __init__(self, ):
        self.items = []
        self.maximumes = []

    def push(self, n):
        self.items.append(n)
        if not self.maximumes or n >= self.maximumes[-1]:
            self.maximumes.append(n)

    def pop(self):
        if not self.items:
            print('error')
        else:
            if self.maximumes and self.items[-1] == self.maximumes[-1]:
                self.maximumes.pop()
            self.items.pop()

    def get_max(self):
        if not self.maximumes:
            print('None')
        else:
            print(self.maximumes[-1])

    def top(self):
        print(self.items[-1] if self.items else 'error')


if __name__ == '__main__':
    stack = Stack()
    n = int(input())
    for _ in range(n):
        command = sys.stdin.readline().rstrip().split()
        match command[0]:
            case 'get_max':
                stack.get_max()
            case 'push':
                stack.push(int(command[1]))
            case 'pop':
                stack.pop()
            case 'top':
                stack.top()
