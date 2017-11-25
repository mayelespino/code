#!/usr/bin/python

def fibonacci(n):
    if n <= 2:
        return 1
    i = 3
    a = 1
    b = 1
    while i <= n:
        c = a + b 
        a = b 
        b = c
        i = i + 1
    return c

print "f(10)"
print fibonacci(10)
try:
    aNumber=int(raw_input('Give me a number:'))
except ValueError:
    print "Not a number"

print fibonacci(aNumber)