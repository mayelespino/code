#!/usr/bin/python

def fibonacci(n):
	if n < 2:
			return n
	else:
		return(fibonacci(n-1)+fibonacci(n-2))

print "f(10)"
print fibonacci(10)
try:
    aNumber=int(raw_input('Give me a number:'))
except ValueError:
    print "Not a number"

print fibonacci(aNumber)