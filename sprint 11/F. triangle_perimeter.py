def triangle_perimeter(k, numbers):
    numbers = sorted(numbers, reverse=True)
    for i in range(k):
        if numbers[i] < sum(numbers[i+1:i+3]):
            return numbers[i] + sum(numbers[i+1:i+3])


def read_input():
    k = int(input())
    numbers = list(map(int, input().split()))
    return k, numbers


if __name__ == "__main__":
    k, numbers = read_input()
    print(triangle_perimeter(k, numbers))
