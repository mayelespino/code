# 8. String to Integer (atoi)
# The atoi function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.

def atoi(number_string):
    first_char = number_string[0]
    if first_char in "0123456789" or first_char is "+":
        positive = True
    elif first_char is "-":
        positive = False
    else:
        positive = True

    total = 0

    for char in number_string:
        if char not in "0123456789":
            continue
        total *= 10
        total += int(char)

    if total > 2147483647:
        total = 2147483647
        
    if positive is False:
        total *= -1

    return (total)


def main():
    print(atoi("123"))
    print(atoi("-1234567890"))
    print(atoi("+2147483647"))
    print(atoi("+2147483649"))
if __name__ == "__main__": main()