import sys


def monitoring(n, m, matrix):
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print('')


def read_input():
    n, m = int(input()), int(input())

    matrix = []
    for _ in range(n):
        line = sys.stdin.readline().strip()
        matrix.append(line.split())
    return n, m, matrix


if __name__ == "__main__":
    n, m, matrix = read_input()
    monitoring(n, m, matrix)
