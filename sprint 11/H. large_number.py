def which_is_larger(num_1, num_2):
    if int(num_2 + num_1) > int(num_1 + num_2):
        return True
    return False


def large_number(numbers, n, key):
    for i in range(n):
        for j in range(n-1-i):
            if key(numbers[j], numbers[j+1]):
                numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
    return ''.join(numbers)


def read_input():
    n = int(input())
    numbers = [x for x in input().split()]
    return n, numbers


if __name__ == '__main__':
    n, numbers = read_input()
    print(large_number(numbers, n, which_is_larger))
