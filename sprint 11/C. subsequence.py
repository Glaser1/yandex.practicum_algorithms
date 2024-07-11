def subsequence(s, t):
    i = 0
    for el in t:
        if i < len(s) and el == s[i]:
            i += 1
    return i == len(s)


if __name__ == "__main__":
    s, t = input(), input()
    print(subsequence(s, t))
