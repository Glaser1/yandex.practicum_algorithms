def factorization(number):
    result = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            number //= i
            result.append(str(i))
        else:
            i += 1
    result.append(str(number))
    return result


if __name__ == '__main__':
    print(' '.join(factorization(int(input()))))
