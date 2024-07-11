def longest_word(n, sentence):
    length = 0
    longest = ''
    for el in sentence:
        if len(el) > length:
            length = len(el)
            longest = el
    return longest, length


def read_input():
    n = int(input())
    sentence = input().strip().split()
    return n, sentence


if __name__ == '__main__':
    n, sentence = read_input()
    print(*longest_word(n, sentence), sep='\n')
