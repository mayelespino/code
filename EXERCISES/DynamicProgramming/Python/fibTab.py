#
# Dynamic solution to Fibunacci series, using tables
#

def fib(num):
    table = [0] * (num + 1)
    table[1] = 1

    for i in range(2, num + 1):
        table[i] = table[i-1] + table[i-2]

    return table[num]


if __name__ == "__main__":
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))