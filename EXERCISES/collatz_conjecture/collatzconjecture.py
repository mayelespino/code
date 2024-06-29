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

    for _ in range(5):
        collatz(randint(0, sys.maxsize))

if __name__ == "__main__":
    main()