def recursive_fibonacci_numbers(n):
    if n == 0 or n == 1:
        return 1
    return recursive_fibonacci_numbers(n - 1) + recursive_fibonacci_numbers(n - 2)


if __name__ == '__main__':
    print(recursive_fibonacci_numbers(5))
