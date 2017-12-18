import sys

def fibonacci(n):
	if n < 2:
			return n
	else:
		one = fibonacci(n-1)
		two = fibonacci(n-2)
		return(one + two)

if len(sys.argv) < 2:
	print("Please provide a number.")
	exit()

target = int(sys.argv[1])
print(target)
print (fibonacci(target))
