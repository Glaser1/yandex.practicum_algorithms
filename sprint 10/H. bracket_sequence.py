import sys


BRACKETS_MAPPING = {
    '{': '}',
    '[': ']',
    '(': ')'
}

class Stack:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        if not self.items:
            print('error')
        else:
            return self.items.pop()


def is_correct_bracket_seq(stack, bracket_seq):
    if bracket_seq.strip() == '':
        return True
    elif len(bracket_seq) % 2 != 0:
        return False

    for el in bracket_seq:
        if el in ('{', '[', '('):
            stack.push(el)
        else:
            if stack.items and el == BRACKETS_MAPPING[stack.items[-1]]:
                stack.pop()
            else:
                return False
    return True


if __name__ == '__main__':
    stack = Stack()
    bracket_seq = input()
    print(is_correct_bracket_seq(stack, bracket_seq))
