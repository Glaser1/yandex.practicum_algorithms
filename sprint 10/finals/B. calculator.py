class Stack:
    def __init__(self):
        self.items = []

    def peek(self):
        if self.items:
            return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
    }
    command = input().split(' ')
    stack = Stack()
    for el in command:
        if el.lstrip('-').isdigit():
            stack.items.append(int(el))
        else:
            a, b = stack.pop(), stack.pop()
            stack.push(operations[el](b, a))
    print(stack.peek())
