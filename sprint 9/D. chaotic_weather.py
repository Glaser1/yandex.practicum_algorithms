def chaotic_weather(n, temperature_readings):
    if n == 1:
        return 1
    result = 0
    if temperature_readings[0] > temperature_readings[1]:
        result += 1
    if temperature_readings[-1] > temperature_readings[-2]:
        result += 1

    for i in range(1, n - 1):
        if temperature_readings[i-1] < temperature_readings[i] > temperature_readings[i+1]:
            result += 1

    return result


def read_input():
    n = int(input())
    temperatures = list(map(int, input().split()))
    return n, temperatures


if __name__ == '__main__':
    n, temperature_readings = read_input()
    print(chaotic_weather(n, temperature_readings))
