def bubble_sort(numbers, n):
    sorted_flag = True
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
                sorted_flag = False
        if not swapped:
            break
        print(' '.join(map(str, numbers)))
    if sorted_flag:
        print(' '.join(map(str, numbers)))


def read_input():
    n = int(input())
    numbers = list(map(int, input().split()))
    return n, numbers


if __name__ == "__main__":
    n, numbers = read_input()
    bubble_sort(numbers, n)
