def comparison(participant_1, participant_2):
    if participant_1[1] > participant_2[1]:
        return True
    if participant_1[1] < participant_2[1]:
        return False

    if participant_1[2] < participant_2[2]:
        return True

    if participant_1[2] > participant_2[2]:
        return False

    if participant_1[0] < participant_2[0]:
        return True

    return False


def in_place_quick_sort(numbers, left, right):
    l, r = left, right
    if left >= right:
        return numbers

    pivot = numbers[(left + right) // 2]
    left, right = left, right

    while left < right:
        while comparison(pivot, numbers[left]):
            left += 1
        while comparison(numbers[right], pivot):
            right -= 1
        if left <= right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1

    in_place_quick_sort(numbers, l, right)
    in_place_quick_sort(numbers, left, r)


def read_input():
    return [
        [x[0], int(x[1]), int(x[2])]
        for x in (input().split() for _ in range(int(input())))
    ]


if __name__ == "__main__":
    participants = read_input()
    in_place_quick_sort(participants, 0, len(participants) - 1)
    for el in participants[::-1]:
        print(el[0])
