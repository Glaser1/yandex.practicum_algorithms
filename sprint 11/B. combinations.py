def combinations(digits, combination, index, res):
    if len(digits) == index:
        res.append(combination)
        return res
    letters = DIAL[int(digits[index])]
    for letter in letters:
        combinations(digits, combination + letter, index + 1, res)
    return res


if __name__ == '__main__':
    DIAL = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    digits = input()
    res = []
    print(*combinations(digits, '', 0, res))
