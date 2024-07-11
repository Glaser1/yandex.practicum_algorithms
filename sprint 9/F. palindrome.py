def is_palindrome(line: str) -> bool:
    line = ''.join(element for element in line if element.isalpha())
    line = line.lower()
    return True if line == line[::-1] else False


print(is_palindrome(input().strip()))
