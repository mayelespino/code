from random import randint
import sys

def collatz(number):
    n = number
    count = 0
    print("N:", n, "count", count)

    def isEven(num):
        return((num % 2) == 0)

    while n != 4:
        count += 1
        if isEven(n):
            n = int(n/2)
        else:
            n = int(3*n + 1)

        print("N:", n, "count", count)

    print("\n\n\n")

def main():
    collatz(5)
    collatz(6)
    collatz(7)
    collatz(sys.maxsize)
    
    collatz(11)
    collatz(13)
    collatz(17)
    collatz(19)
    collatz(23)
    collatz(29)
    collatz(31)
    collatz(37)
    collatz(41)
    collatz(43)
    collatz(47)
    collatz(53)
    collatz(59)
    collatz(61)
    collatz(67)
    collatz(71)

    for _ in range(5):
        collatz(randint(0, sys.maxsize))

if __name__ == "__main__":
    main()