def extra_letter(s, t):
    letters = {}
    for el in s:
        letters[el] = letters.get(el, 0) + 1
    extra_letters = {}
    for el in t:
        extra_letters[el] = extra_letters.get(el, 0) + 1
        if extra_letters.get(el, 0) > letters.get(el, 0):
            return el


def read_input():
    s, t = input(), input()
    return s, t


if __name__ == '__main__':
    s, t = read_input()
    print(extra_letter(s, t))
