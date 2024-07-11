def two_bicycles(numbers, s, left, right):
    mid = (left + right) // 2
    if numbers[left] >= s:
        return left + 1
    elif numbers[mid] >= s:
        return two_bicycles(numbers, s, left, mid)
    return two_bicycles(numbers, s, mid+1, right)


def read_input():
    n = int(input())
    numbers = list(map(int, input().split()))
    s = int(input())
    return n, numbers, s


if __name__ == '__main__':
    n, numbers, s = read_input()
    left = 0
    right = n - 1
    result_1 = two_bicycles(numbers, s, left, right) if s <= numbers[right] else -1
    result_2 = two_bicycles(numbers, 2 * s, left, right) if 2 * s <= numbers[right] else -1
    print(result_1, result_2)
