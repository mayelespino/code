#!/usr/bin/python
from random import randint



if __name__ == "__main__" :

    number =  0
    while number != 1000:
        number = randint(0,1000)

        if number % 5 == 0 and number % 3 == 0:
            print("zig-zag")
        elif number % 5 == 0:
            print("zig")
        elif number % 3 == 0:
            print("zag")
        else:
            print(number)