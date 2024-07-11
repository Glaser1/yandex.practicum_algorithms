def brackets_generator(n, i, j, prefix):
    if len(prefix) == 2 * n:
        print(prefix)
    else:
        if i < n:
            brackets_generator(n, i + 1, j, prefix + '(')
        if j < i:
            brackets_generator(n, i, j + 1, prefix + ')')


if __name__ == '__main__':
    n = int(input())
    brackets_generator(n, 0, 0, '')
