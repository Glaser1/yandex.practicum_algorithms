def neighbours(n, m, matrix, row, col):
    max_row = n - 1
    max_col = m - 1
    result = []
    if 0 < row < max_row:
        result.append(matrix[row - 1][col])
        result.append(matrix[row + 1][col])
    elif row == 0 and max_row != row:
        result.append(matrix[row + 1][col])
    elif row != 0 and max_row == row:
        result.append(matrix[row - 1][col])

    if col == 0 and col != max_col:
        result.append(matrix[row][col + 1])
    elif col != 0 and col == max_col:
        result.append(matrix[row][col - 1])
    elif 0 < col < max_col:
        result.append(matrix[row][col-1])
        result.append(matrix[row][col+1])

    return sorted(result)


def read_input():
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return n, m, matrix, row, col


if __name__ == '__main__':
    n, m, matrix, row, col = read_input()
    print(*neighbours(n, m, matrix, row, col))
