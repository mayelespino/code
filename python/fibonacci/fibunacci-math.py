#!/usr/bin/python
# Got this solution from http://www.nerdparadise.com/tech/interview/fibonacci/
from math import sqrt

def fibonacci(n):
    root5 = sqrt(5)
    gr = (1 + root5) / 2
    igr = 1 - gr
    value = (pow(gr, n) - pow(igr, n)) / root5

    # round it to the closest integer since floating 
    # point arithmetic cannot be trusted to give
    # perfect integer answers. 
    return round(value,9)

target = 100
print(target)
print (fibonacci(target))
# try:
#     aNumber=int(raw_input('Give me a number:'))
# except ValueError:
#     print ("Not a number"

#print fibonacci(aNumber)