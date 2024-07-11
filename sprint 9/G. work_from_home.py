def work_from_home(number):
    binary_number = ''
    while number > 1:
        number, remainder = number // 2, number % 2
        binary_number += str(remainder)
    binary_number += str(number)
    return binary_number[::-1]


if __name__ == '__main__':
    print(work_from_home(int(input())))
