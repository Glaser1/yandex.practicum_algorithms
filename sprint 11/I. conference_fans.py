def conference_fans(identifiers, k):
    count_of_participants = {}
    for el in identifiers:
        count_of_participants[el] = count_of_participants.get(el, 0) + 1
    count_of_participants = {
        m: v for m, v in sorted(count_of_participants.items(),
                                key=lambda item: item[1], reverse=True)
    }
    max_keys = []
    for key in count_of_participants:
        if k == 0:
            return max_keys
        max_keys.append(key)
        k -= 1
    return max_keys


def read_input():
    n = int(input())
    identifiers = list(map(int, input().split()))
    k = int(input())
    return n, identifiers, k


if __name__ == "__main__":
    n, identifiers, k = read_input()
    print(*conference_fans(sorted(identifiers), k))
