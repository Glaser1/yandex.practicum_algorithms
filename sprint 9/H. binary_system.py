def binary_system(a, b):
    if a == '0' or b == '0':
        return max(a, b)

    size = max(len(a), len(b))
    a = '0' * (size - len(a)) + a
    b = '0' * (size - len(b)) + b
    result = ''
    remainder = 0
    for i in range(size - 1, -1, -1):
        if a[i] == b[i] == '1':
            if remainder == 0:
                result += '0'
                remainder = 1
            else:
                result += '1'
        elif a[i] == b[i] == '0':
            if remainder == 0:
                result += '0'
            else:
                result += '1'
                remainder = 0
        else:
            if remainder == 0:
                result += '1'
            else:
                result += '0'
                remainder = 1
    if remainder == 1:
        result += '1'
    return result[::-1]


if __name__ == '__main__':
    a, b = input(), input()
    print(binary_system(a, b))
