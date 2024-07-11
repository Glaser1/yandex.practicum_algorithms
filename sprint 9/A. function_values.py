def function_values(a, x, b, c):
    return a * x * x + b * x + c


def read_input():
    a, x, b, c = map(int, input().split())
    return a, x, b, c


if __name__ == '__main__':
    a, x, b, c = read_input()
    print(function_values(a, x, b, c))
