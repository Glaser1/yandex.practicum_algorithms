def is_power_of_four(number: int) -> bool:
    if number == 1:
        return True
    k = 4
    n = 1
    while k ** n < number:
        n += 1
    return k ** n == number


print(is_power_of_four(int(input())))
