def list_form(l, x, k):
    res = ''
    remainder = 0

    for j in range(len(k) - 1, -1, -1):
        to_append = int(k[j]) + remainder
        if to_append + int(x[l]) < 10:
            res += str(to_append + int(x[l]))
            remainder = 0
        else:
            remainder = 1
            res += str((to_append + int(x[l])) % 10)
        l -= 1

    rest = x[:l + 1]
    if remainder:
        rest = str(int(rest) + remainder) if rest else str(remainder)
    return ' '.join(rest + res[::-1])


def read_input():
    l = int(input())
    x = input().replace(' ', '')
    k = input()
    if int(k) > int(x):
        x, k = k, x
    return len(x), x, k


if __name__ == '__main__':
    l, x, k = read_input()
    print(list_form(l - 1, x, k))
