def modulo_fibonacci(n, k):
    a, b = 0, 1

    for i in range(n+1):
        a, b = b, (a + b) % 10 ** k
        print(i, a, b)
    return a


if __name__ == '__main__':
    command = input().split()
    n = int(command[0])
    k = int(command[1])
    print(modulo_fibonacci(n, k))
