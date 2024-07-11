def evenly_odd_numbers(a, b, c):
    if a % 2 == b % 2 == c % 2:
        return 'WIN'
    return 'FAIL'


def read_input():
    a, b, c = map(int, input().split())
    return a, b, c


if __name__ == '__main__':
    a, b, c = read_input()
    print(evenly_odd_numbers(a, b, c))
